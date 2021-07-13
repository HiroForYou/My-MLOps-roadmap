import os
import json
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras

DATAPATH = f"{os.getcwd()}/../1 Preparing the Dataset/data.json"
SAVED_MODEL_PATH = "modelo.h5"

LEARNING_RATE = 0.0001
EPOCHS = 100
BATCH_SIZE = 612

NUM_KEYWORDS = 10


def load_dataset(data_path):

    with open(data_path, "r") as fp:
        data = json.load(fp)
    
    # extraemos los inputs y los targets
    X = np.array(data["MFCCs"])
    y = np.array(data["labels"])

    return X, y


def get_data_splits(data_path, test_size=0.2, validation_size=0.2):

    # cargamos el dataset
    X, y = load_dataset(data_path)

    # creamos las particiones train/validation/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)

    # convertimos los inputs de un arreglo 2d a uno 3d
    X_train = X_train[..., np.newaxis]
    X_test = X_test[..., np.newaxis]
    X_validation = X_validation[..., np.newaxis]

    

    return X_train, y_train, X_validation, y_validation, X_test, y_test


def build_model( input_shape, learning_rate, error):

    # construyendo la red
    model = keras.models.Sequential()

    # 1st conv layer
    model.add(keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=input_shape,
                                     kernel_regularizer=keras.regularizers.l2(0.002)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2,2), padding='same'))

    # 2nd conv layer
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu',
                                     kernel_regularizer=keras.regularizers.l2(0.002)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2,2), padding='same'))

    # 3rd conv layer
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu',
                                     kernel_regularizer=keras.regularizers.l2(0.003)))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D((2, 2), strides=(2,2), padding='same'))

    # flatten 
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.25))

    # softmax 
    model.add(keras.layers.Dense(10, activation='softmax'))

    # compilando el modelo
    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer, loss=error, metrics=["accuracy"])

    # resumen
    model.summary()
    
    return model

def main():

    # cargando las particiones train/validation/test
    X_train, y_train, X_validation, y_validation, X_test, y_test = get_data_splits(DATAPATH)

    # construyendo el modelo CNN
    input_shape = (X_train.shape[1], X_train.shape[2], 1) # (# SEGMENTOS, # COEFICIENTES, 1 (CANAL))
    model = build_model(input_shape, learning_rate=LEARNING_RATE, error="sparse_categorical_crossentropy")

    # entrenando el modelo
    history = model.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, 
                        validation_data=(X_validation, y_validation))

    # evaluando el modelo
    test_error, test_accuracy = model.evaluate(X_test, y_test)

    print(f"Test error: {test_error}, Test accuracy: {test_accuracy}")

    # guardando el modelo
    model.save(SAVED_MODEL_PATH)

if __name__ == "__main__":
    main()