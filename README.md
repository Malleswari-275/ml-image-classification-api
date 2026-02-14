# 🚀 Production-Ready ML Image Classification API  
### FastAPI • TensorFlow/Keras • Docker • CI/CD (GitHub Actions)

---

## 📌 Project Overview

This project demonstrates how to convert a trained Keras image classification model into a production-ready RESTful API. The model is served using FastAPI, containerized using Docker, and integrated with a CI/CD pipeline using GitHub Actions.

The goal of this project is to bridge the gap between machine learning development and real-world production deployment using MLOps best practices.

This API performs real-time inference on uploaded images and returns predicted class labels along with class probabilities.

---

## 🎯 Key Features

- ✅ RESTful API using FastAPI  
- ✅ Image classification using TensorFlow/Keras  
- ✅ Model loaded once at startup (optimized inference)  
- ✅ Image preprocessing inside API  
- ✅ Docker containerization (multi-stage build)  
- ✅ Docker Compose for simplified local setup  
- ✅ Automated CI/CD pipeline with GitHub Actions  
- ✅ Unit tests using pytest  
- ✅ Structured logging & proper error handling  
- ✅ Example prediction outputs included  

---

## 🛠 Technology Stack

- Python 3.11  
- FastAPI  
- TensorFlow / Keras  
- NumPy  
- Pillow  
- Pytest  
- Docker  
- Docker Compose  
- GitHub Actions  

---

## 📂 Project Structure

```
ML_Prediction/
│
├── .github/workflows/        # CI/CD workflow
├── src/
│   ├── main.py              # FastAPI application
│   ├── model.py             # Model loading & prediction logic
│   └── __init__.py
│
├── models/
│   └── my_classifier_model.h5
│
├── tests/
│   └── test_api.py
│
├── predictions/             # Example prediction outputs
│   ├── example_prediction_1.json
│   └── example_prediction_2.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── pytest.ini
└── README.md
```

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the API

```bash
uvicorn src.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker (Recommended)

### Build & Run

```bash
docker compose up --build
```

Or (older versions):

```bash
docker-compose up --build
```

API will be available at:

```
http://localhost:8000
```

---

## 📡 API Endpoints

### 🔍 Health Check

**GET** `/health`

Example:

```bash
curl http://localhost:8000/health
```

Response:

```json
{
  "status": "ok",
  "message": "API is healthy and model is loaded."
}
```

### 🧠 Predict Image

**POST** `/predict`

Example:

```bash
curl -X POST \
  -F "file=@digit.png" \
  http://localhost:8000/predict
```

Example Response:

```json
{
  "class_label": "7",
  "probabilities": [0.01, 0.02, 0.03, 0.04, 0.05, 0.02, 0.01, 0.80, 0.01, 0.01]
}
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

Expected output:

```
4 passed
```

---

## 🔄 CI/CD Pipeline

This project includes a GitHub Actions workflow that automatically:

- ✅ Checks out repository code
- ✅ Sets up Python environment
- ✅ Installs dependencies
- ✅ Runs unit tests
- ✅ Builds Docker image

The pipeline is triggered on:

- Push to `main`
- Pull requests to `main`

You can view workflow runs in the **Actions** tab of the repository.

---

## 🔐 Environment Variables

See `.env.example`

| Variable | Description |
|----------|-------------|
| MODEL_PATH | Path to trained model inside container |
| LOG_LEVEL | Logging level (DEBUG, INFO, etc.) |

---

## 📦 Prediction Examples

The `predictions/` directory contains sample JSON outputs from successful inference requests. These demonstrate expected API behavior.

---

## 🚀 Future Enhancements

- 🔐 Add authentication (JWT-based)
- 📊 Add model performance monitoring
- 📈 Add Prometheus metrics endpoint
- ☁️ Deploy to AWS / GCP
- 🧩 Add model versioning
- 🐳 Push Docker image to container registry
- ⚡ Add GPU support
- 🧪 Run containerized tests inside CI/CD pipeline

---

## 🏆 What This Project Demonstrates

This project demonstrates:

- ✅ End-to-end ML model deployment
- ✅ REST API development for inference
- ✅ Production containerization
- ✅ Automated CI/CD workflows
- ✅ Clean architecture & modular code
- ✅ MLOps best practices

---