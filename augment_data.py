import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import tensorflow.keras as keras
import numpy as np

data_augmentation = keras.Sequential([
    keras.layers.RandomFlip("horizontal_and_vertical"),
    keras.layers.RandomRotation(0.2)
])

folder = "F:/Datasets/CatsVsDogs"
split = 0.4


def augment_image(image):
    image_open = open(image, 'rb')
    data = image_open.read()
    image_open.close()

    try:
        content = tf.io.decode_jpeg(data)
    except:
        print(f"Failed to load -> {image}")
        return None

    return data_augmentation(content)


def save(image, path):
    tf.keras.utils.save_img(path, image)


for dir in os.listdir(folder):
    used = []
    max_num = len(os.listdir(f"{folder}/{dir}"))
    files = os.listdir(f"{folder}/{dir}")
    saved_count = 0

    print(f"{folder}/{dir}")

    while len(used) < int(max_num * split):
        while True:
            file_name = files[np.random.randint(low=1, high=max_num)]
            file_index = int(file_name.split(".")[0])

            if not used.__contains__(file_index):
                break

        output = augment_image(f"{folder}/{dir}/{file_name}")
        if output is not None:
            save(output, f"{folder}/{dir}/{file_index}_aug.jpg")
            saved_count += 1

        used.append(file_index)

    print(f"Saved: {saved_count}")
