#
# This code is auto-generated using the sklearn_wrapper_template.py_template template.
# Do not modify the auto-generated code(except automatic reformatting by precommit hooks).
#
import inspect
import os
import posixpath
from typing import Iterable, Optional, Union, List, Any, Dict, Callable, Set
from typing_extensions import TypeGuard
from uuid import uuid4

import cloudpickle as cp
import pandas as pd
import numpy as np
from numpy import typing as npt

import numpy
import xgboost
from sklearn.utils.metaestimators import available_if

from snowflake.ml.modeling.framework.base import BaseTransformer, _process_cols
from snowflake.ml._internal import telemetry
from snowflake.ml._internal.exceptions import error_codes, exceptions, modeling_error_messages
from snowflake.ml._internal.env_utils import SNOWML_SPROC_ENV
from snowflake.ml._internal.utils import pkg_version_utils, identifier
from snowflake.snowpark import DataFrame, Session
from snowflake.snowpark._internal.type_utils import convert_sp_to_sf_type
from snowflake.ml.modeling._internal.snowpark_handlers import SnowparkHandlers as HandlersImpl
from snowflake.ml.modeling._internal.model_trainer_builder import ModelTrainerBuilder
from snowflake.ml.modeling._internal.model_trainer import ModelTrainer
from snowflake.ml.modeling._internal.estimator_utils import (
    gather_dependencies,
    original_estimator_has_callable,
    transform_snowml_obj_to_sklearn_obj,
    validate_sklearn_args,
)
from snowflake.ml.modeling._internal.estimator_protocols import FitPredictHandlers

from snowflake.ml.model.model_signature import (
    DataType,
    FeatureSpec,
    ModelSignature,
    _infer_signature,
    _rename_signature_with_snowflake_identifiers,
    BaseFeatureSpec,
)
from snowflake.ml.model._signatures import utils as model_signature_utils

_PROJECT = "ModelDevelopment"
# Derive subproject from module name by removing "sklearn"
# and converting module name from underscore to CamelCase
# e.g. sklearn.linear_model -> LinearModel.
_SUBPROJECT = "".join([s.capitalize() for s in "xgboost".replace("sklearn.", "").split("_")])


def _is_fit_predict_method_enabled() -> Callable[[Any], bool]:
    def check(self: BaseTransformer) -> TypeGuard[Callable[..., object]]:
        return False and callable(getattr(self._sklearn_object, "fit_predict", None))
    return check


def _is_fit_transform_method_enabled() -> Callable[[Any], bool]:
    def check(self: BaseTransformer) -> TypeGuard[Callable[..., object]]:
        return False and callable(getattr(self._sklearn_object, "fit_transform", None))
    return check


