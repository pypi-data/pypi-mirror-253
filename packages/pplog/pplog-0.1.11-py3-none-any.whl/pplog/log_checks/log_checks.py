""" LogEvent classes (Checks) """


import logging
from abc import ABC, abstractmethod

from pyspark.sql import DataFrame as SparkDF

from pplog.config import Operator
from pplog.integrations import great_expectations as ge
from pplog.integrations import http

from .check_model import LogCheckResult, Metric, OperatorModel

logger = logging.getLogger(__name__)


#  pylint:disable=fixme,too-few-public-methods,too-many-function-args,too-many-instance-attributes,too-many-arguments
class _ICheck(ABC):
    """Abtract log checking class"""

    @abstractmethod
    def check(self) -> LogCheckResult:
        """Basic interface to be implemented."""
        raise NotImplementedError

    def log(self, result=None) -> None:
        """Logs payload from the check() function result"""
        if result is None:
            log_check_result = self.check()
        else:
            log_check_result = result

        payload = {
            "payload_type": log_check_result.payload_type,
            "log_check_name": log_check_result.log_check_name,
            "metric_name": log_check_result.metric.name,
            "metric_value": log_check_result.metric.value,
            "target": log_check_result.target,
            "operator_name": log_check_result.operator.name,
            "operator": log_check_result.operator.function,
            "check": "OK" if log_check_result.check else "Failed",
        }
        logger.info(payload)


class CheckFloatValue(_ICheck):
    """Spark DataFrame Count Checker"""

    def __init__(self, identifier: str, float_value: float, params: dict) -> None:
        self._identifier = identifier
        self._float_value = float_value
        self._params = params
        self._comparison_function_string = params["comparison_function"]
        self._comparison_function = getattr(Operator, self._comparison_function_string.upper())
        self._comparison_value = params["comparison_value"]

    def check(self) -> LogCheckResult:
        """Perform check and log result"""
        success = self._comparison_function(self._float_value, self._comparison_value)
        result = LogCheckResult(
            payload_type="log_check",
            log_check_name=self._identifier,
            metric=Metric(
                name="float_check",
                value=self._float_value,
            ),
            target=self._comparison_value,
            operator=OperatorModel.from_string(self._comparison_function_string.upper()),
            check=success,
        )
        return result


class CheckDataFrameCount(_ICheck):
    """Spark DataFrame Count Checker"""

    def __init__(self, identifier: str, sdf: SparkDF, params: dict) -> None:
        self._identifier = identifier
        self._sdf = sdf
        self._params = params
        self._comparison_function_string = params["comparison_function"]
        self._comparison_function = getattr(Operator, self._comparison_function_string.upper())
        self._comparison_value = params["comparison_value"]
        self._sdf_count = sdf.count()

    def check(self) -> LogCheckResult:
        """Perform check and log result"""
        success = self._comparison_function(self._sdf_count, self._comparison_value)
        result = LogCheckResult(
            payload_type="log_check",
            log_check_name=self._identifier,
            metric=Metric(
                name="row_count",
                value=self._sdf_count,
            ),
            target=self._comparison_value,
            operator=OperatorModel.from_string(self._comparison_function_string.upper()),
            check=success,
        )
        return result


class GreatExpectationsSparkDFCheck(_ICheck):
    """Checks a SparkDataFrame with great expectations library."""

    def __init__(self, identifier: str, sdf: SparkDF, params: dict) -> None:
        self._identifier = identifier
        self._sdf = sdf
        self._params = params
        self._expectation_type = params["expectation_type"]
        self._ge_kwargs = params["kwargs"]

        expectation_config = ge.ExpectationConfiguration(
            expectation_type=self._expectation_type,
            kwargs=self._ge_kwargs,
        )

        suite = ge.create_expectation_suite(expectation_config)
        self.checkpoint = ge.create_checkpoint(
            context=ge.get_in_memory_gx_context(), suite=suite, dataframe=sdf
        )

    def check(self) -> LogCheckResult:
        """Perform check and log result"""
        results = self.checkpoint.run()
        simple_results: ge.SimpleValidationResult = ge.get_validation_results(results)
        result = LogCheckResult(
            payload_type="log_check",
            log_check_name=self._identifier,
            metric=Metric(
                name=self._expectation_type,
                value="great-expectations-check",  # not sure what to put in here for GE
            ),
            target="great-expectation-check",
            operator=OperatorModel.from_great_expectations(self._expectation_type),
            check=simple_results.is_suite_success,
        )
        return result


class CheckHttpResponseCheck(_ICheck):
    """Http Response Checker"""

    def __init__(
        self,
        identifier: str,
        request: http.Request,
        response: http.Response,
        elapsed_time_in_ms: float,
        params: dict,
    ) -> None:
        self._identifier = identifier
        self._request = request
        self._response = response
        self._params = params
        self._comparison_function_string = params["comparison_function"]
        self._comparison_attribute = params["comparison_attribute"]
        self._comparison_function = getattr(Operator, self._comparison_function_string.upper())
        self._comparison_value = params["comparison_value"]
        self._url_pattern = params["url_pattern"]

        # Special value to measure latency of request
        if self._comparison_attribute == "elapsed_time_in_ms":
            self._value = elapsed_time_in_ms
        else:
            self._value = getattr(self._response, self._comparison_attribute)

    def check(self) -> LogCheckResult:
        """Perform check and log result"""
        success = self._comparison_function(self._value, self._comparison_value)
        result = LogCheckResult(
            payload_type="log_check",
            log_check_name=self._identifier,
            metric=Metric(
                name="http_request_check",
                value=self._value,
            ),
            target=self._comparison_value,
            operator=OperatorModel.from_string(self._comparison_function_string.upper()),
            check=success,
        )
        return result
