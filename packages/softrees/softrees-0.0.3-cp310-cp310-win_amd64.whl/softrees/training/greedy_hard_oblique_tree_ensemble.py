"""Module that implements the greedy training of an oblique regression tree ensemble."""
from typing import Optional, Tuple

import numpy as np
from numba import njit
from tqdm import tqdm

from ..runtime.hard_oblique_tree_ensemble import (
    ObliqueTrees,
    ObliqueTreesParameters,
    regression_tree_ensemble_apply,
)


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


@njit(cache=True)
def get_best_split(
    features: np.ndarray,
    targets: np.ndarray,
    perm: np.ndarray,
    begin: int,
    end: int,
    num_split_feat: int,
    regu_leaves: float,
    num_test_splits: int,
) -> Tuple[Tuple[np.ndarray, np.ndarray], Tuple[int, int, int],]:
    best_div_mse = np.inf
    best_split_feat_ids = np.zeros((num_split_feat), dtype=np.uint32)

    best_midpoint = begin
    nb_samples = features.shape[0]

    num_features = features.shape[1]
    split_coefs = np.zeros((num_features + 1,))
    best_split_coefs = split_coefs
    if begin == end:
        return (
            (best_split_feat_ids, best_split_coefs),
            (begin, best_midpoint, end),
        )

    group = perm[begin:end]
    features_group = features[group, :]
    target_group = targets[group]

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

        division = f > 0
        right_cnt = int(np.sum(division))
        if right_cnt == 0:
            right_mse = 0.0
        else:
            _, right_mse = regularized_linear_regression(
                features_group[division],
                target_group[division],
                regu_leaves,
            )

        left_cnt = int(np.sum(~division))
        if left_cnt == 0:
            left_mse = 0.0
        else:
            _, left_mse = regularized_linear_regression(
                features_group[~division],
                target_group[~division],
                regu_leaves,
            )

        combined_mse = (right_cnt * right_mse + left_cnt * left_mse) / nb_samples
        # print(score)
        if combined_mse < best_div_mse:
            best_split_feat_ids = split_feature_ids
            best_split_coefs = split_coefs.copy()
            best_midpoint = begin + left_cnt
            best_div_mse = combined_mse

    f = best_split_coefs[-1] + features_group[:, best_split_feat_ids].dot(
        best_split_coefs[:-1]
    )
    best_division = f > 0

    ind = np.argsort(best_division)
    perm[begin:end] = perm[begin:end][ind]

    return (
        (best_split_feat_ids, best_split_coefs),
        (begin, best_midpoint, end),
    )


class GreedyObliqueTreesTrainer:
    """Trainer for GreedyRegressionTrees."""

    def __init__(
        self,
        num_trees: int,
        depth: int,
        num_test_splits: int,
        mu: float,
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

        self.num_split_feat = num_split_feat
        self._regu_leaves = regu_leaves
        self.num_nodes = (1 << self.depth) - 1
        self.num_split_nodes = (1 << (self.depth - 1)) - 1
        self.num_leaves = self.num_nodes - self.num_split_nodes

    def _train_tree(
        self, x: np.ndarray, y: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Train a single tree."""
        target_size = y.shape[1]
        num_features = x.shape[1]

        buckets = np.zeros((self.num_nodes, 2), dtype=np.uint32)

        num_split_feat = (
            x.shape[1] if self.num_split_feat is None else self.num_split_feat
        )

        split_feat_ids = np.zeros(
            (self.num_split_nodes, num_split_feat), dtype=np.uint32
        )
        split_coefs = np.zeros(
            (self.num_split_nodes, num_split_feat + 1), dtype=np.float32
        )

        buckets[0] = (0, len(y))

        perm = np.arange(0, len(y), dtype=np.uint32)

        for i in range(self.num_split_nodes):
            split, division = get_best_split(
                features=x,
                targets=y,
                perm=perm,
                begin=buckets[i][0],
                end=buckets[i][1],
                num_split_feat=num_split_feat,
                num_test_splits=self.num_test_splits,
                regu_leaves=self._regu_leaves,
            )
            node_split_feat_ids, node_split_coefs = split

            begin, mid, end = division
            split_feat_ids[i, :] = node_split_feat_ids
            split_coefs[i, :] = node_split_coefs
            buckets[2 * i + 1] = (begin, int(mid))
            buckets[2 * i + 2] = (int(mid), end)

        leaves_coefs = np.zeros(
            shape=(self.num_leaves, target_size, num_features + 1), dtype=np.float32
        )

        for i in range(self.num_split_nodes, self.num_nodes):
            begin, end = buckets[i]
            leaf_coefs, _ = regularized_linear_regression(
                x[perm[begin:end]], y[perm[begin:end]], regu=self._regu_leaves
            )
            leaves_coefs[i - self.num_split_nodes, :, :] = self.mu * leaf_coefs.T

        return split_feat_ids, split_coefs, leaves_coefs

    def fit(self, x: np.ndarray, y: np.ndarray) -> ObliqueTrees:
        assert x.ndim == 2
        assert x.ndim == 2
        assert x.shape[0] == y.shape[0]

        num_features = x.shape[1]

        if self.random_seed is not None:
            np.random.seed(self.random_seed)
            numba_set_seed(self.random_seed)

        mse_iter = []

        all_split_feat_ids = []
        all_split_coefs = []
        all_leaves_coefs = []
        pred = np.zeros_like(y)
        residuals = y - pred

        ensemble_leaves_feat_ids = (
            np.ones((self.num_trees, self.num_leaves, num_features), np.uint32)
            * np.arange(num_features)[None, :]
        ).astype(np.uint32)
        mse = np.mean(residuals**2)
        for tree_idx in tqdm(range(self.num_trees)):
            split_feat_ids, split_coefs, leaves_coefs = self._train_tree(x, residuals)
            all_split_feat_ids.append(split_feat_ids)
            all_split_coefs.append(split_coefs)
            all_leaves_coefs.append(leaves_coefs)

            # Update residuals.
            delta_pred = regression_tree_ensemble_apply(
                split_feat_ids=split_feat_ids[None, :],
                split_coefs=split_coefs[None, :],
                leaves_feat_ids=ensemble_leaves_feat_ids[tree_idx, :, :][None, :, :],
                leaves_coefs=leaves_coefs[None, :],
                depth=self.depth,
                features=x.astype(np.float32),
            )
            pred += delta_pred
            residuals = y - pred
            new_mse = np.mean(residuals**2)
            assert new_mse <= mse
            mse = new_mse
            mse_iter.append(mse)

        ensemble_split_feat_ids = np.stack(all_split_feat_ids, axis=0).astype(np.uint32)
        ensemble_split_coefs = np.stack(all_split_coefs, axis=0).astype(np.float32)
        ensemble_leaves_coefs = np.stack(all_leaves_coefs, axis=0).astype(np.float32)

        pred = regression_tree_ensemble_apply(
            ensemble_split_feat_ids,
            ensemble_split_coefs,
            ensemble_leaves_feat_ids,
            ensemble_leaves_coefs,
            self.depth,
            x.astype(np.float32),
        )
        residuals = y - pred
        assert np.allclose(mse, np.mean(residuals**2), rtol=1e-2)

        tree_para = ObliqueTreesParameters(
            depth=self.depth,
            split_feat_ids=ensemble_split_feat_ids,
            split_coefs=ensemble_split_coefs,
            leaves_feat_ids=ensemble_leaves_feat_ids,
            leaves_coefs=ensemble_leaves_coefs,
        )
        return ObliqueTrees(tree_para)
