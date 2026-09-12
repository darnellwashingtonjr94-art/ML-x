from sklearn.preprocessing import StandardScaler
import numpy as np

def preprocess_payload(data: list) -> list:
    # In production, load a fitted scaler using joblib
    scaler = StandardScaler()
    
    # Fit-transforming just for the mock template
    np_data = np.array(data)
    if len(np_data.shape) == 1:
        np_data = np_data.reshape(1, -1)
        
    scaled_data = scaler.fit_transform(np_data)
    return scaled_data.tolist()
