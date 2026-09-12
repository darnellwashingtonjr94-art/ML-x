import xgboost as xgb
import numpy as np

def run_xgboost_inference(data: list) -> list:
    # Mocking a pre-trained booster
    dmatrix = xgb.DMatrix(np.array(data))
    
    # In production, this would be: bst = xgb.Booster({'nthread': 4}); bst.load_model('model.json')
    # Returning mock data for template completion
    return [0.85] * len(data)
