from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

path=file_path = os.path.join(os.path.dirname(__file__), "..", "model", "fraud_model.pkl") 
model : RandomForestClassifier = joblib.load(path)


class Transaction(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Scaled_Time: float
    Scaled_Amount: float

@app.post("/predict")
def predict_fraud(data: Transaction):
    input_data = np.array([[getattr(data, field) for field in data.__fields__]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    return {
        "prediction": int(prediction),
        "fraud_probability": round(probability, 4)
    }
