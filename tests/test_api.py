from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app
from PIL import Image
import io

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@patch("src.main.predict_image")
@patch("src.main.preprocess_image")

def test_predict_success(mock_preprocess, mock_predict):

    mock_preprocess.return_value = "mock_array"
    mock_predict.return_value = {
        "class_label": "5",
        "probabilities": [0.1] * 10
    }

    dummy_image = Image.new("L", (28, 28), color=128)
    img_bytes = io.BytesIO()
    dummy_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    response = client.post(
        "/predict",
        files={"file": ("test.png", img_bytes, "image/png")}
    )

    assert response.status_code == 200
    assert response.json()["class_label"] == "5"


def test_predict_invalid_file():
    response = client.post(
        "/predict",
        files={"file": ("test.txt", b"not image", "text/plain")}
    )

    assert response.status_code == 400


def test_predict_missing_file():
    response = client.post("/predict")

    assert response.status_code == 422
