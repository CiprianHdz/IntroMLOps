import config as config
from data_management import load_pipeline

pipeline_file_name = "classification_v1.pkl"

_loan_pipe = load_pipeline(pipeline_file_name)


def predict(input_data):
    """Predicting the output"""

    # Read Data
    data = input_data.copy()

    # prediction
    prediction = _loan_pipe.predict(data[config.FEATURES])[0]
    return prediction
