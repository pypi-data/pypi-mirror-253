"""Training the soft regression tree ensemble using a pytorch optimizer"""
import time
from math import ceil
from typing import Callable, Optional, Union

import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset

from softrees.pytorch.soft_tree_ensemble_layer import SoftTreeEnsembleLayer
from softrees.runtime.soft_tree_ensemble import SoftTreeEnsembleTrainedParameters
from softrees.training.greedy_hard_axis_aligned_tree_ensemble import (
    AxisAlignedTrees,
    GreedyAxisAlignedTreesTrainer,
)
from softrees.training.greedy_soft_oblique_tree_ensemble import (
    GreedySoftObliqueTreesTrainer,
    SoftTreeEnsemble,
)
from softrees.training.soft_tree_ensemble_api import (
    SoftTreeEnsembleLayerOptions,
    SoftTreeEnsembleTrainingOptions,
)


def fit_layer(
    layer: SoftTreeEnsembleLayer,
    x: np.ndarray,
    y: np.ndarray,
    training_options: SoftTreeEnsembleTrainingOptions,
    callback: Optional[Callable[["SoftTreeEnsembleLayer"], None]] = None,
) -> None:
    """Fit a tree Ensemble to training data using gradient descent."""
    assert x.ndim == 2
    assert x.shape[1] == layer.in_features

    dtype = np.float32 if layer.float32 else np.float64
    if training_options.classification:
        assert y.ndim == 1
        x_torch = torch.from_numpy(x.astype(dtype))
        y_torch = torch.from_numpy(y)

    else:
        assert y.ndim == 2
        assert y.shape[1] == layer.out_features
        x_torch = torch.from_numpy(x.astype(dtype))
        y_torch = torch.from_numpy(y.astype(dtype))

    dataset = TensorDataset(
        x_torch,
        y_torch,
    )
    assert x.shape[0] == y.shape[0]

    batch_size = (
        x.shape[0] if training_options.batch_size == 0 else training_options.batch_size
    )
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    size = len(x)

    optimizer = torch.optim.Adagrad(
        layer.parameters(), lr=training_options.learning_rate
    )

    if callback is not None:
        assert isinstance(layer, SoftTreeEnsembleLayer)
        callback(layer)
    for epoch in range(ceil(training_options.num_epoch)):
        start = time.time()
        for batch, (x_batch, y_batch) in enumerate(dataloader):
            current = (batch + 1) * len(x_batch)
            epoch_float = epoch + current / size
            if epoch_float > training_options.num_epoch:
                break
            if training_options.conditional_compute:
                # Compute prediction and regularization_loss
                (pred_batch, regularization_loss) = layer.forward(x_batch)
            else:
                pred_batch = layer.forward_tensor(x_batch)

            if training_options.classification:
                data_loss = torch.nn.CrossEntropyLoss()(pred_batch, y_batch)
                data_loss_name = "cross entropy"
            else:
                data_loss = torch.mean((pred_batch - y_batch) ** 2)
                data_loss_name = "mse"

            loss = training_options.data_coef * data_loss
            if training_options.conditional_compute:
                loss += regularization_loss
            # Back-propagation
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            loss_float = loss.item()
            elapsed = time.time() - start
            print(
                f"epoch {epoch}: loss = {loss_float:>7f} "
                f"{data_loss_name} = {data_loss:>7f} "
                # f"regularization_loss = {regularization_loss:>7f} "
                f"{1000*elapsed/(batch+1):0.1f}ms/step"
                f"[{current:>5d}/{size:>5d}] "
            )
        if training_options.classification:
            with torch.no_grad():
                if training_options.conditional_compute:
                    (pred, regularization_loss) = layer.forward(x_torch)
                else:
                    pred = layer.forward_tensor(x_torch)

                predicy = torch.max(pred, 1)[1].data.squeeze()
                accu = (predicy == y_torch).sum() / y_torch.size(0)
                print(f"Accuracy of the model on train data {accu}")

        if callback is not None:
            assert isinstance(layer, SoftTreeEnsembleLayer)
            callback(layer)
    if callback is not None:
        assert isinstance(layer, SoftTreeEnsembleLayer)
        callback(layer)


def convert_axis_aligned_tree_ensemble_to_layer(
    options: SoftTreeEnsembleLayerOptions, reg: AxisAlignedTrees, mu: float
) -> SoftTreeEnsembleLayer:
    assert options.oblique is False
    layer = SoftTreeEnsembleLayer(options)
    layer._split_feat_ids = reg.tree_para.splits[:, :, 0].astype(np.uint32)
    num_trees = reg.tree_para.splits.shape[0]
    dtype = np.float32 if options.float32 else np.float64

    split_coefs = np.dstack(
        (
            reg.tree_para.splits[:, :, 1],
            mu * np.ones((num_trees, layer._num_split_nodes)),
        )
    ).astype(dtype)
    layer._split_coefs = torch.nn.parameter.Parameter(
        torch.from_numpy(split_coefs.astype(dtype))
    )
    layer._leaves_feat_ids = np.zeros((num_trees, layer._num_leaves, 0), np.uint32)
    layer._leaves_coefs = torch.nn.parameter.Parameter(
        torch.from_numpy(reg.tree_para.leaves[:, :, :, None].astype(dtype))
    )
    return layer


