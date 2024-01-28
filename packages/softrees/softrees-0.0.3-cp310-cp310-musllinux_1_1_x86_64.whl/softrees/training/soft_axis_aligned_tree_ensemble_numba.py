"""Module that implements the numba accelerated function for the soft tree ensemble"""
from typing import Tuple

import numba
import numpy as np
from numba import njit

from ..runtime.soft_oblique_tree_ensemble_numba import (
    smooth_abs,
    smooth_abs_deriv,
    smooth_step,
    smooth_step_deriv,
)


@njit(cache=True, boundscheck=False, fastmath=True)
def soft_tree_ensemble_axis_aligned_backward(
    features: np.ndarray,
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
    active_tol: float,
    abs_tol: float,
    output_grad: np.ndarray,
    num_active_leaves_average_grad: np.ndarray,
    leaves_frequency_grad: np.ndarray,
    mean_decision_abs_distance_grad: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
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
    assert leaves_coefs.shape[3] == leaves_num_features + 1

    leaves_coefs_grad = np.zeros_like(leaves_coefs)
    split_coefs_grad = np.zeros_like(split_coefs)
    features_grad = np.zeros_like(features)

    depth_num_nodes = np.zeros((depth + 1), dtype=np.uint32)
    for sample_id in range(num_samples):
        for tree_id in numba.prange(num_trees):
            nodes = [0]
            weights = [1.0]
            actives = [1.0]
            subtree_node_id = 0
            depth_num_nodes[0] = 0
            depth_num_nodes[1] = 1
            for k in range(depth - 1):
                for subtree_node_id in range(
                    depth_num_nodes[k], depth_num_nodes[k + 1]
                ):
                    node = nodes[subtree_node_id]
                    weight = weights[subtree_node_id]
                    active = actives[subtree_node_id]
                    feature_id = split_feat_ids[tree_id, node]
                    thresh, coef = split_coefs[tree_id, node]
                    feature_value = features[sample_id, feature_id]

                    t_weight = coef * (feature_value - thresh)
                    s_weight = smooth_step(t_weight)

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
                depth_num_nodes[k + 2] = len(nodes)

            weights_grad = np.zeros((len(weights),))
            actives_grad = np.zeros((len(weights),))
            k = depth - 1
            for subtree_node_id in range(depth_num_nodes[k], depth_num_nodes[k + 1]):
                node = nodes[subtree_node_id]
                weight = weights[subtree_node_id]
                leaf_index = node - num_split_nodes

                leaf_features_ids = leaves_feat_ids[tree_id, leaf_index, :]
                leaf_feature_values = features[sample_id][leaf_features_ids]
                leaf_coefs = leaves_coefs[tree_id, leaf_index, :, :]

                bias = leaf_coefs[:, -1]
                weight_grad = np.sum(
                    output_grad[sample_id]
                    * (leaf_coefs[:, :-1].dot(leaf_feature_values) + bias)
                )
                leaves_coefs_grad[tree_id, leaf_index, :, -1] += (
                    output_grad[sample_id] * weight
                )
                leaves_coefs_grad[tree_id, leaf_index, :, :-1] += (
                    np.expand_dims(output_grad[sample_id], 1)
                    * leaf_feature_values
                    * weight
                )
                features_grad[sample_id][leaf_features_ids] += (
                    output_grad[sample_id].dot(leaf_coefs[:, :-1]) * weight
                )

                weight_grad += leaves_frequency_grad[tree_id, leaf_index] / num_samples
                weights_grad[subtree_node_id] += weight_grad
                actives_grad[subtree_node_id] += num_active_leaves_average_grad[
                    sample_id
                ]
            for k in range(depth - 2, -1, -1):
                child_subtree_node_id = depth_num_nodes[k + 1]
                for subtree_node_id in range(
                    depth_num_nodes[k], depth_num_nodes[k + 1]
                ):
                    node = nodes[subtree_node_id]
                    weight = weights[subtree_node_id]
                    active = actives[subtree_node_id]
                    feature_id = split_feat_ids[tree_id, node]
                    thresh, coef = split_coefs[tree_id, node]
                    feature_value = features[sample_id, feature_id]

                    t_weight = coef * (feature_value - thresh)
                    s_weight = smooth_step(t_weight)
                    # to have an upper bound on the number of activated leaves we want s2 to be one when s>0

                    t_left = (0.5 + active_tol * 0.5 - t_weight) / active_tol
                    s_left = smooth_step(t_left)
                    t_right = (0.5 + active_tol * 0.5 + t_weight) / active_tol
                    s_right = smooth_step(t_right)

                    s_weight_grad = 0
                    weight_grad = 0
                    active_grad = 0
                    s_left_grad = 0
                    s_right_grad = 0
                    if s_left > 0:
                        s_weight_grad += -weight * weights_grad[child_subtree_node_id]
                        s_left_grad += active * actives_grad[child_subtree_node_id]
                        weight_grad += (1 - s_weight) * weights_grad[
                            child_subtree_node_id
                        ]
                        active_grad += s_left * actives_grad[child_subtree_node_id]
                        child_subtree_node_id += 1
                    if s_right > 0:
                        s_weight_grad += weight * weights_grad[child_subtree_node_id]
                        s_right_grad += active * actives_grad[child_subtree_node_id]
                        weight_grad += s_weight * weights_grad[child_subtree_node_id]
                        active_grad += s_right * actives_grad[child_subtree_node_id]
                        child_subtree_node_id += 1

                    weight_grad += mean_decision_abs_distance_grad[
                        sample_id
                    ] * smooth_abs(t_weight, abs_tol)

                    weights_grad[subtree_node_id] = weight_grad
                    actives_grad[subtree_node_id] = active_grad

                    t_right_grad = smooth_step_deriv(t_right) * s_right_grad
                    t_left_grad = smooth_step_deriv(t_left) * s_left_grad
                    t_weight_grad = smooth_step_deriv(t_weight) * s_weight_grad

                    t_weight_grad += (
                        weight
                        * mean_decision_abs_distance_grad[sample_id]
                        * smooth_abs_deriv(t_weight, abs_tol)
                    )

                    if t_left_grad != 0:
                        t_weight_grad += -t_left_grad / active_tol
                    if t_right_grad != 0:
                        t_weight_grad += t_right_grad / active_tol

                    if t_weight_grad != 0:
                        coef_grad = t_weight_grad * (feature_value - thresh)
                        thresh_grad = -t_weight_grad * coef
                        split_coefs_grad[tree_id, node, 0] += thresh_grad
                        split_coefs_grad[tree_id, node, 1] += coef_grad
                        feature_value_grad = t_weight_grad * coef
                        features_grad[sample_id, feature_id] += feature_value_grad

    return split_coefs_grad, leaves_coefs_grad, features_grad
