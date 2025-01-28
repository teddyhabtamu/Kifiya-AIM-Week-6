from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load('best_model.pkl')  # Replace with the path to your trained model

# Define the input data model
class InputData(BaseModel):
    CurrencyCode: str
    CountryCode: int
    ProviderId: int
    ProductId: int
    ProductCategory: str
    ChannelId: str
    Amount: float
    Value: float
    TransactionStartTime: str
    PricingStrategy: int

# Define the prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input data to DataFrame
        input_df = pd.DataFrame([data.dict()])

        # Preprocess input data
        input_df['TransactionStartTime'] = pd.to_datetime(input_df['TransactionStartTime'])
        input_df['transaction_hour'] = input_df['TransactionStartTime'].dt.hour
        input_df['transaction_day'] = input_df['TransactionStartTime'].dt.day
        input_df['transaction_month'] = input_df['TransactionStartTime'].dt.month
        input_df['transaction_year'] = input_df['TransactionStartTime'].dt.year

        # Encode categorical variables
        categorical_features = ['CurrencyCode', 'ProductCategory', 'ChannelId']
        input_df = pd.get_dummies(input_df, columns=categorical_features, drop_first=True)

        # Ensure all expected columns are present
        expected_columns = model.feature_names_in_
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns to match the training data
        input_df = input_df[expected_columns]

        # Make prediction
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)[:, 1]

        # Return prediction
        return {
            "prediction": int(prediction[0]),
            "probability": float(prediction_proba[0])
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))