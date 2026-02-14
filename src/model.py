import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

# Global variable to store model
MODEL = None

# MNIST image size
IMAGE_SIZE = (28, 28)

# Class labels for MNIST (digits 0–9)
CLASS_LABELS = [str(i) for i in range(10)]


def load_model(model_path: str = None):
    global MODEL

    if MODEL is None:
        effective_path = model_path if model_path else os.environ.get(
            "MODEL_PATH",
            "models/my_classifier_model.h5"
        )

        if not os.path.exists(effective_path):
            raise FileNotFoundError(f"Model file not found at {effective_path}")

        MODEL = tf.keras.models.load_model(effective_path)

    return MODEL


def preprocess_image(image_bytes: bytes) -> np.ndarray:
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("L")  # grayscale
        image = image.resize(IMAGE_SIZE)

        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)  # batch dimension

        return image_array

    except Exception as e:
        raise ValueError(f"Error processing image: {e}")


def predict_image(preprocessed_image: np.ndarray):
    model = load_model()

    predictions = model.predict(preprocessed_image)

    predicted_class_index = np.argmax(predictions, axis=1)[0]
    probabilities = predictions[0].tolist()

    return {
        "class_label": CLASS_LABELS[predicted_class_index],
        "probabilities": probabilities
    }
