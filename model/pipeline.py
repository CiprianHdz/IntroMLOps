# Import Libraries
# Import other files/modules
import config
import preprocessors as pp
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

loan_pipe = Pipeline(
    [
        ("Numerical Imputer", pp.NumericalImputer(variables=config.NUMERICAL_FEATURES)),
        (
            "Categorical Imputer",
            pp.CategoricalImputer(variables=config.CATEGORICAL_FEATURES),
        ),
        (
            "Temporal Features",
            pp.TemporalVariableEstimator(
                variables=config.TEMPORAL_FEATURES,
                reference_variable=config.TEMPORAL_ADDITION,
            ),
        ),
        (
            "Categorical Encoder",
            pp.CategoricalEncoder(variables=config.FEATURES_TO_ENCODE),
        ),
        ("Log Transform", pp.LogTransformation(variables=config.LOG_FEATURES)),
        ("Drop Features", pp.DropFeatures(variables_to_drop=config.DROP_FEATURES)),
        ("Scaler Transform", MinMaxScaler()),
        ("Linear Model", LogisticRegression(random_state=1)),
    ]
)
