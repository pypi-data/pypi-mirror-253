"""Module that implements the greedy training of a soft oblique regression tree ensemble."""
from typing import Optional, Tuple

import numpy as np
from numba import njit
from tqdm import tqdm

from ..runtime.soft_tree_ensemble import (
    SoftTreeEnsemble,
    SoftTreeEnsembleTrainedParameters,
)
from ..runtime.soft_tree_ensemble_common import soft_tree_ensemble_forward_fast


@njit
def numba_set_seed(value: float) -> None:
    """Reset the seed for numba"""
    np.random.seed(value)


@njit(cache=True)
def regularized_linear_regression(
    x: np.ndarray, y: np.ndarray, regu: float
) -> Tuple[np.ndarray, float]:
    x_h = np.column_stack((x, np.ones((x.shape[0],))))  # bias stored in the last coef
    coefs = np.linalg.solve(x_h.T.dot(x_h) + regu * np.eye(x_h.shape[1]), x_h.T.dot(y))
    mse = np.mean((y - x_h.dot(coefs)) ** 2)
    return coefs, mse


# @numba.vectorize([numba.float64(numba.float64, numba.float64)])
@njit
def smooth_step(t: float) -> float:
    if t < -0.5:
        return 0
    elif t > 0.5:
        return 1
    else:
        return -2 * t**3 + 1.5 * t + 0.5


@njit
def smooth_step_vec(t: np.ndarray) -> np.ndarray:
    assert t.ndim == 1
    o = np.zeros_like(t)
    for i in range(len(t)):
        o[i] = smooth_step(t[i])
    return o


# @njit(cache=True)
def get_best_split(
    features: np.ndarray,
    targets: np.ndarray,
    pred: np.ndarray,
    node_coefs: np.ndarray,
    sample_ids: np.ndarray,
    sample_activations: np.ndarray,
    num_split_feat: int,
    regu_leaves: float,
    num_test_splits: int,
) -> Tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    best_div_mse = np.inf
    best_split_feat_ids = np.zeros((num_split_feat), dtype=np.uint32)

    num_features = features.shape[1]
    split_coefs = np.zeros((num_features + 1,))
    best_split_coefs = split_coefs

    features_group = features[sample_ids, :]
    targets_group = targets[sample_ids]

    # remove the contribution of the linear model attached to the leaf node that
    # we will replace by two new leaves
    pred_group_node_removed = pred[sample_ids] - sample_activations[:, None] * (
        features_group.dot(node_coefs[:-1, :]) + node_coefs[-1, :]
    )
    residual = targets_group - pred_group_node_removed
    for _ in range(num_test_splits):
        split_feature_ids = np.sort(
            np.random.choice(num_features, num_split_feat, replace=False).astype(
                np.uint32
            )
        )
        direction = np.random.randn(num_split_feat)
        f = features_group[:, split_feature_ids].dot(direction)
        f_min = np.min(f)
        f_max = np.max(f)
        threshold = f_min + (f_max - f_min) * np.random.rand()

        split_coefs[-1] = -threshold
        split_coefs[:-1] = direction

        f = split_coefs[-1] + features_group[:, split_feature_ids].dot(split_coefs[:-1])
        t = smooth_step_vec(f)

        left_activation = sample_activations * (1 - t)
        right_activation = sample_activations * t
        x_h = np.column_stack(
            (
                features_group * left_activation[:, None],
                left_activation,
                features_group * right_activation[:, None],
                right_activation,
            )
        )

        coefs = np.linalg.solve(
            x_h.T.dot(x_h) + regu_leaves * np.eye(x_h.shape[1]), x_h.T.dot(residual)
        )
        new_group_pred = x_h.dot(coefs) + pred_group_node_removed
        mse = np.mean((targets_group - new_group_pred) ** 2)

        # print(score)
        if mse < best_div_mse:
            best_split_feat_ids = split_feature_ids
            best_split_coefs = split_coefs.copy()
            best_left_coefs = coefs[: num_features + 1 :, :]
            best_right_coefs = coefs[num_features + 1 :, :]

            left_active = left_activation > 0
            best_left_samples = sample_ids[left_active]
            best_left_activation = left_activation[left_active]

            right_active = right_activation > 0
            best_right_samples = sample_ids[right_active]
            best_right_activation = right_activation[right_active]
            best_group_pred = new_group_pred
            best_div_mse = mse

    new_pred = pred.copy()
    new_pred[sample_ids, :] = best_group_pred
    return (
        best_split_feat_ids,
        best_split_coefs,
        best_left_samples,
        best_left_activation,
        best_left_coefs,
        best_right_samples,
        best_right_activation,
        best_right_coefs,
        new_pred,
    )


