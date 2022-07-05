import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

folder = "F:/Datasets/CatsVsDogs"


def fix_subdir(name):
    subdir = f"{folder}/{name}"
    total = len(os.listdir(subdir))
    index = 0

    for file in os.listdir(subdir):
        image_open = open(f"{subdir}/{file}", 'rb')
        data = image_open.read()
        image_open.close()

        print(f'\r Processing /{name} |{index / total * 100 : 0.0f}%', end='')

        try:
            content = tf.io.decode_jpeg(data)
        except:
            print("Failed to load")
            continue

        try:
            tf.keras.utils.save_img(f"{subdir}/{file}", content)
        except:
            print("Failed to save")
        index += 1

    print()


def check_subdir(name):
    subdir = f"{folder}/{name}"
    total = len(os.listdir(subdir))
    index = 0

    for file in os.listdir(subdir):
        image_open = open(f"{subdir}/{file}", 'rb')
        data = image_open.read()
        image_open.close()

        print(f'\r Processing /{name} |{index / total * 100 : 0.0f}%', end='')

        try:
            content = tf.io.decode_jpeg(data)
        except:
            print(f"Failed to load -> {file}")
            continue

        index += 1

    print()


def check_file(path):
    image_open = open(path, 'rb')
    data = image_open.read()

    content = tf.io.decode_jpeg(data)


check_subdir("Cat")
check_subdir("Dog")
# check_file("F:/Datasets/CatsVsDogs/Cat/1614.jpg")
