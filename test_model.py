import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import numpy as np

# model_path = "./saves/model_26_22_50_35.h5"
folder = "./images"
model_path = "./checkpoints"

model = keras.models.load_model(model_path)
model.summary()


def normalize_image(image):
    normalization_layer1 = keras.layers.Rescaling(1. / 255)

    return normalization_layer1(image)


right_count = 0
total_count = len(os.listdir("./images"))

for file in os.listdir("./images"):
    with open(f"{folder}/{file}", "rb") as image:
        data = image.read()

    image = tf.io.decode_jpeg(data)
    image = tf.image.resize(image, [128, 128])
    image = normalize_image(image)

    image = np.expand_dims(image, 0)

    output = model(image).numpy()[0]
    index = np.argmax(output)
    # print(output)

    if (file.__contains__("cat") and index == 0) or \
            (file.__contains__("dog") and index == 1):
        right_count += 1

    if index == 0:
        print(f"{file} -> cat with prob {output[index]:0.2f}")
    elif index == 1:
        print(f"{file} -> dog with prob {output[index]:0.2f}")

print(f"Result: {right_count / total_count:0.2f}")
