from time import gmtime, strftime
import tensorflow as tf


def train_model(model, train_ds, val_ds, epochs=30):
    model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath="./checkpoints/",
        save_weights_only=False,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)

    model.fit(train_ds, validation_data=val_ds, epochs=epochs,
              callbacks=[model_checkpoint_callback])
    model.save(f"./saves/model_{strftime('%d_%H_%M_%S', gmtime())}.h5")
