"""Module that implements the evaluation of the tree ensemble"""
from dataclasses import dataclass

import numba
import numpy as np
from numba import njit


@njit(cache=True, fastmath=True, parallel=False, boundscheck=False)
def regression_tree_ensemble_apply(
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
    features: np.ndarray,
) -> np.ndarray:
    # get leaf index
    assert features.ndim == 2
    num_samples = features.shape[0]
    num_trees = split_feat_ids.shape[0]
    assert split_coefs.shape[0] == num_trees
    num_splits = split_coefs.shape[1]
    assert leaves_coefs.ndim == 4
    assert leaves_coefs.shape[0] == num_trees
    num_out = leaves_coefs.shape[2]
    output = np.empty((num_samples, num_out), dtype=np.float32)
    outputs_trees = np.empty((num_trees, num_out), dtype=np.float32)
    for sample_id in range(num_samples):
        for tree_id in numba.prange(num_trees):
            node = 0
            for _ in range(depth - 1):
                feature_ids = split_feat_ids[tree_id, node, :]
                projected = features[sample_id][feature_ids]
                s = split_coefs[tree_id, node, -1] + projected.dot(
                    split_coefs[tree_id, node, :-1]
                )
                node = 2 * node + 1
                if s > 0:
                    node += 1
            leaf_index = node - num_splits
            leaf_coefs = leaves_coefs[tree_id, leaf_index]
            feature_ids = leaves_feat_ids[tree_id, leaf_index, :]
            outputs_trees[tree_id, :] = leaf_coefs[:, -1] + leaves_coefs[
                tree_id, leaf_index, :, :-1
            ].dot(features[sample_id][feature_ids])
        output[sample_id, :] = outputs_trees.sum(axis=0)
    return output


@dataclass
class ObliqueTreesParameters:
    """Trained Parameters for the RegressionTrees"""

    depth: int
    split_feat_ids: np.ndarray
    split_coefs: np.ndarray
    leaves_feat_ids: np.ndarray
    leaves_coefs: np.ndarray

    def __post_init__(self) -> None:
        """Doing some checks"""
        assert self.split_feat_ids.ndim == 3
        assert self.split_coefs.ndim == 3
        num_trees = self.split_feat_ids.shape[0]
        assert self.split_coefs.shape[0] == num_trees
        assert self.split_feat_ids.shape[1] == self.split_coefs.shape[1]
        assert self.split_feat_ids.shape[2] + 1 == self.split_coefs.shape[2]
        assert self.leaves_coefs.shape[0] == num_trees


class ObliqueTrees:
    """Regression tree class"""

    def __init__(self, tree_para: ObliqueTreesParameters):
        self.tree_para = tree_para

    def predict(self, x: np.ndarray) -> np.ndarray:
        return regression_tree_ensemble_apply(
            split_coefs=self.tree_para.split_coefs,
            split_feat_ids=self.tree_para.split_feat_ids,
            leaves_coefs=self.tree_para.leaves_coefs,
            leaves_feat_ids=self.tree_para.leaves_feat_ids,
            depth=self.tree_para.depth,
            features=x.astype(np.float32),
        )
