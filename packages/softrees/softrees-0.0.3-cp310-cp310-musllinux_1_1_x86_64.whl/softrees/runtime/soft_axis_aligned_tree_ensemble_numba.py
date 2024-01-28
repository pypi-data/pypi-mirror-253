"""Module that implements the numba accelerated function for the soft tree ensemble"""
from typing import Tuple

import numba
import numpy as np
from numba import njit


@njit
def numba_set_seed(value: int) -> None:
    """Reset la seed pour numba meme si l'appel est np.random.seed(value)"""
    np.random.seed(value)
    pass


@njit(cache=True, boundscheck=False, fastmath=True)
def smooth_step(t: float) -> float:
    if t < -0.5:
        return 0
    elif t > 0.5:
        return 1
    else:
        return -2 * t**3 + 1.5 * t + 0.5


@njit(cache=True, boundscheck=False, fastmath=True)
def smooth_step_deriv(t: float) -> float:
    if t < -0.5 or t > 0.5:
        return 0
    else:
        return -6 * t**2 + 1.5


@njit(cache=True, boundscheck=False, fastmath=True)
def smooth_abs(t: float, tol: float) -> float:
    if t < -tol:
        return -t - 0.5 * tol
    elif t > tol:
        return t - 0.5 * tol
    else:
        return 0.5 * t**2 / tol


@njit(cache=True, boundscheck=False, fastmath=True)
def smooth_abs_deriv(t: float, tol: float) -> float:
    if t < -tol:
        return -1
    elif t > tol:
        return 1
    else:
        return t / tol


