# Import Libraries

import config
from data_management import load_dataset, save_pipeline
from pipeline import loan_pipe as pl


def run_training():
    """Train the model"""

    # Read Data
    dataset = load_dataset()
    train_df, _ = dataset["train"], dataset["test"]

    print("Trainig dataset", train_df.shape)

    # separating Loan_status in y
    y = train_df[config.TARGET].map({"N": 0, "Y": 1})
    pl.fit(train_df[config.FEATURES], y)
    save_pipeline(pipeline_to_save=pl)


if __name__ == "__main__":
    run_training()
