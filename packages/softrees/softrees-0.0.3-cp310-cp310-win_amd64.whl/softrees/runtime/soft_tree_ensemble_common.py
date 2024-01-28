"""Common functions for soft tree ensemble."""
from typing import Tuple

import numpy as np

from ..runtime.soft_axis_aligned_tree_ensemble_numba import (
    soft_tree_ensemble_axis_aligned_forward,
    soft_tree_ensemble_axis_aligned_forward_fast,
)
from .soft_oblique_tree_ensemble_c import (
    soft_tree_ensemble_sparse_oblique_forward_fast_double_cpp,
    soft_tree_ensemble_sparse_oblique_forward_fast_float_cpp,
)
from .soft_oblique_tree_ensemble_cython import (
    soft_tree_ensemble_sparse_oblique_forward_fast as soft_tree_ensemble_sparse_oblique_forward_fast_cython,
)
from .soft_oblique_tree_ensemble_numba import (
    soft_tree_ensemble_sparse_oblique_forward,
    soft_tree_ensemble_sparse_oblique_forward_fast,
)


def soft_tree_ensemble_forward(
    features: np.ndarray,
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
    active_tol: float,
    abs_tol: float,
    oblique: bool,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if oblique:
        (
            output,
            num_active_leave_average,
            leaves_frequency,
            mean_decision_abs_distance,
        ) = soft_tree_ensemble_sparse_oblique_forward(
            split_feat_ids=split_feat_ids,
            split_coefs=split_coefs,
            leaves_feat_ids=leaves_feat_ids,
            leaves_coefs=leaves_coefs,
            depth=depth,
            features=features,
            active_tol=active_tol,
            abs_tol=abs_tol,
        )
    else:
        (
            output,
            num_active_leave_average,
            leaves_frequency,
            mean_decision_abs_distance,
        ) = soft_tree_ensemble_axis_aligned_forward(
            split_feat_ids=split_feat_ids,
            split_coefs=split_coefs,
            leaves_feat_ids=leaves_feat_ids,
            leaves_coefs=leaves_coefs,
            depth=depth,
            features=features,
            active_tol=active_tol,
            abs_tol=abs_tol,
        )
    return (
        output,
        num_active_leave_average,
        leaves_frequency,
        mean_decision_abs_distance,
    )


def soft_tree_ensemble_forward_fast(
    features: np.ndarray,
    split_feat_ids: np.ndarray,
    split_coefs: np.ndarray,
    leaves_feat_ids: np.ndarray,
    leaves_coefs: np.ndarray,
    depth: int,
    oblique: bool,
    method: str = "numba",
    num_max_procs: int = 0,
) -> np.ndarray:
    if oblique:
        if method == "numba":
            output = soft_tree_ensemble_sparse_oblique_forward_fast(
                features=features,
                split_feat_ids=split_feat_ids,
                split_coefs=split_coefs,
                leaves_feat_ids=leaves_feat_ids,
                leaves_coefs=leaves_coefs,
                depth=depth,
            )
        elif method == "cython":
            output = soft_tree_ensemble_sparse_oblique_forward_fast_cython(
                features=features,
                split_feat_ids=split_feat_ids,
                split_coefs=split_coefs,
                leaves_feat_ids=leaves_feat_ids,
                leaves_coefs=leaves_coefs,
                depth=depth,
            )
        elif method == "cpp":
            if leaves_coefs.dtype == np.float64:
                output = soft_tree_ensemble_sparse_oblique_forward_fast_double_cpp(
                    features=features,
                    split_feat_ids=split_feat_ids,
                    split_coefs=split_coefs,
                    leaves_feat_ids=leaves_feat_ids,
                    leaves_coefs=leaves_coefs,
                    depth=depth,
                )
            else:
                output = soft_tree_ensemble_sparse_oblique_forward_fast_float_cpp(
                    features=features,
                    split_feat_ids=split_feat_ids,
                    split_coefs=split_coefs,
                    leaves_feat_ids=leaves_feat_ids,
                    leaves_coefs=leaves_coefs,
                    depth=depth,
                    num_max_procs=num_max_procs,
                )
        else:
            raise ValueError(f"Ubnkown method {method}")
    else:
        output = soft_tree_ensemble_axis_aligned_forward_fast(
            split_feat_ids=split_feat_ids,
            split_coefs=split_coefs,
            leaves_feat_ids=leaves_feat_ids,
            leaves_coefs=leaves_coefs,
            depth=depth,
            features=features,
        )
    return output
