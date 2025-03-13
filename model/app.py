import logging

import pandas as pd
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from wrapper import predict

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Format logs
)
logger = logging.getLogger(__name__)  # Get a logger for the app

app = FastAPI(
    title="Loan Prediction Model API",
    description="A simple API that use ML model to predict the Loan application status",
    version="0.1",
)


# This defined the input expected from the client
class LoanPred(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str


@app.get("/")
async def home():
    return {"message": "Hello, FastAPI!"}


@app.post("/predict_status")
def predict_loan_status(loan_details: LoanPred):
    data = loan_details.model_dump()

    logger.info(f"Received request: {data}")

    input_df = pd.DataFrame([data])

    features_names = [
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "ApplicantIncome",
        "CoapplicantIncome",
        "LoanAmount",
        "Loan_Amount_Term",
        "Credit_History",
        "Property_Area",
    ]

    prediction = predict(input_df[features_names])
    logger.info(f"Prediction successful: {prediction}")

    if prediction == 1:
        pred = "Approved"
    else:
        pred = "Rejected"

    return {"status": pred}


if __name__ == "__main__":
    uvicorn.run(app)
