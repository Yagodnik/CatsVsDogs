import tensorflow.keras as keras

def gen_ds(path, batch_size=64, split=0.15, seed=123, img_height=128, img_width=128):
    ds1 = keras.utils.image_dataset_from_directory(
        path,
        batch_size=batch_size,
        validation_split=split,
        seed=seed,
        subset="training",
        image_size=(img_height, img_width),
        label_mode="int"
    )

    ds2 = keras.utils.image_dataset_from_directory(
        path,
        batch_size=batch_size,
        validation_split=split,
        seed=seed,
        subset="validation",
        image_size=(img_height, img_width),
        label_mode="int"
    )

    return ds1, ds2


def normalize_ds(ds):
    normalization_layer1 = keras.layers.Rescaling(1. / 255)
    ds = ds.map(lambda x, y: (normalization_layer1(x), y))

    return ds