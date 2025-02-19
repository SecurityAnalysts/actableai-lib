from __future__ import annotations

from functools import lru_cache
from copy import deepcopy
from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from actableai.parameters.parameters import Parameters
    from actableai.timeseries.models.predictor import AAITimeSeriesPredictor

from actableai.timeseries.models.params.base import BaseParams


class ConstantValueParams(BaseParams):
    """Parameters class for the Constant Value Model."""

    @staticmethod
    @lru_cache(maxsize=None)
    def get_hyperparameters() -> Parameters:
        """Returns the hyperparameters space of the model.

        Returns:
            The hyperparameters space.
        """
        from actableai.parameters.numeric import FloatRangeSpace
        from actableai.parameters.parameters import Parameters
        from actableai.timeseries.models.params.base import Model

        parameters = [
            FloatRangeSpace(
                name="value",
                display_name="Value",
                description="Constant value used for prediction.",
                default=(0, 100),
            ),
        ]

        return Parameters(
            name=Model.constant_value,
            display_name="Constant Value Predictor",
            parameters=parameters,
        )

    def __init__(
        self,
        hyperparameters: Dict = None,
        process_hyperparameters: bool = True,
        multivariate: bool = False,
    ):
        """ConstantValueParams Constructor.

        Args:
            hyperparameters: Dictionary representing the hyperparameters space.
            process_hyperparameters: If True the hyperparameters will be validated and
                processed (deactivate if they have already been validated).
            multivariate: True if the model is multivariate.
        """

        super().__init__(
            model_name="ConstantValue",
            is_multivariate_model=multivariate,
            has_estimator=False,
            handle_feat_static_real=False,
            handle_feat_static_cat=False,
            handle_feat_dynamic_real=False,
            handle_feat_dynamic_cat=False,
            hyperparameters=hyperparameters,
            process_hyperparameters=process_hyperparameters,
        )

    def tune_config(self, prediction_length) -> Dict[str, Any]:
        """Select parameters in the pre-defined hyperparameter space.

        Returns:
            Selected parameters.
        """
        return {"value": self._auto_select("value")}

    def build_predictor(
        self,
        *,
        prediction_length: int,
        target_dim: int,
        params: Dict[str, Any],
        **kwargs,
    ) -> AAITimeSeriesPredictor:
        """Build a predictor from the underlying model using selected parameters.

        Args:
            prediction_length: Length of the prediction that will be forecasted.
            target_dim: Target dimension (number of columns to predict).
            params: Selected parameters from the hyperparameter space.
            kwargs: Ignored arguments.

        Returns:
            Built predictor.
        """
        from actableai.timeseries.models.custom.constant import ConstantValuePredictor

        return self._create_predictor(
            ConstantValuePredictor(
                value=params["value"],
                prediction_length=prediction_length,
                target_dim=target_dim,
            )
        )


class MultivariateConstantValueParams(ConstantValueParams):
    """Parameters class for the Multivariate Constant Value Model."""

    @staticmethod
    @lru_cache(maxsize=None)
    def get_hyperparameters() -> Parameters:
        """Returns the hyperparameters space of the model.

        Returns:
            The hyperparameters space.
        """
        from actableai.timeseries.models.params.base import Model

        hyperparameters = ConstantValueParams.get_hyperparameters()
        hyperparameters = deepcopy(hyperparameters)
        hyperparameters.name = Model.multivariate_constant_value
        hyperparameters.display_name = "Multivariate Constant Value Predictor"

        return hyperparameters

    def __init__(
        self,
        hyperparameters: Dict = None,
        process_hyperparameters: bool = True,
    ):
        """MultivariateConstantValueParams Constructor.

        Args:
            hyperparameters: Dictionary representing the hyperparameters space.
            process_hyperparameters: If True the hyperparameters will be validated and
                processed (deactivate if they have already been validated).
        """

        super().__init__(
            hyperparameters=hyperparameters,
            process_hyperparameters=process_hyperparameters,
            multivariate=True,
        )
