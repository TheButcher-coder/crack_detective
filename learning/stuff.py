import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10


print(tf.__version__)
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

#normalize
x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32')/255.0

#init model(sequential 1inp 1 out)
model = tf.keras.models.Sequential([
    keras.Input(shape=(32, 32, 3)),     #shape of image
    layers.Conv2D(32, (3, 3), activation='relu', padding='same'),   #how many output channels
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),   #MORE LAYERS
    layers.MaxPooling2D(pool_size=(2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),  #MOREE!!!
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

#compile model
model.compile(optimizer='adam', metrics=['accuracy'], loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

#train model
model.fit(x_train, y_train, epochs=10, batch_size=64)

#evaluate model
model.evaluate(x_test, y_test, batch_size=64)