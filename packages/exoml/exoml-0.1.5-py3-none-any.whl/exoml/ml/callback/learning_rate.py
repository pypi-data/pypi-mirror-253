import logging

from keras import backend
from keras.callbacks import Callback
from tensorflow_addons.optimizers import MultiOptimizer


class WarmUpAndLinDecreaseCallback(Callback):
    def __init__(
            self,
            initial_lr,
            top_lr,
            baseline_lr,
            warmup_epochs,
            baseline_epochs,
            name=None):
        """Applies linear decrease with a first stage of warmup
    """
        super(WarmUpAndLinDecreaseCallback, self).__init__()
        assert initial_lr > 0
        self.initial_lr = initial_lr
        self.top_lr = top_lr
        self.baseline_lr = baseline_lr
        self.warmup_epochs = warmup_epochs
        self.baseline_epochs = baseline_epochs
        self.name = name
        super().__init__()

    def on_epoch_end(self, epoch, logs=None):
        if isinstance(self.model.optimizer, MultiOptimizer):
            for index, optimizer_spec in enumerate(self.model.optimizer.optimizer_specs):
                optimizer = optimizer_spec['optimizer']
                warmup_slope = (self.top_lr - self.initial_lr) / self.warmup_epochs
                decreasing_slope = (self.baseline_lr - self.top_lr) / self.baseline_epochs
                new_lr_decreasing = epoch * decreasing_slope + self.top_lr
                new_lr_warmup = epoch * warmup_slope + self.initial_lr
                new_learning_rate = new_lr_warmup if epoch <= self.warmup_epochs else new_lr_decreasing
                new_learning_rate = new_learning_rate if new_learning_rate < self.baseline_lr else new_learning_rate
                new_learning_rate = new_learning_rate * optimizer.progressive_lr_factor
                backend.set_value(optimizer.lr, new_learning_rate)
        else:
            optimizer = self.model.optimizer
            warmup_slope = (self.top_lr - self.initial_lr) / self.warmup_epochs
            decreasing_slope = (self.baseline_lr - self.top_lr) / self.baseline_epochs
            new_lr_decreasing = epoch * decreasing_slope + self.top_lr
            new_lr_warmup = epoch * warmup_slope + self.initial_lr
            new_learning_rate = new_lr_warmup if epoch <= self.warmup_epochs else new_lr_decreasing
            new_learning_rate = new_learning_rate if new_learning_rate < self.baseline_lr else new_learning_rate
            backend.set_value(optimizer.lr, new_learning_rate)
