"""API for the tree ensemble"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class SoftTreeEnsembleTrainingOptions:
    """Options for the SoftTreeEnsemble training"""

    batch_size: int
    num_epoch: float
    learning_rate: float
    classification: bool
    greedy_init: bool
    test_gradient: bool
    greedy_init_mu: float = 1
    greedy_init_num_test_splits: int = 200
    verbose: bool = True
    data_coef: float = 1
    conditional_compute: bool = True


@dataclass
class SoftTreeEnsembleLayerOptions:
    """Options for the SoftTreeEnsemble"""

    active_tol: float
    abs_tol: float
    depth: int
    num_trees: int
    in_features: int
    out_features: int
    oblique: bool
    num_split_feat: Optional[int] = None
    num_leaf_features: Optional[int] = None
    random_seed: Optional[int] = None
    sparse_leaves_coef: float = 1e-3
    balancing_cost_coef: float = 1e-4
    mean_decision_abs_distance_coef: float = 1e-4
    regu_split_coef: float = 1e-4
    regu_inv_split_coef: float = 0
    regu_leaves: float = 1e-7
    float32: bool = True

    def __post_init__(self) -> None:
        """Do some checks."""
        assert self.depth >= 1
        assert (
            self.num_leaf_features is None
            or 0 <= self.num_leaf_features <= self.in_features
        )
        assert self.sparse_leaves_coef >= 0
        assert self.balancing_cost_coef >= 0
        if not self.oblique:
            assert self.num_split_feat is None or self.num_split_feat == 1
        else:
            assert (
                self.num_split_feat is None
                or 0 < self.num_split_feat <= self.in_features
            )
