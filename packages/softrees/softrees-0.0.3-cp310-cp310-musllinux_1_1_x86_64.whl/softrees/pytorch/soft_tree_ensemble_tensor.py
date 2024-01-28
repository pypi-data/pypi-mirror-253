"""Reimplementing FASTEL in pytorch
original tensorflow code https://github.com/ShibalIbrahim/FASTEL
"""
from typing import Optional

import torch


def smooth_step(t: torch.Tensor) -> torch.Tensor:
    t_clipped = t.clip(-0.5, 0.5)
    return -2 * t_clipped**3 + 1.5 * t_clipped + 0.5


class SoftTreeEnsembleLayerTensor(torch.nn.Module):
    """Pytorch implementation of FASTEL
    original tensorflow code https://github.com/ShibalIbrahim/FASTEL
    """

    def __init__(
        self,
        in_features: int,
        num_trees: int,
        max_depth: int,
        out_features: int,
        node_index: int = 0,
        float32: bool = False,
    ):
        super().__init__()
        self.in_features = in_features
        self.max_depth = max_depth
        self.out_features = out_features
        self.num_trees = num_trees
        self.node_index = node_index
        self.leaf = node_index >= 2**max_depth - 1
        self.float32 = float32
        dtype = torch.float32 if float32 else torch.float64
        if not self.leaf:
            self.dense_layer = torch.nn.Linear(
                in_features, self.num_trees, bias=True, dtype=dtype
            )
            self.left_child = self.__class__(
                in_features,
                self.num_trees,
                self.max_depth,
                self.out_features,
                node_index=2 * self.node_index + 1,
            )
            self.right_child = self.__class__(
                in_features,
                self.num_trees,
                self.max_depth,
                self.out_features,
                node_index=2 * self.node_index + 2,
            )

        else:
            # self.leaf_weight = torch.nn.Parameter(
            #     torch.randn(size=[1, self.out_features, self.num_trees], dtype=dtype)
            # )

            rank = 3
            self.leaf_weight_1 = torch.nn.Parameter(
                torch.randn(size=[in_features + 1, rank, self.num_trees], dtype=dtype)
            )
            self.leaf_weight_2 = torch.nn.Parameter(
                torch.randn(size=[10, self.out_features, self.num_trees], dtype=dtype)
            )

    def forward(
        self, x: torch.Tensor, prob: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        if not self.leaf:
            current_prob = smooth_step(self.dense_layer(x))
            if prob is None:
                return self.left_child(x, current_prob) + self.right_child(
                    x, (1 - current_prob)
                )
            else:
                return self.left_child(x, current_prob * prob) + self.right_child(
                    x, (1 - current_prob) * prob
                )
        else:
            assert prob is not None
            output = prob[:, None, :] * self.leaf_weight
            output = torch.sum(output, dim=2)
            return output
