TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

TARGET = "Loan_Status"

# Features to keep
FEATURES = [
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
]  # Final feature to keep in data

NUMERICAL_FEATURES = ["ApplicantIncome", "LoanAmount", "Loan_Amount_Term"]  # Numerical

CATEGORICAL_FEATURES = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Credit_History",
    "Property_Area",
]  # Categorical

FEATURES_TO_ENCODE = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Credit_History",
    "Property_Area",
]  # Features to Encode

TEMPORAL_FEATURES = ["ApplicantIncome"]
TEMPORAL_ADDITION = "CoapplicantIncome"

LOG_FEATURES = ["ApplicantIncome", "LoanAmount"]  # Features for Log Transformation

DROP_FEATURES = ["CoapplicantIncome"]  # Features to Drop
