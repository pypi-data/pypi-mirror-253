import numbers

import tensorflow as tf
import keras
from keras import backend
from keras.layers import Dropout
from keras.utils import control_flow_util


class AdaptiveStdDropout(Dropout):
    """
    Experimental dropout increasing the base rate by the inverse of the tanh of the standard deviation of the input
    layer.
    """
    def __init__(self, rate, max_rate=0.8, noise_shape=None, seed=None, **kwargs):
        super().__init__(rate, noise_shape, seed, **kwargs)
        assert rate <= max_rate < 1
        self.max_rate = max_rate

    def call(self, inputs, training=None):
        if isinstance(self.rate, numbers.Real) and self.rate == 0:
            return tf.identity(inputs)

        if training is None:
            training = backend.learning_phase()
        dropout_rate = self.rate
        if self.max_rate > self.rate:
            dropout_rate = tf.math.reduce_std(inputs)
            dropout_rate = tf.math.subtract(1.0, tf.math.tanh(dropout_rate))
            dropout_rate = tf.add(tf.math.multiply(dropout_rate, self.max_rate - self.rate), self.rate)
            max_rate_tensor = tf.convert_to_tensor(self.max_rate, dtype=tf.float32)
            dropout_rate = tf.cond(tf.greater(dropout_rate, self.max_rate), lambda: max_rate_tensor, lambda: dropout_rate)

        def dropped_inputs():
            return self._random_generator.dropout(
                inputs, dropout_rate, noise_shape=self._get_noise_shape(inputs)
            )

        output = control_flow_util.smart_cond(
            training, dropped_inputs, lambda: tf.identity(inputs)
        )
        return output

    def get_config(self):
        config = {
            "rate": self.rate,
            "noise_shape": self.noise_shape,
            "seed": self.seed,
            "max_rate": self.max_rate
        }
        base_config = super().get_config()
        return dict(list(base_config.items()) + list(config.items()))

