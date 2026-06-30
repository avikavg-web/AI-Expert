import tensorflow as tf
from tensorflow.keras import layers, models, optimizers


def build_enhanced_model(activation_func="relu"):
    model = models.Sequential([ layers.Input(shape=(28, 28, 1)), layers.Conv2D(32, (3, 3), activation=activation_func), layers.MaxPooling2D((2, 2)), layers.Conv2D(64, (3, 3), activation=activation_func), layers.MaxPooling2D((2, 2)), layers.Flatten(), layers.Dense(128, activation=activation_func),layers.Dropout(0.2), layers.Dense(10, activation="softmax"),])
    return model


def get_data_augmentation():
    data_augmentation = models.Sequential([ layers.RandomRotation(0.1), layers.RandomZoom(0.1),])
    return data_augmentation


def run_training():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

    print("Data processed.\n")

    aug_layer = get_data_augmentation()
    x_train_augmented = aug_layer(x_train)

    model = build_enhanced_model(activation_func="relu")

    model.compile( optimizer=optimizers.Adam(learning_rate=0.001),loss="sparse_categorical_crossentropy",metrics=["accuracy"],)

    print("Model compilation complete.\n")

    model.fit(x_train_augmented,y_train,epochs=5,batch_size=64,validation_data=(x_test, y_test),)

    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"Evaluation Complete - Loss: {test_loss:.4f} | Accuracy: {test_acc:.4f}\n")


if __name__ == "__main__":
    run_training()