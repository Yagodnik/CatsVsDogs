## Cats Vs Dogs Model

This my model which got 80% accuracy on this dataset.

### Scripts
Small description for some scripts in my project \
```model.py → File that contains my model code``` \
```augment_data.py → Data augmention for dataset``` \
```test_model.py → Loads model from ./checkpoints and test it on images from ./images``` \
```fix_tf_jpeg.py → Resaves broken images from dataset``` \
```corrupted_images.py → My util for checking dataset on broken images```

### Model Summary
```commandline
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 63, 63, 38)        1064      
                                                                 
 max_pooling2d (MaxPooling2D  (None, 31, 31, 38)       0         
 )                                                               
                                                                 
 dropout (Dropout)           (None, 31, 31, 38)        0         
                                                                 
 conv2d_1 (Conv2D)           (None, 15, 15, 38)        13034     
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 7, 7, 38)         0         
 2D)                                                             
                                                                 
 dropout_1 (Dropout)         (None, 7, 7, 38)          0         
                                                                 
 conv2d_2 (Conv2D)           (None, 3, 3, 38)          13034     
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 1, 1, 38)         0         
 2D)                                                             
                                                                 
 dropout_2 (Dropout)         (None, 1, 1, 38)          0         
                                                                 
 flatten (Flatten)           (None, 38)                0         
                                                                 
 dense (Dense)               (None, 2)                 78        
                                                                 
=================================================================
Total params: 27,210
Trainable params: 27,210
Non-trainable params: 0
_________________________________________________________________
```

### Model statistics
My result are not very good but 81% is not a bad result?
```commandline
Epoch 1/100
462/462 [==============================] - 94s 203ms/step - loss: 0.6719 - accuracy: 0.5714 - val_loss: 0.6312 - val_accuracy: 0.6669
Epoch 2/100
462/462 [==============================] - 89s 192ms/step - loss: 0.6114 - accuracy: 0.6682 - val_loss: 0.5757 - val_accuracy: 0.7105
Epoch 3/100
462/462 [==============================] - 87s 187ms/step - loss: 0.5717 - accuracy: 0.7010 - val_loss: 0.5435 - val_accuracy: 0.7304
Epoch 4/100
462/462 [==============================] - 85s 184ms/step - loss: 0.5442 - accuracy: 0.7237 - val_loss: 0.5575 - val_accuracy: 0.7137
Epoch 5/100
462/462 [==============================] - 92s 198ms/step - loss: 0.5236 - accuracy: 0.7427 - val_loss: 0.4933 - val_accuracy: 0.7627
Epoch 6/100
462/462 [==============================] - 87s 188ms/step - loss: 0.5046 - accuracy: 0.7532 - val_loss: 0.4961 - val_accuracy: 0.7586
Epoch 7/100
462/462 [==============================] - 89s 191ms/step - loss: 0.4886 - accuracy: 0.7647 - val_loss: 0.4762 - val_accuracy: 0.7774
Epoch 8/100
462/462 [==============================] - 89s 191ms/step - loss: 0.4746 - accuracy: 0.7729 - val_loss: 0.4666 - val_accuracy: 0.7782
Epoch 9/100
462/462 [==============================] - 87s 188ms/step - loss: 0.4688 - accuracy: 0.7791 - val_loss: 0.4756 - val_accuracy: 0.7730
Epoch 10/100
462/462 [==============================] - 95s 206ms/step - loss: 0.4564 - accuracy: 0.7839 - val_loss: 0.4446 - val_accuracy: 0.7903
Epoch 11/100
462/462 [==============================] - 90s 194ms/step - loss: 0.4455 - accuracy: 0.7874 - val_loss: 0.4442 - val_accuracy: 0.7903
Epoch 12/100
462/462 [==============================] - 90s 194ms/step - loss: 0.4368 - accuracy: 0.7954 - val_loss: 0.4683 - val_accuracy: 0.7788
Epoch 13/100
462/462 [==============================] - 91s 196ms/step - loss: 0.4295 - accuracy: 0.8031 - val_loss: 0.4321 - val_accuracy: 0.8022
Epoch 14/100
462/462 [==============================] - 90s 194ms/step - loss: 0.4243 - accuracy: 0.8041 - val_loss: 0.4175 - val_accuracy: 0.8078
Epoch 15/100
462/462 [==============================] - 89s 191ms/step - loss: 0.4163 - accuracy: 0.8056 - val_loss: 0.4260 - val_accuracy: 0.8003
Epoch 16/100
462/462 [==============================] - 88s 190ms/step - loss: 0.4120 - accuracy: 0.8092 - val_loss: 0.4306 - val_accuracy: 0.7980
Epoch 17/100
462/462 [==============================] - 90s 194ms/step - loss: 0.4062 - accuracy: 0.8146 - val_loss: 0.4128 - val_accuracy: 0.8175
Epoch 18/100
462/462 [==============================] - 89s 191ms/step - loss: 0.4021 - accuracy: 0.8136 - val_loss: 0.4171 - val_accuracy: 0.8104
Epoch 19/100
462/462 [==============================] - 91s 197ms/step - loss: 0.3986 - accuracy: 0.8179 - val_loss: 0.4126 - val_accuracy: 0.8172
```