@njit(cache=True, boundscheck=False, fastmath=True)
def soft_tree_ensemble_axis_aligned_forward(
    features: np.ndarray,
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
    active_tol: float,
    abs_tol: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    assert features.ndim == 2
    num_leaves = 2 ** (depth - 1)
    num_samples = features.shape[0]
    num_trees, num_split_nodes = split_feat_ids.shape
    assert split_coefs.shape == (num_trees, num_split_nodes, 2)
    assert num_split_nodes == 2 ** (depth - 1) - 1

    assert leaves_feat_ids.ndim == 3
    assert leaves_feat_ids.shape[0] == num_trees
    assert leaves_feat_ids.shape[1] == num_leaves
    leaves_num_features = leaves_feat_ids.shape[2]
    assert leaves_coefs.ndim == 4
    assert leaves_coefs.shape[0] == num_trees
    assert leaves_coefs.shape[1] == num_leaves
    num_out = leaves_coefs.shape[2]
    assert leaves_coefs.shape[3] == leaves_num_features + 1

    output_dtype = features.dtype

    output = np.zeros((num_samples, num_out), dtype=output_dtype)
    leaves_frequency = np.zeros((num_trees, num_leaves), dtype=output_dtype)
    num_active_leaves_average = np.zeros(num_samples, dtype=output_dtype)
    mean_decision_abs_distance = np.zeros((num_samples), dtype=output_dtype)

    for sample_id in range(num_samples):
        for tree_id in numba.prange(num_trees):
            nodes = [0]
            weights = [1.0]
            actives = [1.0]
            prev_subtree_num_nodes = 0
            subtree_num_nodes = 1
            for _ in range(depth - 1):
                for subtree_node_id in range(prev_subtree_num_nodes, subtree_num_nodes):
                    node = nodes[subtree_node_id]
                    weight = weights[subtree_node_id]
                    active = actives[subtree_node_id]
                    feature_id = split_feat_ids[tree_id, node]
                    thresh, coef = split_coefs[tree_id, node]
                    feature_value = features[sample_id, feature_id]

                    t_weight = coef * (feature_value - thresh)
                    s_weight = smooth_step(t_weight)

                    mean_decision_abs_distance[sample_id] += weight * smooth_abs(
                        t_weight, abs_tol
                    )

                    # to get a strict upper bound on the number of activated leaves
                    # we want s_left=1 when s<1
                    # we want s_right=1 when s>0
                    t_left = (0.5 + active_tol * 0.5 - t_weight) / active_tol
                    s_left = smooth_step(t_left)
                    t_right = (0.5 + active_tol * 0.5 + t_weight) / active_tol
                    s_right = smooth_step(t_right)

                    if s_left > 0:
                        # keep the left node
                        nodes.append(2 * node + 1)
                        weights.append((1 - s_weight) * weight)
                        actives.append(s_left * active)
                    if s_right > 0:
                        # keep the right node
                        nodes.append(2 * node + 2)
                        weights.append(s_weight * weight)
                        actives.append(s_right * active)
                prev_subtree_num_nodes = subtree_num_nodes
                subtree_num_nodes = len(nodes)

            for subtree_node_id in range(prev_subtree_num_nodes, subtree_num_nodes):
                node = nodes[subtree_node_id]
                weight = weights[subtree_node_id]
                leaf_index = node - num_split_nodes
                leaf_features_ids = leaves_feat_ids[tree_id, leaf_index, :]
                leaf_feature_values = features[sample_id][leaf_features_ids]
                leaf_coefs = leaves_coefs[tree_id, leaf_index, :, :]
                bias = leaf_coefs[:, -1]
                output[sample_id] += weight * (
                    leaf_coefs[:, :-1].dot(leaf_feature_values) + bias
                )
                leaves_frequency[tree_id, leaf_index] += weight / num_samples
                num_active_leaves_average[sample_id] += actives[subtree_node_id]

    return (
        output,
        num_active_leaves_average,
        leaves_frequency,
        mean_decision_abs_distance,
    )


@njit(cache=True, boundscheck=False, fastmath=True, parallel=True)
def soft_tree_ensemble_axis_aligned_forward_fast(
    features: np.ndarray,
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
) -> np.ndarray:
    """Evaluate the tree without additional outputs"""
    assert features.ndim == 2
    num_leaves = 2 ** (depth - 1)
    num_samples = features.shape[0]
    num_trees, num_split_nodes = split_feat_ids.shape
    assert split_coefs.shape == (num_trees, num_split_nodes, 2)
    assert num_split_nodes == 2 ** (depth - 1) - 1

    assert leaves_feat_ids.ndim == 3
    assert leaves_feat_ids.shape[0] == num_trees
    assert leaves_feat_ids.shape[1] == num_leaves
    leaves_num_features = leaves_feat_ids.shape[2]
    assert leaves_coefs.ndim == 4
    assert leaves_coefs.shape[0] == num_trees
    assert leaves_coefs.shape[1] == num_leaves
    num_out = leaves_coefs.shape[2]
    assert leaves_coefs.shape[3] == leaves_num_features + 1

    output_dtype = features.dtype
    output = np.zeros((num_samples, num_out), dtype=output_dtype)
    outputs_trees = np.empty((num_trees, num_out), dtype=output_dtype)
    for sample_id in range(num_samples):
        outputs_trees.fill(0)
        for tree_id in numba.prange(num_trees):
            nodes = np.empty((2**depth), dtype=np.uint32)
            weights = np.empty((2**depth), dtype=output_dtype)
            nodes[0] = 0
            weights[0] = 1.0
            len_nodes = 1
            prev_subtree_num_nodes = 0
            subtree_num_nodes = 1
            for _ in range(depth - 1):
                for subtree_node_id in range(prev_subtree_num_nodes, subtree_num_nodes):
                    node = nodes[subtree_node_id]
                    weight = weights[subtree_node_id]
                    feature_id = split_feat_ids[tree_id, node]
                    thresh, coef = split_coefs[tree_id, node]
                    feature_value = features[sample_id, feature_id]

                    t_weight = coef * (feature_value - thresh)
                    s_weight = smooth_step(t_weight)

                    if s_weight < 1:
                        # keep the left node
                        nodes[len_nodes] = 2 * node + 1
                        weights[len_nodes] = (1 - s_weight) * weight
                        len_nodes += 1

                    if s_weight > 0:
                        # keep the right node
                        nodes[len_nodes] = 2 * node + 2
                        weights[len_nodes] = s_weight * weight
                        len_nodes += 1

                prev_subtree_num_nodes = subtree_num_nodes
                subtree_num_nodes = len_nodes

            for subtree_node_id in range(prev_subtree_num_nodes, subtree_num_nodes):
                node = nodes[subtree_node_id]
                weight = weights[subtree_node_id]
                leaf_index = node - num_split_nodes

                if leaves_num_features > 0:
                    leaf_features_ids = leaves_feat_ids[tree_id, leaf_index, :]
                    leaf_feature_values = features[sample_id][leaf_features_ids]
                    leaf_coefs = leaves_coefs[tree_id, leaf_index, :, :]
                    bias = leaf_coefs[:, -1]
                    outputs_trees[tree_id] += weight * (
                        leaf_coefs[:, :-1].dot(leaf_feature_values) + bias
                    )
                else:
                    outputs_trees[tree_id] += (
                        weight * leaves_coefs[tree_id, leaf_index, :, 0]
                    )
        output[sample_id] = outputs_trees.sum(axis=0)

    return output
