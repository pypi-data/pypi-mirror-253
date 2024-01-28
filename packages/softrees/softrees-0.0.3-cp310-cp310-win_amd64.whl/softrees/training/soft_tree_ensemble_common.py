"""Common functions for soft tree ensemble."""
from typing import Tuple

import numpy as np

from .soft_axis_aligned_tree_ensemble_numba import (
    soft_tree_ensemble_axis_aligned_backward,
)
from .soft_oblique_tree_ensemble_numba import soft_tree_ensemble_sparse_oblique_backward


def soft_tree_ensemble_backward(
    features: np.ndarray,
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
    active_tol: float,
    abs_tol: float,
    oblique: bool,
    output_grad: np.ndarray,
    num_active_leaves_average_grad: np.ndarray,
    leaves_frequency_grad: np.ndarray,
    mean_decision_abs_distance_grad: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if oblique:
        (
            split_coefs_grad,
            leaves_coefs_grad,
            features_grad,
        ) = soft_tree_ensemble_sparse_oblique_backward(
            features=features,
            split_feat_ids=split_feat_ids,
            split_coefs=split_coefs,
            leaves_feat_ids=leaves_feat_ids,
            leaves_coefs=leaves_coefs,
            depth=depth,
            active_tol=active_tol,
            abs_tol=abs_tol,
            output_grad=output_grad,
            num_active_leaves_average_grad=num_active_leaves_average_grad,
            leaves_frequency_grad=leaves_frequency_grad,
            mean_decision_abs_distance_grad=mean_decision_abs_distance_grad,
        )
    else:
        (
            split_coefs_grad,
            leaves_coefs_grad,
            features_grad,
        ) = soft_tree_ensemble_axis_aligned_backward(
            features=features,
            split_feat_ids=split_feat_ids,
            split_coefs=split_coefs,
            leaves_feat_ids=leaves_feat_ids,
            leaves_coefs=leaves_coefs,
            depth=depth,
            active_tol=active_tol,
            abs_tol=abs_tol,
            output_grad=output_grad,
            num_active_leaves_average_grad=num_active_leaves_average_grad,
            leaves_frequency_grad=leaves_frequency_grad,
            mean_decision_abs_distance_grad=mean_decision_abs_distance_grad,
        )

    return split_coefs_grad, leaves_coefs_grad, features_grad
