from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List

# Import the ML engines and preprocessor
from src.ml_engine.pytorch_models.inference import run_pytorch_inference
from src.ml_engine.tensorflow_models.inference import run_tensorflow_inference
from src.ml_engine.xgboost_pipelines.inference import run_xgboost_inference
from src.ml_engine.scikit_preprocessors.pipeline import preprocess_payload

router = APIRouter()

class InferenceRequest(BaseModel):
    # Enforce a 2D numerical array for model inputs
    data: List[List[float]] = Field(..., example=[[1.0, 2.0, 3.0]])
    # Optional flag to route data through the scikit-learn scaler first
    preprocess: bool = False

@router.post("/predict/pytorch")
async def predict_pytorch(payload: InferenceRequest):
    try:
        input_data = payload.data
        if payload.preprocess:
            input_data = preprocess_payload(input_data)
            
        predictions = run_pytorch_inference(input_data)
        
        return {
            "framework": "PyTorch", 
            "preprocessed": payload.preprocess,
            "prediction": predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PyTorch inference failed: {str(e)}")

@router.post("/predict/tensorflow")
async def predict_tensorflow(payload: InferenceRequest):
    try:
        input_data = payload.data
        if payload.preprocess:
            input_data = preprocess_payload(input_data)
            
        predictions = run_tensorflow_inference(input_data)
        
        return {
            "framework": "TensorFlow", 
            "preprocessed": payload.preprocess,
            "prediction": predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TensorFlow inference failed: {str(e)}")

@router.post("/predict/xgboost")
async def predict_xgboost(payload: InferenceRequest):
    try:
        input_data = payload.data
        if payload.preprocess:
            input_data = preprocess_payload(input_data)
            
        predictions = run_xgboost_inference(input_data)
        
        return {
            "framework": "XGBoost", 
            "preprocessed": payload.preprocess,
            "prediction": predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"XGBoost inference failed: {str(e)}")
