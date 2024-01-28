"""Module that implements the training of the tree ensemble"""
from typing import Optional, Tuple

import numpy as np
from numba import njit
from tqdm import tqdm

from ..runtime.hard_axis_aligned_tree_ensemble import (
    AxisAlignedTrees,
    AxisAlignedTreesParameters,
    regression_tree_ensemble_apply,
)


@njit
def numba_set_seed(value: float) -> None:
    """Reset the seed for numba"""
    np.random.seed(value)


@njit(cache=True)
def get_best_split(
    features: np.ndarray,
    targets: np.ndarray,
    perm: np.ndarray,
    begin: int,
    end: int,
    num_test_splits: int = 20,
) -> Tuple[Tuple[int, float], Tuple[int, int, int], Tuple[np.ndarray, np.ndarray]]:
    best_div_score = -1.0
    best_feature = 0
    best_midpoint = begin
    target_size = len(targets[0])
    best_sums = (np.zeros(target_size), np.zeros(target_size))
    if begin == end:
        return ((best_feature, 0.0), (begin, best_midpoint, end), best_sums)

    group = perm[begin:end]
    features_group = features[group, :]
    target_group = targets[group]
    num_features = features.shape[1]
    best_threshold = 0.0
    for _ in range(num_test_splits):
        feature_id = int(np.random.rand() * num_features)
        f = features_group[:, feature_id]
        f_min = np.min(f)
        f_max = np.max(f)
        threshold = f_min + (f_max - f_min) * np.random.rand()
        division = f > threshold
        right_cnt = float(np.sum(division))
        if right_cnt == 0:
            right_sum = np.zeros((target_size), dtype=targets.dtype)
            right_score = 0.0
        else:
            right_sum = target_group[division].sum(axis=0)
            right_score = right_sum.dot(right_sum) / right_cnt

        left_cnt = int(np.sum(~division))
        if left_cnt == 0:
            left_sum = np.zeros((target_size), dtype=targets.dtype)
            left_score = 0.0
        else:
            left_sum = target_group[~division].sum(axis=0)
            left_score = left_sum.dot(left_sum) / left_cnt

        # assert np.all(np.abs(left_sum - overall_sum + right_sum) < 1e-6)
        # assert np.all(np.abs(left_cnt - overall_cnt + right_cnt) < 1e-6)
        # TODO: Should this be *left_cnt, *right_cnt?

        score = left_score + right_score
        # print(score)
        if score > best_div_score:
            best_feature = feature_id
            best_threshold = threshold
            best_midpoint = begin + left_cnt
            best_div_score = score
            best_sums = (left_sum, right_sum)

    best_division = features_group[:, best_feature] > best_threshold

    ind = np.argsort(best_division)
    perm[begin:end] = perm[begin:end][ind]

    # assert np.allclose(targets[perm[begin:int(best_midpoint)],:].sum(axis=0),best_sums[0])

    return ((best_feature, best_threshold), (begin, best_midpoint, end), best_sums)


class GreedyAxisAlignedTreesTrainer:
    """Trainer for GreedyRegressionTrees."""

    def __init__(
        self,
        num_trees: int,
        depth: int,
        num_test_splits: int,
        mu: float,
        float32: bool,
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
        self.float32 = float32

    def _train_tree(
        self, x: np.ndarray, y: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Train a single tree."""
        num_nodes = (1 << self.depth) - 1
        num_split_nodes = (1 << (self.depth - 1)) - 1
        num_leaves = num_nodes - num_split_nodes
        target_size = y.shape[1]

        buckets = np.zeros((num_nodes, 2), dtype=np.uint32)
        sums = np.zeros((num_nodes, y.shape[1]), dtype=np.float64)
        cnts = np.zeros((num_nodes,), dtype=np.uint32)
        if self.float32:
            splits = np.zeros((num_split_nodes, 2), dtype=np.float32)
        else:
            splits = np.zeros((num_split_nodes, 2), dtype=np.float64)

        buckets[0] = (0, len(y))
        sums[0, :] = y.sum(axis=0)

        cnts[0] = int(y.shape[0])

        perm = np.arange(0, len(y), dtype=np.uint32)

        for i in range(num_split_nodes):
            split, division, best_sums = get_best_split(
                x,
                y,
                perm,
                buckets[i][0],
                buckets[i][1],
                self.num_test_splits,
            )
            begin, mid, end = division
            splits[i, :] = split
            buckets[2 * i + 1] = (begin, int(mid))
            buckets[2 * i + 2] = (int(mid), end)
            sums[2 * i + 1, :] = best_sums[0]
            sums[2 * i + 2, :] = best_sums[1]
            cnts[2 * i + 1] = mid - begin
            cnts[2 * i + 2] = end - mid
        if self.float32:
            leaves = np.zeros(shape=(num_leaves, target_size), dtype=np.float32)
        else:
            leaves = np.zeros(shape=(num_leaves, target_size), dtype=np.float64)

        for i in range(num_split_nodes, num_nodes):
            if cnts[i] != 0:
                leaves[i - num_split_nodes] = self.mu * sums[i] / cnts[i]

        return splits, leaves

    def fit(self, x: np.ndarray, y: np.ndarray) -> AxisAlignedTrees:
        assert x.ndim == 2
        assert x.ndim == 2
        assert x.shape[0] == y.shape[0]

        if self.random_seed is not None:
            np.random.seed(self.random_seed)
            numba_set_seed(self.random_seed)

        mse_iter = []

        all_splits = []
        all_leaves = []

        residuals = y.copy()
        mse = np.mean(residuals**2)
        for _ in tqdm(range(self.num_trees)):
            splits, leaves = self._train_tree(x, residuals)
            all_splits.append(splits)
            all_leaves.append(leaves)

            # Update residuals.
            res_pred = regression_tree_ensemble_apply(
                splits[None, :], leaves[None, :], self.depth, x.astype(np.float32)
            )
            residuals -= res_pred
            new_mse = np.mean(residuals**2)
            assert new_mse <= mse
            mse = new_mse
            mse_iter.append(mse)

        ensemble_splits = np.stack(all_splits, axis=0).astype(np.float32)
        ensemble_leaves = np.stack(all_leaves, axis=0).astype(np.float32)

        pred = regression_tree_ensemble_apply(
            ensemble_splits, ensemble_leaves, self.depth, x
        )
        residuals = y - pred
        mse = np.mean(residuals**2)
        tree_para = AxisAlignedTreesParameters(
            depth=self.depth, splits=ensemble_splits, leaves=ensemble_leaves
        )
        return AxisAlignedTrees(tree_para)
