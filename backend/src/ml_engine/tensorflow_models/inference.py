import tensorflow as tf
import numpy as np

def run_tensorflow_inference(data: list) -> list:
    # Create a simple sequential model to mock inference
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, input_shape=(len(data[0]),))
    ])
    
    input_array = np.array(data, dtype=np.float32)
    predictions = model.predict(input_array)
    
    return predictions.tolist()
