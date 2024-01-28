"""Module that implements the evaluation of the soft tree ensemble"""

from dataclasses import dataclass

import numpy as np

from .soft_tree_ensemble_common import (
    soft_tree_ensemble_forward,
    soft_tree_ensemble_forward_fast,
)


@dataclass
class SoftTreeEnsembleTrainedParameters:
    """Parameters of the soft tree obtained after training"""

    split_feat_ids: np.ndarray
    split_coefs: np.ndarray
    leaves_feat_ids: np.ndarray
    leaves_coefs: np.ndarray
    depth: int
    active_tol: float
    abs_tol: float
    oblique: bool
    in_features: int

    def __post_init__(self) -> None:
        """Do some checks"""
        assert self.split_feat_ids.dtype == np.uint32
        assert self.leaves_feat_ids.dtype == np.uint32
        assert self.split_coefs.dtype in [np.float32, np.float64]
        assert self.leaves_coefs.dtype == self.split_coefs.dtype

    def tofloat32(self) -> "SoftTreeEnsembleTrainedParameters":
        return SoftTreeEnsembleTrainedParameters(
            split_feat_ids=self.split_feat_ids,
            split_coefs=self.split_coefs.astype(np.float32),
            leaves_feat_ids=self.leaves_feat_ids,
            leaves_coefs=self.leaves_coefs.astype(np.float32),
            depth=self.depth,
            active_tol=self.active_tol,
            abs_tol=self.abs_tol,
            oblique=self.oblique,
            in_features=self.in_features,
        )


class SoftTreeEnsemble:
    """Class to evaluate a SoftTreeEnsemble"""

    def __init__(
        self,
        trained_parameters: SoftTreeEnsembleTrainedParameters,
        method: str = "numba",
        num_max_procs: int = 0,
    ):
        self._trained_parameters = trained_parameters
        self._method = method
        self._num_max_procs = num_max_procs

    def tofloa32(self) -> "SoftTreeEnsemble":
        return SoftTreeEnsemble(trained_parameters=self._trained_parameters.tofloat32())

    def set_method(self, method: str) -> None:
        self._method = method

    def set_num_max_procs(self, num_max_procs: int) -> None:
        self._num_max_procs = num_max_procs

    @property
    def input_dtype(self) -> np.dtype:
        return self._trained_parameters.split_coefs.dtype

    def predict(self, x: np.ndarray) -> np.ndarray:
        assert x.ndim == 2
        assert x.shape[1] == self._trained_parameters.in_features
        assert self._trained_parameters is not None, "You need to fit the model first."

        assert x.dtype == self.input_dtype

        output = soft_tree_ensemble_forward_fast(
            features=x,
            split_feat_ids=self._trained_parameters.split_feat_ids,
            split_coefs=self._trained_parameters.split_coefs,
            leaves_feat_ids=self._trained_parameters.leaves_feat_ids,
            leaves_coefs=self._trained_parameters.leaves_coefs,
            depth=self._trained_parameters.depth,
            oblique=self._trained_parameters.oblique,
            method=self._method,
            num_max_procs=self._num_max_procs,
        )
        return output

    def count_active_leaves_average(self, x: np.ndarray) -> np.ndarray:
        assert x.ndim == 2
        assert x.shape[1] == self._trained_parameters.in_features
        assert self._trained_parameters is not None, "You need to fit the model first."
        dtype = self._trained_parameters.leaves_coefs.dtype
        _, num_active_leave_average, _, _ = soft_tree_ensemble_forward(
            features=x.astype(dtype),
            split_feat_ids=self._trained_parameters.split_feat_ids,
            split_coefs=self._trained_parameters.split_coefs,
            leaves_feat_ids=self._trained_parameters.leaves_feat_ids,
            leaves_coefs=self._trained_parameters.leaves_coefs,
            depth=self._trained_parameters.depth,
            oblique=self._trained_parameters.oblique,
            active_tol=self._trained_parameters.active_tol,
            abs_tol=self._trained_parameters.abs_tol,
        )
        return num_active_leave_average
