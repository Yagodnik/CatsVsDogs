import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from time import gmtime, strftime

from dataset import *
from train_model import *
import tensorflow as tf
import tensorflow.keras as keras


train_ds, val_ds = gen_ds("F:/Datasets/CatsVsDogs")
train_ds = normalize_ds(train_ds)
val_ds = normalize_ds(val_ds)

# idk what it does lol
tf.config.run_functions_eagerly(True)

model = keras.Sequential()
model.add(keras.layers.Conv2D(filters=38, kernel_size=3, strides=(2, 2),
                              activation="relu"))
model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))
model.add(keras.layers.Dropout(0.15))
model.add(keras.layers.Conv2D(filters=38, kernel_size=3, strides=(2, 2),
                              activation="relu"))
model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))
model.add(keras.layers.Dropout(0.15))
model.add(keras.layers.Conv2D(filters=38, kernel_size=3, strides=(2, 2),
                              activation="relu"))
model.add(keras.layers.MaxPooling2D(pool_size=2, strides=2))
model.add(keras.layers.Dropout(0.15))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(2, activation="softmax", use_bias=True))

model.build(input_shape=(None, 128, 128, 3))
model.summary()
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=["accuracy"])


train_model(model=model,
            train_ds=train_ds,
            val_ds=val_ds,
            epochs=100)
