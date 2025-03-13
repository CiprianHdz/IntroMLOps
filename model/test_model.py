import pytest
from data_management import load_dataset
from wrapper import predict


@pytest.fixture
def single_prediction():
    """This function will predict the result for a single record"""
    test_df = load_dataset()["test"]
    single_test = test_df[0:1]
    print(single_test.to_dict(orient="records")[0])
    result = predict(single_test)
    print("Result", result)
    return result


def test_single_prediction_not_none(single_prediction):
    """This function will check if result of prediction is not None"""
    assert single_prediction is not None