def convert_soft_oblique_tree_ensemble_to_layer(
    options: SoftTreeEnsembleLayerOptions, reg: SoftTreeEnsemble, mu: float
) -> SoftTreeEnsembleLayer:
    assert options.oblique is True
    layer = SoftTreeEnsembleLayer(options)
    layer._split_feat_ids = reg._trained_parameters.split_feat_ids
    num_trees = reg._trained_parameters.split_feat_ids.shape[0]
    dtype = np.float32 if options.float32 else np.float64

    layer._split_coefs = torch.nn.parameter.Parameter(
        mu * torch.from_numpy(reg._trained_parameters.split_coefs.astype(dtype))
    )
    num_features = reg._trained_parameters.split_coefs.shape[-1] - 1
    layer._leaves_feat_ids = (
        np.ones((num_trees, layer._num_leaves, num_features), np.uint32)
        * np.arange(num_features)[None, None, :]
    ).astype(np.uint32)
    layer._leaves_coefs = torch.nn.parameter.Parameter(
        torch.from_numpy(reg._trained_parameters.leaves_coefs.astype(dtype))
    )
    return layer


def convert_tree_ensemble_to_layer(
    options: SoftTreeEnsembleLayerOptions,
    reg: Union[SoftTreeEnsemble, AxisAlignedTrees],
    mu: float,
) -> SoftTreeEnsembleLayer:
    if isinstance(reg, SoftTreeEnsemble):
        return convert_soft_oblique_tree_ensemble_to_layer(
            options=options, reg=reg, mu=mu
        )
    else:
        return convert_axis_aligned_tree_ensemble_to_layer(
            options=options, reg=reg, mu=mu
        )


def fit_pytorch(
    x: np.ndarray,
    y: np.ndarray,
    options: SoftTreeEnsembleLayerOptions,
    training_options: SoftTreeEnsembleTrainingOptions,
) -> SoftTreeEnsembleTrainedParameters:
    assert x.ndim == 2
    assert x.shape[1] == options.in_features

    if training_options.classification:
        assert y.ndim == 1
    else:
        assert y.ndim == 2
        assert y.shape[1] == options.out_features
    assert x.shape[0] == y.shape[0]

    dtype = np.float32 if options.float32 else np.float64
    assert x.dtype == dtype
    greedy_trainer: Union[GreedySoftObliqueTreesTrainer, GreedyAxisAlignedTreesTrainer]
    layer: SoftTreeEnsembleLayer
    if training_options.greedy_init:
        if training_options.classification:
            raise ValueError("Greedy init for classification not implemented yet")
        if options.oblique:
            assert (
                options.num_leaf_features is None
                or options.num_leaf_features == x.shape[-1]
            )
            greedy_trainer = GreedySoftObliqueTreesTrainer(
                num_trees=options.num_trees,
                depth=options.depth,
                mu=min(0.5, 5 / options.num_trees),
                num_test_splits=training_options.greedy_init_num_test_splits,
                random_seed=options.random_seed,
                num_split_feat=options.num_split_feat,
                float32=options.float32,
            )

        else:
            assert options.num_leaf_features == 0
            greedy_trainer = GreedyAxisAlignedTreesTrainer(
                num_trees=options.num_trees,
                depth=options.depth,
                mu=min(0.5, 5 / options.num_trees),
                num_test_splits=training_options.greedy_init_num_test_splits,
                random_seed=options.random_seed,
                float32=options.float32,
            )
        reg = greedy_trainer.fit(x=x, y=y)
        init_mse = np.mean((reg.predict(x=x) - y) ** 2)
        if training_options.verbose:
            print(f"Greedy init mse = {init_mse}")
        mu = training_options.greedy_init_mu
        layer = convert_tree_ensemble_to_layer(options=options, reg=reg, mu=mu)

        y2_a = reg.predict(x)
        np.mean((y - y2_a) ** 2)
        y2_torch, _ = layer.forward(torch.from_numpy(x.astype(dtype)))
        y2_b = y2_torch.detach().numpy()
        smoothed_init_mse = np.mean((y - y2_b) ** 2)
        if training_options.verbose:
            print(f"Smoothed greedy init mse = {smoothed_init_mse}")
        # assert np.allclose(y2_a, y2_b)
    else:
        layer = SoftTreeEnsembleLayer(options)

    if training_options.conditional_compute and training_options.test_gradient:
        assert isinstance(layer, SoftTreeEnsembleLayer)
        layer.test_gradient(x=x[:10, :].astype(dtype))

    fit_layer(layer=layer, x=x, y=y, training_options=training_options)

    trained_parameters = SoftTreeEnsembleTrainedParameters(
        split_feat_ids=layer._split_feat_ids,
        split_coefs=layer._split_coefs.detach().numpy(),
        leaves_feat_ids=layer._leaves_feat_ids,
        leaves_coefs=layer._leaves_coefs.detach().numpy(),
        depth=options.depth,
        active_tol=options.active_tol,
        abs_tol=options.abs_tol,
        oblique=options.oblique,
        in_features=options.in_features,
    )
    return trained_parameters
