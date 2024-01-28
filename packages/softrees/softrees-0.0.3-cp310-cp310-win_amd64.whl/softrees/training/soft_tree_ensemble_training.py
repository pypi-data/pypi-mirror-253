"""Module that implements the training of the soft tree ensemble"""
import numpy as np

from ..pytorch.soft_tree_ensemble_train import fit_pytorch
from ..runtime.soft_tree_ensemble import SoftTreeEnsemble
from .soft_tree_ensemble_api import (
    SoftTreeEnsembleLayerOptions,
    SoftTreeEnsembleTrainingOptions,
)


class SoftTreeEnsembleTrainer:
    """Class to train an SoftTreeEnsemble"""

    def __init__(
        self,
        options: SoftTreeEnsembleLayerOptions,
        training_options: SoftTreeEnsembleTrainingOptions,
    ):
        self._training_options = training_options
        self._options = options

    def fit(self, x: np.ndarray, y: np.ndarray) -> SoftTreeEnsemble:
        # TODO would be good to import pytorch only when training
        trained_parameters = fit_pytorch(
            x=x, y=y, options=self._options, training_options=self._training_options
        )
        return SoftTreeEnsemble(trained_parameters=trained_parameters)
