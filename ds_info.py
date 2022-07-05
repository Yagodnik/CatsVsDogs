import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow.keras as keras


folder = "F:/Datasets/CatsVsDogs"

seed = 123
split = 0.3

print(f"Dataset split {split}")

ds1 = keras.utils.image_dataset_from_directory(
    folder,
    validation_split=split,
    seed=seed,
    subset="training",
    label_mode="int"
)

ds2 = keras.utils.image_dataset_from_directory(
    folder,
    validation_split=split,
    seed=seed,
    subset="validation",
    label_mode="int"
)
