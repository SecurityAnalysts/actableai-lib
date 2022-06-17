from enum import Enum, unique


@unique
class TaskType(str, Enum):
    """
    Enum representing the different tasks available
    """

    CAUSAL_INFERENCE = "causal_inference"
    CLASSIFICATION = "classification"
    CLASSIFICATION_TRAIN = "classification_train"
    CLUSTERING = "clustering"
    DEC_ANCHOR_CLUSTERING = "dec_anchor_clustering"
    CORRELATION = "correlation"
    DATA_IMPUTATION = "data_imputation"
    FORECAST = "forecast"
    REGRESSION = "regression"
    REGRESSION_TRAIN = "regression_train"
    BAYESIAN_REGRESSION = "bayesian_regression"
    SENTIMENT_ANALYSIS = "sentiment_analysis"
    INTERVENTION = "intervention"
    ASSOCIATION_RULES = "association_rules"
