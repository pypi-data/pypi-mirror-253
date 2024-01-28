"""Module that implements the evaluation of the tree ensemble"""
from dataclasses import dataclass

import numba
import numpy as np
from numba import njit


@njit(cache=True, fastmath=True, parallel=False, boundscheck=False)
def regression_tree_ensemble_apply(
    splits: np.ndarray, leaves: np.ndarray, depth: int, features: np.ndarray
) -> np.ndarray:
    # get leaf index
    assert features.ndim == 2
    num_samples = features.shape[0]
    num_trees = splits.shape[0]
    assert leaves.ndim == 3
    assert leaves.shape[0] == num_trees
    num_out = leaves.shape[2]
    output = np.empty((num_samples, num_out), dtype=np.float32)
    outputs_trees = np.empty((num_trees, num_out), dtype=np.float32)
    for sample_id in range(num_samples):
        for tree_id in numba.prange(num_trees):
            node = 0
            for _ in range(depth - 1):
                feature_id, thresh = splits[tree_id, node]
                node = 2 * node + 1
                if features[sample_id, int(feature_id)] > thresh:
                    node += 1
            leaf_index = node - splits.shape[1]
            outputs_trees[tree_id, :] = leaves[tree_id, leaf_index, :]
        output[sample_id, :] = outputs_trees.sum(axis=0)
    return output


@dataclass
class AxisAlignedTreesParameters:
    """Trained Parameters for the RegressionTrees"""

    depth: int
    splits: np.ndarray
    leaves: np.ndarray


class AxisAlignedTrees:
    """Regression tree class"""

    def __init__(self, tree_para: AxisAlignedTreesParameters):
        self.tree_para = tree_para

    def predict(self, x: np.ndarray) -> np.ndarray:
        return regression_tree_ensemble_apply(
            self.tree_para.splits,
            self.tree_para.leaves,
            depth=self.tree_para.depth,
            features=x,
        )