class XGBRFClassifier(BaseTransformer):
    r"""scikit-learn API for XGBoost random forest classification
    For more details on this class, see [xgboost.XGBRFClassifier]
    (https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier)

    Parameters
    ----------

    input_cols: Optional[Union[str, List[str]]]
        A string or list of strings representing column names that contain features.
        If this parameter is not specified, all columns in the input DataFrame except
        the columns specified by label_cols, sample_weight_col, and passthrough_cols
        parameters are considered input columns. Input columns can also be set after
        initialization with the `set_input_cols` method.
    
    label_cols: Optional[Union[str, List[str]]]
        A string or list of strings representing column names that contain labels.
        Label columns must be specified with this parameter during initialization
        or with the `set_label_cols` method before fitting.

    output_cols: Optional[Union[str, List[str]]]
        A string or list of strings representing column names that will store the
        output of predict and transform operations. The length of output_cols must
        match the expected number of output columns from the specific predictor or
        transformer class used.
        If you omit this parameter, output column names are derived by adding an
        OUTPUT_ prefix to the label column names for supervised estimators, or
        OUTPUT_<IDX>for unsupervised estimators. These inferred output column names
        work for predictors, but output_cols must be set explicitly for transformers.
        In general, explicitly specifying output column names is clearer, especially
        if you don’t specify the input column names.
        To transform in place, pass the same names for input_cols and output_cols.
        be set explicitly for transformers. Output columns can also be set after
        initialization with the `set_output_cols` method.

    sample_weight_col: Optional[str]
        A string representing the column name containing the sample weights.
        This argument is only required when working with weighted datasets. Sample
        weight column can also be set after initialization with the
        `set_sample_weight_col` method.

    passthrough_cols: Optional[Union[str, List[str]]]
        A string or a list of strings indicating column names to be excluded from any
        operations (such as train, transform, or inference). These specified column(s)
        will remain untouched throughout the process. This option is helpful in scenarios
        requiring automatic input_cols inference, but need to avoid using specific
        columns, like index columns, during training or inference. Passthrough columns
        can also be set after initialization with the `set_passthrough_cols` method.

    drop_input_cols: Optional[bool], default=False
        If set, the response of predict(), transform() methods will not contain input columns.

    use_external_memory_version: bool, default=False
        If set, external memory version of XGBoost trainer is used. External memory training
        is done in a two-step process. First,in the preprocessing step, input data is read and
        parsed into an internal format, which can be CSR, CSC, or sorted CSC, and stored in
        in-memory buffers. The in-memory buffers are continuously flushed out to disk when
        predefined memory limit is reached. Second, in the tree construction step, the data
        pages are streamed from disk via a multi-threaded pre-fetcher as needed for tree construction.
        Note:'tree_method's 'approx', and 'hist' are supported in the external memory version.
        Note:'grow_policy=depthwise' is used for optimal performance in the external memory version.

    batch_size: int, default=10000
        Number of rows in each batch of input data while using external memory training.
        It is not recommended to set small batch sizes, like 32 samples per batch, as this
        can seriously hurt performance in gradient boosting. Set the batch_size as large as possible
        based on the available memory.

    n_estimators: int
            Number of trees in random forest to fit.

        max_depth:  Optional[int]
            Maximum tree depth for base learners.
        max_leaves :
            Maximum number of leaves; 0 indicates no limit.
        max_bin :
            If using histogram-based algorithm, maximum number of bins per feature
        grow_policy :
            Tree growing policy. 0: favor splitting at nodes closest to the node, i.e. grow
            depth-wise. 1: favor splitting at nodes with highest loss change.
        learning_rate: Optional[float]
            Boosting learning rate (xgb's "eta")
        verbosity: Optional[int]
            The degree of verbosity. Valid values are 0 (silent) - 3 (debug).
        objective: typing.Union[str, typing.Callable[[numpy.ndarray, numpy.ndarray], typing.Tuple[numpy.ndarray, numpy.ndarray]], NoneType]
            Specify the learning task and the corresponding learning objective or
            a custom objective function to be used (see note below).
        booster: Optional[str]
            Specify which booster to use: gbtree, gblinear or dart.
        tree_method: Optional[str]
            Specify which tree method to use.  Default to auto.  If this parameter is set to
            default, XGBoost will choose the most conservative option available.  It's
            recommended to study this option from the parameters document :doc:`tree method
            </treemethod>`
        n_jobs: Optional[int]
            Number of parallel threads used to run xgboost.  When used with other
            Scikit-Learn algorithms like grid search, you may choose which algorithm to
            parallelize and balance the threads.  Creating thread contention will
            significantly slow down both algorithms.
        gamma: Optional[float]
            (min_split_loss) Minimum loss reduction required to make a further partition on a
            leaf node of the tree.
        min_child_weight: Optional[float]
            Minimum sum of instance weight(hessian) needed in a child.
        max_delta_step: Optional[float]
            Maximum delta step we allow each tree's weight estimation to be.
        subsample: Optional[float]
            Subsample ratio of the training instance.
        sampling_method :
            Sampling method. Used only by `gpu_hist` tree method.
              - `uniform`: select random training instances uniformly.
              - `gradient_based` select random training instances with higher probability when
                the gradient and hessian are larger. (cf. CatBoost)
        colsample_bytree: Optional[float]
            Subsample ratio of columns when constructing each tree.
        colsample_bylevel: Optional[float]
            Subsample ratio of columns for each level.
        colsample_bynode: Optional[float]
            Subsample ratio of columns for each split.
        reg_alpha: Optional[float]
            L1 regularization term on weights (xgb's alpha).
        reg_lambda: Optional[float]
            L2 regularization term on weights (xgb's lambda).
        scale_pos_weight: Optional[float]
            Balancing of positive and negative weights.
        base_score: Optional[float]
            The initial prediction score of all instances, global bias.
        random_state: Optional[Union[numpy.random.RandomState, int]]
            Random number seed.

               Using gblinear booster with shotgun updater is nondeterministic as
               it uses Hogwild algorithm.

        missing: float, default np.nan
            Value in the data which needs to be present as a missing value.
        num_parallel_tree: Optional[int]
            Used for boosting random forest.
        monotone_constraints: Optional[Union[Dict[str, int], str]]
            Constraint of variable monotonicity.  See :doc:`tutorial </tutorials/monotonic>`
            for more information.
        interaction_constraints: Optional[Union[str, List[Tuple[str]]]]
            Constraints for interaction representing permitted interactions.  The
            constraints must be specified in the form of a nested list, e.g. ``[[0, 1], [2,
            3, 4]]``, where each inner list is a group of indices of features that are
            allowed to interact with each other.  See :doc:`tutorial
            </tutorials/feature_interaction_constraint>` for more information
        importance_type: Optional[str]
            The feature importance type for the feature_importances\_ property:

            * For tree model, it's either "gain", "weight", "cover", "total_gain" or
              "total_cover".
            * For linear model, only "weight" is defined and it's the normalized coefficients
              without bias.

        gpu_id: Optional[int]
            Device ordinal.
        validate_parameters: Optional[bool]
            Give warnings for unknown parameter.
        predictor: Optional[str]
            Force XGBoost to use specific predictor, available choices are [cpu_predictor,
            gpu_predictor].
        enable_categorical: bool

            Experimental support for categorical data.  When enabled, cudf/pandas.DataFrame
            should be used to specify categorical data type.  Also, JSON/UBJSON
            serialization format is required.

        feature_types: FeatureTypes

            Used for specifying feature types without constructing a dataframe. See
            :py:class:`DMatrix` for details.

        max_cat_to_onehot: Optional[int]

            A threshold for deciding whether XGBoost should use one-hot encoding based split
            for categorical data.  When number of categories is lesser than the threshold
            then one-hot encoding is chosen, otherwise the categories will be partitioned
            into children nodes. Also, `enable_categorical` needs to be set to have
            categorical feature support. See :doc:`Categorical Data
            </tutorials/categorical>` and :ref:`cat-param` for details.

        max_cat_threshold: Optional[int]

            Maximum number of categories considered for each split. Used only by
            partition-based splits for preventing over-fitting. Also, `enable_categorical`
            needs to be set to have categorical feature support. See :doc:`Categorical Data
            </tutorials/categorical>` and :ref:`cat-param` for details.

        eval_metric: Optional[Union[str, List[str], Callable]]

            Metric used for monitoring the training result and early stopping.  It can be a
            string or list of strings as names of predefined metric in XGBoost (See
            doc/parameter.rst), one of the metrics in :py:mod:`sklearn.metrics`, or any other
            user defined metric that looks like `sklearn.metrics`.

            If custom objective is also provided, then custom metric should implement the
            corresponding reverse link function.

            Unlike the `scoring` parameter commonly used in scikit-learn, when a callable
            object is provided, it's assumed to be a cost function and by default XGBoost will
            minimize the result during early stopping.

            For advanced usage on Early stopping like directly choosing to maximize instead of
            minimize, see :py:obj:`xgboost.callback.EarlyStopping`.

            See :doc:`Custom Objective and Evaluation Metric </tutorials/custom_metric_obj>`
            for more.

                 This parameter replaces `eval_metric` in :py:meth:`fit` method.  The old one
                 receives un-transformed prediction regardless of whether custom objective is
                 being used.

                from sklearn.datasets import load_diabetes
                from sklearn.metrics import mean_absolute_error
                X, y = load_diabetes(return_X_y=True)
                reg = xgb.XGBRegressor(
                    tree_method="hist",
                    eval_metric=mean_absolute_error,
                )
                reg.fit(X, y, eval_set=[(X, y)])

        early_stopping_rounds: Optional[int]

            Activates early stopping. Validation metric needs to improve at least once in
            every **early_stopping_rounds** round(s) to continue training.  Requires at least
            one item in **eval_set** in :py:meth:`fit`.

            The method returns the model from the last iteration (not the best one).  If
            there's more than one item in **eval_set**, the last entry will be used for early
            stopping.  If there's more than one metric in **eval_metric**, the last metric
            will be used for early stopping.

            If early stopping occurs, the model will have three additional fields:
            :py:attr:`best_score`, :py:attr:`best_iteration` and
            :py:attr:`best_ntree_limit`.

                This parameter replaces `early_stopping_rounds` in :py:meth:`fit` method.

        callbacks: Optional[List[TrainingCallback]]
            List of callback functions that are applied at end of each iteration.
            It is possible to use predefined callbacks by using
            :ref:`Callback API <callback_api>`.

               States in callback are not preserved during training, which means callback
               objects can not be reused for multiple training sessions without
               reinitialization or deepcopy.

                for params in parameters_grid:
                    # be sure to (re)initialize the callbacks before each run
                    callbacks = [xgb.callback.LearningRateScheduler(custom_rates)]
                    xgboost.train(params, Xy, callbacks=callbacks)

        kwargs: dict, optional
            Keyword arguments for XGBoost Booster object.  Full documentation of parameters
            can be found :doc:`here </parameter>`.
            Attempting to set a parameter via the constructor args and \*\*kwargs
            dict simultaneously will result in a TypeError.

                \*\*kwargs is unsupported by scikit-learn.  We do not guarantee
                that parameters passed via this argument will interact properly
                with scikit-learn.

                A custom objective function can be provided for the ``objective``
                parameter. In this case, it should have the signature
                ``objective(y_true, y_pred) -> grad, hess``:

                y_true: array_like of shape [n_samples]
                    The target values
                y_pred: array_like of shape [n_samples]
                    The predicted values

                grad: array_like of shape [n_samples]
                    The value of the gradient for each sample point.
                hess: array_like of shape [n_samples]
                    The value of the second derivative for each sample point
    """

    def __init__(  # type: ignore[no-untyped-def]
        self,
        *,
        learning_rate=1.0,
        subsample=0.8,
        colsample_bynode=0.8,
        reg_lambda=1e-05,
        input_cols: Optional[Union[str, Iterable[str]]] = None,
        output_cols: Optional[Union[str, Iterable[str]]] = None,
        label_cols: Optional[Union[str, Iterable[str]]] = None,
        passthrough_cols: Optional[Union[str, Iterable[str]]] = None,
        drop_input_cols: Optional[bool] = False,
        sample_weight_col: Optional[str] = None,
        use_external_memory_version: bool = False,
        batch_size: int = 10000,
        **kwargs,
    ) -> None:
        super().__init__()

        self.set_input_cols(input_cols)
        self.set_output_cols(output_cols)
        self.set_label_cols(label_cols)
        self.set_passthrough_cols(passthrough_cols)
        self.set_drop_input_cols(drop_input_cols)
        self.set_sample_weight_col(sample_weight_col)
        self._use_external_memory_version = use_external_memory_version
        self._batch_size = batch_size        
        deps: Set[str] = set([f'numpy=={np.__version__}', f'xgboost=={xgboost.__version__}', f'cloudpickle=={cp.__version__}'])
        
        self._deps = list(deps)
        
        init_args = {'learning_rate':(learning_rate, 1.0, False),
            'subsample':(subsample, 0.8, False),
            'colsample_bynode':(colsample_bynode, 0.8, False),
            'reg_lambda':(reg_lambda, 1e-05, False),}
        cleaned_up_init_args = validate_sklearn_args(
            args=init_args,
            klass=xgboost.XGBRFClassifier
        )
        self._sklearn_object: Any = xgboost.XGBRFClassifier(
            **cleaned_up_init_args,
            **kwargs,
        )
        self._model_signature_dict: Optional[Dict[str, ModelSignature]] = None
        # If user used snowpark dataframe during fit, here it stores the snowpark input_cols, otherwise the processed input_cols
        self._snowpark_cols: Optional[List[str]] = self.input_cols
        self._handlers: FitPredictHandlers = HandlersImpl(class_name=XGBRFClassifier.__class__.__name__, subproject=_SUBPROJECT, autogenerated=True)
        self._autogenerated = True

    def _get_rand_id(self) -> str:
        """
        Generate random id to be used in sproc and stage names.

        Returns:
            Random id string usable in sproc, table, and stage names.
        """
        return str(uuid4()).replace("-", "_").upper()

    def set_input_cols(self, input_cols: Optional[Union[str, Iterable[str]]]) -> "XGBRFClassifier":
        """
        Input columns setter.

        Args:
            input_cols: A single input column or multiple input columns.

        Returns:
            self
        """
        self.input_cols = _process_cols(input_cols)
        self._snowpark_cols = self.input_cols
        return self

    def _get_active_columns(self) -> List[str]:
        """"Get the list of columns that are relevant to the transformer."""
        selected_cols = (
            self.input_cols +
            self.label_cols +
            ([self.sample_weight_col] if self.sample_weight_col is not None else [])
        )
        return selected_cols

    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def fit(self, dataset: Union[DataFrame, pd.DataFrame]) -> "XGBRFClassifier":
        """Fit gradient boosting classifier
        For more details on this function, see [xgboost.XGBRFClassifier.fit]
        (https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.fit)


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.

        Returns:
            self
        """
        self._infer_input_output_cols(dataset)
        if isinstance(dataset, DataFrame):
            session = dataset._session
            assert session is not None  # keep mypy happy
            # Specify input columns so column pruning will be enforced
            selected_cols = self._get_active_columns()
            if len(selected_cols) > 0:
                dataset = dataset.select(selected_cols)

            self._snowpark_cols = dataset.select(self.input_cols).columns

             # If we are already in a stored procedure, no need to kick off another one.
            if SNOWML_SPROC_ENV in os.environ:
                statement_params = telemetry.get_function_usage_statement_params(
                    project=_PROJECT,
                    subproject=_SUBPROJECT,
                    function_name=telemetry.get_statement_params_full_func_name(inspect.currentframe(), XGBRFClassifier.__class__.__name__),
                    api_calls=[Session.call],
                    custom_tags=dict([("autogen", True)]) if self._autogenerated else None,
                )
                pd_df: pd.DataFrame = dataset.to_pandas(statement_params=statement_params)
                pd_df.columns = dataset.columns
                dataset = pd_df

        model_trainer = ModelTrainerBuilder.build(
            estimator=self._sklearn_object,
            dataset=dataset,
            input_cols=self.input_cols,
            label_cols=self.label_cols,
            sample_weight_col=self.sample_weight_col,
            autogenerated=self._autogenerated,
            subproject=_SUBPROJECT,
            use_external_memory_version=self._use_external_memory_version,
            batch_size=self._batch_size,
        )
        self._sklearn_object = model_trainer.train()
        self._is_fitted = True
        self._get_model_signatures(dataset)
        return self

    def _get_pass_through_columns(self, dataset: DataFrame) -> List[str]:
        if self._drop_input_cols:
            return []
        else:
            return list(set(dataset.columns) - set(self.output_cols))

    def _batch_inference(
        self,
        dataset: DataFrame,
        inference_method: str,
        expected_output_cols_list: List[str],
        expected_output_cols_type: str = "",
        *args: Any,
        **kwargs: Any,
    ) -> DataFrame:
        """Util method to create UDF and run batch inference.
        """
        if not self._is_fitted:
            raise exceptions.SnowflakeMLException(
                error_code=error_codes.METHOD_NOT_ALLOWED,
                original_exception=RuntimeError(
                    f"Estimator {self.__class__.__name__} not fitted before calling {inference_method} method."
                ),
            )

        session = dataset._session
        if session is None:
            raise exceptions.SnowflakeMLException(
                error_code=error_codes.NOT_FOUND,
                original_exception=ValueError(
                    "Session must not specified for snowpark dataset."
                ),
            )
        # Validate that key package version in user workspace are supported in snowflake conda channel
        pkg_version_utils.get_valid_pkg_versions_supported_in_snowflake_conda_channel(
            pkg_versions=self._get_dependencies(), session=session, subproject=_SUBPROJECT)

        return self._handlers.batch_inference(
            dataset,
            session,
            self._sklearn_object,
            self._get_dependencies(),
            inference_method,
            self.input_cols,
            self._get_pass_through_columns(dataset),
            expected_output_cols_list,
            expected_output_cols_type,
            *args,
            **kwargs,
        )


    def _sklearn_inference(
        self,
        dataset: pd.DataFrame,
        inference_method: str,
        expected_output_cols_list: List[str],
        *args: Any,
        **kwargs: Any,
    ) -> pd.DataFrame:
        output_cols = expected_output_cols_list.copy()

        # Model expects exact same columns names in the input df for predict call.
        # Given the scenario that user use snowpark DataFrame in fit call, but pandas DataFrame in predict call
        # input cols need to match unquoted / quoted
        input_cols = self.input_cols
        assert self._snowpark_cols is not None  # Keep mypy happy
        _snowpark_input_cols: List[str] = self._snowpark_cols
        
        estimator = self._sklearn_object

        if hasattr(estimator, "feature_names_in_"):
            features_required_by_estimator =  getattr(estimator, "feature_names_in_")  
        else:
            features_required_by_estimator = _snowpark_input_cols
        missing_features = []
        features_in_dataset = set(dataset.columns)
        
        columns_to_select = []
        for i, f in enumerate(features_required_by_estimator):
            if (
                    i >= len(input_cols)
                    or (input_cols[i] != f and _snowpark_input_cols[i] != f)
                    or (input_cols[i] not in features_in_dataset and _snowpark_input_cols[i] not in features_in_dataset)
                ):
                missing_features.append(f)
            elif input_cols[i] in features_in_dataset:
                columns_to_select.append(input_cols[i])
            elif _snowpark_input_cols[i] in features_in_dataset:
                columns_to_select.append(_snowpark_input_cols[i])

        if len(missing_features) > 0:
            raise exceptions.SnowflakeMLException(
                error_code=error_codes.NOT_FOUND,
                original_exception=ValueError(
                    "The feature names should match with those that were passed during fit.\n"
                    f"Features seen during fit call but not present in the input: {missing_features}\n"
                    f"Features in the input dataframe : {input_cols}\n"
                ),
            )
        input_df = dataset[columns_to_select]
        input_df.columns = features_required_by_estimator

        inference_res = getattr(estimator, inference_method)(input_df, *args, **kwargs)

        if (
            isinstance(inference_res, list)
            and len(inference_res) > 0
            and isinstance(inference_res[0], np.ndarray)
        ):
            # In case of multioutput estimators, predict_proba, decision_function etc., functions return a list of
            # ndarrays. We need to concatenate them.

            # First compute output column names
            if len(output_cols) == len(inference_res):
                actual_output_cols = []
                for idx, np_arr in enumerate(inference_res):
                    for i in range(1 if len(np_arr.shape) <= 1 else np_arr.shape[1]):
                        actual_output_cols.append(f"{output_cols[idx]}_{i}")
                output_cols = actual_output_cols

            # Concatenate np arrays
            transformed_numpy_array = np.concatenate(inference_res, axis=1)
        elif (
                isinstance(inference_res, tuple)
                and len(inference_res) > 0
                and isinstance(inference_res[0], np.ndarray)
            ):
                # In case of kneighbors, functions return a tuple of ndarrays.
                transformed_numpy_array = np.stack(inference_res, axis=1)
        else:
            transformed_numpy_array = inference_res

        if (len(transformed_numpy_array.shape) == 3) and inference_method != "kneighbors":
            # VotingClassifier will return results of shape (n_classifiers, n_samples, n_classes)
            # when voting = "soft" and flatten_transform = False. We can't handle unflatten transforms,
            # so we ignore flatten_transform flag and flatten the results.
            transformed_numpy_array = np.hstack(transformed_numpy_array)  # type: ignore[call-overload]

        if len(transformed_numpy_array.shape) == 1:
            transformed_numpy_array = np.reshape(transformed_numpy_array, (-1, 1))

        shape = transformed_numpy_array.shape
        if shape[1] != len(output_cols):
            if len(output_cols) != 1:
                raise exceptions.SnowflakeMLException(
                    error_code=error_codes.INVALID_ARGUMENT,
                    original_exception=TypeError(
                        "expected_output_cols_list must be same length as transformed array or "
                        "should be of length 1"
                    ),
                )
            actual_output_cols = []
            for i in range(shape[1]):
                actual_output_cols.append(f"{output_cols[0]}_{i}")
            output_cols = actual_output_cols

        if inference_method == "kneighbors":
            if (len(transformed_numpy_array.shape) == 3):  # return_distance=True
                shape = transformed_numpy_array.shape
                data = [transformed_numpy_array[:, i, :].tolist() for i in range(shape[1])]
                kneighbors_df = pd.DataFrame({output_cols[i]: data[i] for i in range(shape[1])})
            else:  # return_distance=False
                kneighbors_df = pd.DataFrame(
                    {output_cols[0]: [
                        transformed_numpy_array[i, :].tolist() for i in range(transformed_numpy_array.shape[0])
                    ]}
                )

            if self._drop_input_cols:
                dataset = kneighbors_df
            else:
                dataset = pd.concat([dataset, kneighbors_df], axis=1)
        else:
            if self._drop_input_cols:
                dataset = pd.DataFrame(data=transformed_numpy_array, columns=output_cols)
            else:
                dataset = dataset.copy()
                dataset[output_cols] = transformed_numpy_array
        return dataset

    @available_if(original_estimator_has_callable("predict"))  # type: ignore[misc]
    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def predict(self, dataset: Union[DataFrame, pd.DataFrame]) -> Union[DataFrame, pd.DataFrame]:
        """Predict with `X`
        For more details on this function, see [xgboost.XGBRFClassifier.predict]
        (https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.predict)


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.

        Returns:
            Transformed dataset.
        """
        super()._check_dataset_type(dataset)
        if isinstance(dataset, DataFrame):
            expected_type_inferred = ""
            # when it is classifier, infer the datatype from label columns
            if expected_type_inferred == "" and 'predict' in self.model_signatures:
                # Batch inference takes a single expected output column type. Use the first columns type for now.
                label_cols_signatures = [row for row in self.model_signatures['predict'].outputs if row.name in self.output_cols]
                if len(label_cols_signatures) == 0:
                    error_str = f"Output columns {self.output_cols} do not match model signatures {self.model_signatures['predict'].outputs}."
                    raise exceptions.SnowflakeMLException(
                        error_code=error_codes.INVALID_ATTRIBUTE,
                        original_exception=ValueError(error_str),
                    )
                expected_type_inferred = convert_sp_to_sf_type(
                    label_cols_signatures[0].as_snowpark_type()
                )
            
            output_df = self._batch_inference(
                dataset=dataset,
                inference_method="predict",
                expected_output_cols_list=self.output_cols,
                expected_output_cols_type=expected_type_inferred,
            )
        elif isinstance(dataset, pd.DataFrame):
            output_df = self._sklearn_inference(
                dataset=dataset,
                inference_method="predict",
                expected_output_cols_list=self.output_cols,)

        return output_df

    @available_if(original_estimator_has_callable("transform"))  # type: ignore[misc]
    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def transform(self, dataset: Union[DataFrame, pd.DataFrame]) -> Union[DataFrame, pd.DataFrame]:
        """Method not supported for this class.


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.

        Returns:
            Transformed dataset.
        """
        super()._check_dataset_type(dataset)
        if isinstance(dataset, DataFrame):
            expected_dtype = ""
            if False:  # is child of _BaseHeterogeneousEnsemble
                # transform() method of HeterogeneousEnsemble estimators return responses of varying shapes
                # from (n_samples, n_estimators) to (n_samples, n_estimators * n_classes) (and everything in between)
                # based on init param values. We will convert that to pandas dataframe of shape (n_samples, 1) with
                # each row containing a list of values.
                expected_dtype = "ARRAY"

            # If we were unable to assign a type to this transform in the factory, infer the type here.
            if expected_dtype == "":
                # If this is a clustering transformer, if the number of output columns does not equal the number of clusters the response will be an "ARRAY"
                if hasattr(self._sklearn_object, "n_clusters") and getattr(self._sklearn_object, "n_clusters") != len(self.output_cols):
                    expected_dtype = "ARRAY"
                # If this is a decomposition transformer, if the number of output columns does not equal the number of components the response will be an "ARRAY"
                elif hasattr(self._sklearn_object, "n_components") and getattr(self._sklearn_object, "n_components") != len(self.output_cols):
                    expected_dtype = "ARRAY"
                else:
                    output_types = [signature.as_snowpark_type() for signature in _infer_signature(dataset[self.input_cols], "output", use_snowflake_identifiers=True)]
                    # We can only infer the output types from the input types if the following two statemetns are true:
                    # 1) All of the output types are the same. Otherwise, we still have to fall back to variant because `_sklearn_inference` only accepts one type.
                    # 2) The length of the input columns equals the length of the output columns. Otherwise the transform will likely result in an `ARRAY`.
                    if all(x == output_types[0] for x in output_types) and len(output_types) == len(self.output_cols):
                        expected_dtype = convert_sp_to_sf_type(output_types[0])
            
            output_df = self._batch_inference(
                dataset=dataset,
                inference_method="transform",
                expected_output_cols_list=self.output_cols,
                expected_output_cols_type=expected_dtype,
            )
        elif isinstance(dataset, pd.DataFrame):
            output_df = self._sklearn_inference(
                dataset=dataset,
                inference_method="transform",
                expected_output_cols_list=self.output_cols,
            )

        return output_df
    
    @available_if(_is_fit_predict_method_enabled())  # type: ignore[misc]
    def fit_predict(self, dataset: Union[DataFrame, pd.DataFrame]) -> Union[Any, npt.NDArray[Any]]:
        """ Method not supported for this class.


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.
        Returns:
            Predicted dataset.
        """
        self.fit(dataset)
        assert self._sklearn_object is not None
        return self._sklearn_object.labels_


    @available_if(_is_fit_transform_method_enabled())  # type: ignore[misc]
    def fit_transform(self, dataset: Union[DataFrame, pd.DataFrame]) -> Union[Any, npt.NDArray[Any]]:
        """ 
        Returns:
            Transformed dataset.
        """
        self.fit(dataset)
        assert self._sklearn_object is not None
        return self._sklearn_object.embedding_


    def _get_output_column_names(self, output_cols_prefix: str, output_cols: Optional[List[str]] = None) -> List[str]:
        """ Returns the list of output columns for predict_proba(), decision_function(), etc.. functions.
        Returns a list with output_cols_prefix as the only element if the estimator is not a classifier.
        """
        output_cols_prefix = identifier.resolve_identifier(output_cols_prefix)
        if output_cols:
            output_cols = [
                identifier.concat_names([output_cols_prefix, identifier.resolve_identifier(c)])
                for c in output_cols
            ]
        elif getattr(self._sklearn_object, "classes_", None) is None:
            output_cols = [output_cols_prefix]
        elif self._sklearn_object is not None:
            classes = self._sklearn_object.classes_
            if isinstance(classes, numpy.ndarray):
                output_cols = [f'{output_cols_prefix}{str(c)}' for c in classes.tolist()]
            elif isinstance(classes, list) and len(classes) > 0 and isinstance(classes[0], numpy.ndarray):
                # If the estimator is a multioutput estimator, classes_ will be a list of ndarrays.
                output_cols = []
                for i, cl in enumerate(classes):
                    # For binary classification, there is only one output column for each class
                    # ndarray as the two classes are complementary.
                    if len(cl) == 2:
                        output_cols.append(f'{output_cols_prefix}{i}_{cl[0]}')
                    else:
                        output_cols.extend([
                            f'{output_cols_prefix}{i}_{c}' for c in cl.tolist()
                        ])
        else:
            output_cols = []

        # Make sure column names are valid snowflake identifiers.
        assert output_cols is not None  # Make MyPy happy
        rv = [identifier.rename_to_valid_snowflake_identifier(c) for c in output_cols]

        return rv

    @available_if(original_estimator_has_callable("predict_proba"))  # type: ignore[misc]
    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def predict_proba(
        self, dataset: Union[DataFrame, pd.DataFrame], output_cols_prefix: str = "predict_proba_"
    ) -> Union[DataFrame, pd.DataFrame]:
        """Predict the probability of each `X` example being of a given class
        For more details on this function, see [xgboost.XGBRFClassifier.predict_proba]
        (https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.predict_proba)


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.
            output_cols_prefix: Prefix for the response columns

        Returns:
            Output dataset with probability of the sample for each class in the model.
        """
        super()._check_dataset_type(dataset)
        if isinstance(dataset, DataFrame):
            output_df = self._batch_inference(
                dataset=dataset,
                inference_method="predict_proba",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix),
                expected_output_cols_type="float"
            )
        elif isinstance(dataset, pd.DataFrame):
            output_df = self._sklearn_inference(
                dataset=dataset,
                inference_method="predict_proba",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix),
            )
        
        return output_df

    @available_if(original_estimator_has_callable("predict_log_proba"))  # type: ignore[misc]
    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def predict_log_proba(
        self, dataset: Union[DataFrame, pd.DataFrame], output_cols_prefix: str = "predict_log_proba_"
    ) -> Union[DataFrame, pd.DataFrame]:
        """Predict the probability of each `X` example being of a given class
        For more details on this function, see [xgboost.XGBRFClassifier.predict_proba]
        (https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.predict_proba)


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.
            output_cols_prefix: str
                Prefix for the response columns

        Returns:
            Output dataset with log probability of the sample for each class in the model.
        """
        super()._check_dataset_type(dataset)
        if isinstance(dataset, DataFrame):
            output_df = self._batch_inference(
                dataset=dataset,
                inference_method="predict_log_proba",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix),
                expected_output_cols_type="float"
            )
        elif isinstance(dataset, pd.DataFrame):
            output_df = self._sklearn_inference(
                dataset=dataset,
                inference_method="predict_log_proba",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix),
            )

        return output_df

    @available_if(original_estimator_has_callable("decision_function"))  # type: ignore[misc]
    def decision_function(
        self, dataset: Union[DataFrame, pd.DataFrame], output_cols_prefix: str = "decision_function_"
    ) -> Union[DataFrame, pd.DataFrame]:
        """Method not supported for this class.


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.
            output_cols_prefix: str
                Prefix for the response columns

        Returns:
            Output dataset with results of the decision function for the samples in input dataset.
        """
        super()._check_dataset_type(dataset)
        if isinstance(dataset, DataFrame):
            output_df = self._batch_inference(
                dataset=dataset,
                inference_method="decision_function",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix),
                expected_output_cols_type="float"
            )
        elif isinstance(dataset, pd.DataFrame):
            output_df = self._sklearn_inference(
                dataset=dataset,
                inference_method="decision_function",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix),
            )

        return output_df

    @available_if(original_estimator_has_callable("score"))  # type: ignore[misc]
    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def score(self, dataset: Union[DataFrame, pd.DataFrame]) -> float:
        """Return the mean accuracy on the given test data and labels
        For more details on this function, see [xgboost.XGBRFClassifier.score]
        (https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.XGBRFClassifier.score)


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.

        Returns:
            Score.
        """
        self._infer_input_output_cols(dataset)
        super()._check_dataset_type(dataset)
        if isinstance(dataset, pd.DataFrame):
            output_score = self._handlers.score_pandas(
                dataset,
                self._sklearn_object,
                self.input_cols,
                self.label_cols,
                self.sample_weight_col

            )
        elif isinstance(dataset, DataFrame):
            output_score = self._score_snowpark(dataset)
        return output_score

    def _score_snowpark(self, dataset: DataFrame) -> float:
        # Specify input columns so column pruing will be enforced
        selected_cols = self._get_active_columns()
        if len(selected_cols) > 0:
            dataset = dataset.select(selected_cols)

        session = dataset._session
        assert session is not None  # keep mypy happy

        score = self._handlers.score_snowpark(
            dataset,
            session,
            self._sklearn_object,
            ["snowflake-snowpark-python"] + self._get_dependencies(),
            ['xgboost'],
            self.input_cols,
            self.label_cols,
            self.sample_weight_col,
        )

        return score

    @available_if(original_estimator_has_callable("kneighbors"))  # type: ignore[misc]
    @telemetry.send_api_usage_telemetry(
        project=_PROJECT,
        subproject=_SUBPROJECT,
        custom_tags=dict([("autogen", True)]),
    )
    def kneighbors(
        self,
        dataset: Union[DataFrame, pd.DataFrame],
        n_neighbors: Optional[int] = None,
        return_distance: bool = True,
        output_cols_prefix: str = "kneighbors_",
    ) -> Union[DataFrame, pd.DataFrame]:
        """Method not supported for this class.


        Raises:
            TypeError: Supported dataset types: snowpark.DataFrame, pandas.DataFrame.

        Args:
            dataset: Union[snowflake.snowpark.DataFrame, pandas.DataFrame]
                Snowpark or Pandas DataFrame.
            output_cols_prefix: str
                Prefix for the response columns

        Returns:
            Output dataset with results of the K-neighbors for the samples in input dataset.
        """
        super()._check_dataset_type(dataset)
        output_cols = ["neigh_ind"]
        if return_distance:
            output_cols.insert(0, "neigh_dist")
        if isinstance(dataset, DataFrame):
            output_df = self._batch_inference(
                dataset=dataset,
                inference_method="kneighbors",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix, output_cols),
                expected_output_cols_type="array",
                n_neighbors=n_neighbors,
                return_distance=return_distance,
            )
        elif isinstance(dataset, pd.DataFrame):
            output_df = self._sklearn_inference(
                dataset=dataset,
                inference_method="kneighbors",
                expected_output_cols_list=self._get_output_column_names(output_cols_prefix, output_cols),
                n_neighbors=n_neighbors,
                return_distance=return_distance,
            )

        return output_df

    def _get_model_signatures(self, dataset: Union[DataFrame, pd.DataFrame]) -> None:
        self._model_signature_dict = dict()

        PROB_FUNCTIONS = ["predict_log_proba", "predict_proba", "decision_function"]

        inputs = list(_infer_signature(dataset[self.input_cols], "input"))
        outputs: List[BaseFeatureSpec] = []
        if hasattr(self, "predict"):
            # keep mypy happy
            assert self._sklearn_object is not None and hasattr(self._sklearn_object, "_estimator_type") 
            # For classifier, the type of predict is the same as the type of label
            if self._sklearn_object._estimator_type == 'classifier':
                 # label columns is the desired type for output
                outputs = list(_infer_signature(dataset[self.label_cols], "output", use_snowflake_identifiers=True))
                # rename the output columns
                outputs = list(model_signature_utils.rename_features(outputs, self.output_cols))
                self._model_signature_dict["predict"] = ModelSignature(inputs,
                                                                       ([] if self._drop_input_cols else inputs)
                                                                       + outputs)
            # For mixture models that use the density mixin, `predict` returns the argmax of the log prob.
            # For outlier models, returns -1 for outliers and 1 for inliers.
            # Clusterer returns int64 cluster labels. 
            elif self._sklearn_object._estimator_type in ["DensityEstimator", "clusterer", "outlier_detector"]:
                outputs = [FeatureSpec(dtype=DataType.INT64, name=c) for c in self.output_cols]
                self._model_signature_dict["predict"] = ModelSignature(inputs,
                                                                       ([] if self._drop_input_cols else inputs)
                                                                       + outputs)
            
            # For regressor, the type of predict is float64
            elif self._sklearn_object._estimator_type == 'regressor':
                outputs = [FeatureSpec(dtype=DataType.DOUBLE, name=c) for c in self.output_cols]
                self._model_signature_dict["predict"] = ModelSignature(inputs,
                                                                       ([] if self._drop_input_cols else inputs)
                                                                       + outputs)
                
        for prob_func in PROB_FUNCTIONS:
            if hasattr(self, prob_func):
                output_cols_prefix: str = f"{prob_func}_"
                output_column_names = self._get_output_column_names(output_cols_prefix)
                outputs = [FeatureSpec(dtype=DataType.DOUBLE, name=c) for c in output_column_names]
                self._model_signature_dict[prob_func] = ModelSignature(inputs,
                                                                       ([] if self._drop_input_cols else inputs)
                                                                       + outputs)

        # Output signature names may still need to be renamed, since they were not created with `_infer_signature`.
        items = list(self._model_signature_dict.items())
        for method, signature in items:
            signature._outputs = _rename_signature_with_snowflake_identifiers(signature._outputs)
            self._model_signature_dict[method] = signature

    @property
    def model_signatures(self) -> Dict[str, ModelSignature]:
        """Returns model signature of current class.

        Raises:
            exceptions.SnowflakeMLException: If estimator is not fitted, then model signature cannot be inferred

        Returns:
            Dict[str, ModelSignature]: each method and its input output signature
        """
        if self._model_signature_dict is None:
            raise exceptions.SnowflakeMLException(
                error_code=error_codes.INVALID_ATTRIBUTE,
                original_exception=RuntimeError("Estimator not fitted before accessing property model_signatures!"),
            )
        return self._model_signature_dict

    def to_xgboost(self) -> Any:
        """Get xgboost.XGBRFClassifier object.
        """
        if self._sklearn_object is None:
            self._sklearn_object = self._create_sklearn_object()
        return self._sklearn_object

    def to_sklearn(self) -> Any:
        raise exceptions.SnowflakeMLException(
            error_code=error_codes.METHOD_NOT_ALLOWED,
            original_exception=AttributeError(
                modeling_error_messages.UNSUPPORTED_MODEL_CONVERSION.format(
                    "to_sklearn()", 
                    "to_xgboost()"
                )
            ),
        )

    def to_lightgbm(self) -> Any:
        raise exceptions.SnowflakeMLException(
            error_code=error_codes.METHOD_NOT_ALLOWED,
            original_exception=AttributeError(
                modeling_error_messages.UNSUPPORTED_MODEL_CONVERSION.format(
                    "to_lightgbm()", 
                    "to_xgboost()"
                )
            ),
        )

    def _get_dependencies(self) -> List[str]:
        return self._deps
