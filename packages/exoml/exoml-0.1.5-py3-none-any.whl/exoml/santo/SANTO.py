import os
from typing import List

import keras
import pandas as pd
import numpy as np
import tensorflow as tf
import time

from numpy import ndarray
from sklearn.utils import shuffle

from exoml.ml.layers.transformer_classifier import TransformerClassifier
from exoml.ml.model.base_model import HyperParams


class SANTO:
    """
    Self-Attention Neural Network for Transiting Objects
    """
    def __init__(self) -> None:
        super().__init__()

    def loss_function(self, loss_holder, target, pred):
        #Custom loss function to mask the padding tokens
        mask = tf.math.logical_not(tf.math.equal(target, 0))
        loss_ = loss_holder(target, pred)

        mask = tf.cast(mask, dtype=loss_.dtype)
        loss_ *= mask

        return tf.reduce_mean(loss_)

    def train(self, lcs_dir, model_dir, hyperparams: HyperParams, input_dim=500):
        tf.keras.backend.clear_session()
        checkpoint_path = f"{model_dir}_chk"
        input_layer = keras.Input(shape=(input_dim, 1), name="input")
        transformer = TransformerClassifier(transformer_input_size=input_dim, patch_size=input_dim,
                                            num_heads=4, mlp_dim=input_dim, hyperparams=hyperparams, num_blocks=2,
                                            classes=input_dim)(input_layer)
        leaning_rate = CustomSchedule(input_dim)
        optimizer = tf.keras.optimizers.Adam(leaning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)
        transformer_model = keras.Model(inputs=input_layer, outputs=transformer)
        transformer_model.compile(optimizer=optimizer, loss='binary_crossentropy',
                                  metrics=['accuracy', 'precision', 'recall'])
        transformer_model.run_eagerly = hyperparams.run_eagerly
        # transformer = Transformer(num_heads=4, key_dim=input_dim, ffn_units=input_dim[0], output_dim=input_dim[0],
        #                           stack_depth=2, dropout_rate=hyperparams.dropout_rate)
        train_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(name="accuracy")
        train_precision = tf.keras.metrics.Precision(name="precision")
        train_recall = tf.keras.metrics.Recall(name="recall")
        train_pr99 = tf.keras.metrics.PrecisionAtRecall(recall=0.99, name="p@r99")
        ckpt = tf.train.Checkpoint(transformer=transformer_model, optimizer=optimizer)
        ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)
        if ckpt_manager.latest_checkpoint:
            ckpt.restore(ckpt_manager.latest_checkpoint)
            print("Last checkpoint restored.")
        target_files: List[str] = os.listdir(lcs_dir)
        losses = []
        accuracies = []
        precisions = []
        recalls = []
        pr99s = []
        for epoch in range(hyperparams.epochs):
            print(f"Epoch {epoch + 1}/{hyperparams.epochs}")
            np.random.shuffle(target_files)
            start = time.time()
            train_accuracy.reset_states()
            last_target_file_index: int = 0
            last_target_file_pos: int = 0
            last_target_file: str = target_files[0]
            flux = np.loadtxt(f'{lcs_dir}/{last_target_file}', delimiter=',')
            train_batch: ndarray = np.zeros((hyperparams.batch_size, input_dim))
            train_tags: ndarray = np.zeros((hyperparams.batch_size, input_dim))
            iteration: int = 0
            data_remaining: bool = True
            while data_remaining:
                if last_target_file_pos >= flux.shape[1] - input_dim // 2:
                    last_target_file_pos = input_dim // 2
                    last_target_file_index = last_target_file_index + 1
                    last_target_file = target_files[last_target_file_index]
                    flux = np.loadtxt(f'{lcs_dir}/{last_target_file}', delimiter=',')
                train_batch[iteration] = flux[0][last_target_file_pos:last_target_file_pos + input_dim]
                train_tags[iteration] = flux[1][last_target_file_pos:last_target_file_pos + input_dim]
                train_tags[iteration][train_tags[iteration] == 1] = 0
                train_tags[iteration][train_tags[iteration] > 0] = 1
                last_target_file_pos = last_target_file_pos + 1
                data_remaining = last_target_file_index != len(target_files) or \
                                 last_target_file_pos < flux.shape[1] - input_dim // 2
                batch_index = iteration // hyperparams.batch_size
                if (iteration + 1) % hyperparams.batch_size == 0 or not data_remaining:
                    with tf.GradientTape() as tape:
                        flux_predictions = transformer_model(train_batch, train_tags, True)
                        loss = transformer_model.compute_loss(train_tags, flux_predictions)
                        gradients = tape.gradient(loss, transformer_model.trainable_variables)
                        optimizer.apply_gradients(zip(gradients, transformer_model.trainable_variables))
                    train_accuracy(train_batch, flux_predictions)
                    train_precision(train_batch, flux_predictions)
                    train_recall(train_batch, flux_predictions)
                    train_pr99(train_batch, flux_predictions)
                    losses.append(loss)
                    accuracies.append(train_accuracy.result())
                    precisions.append(train_accuracy.result())
                    recalls.append(train_accuracy.result())
                    pr99s.append(train_accuracy.result())
                    print("Epoch {} Batch {} Loss {:.4f} Accuracy {:.4f}".format(epoch + 1, batch_index + 1,
                                                                                 loss.result(),
                                                                                 train_accuracy.result()))
                iteration = iteration + 1
            # Checkpoint the model on every epoch
            ckpt_save_path = ckpt_manager.save()
            print("Saving checkpoint for epoch {} in {}".format(epoch + 1, ckpt_save_path))
            print("Time for 1 epoch: {} secs\n".format(time.time() - start))
        return losses, accuracies


