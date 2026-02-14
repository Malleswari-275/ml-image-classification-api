from fastapi import FastAPI, UploadFile, File, HTTPException, status
from pydantic import BaseModel
from typing import List
import logging
import os

from src.model import load_model, preprocess_image, predict_image

# Configure logging
logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO").upper())
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="ML Prediction API",
    description="Image Classification API using Keras model",
    version="1.0.0"
)

# Load model on startup
@app.on_event("startup")
async def startup_event():
    try:
        load_model()
        logger.info("✅ Model loaded successfully.")
    except Exception as e:
        logger.critical(f"❌ Failed to load model: {e}")
        raise RuntimeError("Model failed to load.")


# Response schema
class PredictionResponse(BaseModel):
    class_label: str
    probabilities: List[float]


# Health endpoint
@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {
        "status": "ok",
        "message": "API is healthy and model is loaded."
    }


# Prediction endpoint
@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):

    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed."
        )

    try:
        image_bytes = await file.read()
        preprocessed = preprocess_image(image_bytes)
        result = predict_image(preprocessed)

        return result

    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
