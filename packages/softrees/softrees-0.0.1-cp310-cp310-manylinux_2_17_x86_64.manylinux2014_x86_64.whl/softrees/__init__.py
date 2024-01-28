# -*- coding: utf-8 -*-
"""Smoothed regression tree ensemble trained with gradient descent"""
__version__ = "0.0.1"

__all__ = [
    "SoftTreeEnsemble",
    "AxisAlignedTrees",
    "SoftTreeEnsembleTrainingOptions",
    "SoftTreeEnsembleLayerOptions",
    "SoftTreeEnsembleTrainer",
]


from .runtime.hard_axis_aligned_tree_ensemble import AxisAlignedTrees
from .runtime.soft_tree_ensemble import SoftTreeEnsemble
from .training.soft_tree_ensemble_api import (
    SoftTreeEnsembleLayerOptions,
    SoftTreeEnsembleTrainingOptions,
)
from .training.soft_tree_ensemble_training import SoftTreeEnsembleTrainer