class AutoencoderGenerator(tf.keras.utils.Sequence):
    def __init__(self, lc_filenames, batch_size, input_size):
        self.lc_filenames = lc_filenames
        self.batch_size = batch_size
        self.input_size = input_size

    def __len__(self):
        return (np.ceil(len(self.lc_filenames) / float(self.batch_size))).astype(int)

    def __getitem__(self, idx):
        batch_filenames = self.lc_filenames[idx * self.batch_size: (idx + 1) * self.batch_size]
        filenames_shuffled = shuffle(batch_filenames)
        batch_data_array = np.empty((len(filenames_shuffled), self.input_size[0], self.input_size[1]))
        batch_data_values = np.empty((len(filenames_shuffled), (self.input_size, 4)))
        i = 0
        for file in filenames_shuffled:
            input_df = pd.read_csv(file, usecols=['flux', 'flux_err'], low_memory=True)
            values_df = pd.read_csv(file, usecols=['eb_model', 'bckeb_model', 'planet_model'],
                                    low_memory=True)
            batch_data_array[i] = input_df.to_numpy()
            eb_arr = values_df['eb_model'].to_numpy()
            bckeb_arr = values_df['bckeb_model'].to_numpy()
            planet_arr = values_df['planet_model'].to_numpy()
            eb_labels_args = np.argwhere(eb_arr < 1).flatten()
            bckeb_labels_args = np.argwhere(bckeb_arr < 1).flatten()
            planet_labels_args = np.argwhere(planet_arr < 1).flatten()
            nothing_labels_args = np.argwhere((eb_arr == 1) & (bckeb_arr == 1) & (planet_arr == 1)).flatten()
            eb_label = np.zeros(self.input_size[0])
            eb_label[eb_labels_args] = 1
            bckeb_label = np.zeros(self.input_size[0])
            bckeb_label[bckeb_labels_args] = 1
            planet_label = np.zeros(self.input_size[0])
            planet_label[planet_labels_args] = 1
            nothing_label = np.zeros(self.input_size[0])
            nothing_label[nothing_labels_args] = 1
            batch_data_values[i] = np.transpose([nothing_label, eb_label, bckeb_label, planet_label])
            batch_data_values[i] = values_df['model'].to_numpy()
            i = i + 1
        return batch_data_array, batch_data_values

    def __prepare_input_data(self, input_df):
        time = input_df["#time"].to_numpy()
        dif = time[1:] - time[:-1]
        jumps = np.where(np.abs(dif) > 0.25)[0]
        jumps = np.append(jumps, len(input_df))
        previous_jump_index = 0
        for jumpIndex in jumps:
            token = input_df["centroid_x"][previous_jump_index:jumpIndex].to_numpy()
            input_df["centroid_x"][previous_jump_index:jumpIndex] = np.tanh(token - np.nanmedian(token))
            token = input_df["centroid_y"][previous_jump_index:jumpIndex].to_numpy()
            input_df["centroid_y"][previous_jump_index:jumpIndex] = np.tanh(token - np.nanmedian(token))
            token = input_df["motion_x"][previous_jump_index:jumpIndex].to_numpy()
            input_df["motion_x"][previous_jump_index:jumpIndex] = np.tanh(token - np.nanmedian(token))
            token = input_df["motion_y"][previous_jump_index:jumpIndex].to_numpy()
            input_df["motion_y"][previous_jump_index:jumpIndex] = np.tanh(token - np.nanmedian(token))
            token = input_df["bck_flux"][previous_jump_index:jumpIndex].to_numpy()
            input_df["bck_flux"][previous_jump_index:jumpIndex] = np.tanh(token - np.nanmedian(token))
            previous_jump_index = jumpIndex
        return input_df.fillna(0)


class CustomSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, d_model, warmup_steps=4000):
        super(CustomSchedule, self).__init__()

        self.d_model = tf.cast(d_model, tf.float32)
        self.warmup_steps = warmup_steps

    def __call__(self, step):
        warmup_steps = tf.cast(tf.convert_to_tensor(self.warmup_steps, dtype=tf.int64, name="warmup_steps"), tf.float32)
        arg1 = tf.math.rsqrt(tf.cast(step, tf.float32))
        arg2 = tf.cast(step, tf.float32) * tf.math.pow(warmup_steps, -1.5)
        return tf.math.rsqrt(self.d_model) * tf.math.minimum(arg1, arg2)

SANTO().train("/data/scratch/ml/santo/training_data/", "/data/scratch/exoml/SANTO",
              hyperparams=HyperParams(batch_size=100, epochs=10, run_eagerly=True))
