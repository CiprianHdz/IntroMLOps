import config
import joblib
import pandas as pd


def load_dataset():
    """Read Data"""
    train_df = pd.read_csv(config.TRAIN_FILE)
    test_df = pd.read_csv(config.TEST_FILE)
    return {"train": train_df, "test": test_df}


def save_pipeline(pipeline_to_save):
    """Store Output Of Pipeline
    Exporting pickle file of trained Model"""
    save_file_name = "classification_v1.pkl"
    joblib.dump(pipeline_to_save, save_file_name)
    print("Saved Pipeline : ", save_file_name)



def load_pipeline(pipeline_to_load):
    """Importing pickle file of trained Model"""
    return joblib.load(pipeline_to_load)
