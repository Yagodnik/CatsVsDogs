import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from dataset import *
from train_model import *
import tensorflow.keras as keras

model_path = "./checkpoints"

model = keras.models.load_model(model_path)
model.summary()

train_ds, val_ds = gen_ds("F:/Datasets/CatsVsDogs")
train_ds = normalize_ds(train_ds)
val_ds = normalize_ds(val_ds)


train_model(model=model,
            train_ds=train_ds,
            val_ds=val_ds,
            epochs=30)
