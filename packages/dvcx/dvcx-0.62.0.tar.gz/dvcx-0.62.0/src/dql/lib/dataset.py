import inspect
from typing import Callable, Optional, Sequence, Union

from sqlalchemy.sql.elements import ColumnElement

from dql.lib.udf import Aggregator, BatchMapper, Generator, GroupMapper, Mapper, UDFBase
from dql.query.dataset import DatasetQuery, PartitionByType


class Dataset(DatasetQuery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def apply(self, func, *args, **kwargs):
        return func(self, *args, **kwargs)

    def generate(
        self,
        udf: Union[Callable, UDFBase],
        parallel: Optional[int] = None,
        workers: Union[bool, int] = False,
        min_task_size: Optional[int] = None,
        params=None,
        output=None,
    ):
        self._validate_args("generate()", parallel, workers, min_task_size)

        udf_obj = self._udf_to_obj(udf, Generator, "generate()", params, output)
        return DatasetQuery.generate(
            self,
            udf_obj.to_udf_wrapper(),
            parallel=parallel,
            workers=workers,
            min_task_size=min_task_size,
        )

    def aggregate(
        self,
        udf: Union[Callable, UDFBase],
        partition_by: Optional[PartitionByType] = None,
        parallel: Optional[int] = None,
        workers: Union[bool, int] = False,
        min_task_size: Optional[int] = None,
        params=None,
        output=None,
        batch=1,
    ):
        self._validate_args("aggregate()", parallel, workers, min_task_size)

        udf_obj = self._udf_to_obj(
            udf, Aggregator, "aggregate()", params, output, batch
        )
        return DatasetQuery.generate(
            self,
            udf_obj.to_udf_wrapper(),
            partition_by=partition_by,
            parallel=parallel,
            workers=workers,
            min_task_size=min_task_size,
        )

    def map(
        self,
        udf: Union[Callable, UDFBase],
        parallel: Optional[int] = None,
        workers: Union[bool, int] = False,
        min_task_size: Optional[int] = None,
        params=None,
        output=None,
    ):
        self._validate_args("map()", parallel, workers, min_task_size)

        udf_obj = self._udf_to_obj(udf, Mapper, "map()", params, output)
        return self.add_signals(
            udf_obj.to_udf_wrapper(),
            parallel=parallel,
            workers=workers,
            min_task_size=min_task_size,
        )

    def batch_map(
        self,
        udf: Union[Callable, UDFBase],
        parallel: Optional[int] = None,
        workers: Union[bool, int] = False,
        min_task_size: Optional[int] = None,
        params=None,
        output=None,
        batch=1000,
    ):
        self._validate_args("map()", parallel, workers, min_task_size)

        udf_obj = self._udf_to_obj(
            udf, BatchMapper, "batch_map()", params, output, batch
        )
        return self.add_signals(
            udf_obj.to_udf_wrapper(),
            parallel=parallel,
            workers=workers,
            min_task_size=min_task_size,
        )

    def group_map(
        self,
        udf: Union[Callable, UDFBase],
        partition_by: Optional[PartitionByType] = None,
        parallel: Optional[int] = None,
        workers: Union[bool, int] = False,
        min_task_size: Optional[int] = None,
        params=None,
        output=None,
    ):
        self._validate_args(
            "group_map()", parallel, workers, min_task_size, partition_by
        )

        udf_obj = self._udf_to_obj(udf, GroupMapper, "group_map()", params, output)
        return self.add_signals(
            udf_obj.to_udf_wrapper(),
            parallel=parallel,
            workers=workers,
            min_task_size=min_task_size,
            partition_by=partition_by,
        )

    def _udf_to_obj(
        self,
        udf,
        target_class,
        name,
        params=None,
        output=None,
        batch=1,
    ):
        if isinstance(udf, UDFBase):
            if not isinstance(udf, target_class):
                cls_name = target_class.__name__
                raise TypeError(
                    f"{name}: expected an instance derived from {cls_name}"
                    f", but received {udf.name}"
                )
            if params:
                raise ValueError(
                    f"params for BaseUDF class {udf.name} cannot be overwritten"
                )
            if output:
                raise ValueError(
                    f"output for BaseUDF class {udf.name} cannot be overwritten"
                )
            return udf

        if inspect.isfunction(udf):
            return target_class.create_from_func(udf, params, output, batch)

        if isinstance(udf, type):
            raise TypeError(
                f"{name} error: The class '{udf}' needs to be instantiated"
                f" as an object before you can use it as UDF"
            )

        if not callable(udf):
            raise TypeError(f"{name} error: instance {udf} must be callable for UDF")

        return target_class.create_from_func(udf, params, output, batch)

    def _validate_args(
        self, name, parallel, workers, min_task_size=None, partition_by=None
    ):
        msg = None
        if not isinstance(parallel, int) and parallel is not None:
            msg = (
                f"'parallel' argument must be int or None"
                f", {parallel.__class__.__name__} was given"
            )
        elif not isinstance(workers, bool) and not isinstance(workers, int):
            msg = (
                f"'workers' argument must be int or bool"
                f", {workers.__class__.__name__} was given"
            )
        elif min_task_size is not None and not isinstance(min_task_size, int):
            msg = (
                f"'min_task_size' argument must be int or None"
                f", {min_task_size.__class__.__name__} was given"
            )
        elif (
            partition_by is not None
            and not isinstance(partition_by, ColumnElement)
            and not isinstance(partition_by, Sequence)
        ):
            msg = (
                f"'partition_by' argument must be PartitionByType or None"
                f", {partition_by.__class__.__name__} was given"
            )

        if msg:
            raise TypeError(f"Dataset {name} error: {msg}")
