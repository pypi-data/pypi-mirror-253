"""Generalization of the Tree Ensemble Layer."""

from typing import Any, Tuple

import numpy as np
import torch
from numba import njit

from softrees.runtime.soft_tree_ensemble import SoftTreeEnsembleTrainedParameters
from softrees.runtime.soft_tree_ensemble_common import soft_tree_ensemble_forward
from softrees.training.soft_tree_ensemble_api import SoftTreeEnsembleLayerOptions
from softrees.training.soft_tree_ensemble_common import soft_tree_ensemble_backward


@njit
def numba_set_seed(value: int) -> None:
    """Reset la seed pour numba meme si l'appel est np.random.seed(value)"""
    np.random.seed(value)
    pass


def set_random_seed(seed: int) -> None:
    np.random.seed(seed)
    numba_set_seed(seed)
    torch.manual_seed(seed)


def smooth_step_vec(t: torch.Tensor) -> torch.Tensor:
    t_clipped = t.clip(-0.5, 0.5)
    return -2 * t_clipped**3 + 1.5 * t_clipped + 0.5


class SoftTreeEnsembleFunction(torch.autograd.Function):
    """Class to expose a SoftTreeEnsemble as a pytorch function"""

    @staticmethod
    def forward(  # type: ignore
        ctx: Any,
        features: torch.Tensor,
        split_feat_ids: np.ndarray,
        split_coefs: torch.Tensor,
        leaves_feat_ids: np.ndarray,
        leaves_coefs: torch.Tensor,
        depth: int,
        active_tol: float,
        abs_tol: float,
        oblique: bool,
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        ctx.split_feat_ids = split_feat_ids
        ctx.split_coefs = split_coefs.detach().numpy()
        ctx.depth = depth
        ctx.features = features.detach().numpy()
        ctx.leaves_feat_ids = leaves_feat_ids
        ctx.leaves_coefs = leaves_coefs.detach().numpy()
        ctx.oblique = oblique
        ctx.active_tol = active_tol
        ctx.abs_tol = abs_tol

        (
            output,
            num_active_leave_average,
            leaves_frequency,
            mean_decision_abs_distance,
        ) = soft_tree_ensemble_forward(
            split_feat_ids=ctx.split_feat_ids,
            split_coefs=ctx.split_coefs,
            leaves_feat_ids=ctx.leaves_feat_ids,
            leaves_coefs=ctx.leaves_coefs,
            depth=ctx.depth,
            features=ctx.features,
            active_tol=ctx.active_tol,
            abs_tol=ctx.abs_tol,
            oblique=ctx.oblique,
        )

        return (
            torch.as_tensor(output),
            torch.as_tensor(num_active_leave_average),
            torch.as_tensor(leaves_frequency),
            torch.as_tensor(mean_decision_abs_distance),
        )

    @staticmethod
    def backward(ctx: Any, *grad_outputs: Any) -> Any:
        (
            output_grad,
            num_active_leaves_average_grad,
            leaves_frequency_grad,
            mean_decision_abs_distance_grad,
        ) = grad_outputs

        (
            split_coefs_grad,
            leaves_coefs_grad,
            features_grad,
        ) = soft_tree_ensemble_backward(
            features=ctx.features,
            split_feat_ids=ctx.split_feat_ids,
            split_coefs=ctx.split_coefs,
            leaves_feat_ids=ctx.leaves_feat_ids,
            leaves_coefs=ctx.leaves_coefs,
            depth=ctx.depth,
            active_tol=ctx.active_tol,
            abs_tol=ctx.abs_tol,
            oblique=ctx.oblique,
            output_grad=output_grad.numpy(),
            num_active_leaves_average_grad=num_active_leaves_average_grad.numpy(),
            leaves_frequency_grad=leaves_frequency_grad.numpy(),
            mean_decision_abs_distance_grad=mean_decision_abs_distance_grad.numpy(),
        )

        return (
            torch.as_tensor(features_grad),
            None,
            torch.as_tensor(split_coefs_grad),
            None,
            torch.as_tensor(leaves_coefs_grad),
            None,
            None,
            None,
            None,
            None,
        )


def create_random_initial_parameters(
    options: SoftTreeEnsembleLayerOptions,
) -> SoftTreeEnsembleTrainedParameters:
    num_split_nodes = 2 ** (options.depth - 1) - 1
    num_leaves = 2 ** (options.depth - 1)

    num_leaf_features = (
        options.in_features
        if options.num_leaf_features is None
        else options.num_leaf_features
    )

    if options.random_seed is not None:
        set_random_seed(options.random_seed)

    # initialize leaves feature ids and coefficients
    r = np.random.rand(options.num_trees, num_leaves, options.in_features)
    leaves_feat_ids = np.sort(
        np.argsort(r, axis=2)[:, :, :num_leaf_features], axis=2
    ).astype(np.uint32)
    stddevs = np.ones((num_leaf_features + 1)) * np.sqrt(1 / (num_leaf_features + 1))
    # stds[0] = 0.2  # might require some tunning

    dtype = np.float32 if options.float32 else np.float64

    leaves_coefs = (
        np.random.randn(
            options.num_trees,
            num_leaves,
            options.out_features,
            num_leaf_features + 1,
        )
        * stddevs
    ).astype(dtype)

    if options.oblique:
        num_split_feat = (
            options.in_features
            if options.num_split_feat is None
            else options.num_split_feat
        )
        assert 0 < num_split_feat <= options.in_features

        # Unlike in the Trees paper, we have to choose in advance which feature we choose
        r = np.random.rand(options.num_trees, num_split_nodes, options.in_features)
        split_feat_ids = np.sort(
            np.argsort(r, axis=2)[:, :, :num_split_feat], axis=2
        ).astype(np.uint32)

        stddev = np.sqrt(1 / (num_split_feat))
        split_coefs_slope = (
            np.random.randn(options.num_trees, num_split_nodes, num_split_feat) * stddev
        ).astype(dtype)
        split_bias = (
            np.random.randn(options.num_trees, num_split_nodes) * stddev
        ).astype(dtype)

        split_coefs = np.dstack((split_coefs_slope, split_bias))

    else:
        assert options.num_split_feat is None or options.num_split_feat == 1
        num_split_feat = 1
        # Unlike in the Trees paper, we have to choose in advance which feature we choose
        split_feat_ids = np.floor(
            np.random.rand(options.num_trees, num_split_nodes) * options.in_features
        ).astype(np.uint32)
        stds = np.array([0.1, 0.5])
        split_coefs = (
            np.random.randn(options.num_trees, num_split_nodes, 2) * stds
        ).astype(dtype)

    parameters = SoftTreeEnsembleTrainedParameters(
        split_feat_ids=split_feat_ids,
        split_coefs=split_coefs,
        leaves_feat_ids=leaves_feat_ids,
        leaves_coefs=leaves_coefs,
        depth=options.depth,
        active_tol=options.active_tol,
        abs_tol=options.abs_tol,
        oblique=options.oblique,
        in_features=options.in_features,
    )

    return parameters


class SoftTreeEnsembleLayer(torch.nn.Module):
    """Class to expose a SoftTreeEnsemble as a pytorch layer"""

    def __init__(self, options: SoftTreeEnsembleLayerOptions) -> None:
        super().__init__()
        self._num_split_nodes = 2 ** (options.depth - 1) - 1
        self._num_leaves = 2 ** (options.depth - 1)
        self._options = options

        init_parameters = create_random_initial_parameters(options=options)

        self._leaves_feat_ids = init_parameters.leaves_feat_ids

        # TODO use xavier initialization with zero bias ?
        self._leaves_coefs = torch.nn.parameter.Parameter(
            torch.from_numpy(init_parameters.leaves_coefs)
        )

        if self._options.oblique:
            self._split_feat_ids = init_parameters.split_feat_ids
            self._split_coefs = torch.nn.parameter.Parameter(
                torch.from_numpy(init_parameters.split_coefs)
            )
        else:
            # Unlike in the Trees paper, we have to choose in advance which feature we choose
            self._split_feat_ids = init_parameters.split_feat_ids
            self._split_coefs = torch.nn.parameter.Parameter(
                torch.from_numpy(init_parameters.split_coefs)
            )

    @property
    def depth(self) -> int:
        return self._options.depth

    @property
    def float32(self) -> bool:
        return self._options.float32

    @property
    def in_features(self) -> int:
        return self._options.in_features

    @property
    def out_features(self) -> int:
        return self._options.out_features

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        assert x.ndim == 2
        assert x.shape[1] == self.in_features
        (
            pred_batch,
            num_active_leaves_average,
            leaves_frequency,
            mean_decision_abs_distance,
        ) = SoftTreeEnsembleFunction.apply(
            x,
            self._split_feat_ids,
            self._split_coefs,
            self._leaves_feat_ids,
            self._leaves_coefs,
            self._options.depth,
            self._options.active_tol,
            self._options.abs_tol,
            self._options.oblique,
        )

        regularization_loss = self.regularization_loss(
            num_active_leaves_average=num_active_leaves_average,
            leaves_frequency=leaves_frequency,
            mean_decision_abs_distance=mean_decision_abs_distance,
        )

        return pred_batch, regularization_loss

    def forward_tensor(self, x: torch.Tensor) -> torch.Tensor:
        assert self._options.oblique
        num_trees = self._split_coefs.shape[0]
        num_samples = x.shape[0]

        if self._options.num_split_feat is None:
            # all the features are used in the split decision
            t = (
                x.matmul(
                    self._split_coefs[:, :, :-1]
                    .reshape(num_trees * self._num_split_nodes, -1)
                    .transpose(0, 1)
                )
            ).reshape(
                num_samples, num_trees, self._num_split_nodes
            ) + self._split_coefs[
                :, :, -1
            ]
            s = smooth_step_vec(t)

            a_layer = torch.ones(x.shape[0], num_trees, 1)
            for depth in range(0, self.depth - 1):
                node_ids_begin = 2 ** (depth) - 1
                node_ids_end = 2 ** (depth + 1) - 1
                s_layer = s[:, :, node_ids_begin:node_ids_end]
                a_layer = (
                    a_layer[:, :, :, None]
                    * torch.stack(((1 - s_layer), s_layer), dim=3)
                ).reshape(num_samples, num_trees, -1)
            a_leaves = a_layer

        else:
            # as subset of features are used at each split decision
            a_nodes = {}
            a_nodes[0] = torch.ones(x.shape[0], num_trees)
            for node_id in range(self._num_split_nodes):
                # TODO try to use matrix multiplication to avoid the sum
                t = self._split_coefs[:, node_id, -1] + (
                    self._split_coefs[:, node_id, :-1]
                    * x[:, self._split_feat_ids[:, node_id, :]]
                ).sum(dim=2)
                s = smooth_step_vec(t)
                a_nodes[2 * node_id + 1] = a_nodes[node_id] * (1 - s)
                a_nodes[2 * node_id + 2] = a_nodes[node_id] * s

            a_leaves = torch.dstack(
                [
                    a_nodes[leaf_index + self._num_split_nodes]
                    for leaf_index in range(self._num_leaves)
                ]
            )
        # TODO solve inconsistency between position of constant in split and leaf coefs
        if self._leaves_feat_ids.size > 0:
            # TODO try to use matrix multiplication to avoid the sum
            pred_batch = (
                a_leaves[:, :, :, None]
                * (
                    (
                        self._leaves_coefs[:, :, :, :-1]
                        * x[:, self._leaves_feat_ids][:, :, :, None, :]
                    ).sum(dim=4)
                    + self._leaves_coefs[:, :, :, -1]
                )
            ).sum(dim=[1, 2])
        else:
            assert self._leaves_coefs.shape[3] == 1

            num_trees = self._leaves_coefs.shape[0]
            pred_batch = a_leaves.reshape(num_samples, -1).matmul(
                self._leaves_coefs.reshape(num_trees * self._num_leaves, -1)
            )

        return pred_batch

    def regularization_loss(
        self,
        num_active_leaves_average: torch.Tensor,
        leaves_frequency: torch.Tensor,
        mean_decision_abs_distance: torch.Tensor,
    ) -> torch.Tensor:
        sparsity_leaves = torch.mean(num_active_leaves_average)
        sparse_leaves_cost = self._options.sparse_leaves_coef * sparsity_leaves

        splitcoef_square_norms = (
            torch.sum(self._split_coefs[:, :, :-1] ** 2, dim=2) + 1e-5
        )

        coefs_cost = self._options.regu_split_coef * torch.sum(
            self._split_coefs[:, :, :-1] ** 2
        ) + self._options.regu_inv_split_coef * torch.sum(1 / splitcoef_square_norms)

        leaves_coef_cost = self._options.regu_leaves * torch.sum(
            self._leaves_coefs[:, :, :-1] ** 2
        )

        # Note: that cost makes sense only for very large batches
        # as it compute frequencies of samples reaching the leaves
        balancing_cost = self._options.balancing_cost_coef * (
            torch.sum(leaves_frequency**2) - 1 / self._num_leaves
        )

        # term that penalizes the absolute distance from the split decision
        # center for each sample that arrive at a node in order to get the split near the median
        # i.e have balanced samples after the split at the node.
        # This term is probably softer that the balancing_cost defined above.
        distance_cost = self._options.mean_decision_abs_distance_coef * torch.mean(
            mean_decision_abs_distance
        )
        return (
            sparse_leaves_cost
            + coefs_cost
            + leaves_coef_cost
            + balancing_cost
            + distance_cost
        )

    def test_gradient(
        self,
        x: np.ndarray,
    ) -> None:
        assert x.ndim == 2
        assert x.shape[1] == self._options.in_features
        torch.autograd.gradcheck(
            SoftTreeEnsembleFunction.apply,
            (  # type: ignore
                torch.from_numpy(x),
                self._split_feat_ids,
                self._split_coefs,
                self._leaves_feat_ids,
                self._leaves_coefs,
                self._options.depth,
                self._options.active_tol,
                self._options.abs_tol,
                self._options.oblique,
            ),
            eps=1e-6,
            atol=1e-8,
            rtol=1e-5,
        )
