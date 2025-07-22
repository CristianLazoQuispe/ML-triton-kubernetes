from fastapi import FastAPI
import os
import requests
import numpy as np

MODEL_NAME = os.environ.get("MODEL_NAME", "model1")

app = FastAPI()

@app.get("/predict")
def predict():
    url = f"http://triton-service:8000/v2/models/{MODEL_NAME}/infer"
    data = {
        "inputs": [{
            "name": "input",
            "shape": [1, 1, 28, 28],
            "datatype": "FP32",
            "data": np.random.rand(1, 1, 28, 28).tolist()
        }]
    }
    try:
        res = requests.post(url, json=data)
        return {"model": MODEL_NAME, "status": res.status_code, "output": res.json()}
    except Exception as e:
        return {"model": MODEL_NAME, "error": str(e)}
