from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")


class Transaction(BaseModel):
    trans_date_trans_time: str
    cc_num: str
    merchant: str
    category: str
    amt: float
    first: str
    last: str
    gender: str
    street: str
    city: str
    state: str
    zip: int
    lat: float
    long: float
    city_pop: int
    job: str
    dob: str
    trans_num: str
    unix_time: int
    merch_lat: float
    merch_long: float


@app.post("/predict")
def predict(transaction: Transaction):
    X = pd.DataFrame([transaction.dict()])
    pred = model.predict(X)[0]
    return {"prediction": pred}


@app.post("/predict_batch")
def predict_batch(transactions: List[Transaction]):
    X = pd.DataFrame([t.dict() for t in transactions])
    preds = model.predict(X)
    return {"predictions": preds.tolist()}