class GreedySoftObliqueTreesTrainer:
    """Trainer for GreedyRegressionTrees."""

    def __init__(
        self,
        num_trees: int,
        depth: int,
        num_test_splits: int,
        mu: float,
        float32: bool,
        regu_leaves: float = 1e-5,
        num_split_feat: Optional[int] = None,
        random_seed: Optional[int] = None,
    ):
        self.num_trees = num_trees
        self.depth = depth
        self.num_test_splits = num_test_splits
        self.mu = mu
        assert mu > 0
        assert mu <= 1
        self.random_seed = random_seed
        self.splits: Optional[np.ndarray] = None
        self.leaves: Optional[np.ndarray] = None
        self.float32 = float32
        self.num_split_feat = num_split_feat
        self._regu_leaves = regu_leaves

    def _train_tree(
        self, x: np.ndarray, y: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Train a single tree."""
        dtype = np.float32 if self.float32 else np.float64
        assert x.dtype == dtype
        num_nodes = (1 << self.depth) - 1
        num_split_nodes = (1 << (self.depth - 1)) - 1
        num_leaves = num_nodes - num_split_nodes
        target_size = y.shape[1]
        num_features = x.shape[1]

        node_data = {}

        leaves_feat_ids = (
            np.ones((num_leaves, num_features), np.uint32)
            * np.arange(num_features)[None, :]
        ).astype(np.uint32)

        num_split_feat = (
            x.shape[1] if self.num_split_feat is None else self.num_split_feat
        )
        split_feat_ids = np.zeros((num_split_nodes, num_split_feat), dtype=np.uint32)

        split_coefs = np.zeros((num_split_nodes, num_split_feat + 1), dtype=dtype)

        nb_samples = len(x)
        sample_ids = np.arange(nb_samples)
        activations = np.ones(nb_samples)
        node_coefs, mse = regularized_linear_regression(
            x,
            y,
            self._regu_leaves,
        )

        node_data[0] = (sample_ids, activations, node_coefs)

        pred = x.dot(node_coefs[:-1, :]) + node_coefs[-1, :]

        mse = np.mean((y - pred) ** 2)
        for i in range(num_split_nodes):
            samples_ids, activations, node_coefs = node_data.pop(i)

            (
                node_split_feat_ids,
                node_split_coefs,
                left_samples,
                left_activations,
                left_coefs,
                right_samples,
                right_activations,
                right_coefs,
                new_pred,
            ) = get_best_split(
                features=x,
                targets=y,
                pred=pred,
                node_coefs=node_coefs,
                sample_ids=samples_ids,
                sample_activations=activations,
                num_split_feat=num_split_feat,
                num_test_splits=self.num_test_splits,
                regu_leaves=self._regu_leaves,
            )

            node_data[2 * i + 1] = (left_samples, left_activations, left_coefs)
            node_data[2 * i + 2] = (right_samples, right_activations, right_coefs)
            new_mse = np.mean((y - new_pred) ** 2)
            assert new_mse < mse + 1e-5
            pred = new_pred
            mse = new_mse

            split_feat_ids[i, :] = node_split_feat_ids
            split_coefs[i, :] = node_split_coefs
        if self.float32:
            leaves_coefs = np.zeros(
                shape=(num_leaves, target_size, num_features + 1), dtype=np.float32
            )
        else:
            leaves_coefs = np.zeros(
                shape=(num_leaves, target_size, num_features + 1), dtype=np.float64
            )

        for i in range(num_split_nodes, num_nodes):
            leaf_coefs = node_data[i][2]
            leaves_coefs[i - num_split_nodes, :, :] = self.mu * leaf_coefs.T

        return split_feat_ids, split_coefs, leaves_feat_ids, leaves_coefs

    def fit(self, x: np.ndarray, y: np.ndarray) -> SoftTreeEnsemble:
        dtype = np.float32 if self.float32 else np.float64
        assert x.dtype == dtype
        assert x.ndim == 2
        assert y.ndim == 2
        assert x.shape[0] == y.shape[0]

        if self.random_seed is not None:
            np.random.seed(self.random_seed)
            numba_set_seed(self.random_seed)

        mse_iter = []

        all_split_feat_ids = []
        all_split_coefs = []
        all_leaves_coefs = []
        all_leaves_feat_ids = []
        pred = np.zeros_like(y)
        residuals = y - pred

        mse = np.mean(residuals**2)
        for _ in tqdm(range(self.num_trees)):
            (
                split_feat_ids,
                split_coefs,
                leaves_feat_ids,
                leaves_coefs,
            ) = self._train_tree(x, residuals)
            all_split_feat_ids.append(split_feat_ids)
            all_split_coefs.append(split_coefs)
            all_leaves_coefs.append(leaves_coefs)
            all_leaves_feat_ids.append(leaves_feat_ids)
            # Update residuals.
            delta_pred = soft_tree_ensemble_forward_fast(
                features=x,
                split_feat_ids=split_feat_ids[None, :],
                split_coefs=split_coefs[None, :],
                leaves_feat_ids=leaves_feat_ids[None, :],
                leaves_coefs=leaves_coefs[None, :],
                depth=self.depth,
                oblique=True,
            )

            pred += delta_pred
            residuals = y - pred
            new_mse = np.mean(residuals**2)
            assert new_mse <= mse
            mse = new_mse
            mse_iter.append(mse)

        ensemble_split_feat_ids = np.stack(all_split_feat_ids, axis=0).astype(np.uint32)

        ensemble_split_coefs = np.stack(all_split_coefs, axis=0).astype(dtype)
        ensemble_leaves_coefs = np.stack(all_leaves_coefs, axis=0).astype(dtype)
        ensemble_leaves_feat_ids = np.stack(all_leaves_feat_ids, axis=0).astype(
            np.uint32
        )

        pred = soft_tree_ensemble_forward_fast(
            features=x,
            split_feat_ids=ensemble_split_feat_ids,
            split_coefs=ensemble_split_coefs,
            leaves_feat_ids=ensemble_leaves_feat_ids,
            leaves_coefs=ensemble_leaves_coefs,
            depth=self.depth,
            oblique=True,
        )
        residuals = y - pred
        assert np.allclose(mse, np.mean(residuals**2), rtol=1e-2)
        tree_para = SoftTreeEnsembleTrainedParameters(
            depth=self.depth,
            split_feat_ids=ensemble_split_feat_ids,
            split_coefs=ensemble_split_coefs,
            leaves_feat_ids=ensemble_leaves_feat_ids,
            leaves_coefs=ensemble_leaves_coefs,
            active_tol=0,
            abs_tol=0,
            oblique=True,
            in_features=x.shape[1],
        )

        return SoftTreeEnsemble(tree_para)
