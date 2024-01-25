"""Support for different "views" over existing datasets.

These allow constraining the usable data that is exposed to a modeller, or only
presenting a transformed view to the modeller rather than the raw underlying data.
"""
from abc import ABC, abstractmethod
from functools import cached_property
import logging
from typing import (
    Any,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Mapping,
    MutableMapping,
    Optional,
    TypeVar,
    Union,
    cast,
    overload,
)

import methodtools
import numpy as np
import pandas as pd

from bitfount.data.datasources.base_source import BaseSource, FileSystemIterableSource
from bitfount.data.datasources.empty_source import _EmptySource
from bitfount.data.datasplitters import DatasetSplitter
from bitfount.data.schema import BitfountSchema
from bitfount.data.types import _ForceStypeValue, _SemanticTypeValue, _SingleOrMulti
from bitfount.types import _Dtypes
from bitfount.utils import _add_this_to_list, delegates
from bitfount.utils.db_connector import PodDbConnector

logger = logging.getLogger(__name__)


class DataView(BaseSource, ABC):
    """Base class for datasource views.

    Args:
        datasource: The `BaseSource` the view is generated from.
    """

    def __init__(
        self,
        datasource: BaseSource,
        source_dataset_name: str,
        data_splitter: Optional[DatasetSplitter] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._datasource = datasource
        self.source_dataset_name = source_dataset_name
        self.data_splitter = (
            data_splitter
            if data_splitter is not None
            else self._datasource.data_splitter
        )

    @property
    def is_task_running(self) -> bool:
        """Returns `_is_task_running` for the view and the parent datasource."""
        return self._is_task_running and self._datasource.is_task_running

    @is_task_running.setter
    def is_task_running(self, value: bool) -> None:
        """Sets `_is_task_running` to `value` for the view and the parent datasource."""
        self._is_task_running = value
        self._datasource.is_task_running = value

    def load_data(self, **kwargs: Any) -> None:
        """Loads data from the underlying datasource."""
        self._datasource.load_data(**kwargs)
        super().load_data(**kwargs)


@delegates()
class _DataViewFromFileIterableSource(DataView):
    """A data view derived from a file-iterable datasource."""

    _datasource: FileSystemIterableSource

    def __init__(
        self,
        datasource: FileSystemIterableSource,
        source_dataset_name: str,
        data_splitter: Optional[DatasetSplitter] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            datasource=datasource,
            source_dataset_name=source_dataset_name,
            data_splitter=data_splitter,
            **kwargs,
        )

    @property
    def selected_file_names(self) -> List[str]:
        """Returns `selected_file_names` for the view."""
        raise NotImplementedError

    @property
    def file_names(self) -> List[str]:
        """Get filenames for views generated from FileSystemIterableSource."""
        raise NotImplementedError

    def yield_data(
        self, file_names: Optional[List[str]] = None, **kwargs: Any
    ) -> Iterator[pd.DataFrame]:
        """Returns `file_names` for the view and the parent datasource."""
        raise NotImplementedError


@delegates()
class _EmptyDataview(DataView):
    """A data view that presents no data.

    This internal class is used for retuning empty DataView
    when SQLDataView cannot be instantiated because of no
    connector provided.
    We return an _EmptyDataview object and log instead of
    raising an error.
    """

    _datasource: _EmptySource

    def get_values(
        self, col_names: List[str], **kwargs: Any
    ) -> Dict[str, Iterable[Any]]:
        """Returns empty dictionary as there are no columns to return."""
        return {}

    def get_column_names(self, **kwargs: Any) -> Iterable[str]:
        """Returns list as there are no columns to return."""
        return list()

    def get_column(self, col_name: str, **kwargs: Any) -> Union[np.ndarray, pd.Series]:
        """Returns empty np array as there are no columns to return."""
        return np.array([])

    def get_data(self, **kwargs: Any) -> None:
        """Returns None as there is no data."""
        return self._datasource.get_data()

    def get_dtypes(self, **kwargs: Any) -> _Dtypes:
        """Returns an empty dict as there is no data."""
        return self._datasource.get_dtypes()

    def __len__(self) -> int:
        """Returns zero as there is no data."""
        return len(self._datasource)


@delegates()
class DropColsDataview(DataView):
    """A data view that presents data with columns removed."""

    _datasource: BaseSource

    def __init__(
        self,
        datasource: BaseSource,
        drop_cols: _SingleOrMulti[str],
        source_dataset_name: str,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            datasource=datasource, source_dataset_name=source_dataset_name, **kwargs
        )
        self._drop_cols: List[str] = (
            [drop_cols] if isinstance(drop_cols, str) else list(drop_cols)
        )

    # TODO: [BIT-1780] Simplify referencing data in here and in other sources
    #       We want to avoid recalculating but we don't want to cache more
    #       than one result at a time to save memory
    @methodtools.lru_cache(maxsize=1)
    def get_data(self, **kwargs: Any) -> pd.DataFrame:
        """Loads and returns data from underlying dataset.

        Will handle drop columns specified in view.

        Returns:
            A DataFrame-type object which contains the data.

        Raises:
            ValueError: if no data is returned from the original datasource.
        """
        df: Optional[pd.DataFrame] = self._datasource.get_data(**kwargs)
        # Ensure we return a copy of the dataframe rather than mutating the original
        if isinstance(df, pd.DataFrame):
            drop_df = df.drop(columns=self._drop_cols)
            return drop_df
        else:
            raise ValueError("No data returned from the underlying datasource.")

    def get_values(
        self, col_names: List[str], **kwargs: Any
    ) -> Dict[str, Iterable[Any]]:
        """Get distinct values from columns in dataset.

        Args:
            col_names: The list of the columns whose distinct values should be
                returned.

        Returns:
            The distinct values of the requested column as a mapping from col name to
            a series of distinct values.

        """
        data: pd.DataFrame = self.get_data(**kwargs)
        return {col: data[col].unique() for col in col_names}

    def get_column_names(self, **kwargs: Any) -> Iterable[str]:
        """Get the column names as an iterable."""
        df: pd.DataFrame = self.get_data(**kwargs)
        return list(df.columns)

    def get_column(self, col_name: str, **kwargs: Any) -> Union[np.ndarray, pd.Series]:
        """Loads and returns single column from dataset.

        Args:
            col_name: The name of the column which should be loaded.

        Returns:
            The column request as a series.
        """
        df: pd.DataFrame = self.get_data(**kwargs)
        return df[col_name]

    def get_dtypes(self, **kwargs: Any) -> _Dtypes:
        """Loads and returns the columns and column types of the dataset.

        Returns:
            A mapping from column names to column types.
        """
        df: pd.DataFrame = self.get_data(**kwargs)
        return self._get_data_dtypes(df)

    def __len__(self) -> int:
        return len(self.get_data())


@delegates()
class DropColsFileSystemIterableDataview(
    DropColsDataview, _DataViewFromFileIterableSource
):
    """A data view that presents filesystem iterable data with columns removed.

    Raises:
        ValueError: if the underlying datasource is not of
            FileSystemIterableSource type.
    """

    _datasource: FileSystemIterableSource

    def __init__(
        self,
        datasource: BaseSource,
        drop_cols: _SingleOrMulti[str],
        source_dataset_name: str,
        **kwargs: Any,
    ) -> None:
        if not isinstance(datasource, FileSystemIterableSource):
            raise ValueError(
                "Underlying datasource is not a `FileSystemIterableSource`, "
                "which is the only compatible datasource for this view."
            )

        super().__init__(
            datasource=datasource,
            drop_cols=drop_cols,
            source_dataset_name=source_dataset_name,
            **kwargs,
        )

    @property
    def selected_file_names(self) -> List[str]:
        """Returns `selected_file_names` for the view."""
        return self._datasource.selected_file_names

    @cached_property
    def file_names(self) -> List[str]:
        """Get filenames for views generated from FileSystemIterableSource."""
        return self._datasource.file_names

    @property
    def iterable(self) -> bool:
        """Returns `iterable` for the view and the parent datasource."""
        return self._datasource.iterable

    def yield_data(
        self, file_names: Optional[List[str]] = None, **kwargs: Any
    ) -> Iterator[pd.DataFrame]:
        """Returns `file_names` for the view and the parent datasource."""
        return self._datasource.yield_data(file_names=file_names, **kwargs)


@delegates()
class SQLDataView(DataView):
    """A data view that presents data with SQL query applied.

    Raises:
        ValueError: if the underlying datasource is of
            IterableSource type.
    """

    _datasource: BaseSource
    _connector: PodDbConnector

    def __init__(
        self,
        datasource: BaseSource,
        query: str,
        pod_name: str,
        source_dataset_name: str,
        connector: PodDbConnector,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            datasource=datasource, source_dataset_name=source_dataset_name, **kwargs
        )
        self._connector = connector
        self.query = query
        self.pod_db_name = pod_name

    def _get_updated_query_with_metadata(self) -> str:
        """Get updated query with metadata columns included.

        For non-iterable datasources the `datapoint_hash`
        column is added.
        """
        metadata_cols_as_str = '"datapoint_hash",'
        if "datapoint_hash" not in self.query:
            return self.query.replace("SELECT", f"SELECT {metadata_cols_as_str}")
        return self.query

    @methodtools.lru_cache(maxsize=1)
    def get_data(self, **kwargs: Any) -> pd.DataFrame:
        """Loads and returns data from underlying dataset.

        Will handle sql query specified in view.

        Returns:
            A DataFrame-type object which contains the data.

        Raises:
            ValueError: if the table specified in the query is not found.
        """
        # Get tables and check that table requested in
        # the query matches at least one of the tables in the database.
        db_conn = self._connector.get_db_connection_from_name(self.pod_db_name)
        tables = self.get_tables()
        if not any(table in self.query for table in tables):
            db_conn.close()
            logger.warning("The table specified in the query does not exist.")
            # Return empty dataframe
            return pd.DataFrame()
        df = pd.read_sql_query(self.query, db_conn)
        db_conn.close()
        return df

    def get_tables(self) -> List[str]:
        """Get the datasource tables from the pod database."""
        db_conn = self._connector.get_db_connection_from_name(self.pod_db_name)
        cur = db_conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        db_conn.close()
        # tables are returned as a list of tuples where the first tuple
        # is the table name, so we need to unpack them
        return [table[0] for table in tables]

    def get_values(
        self, col_names: List[str], table_name: Optional[str] = None, **kwargs: Any
    ) -> Dict[str, Iterable[Any]]:
        """Get distinct values from columns in the dataset.

        Args:
            col_names: The list of the columns whose distinct values should be
                returned.

        Returns:
            The distinct values of the requested column as a mapping from col name to
            a series of distinct values.

        """
        data: pd.DataFrame = self.get_data(**kwargs)
        return {col: data[col].unique() for col in col_names}

    def get_column_names(self, **kwargs: Any) -> Iterable[str]:
        """Get the column names as an iterable."""
        df: pd.DataFrame = self.get_data(**kwargs)
        return list(df.columns)

    def get_column(
        self, col_name: str, table_name: Optional[str] = None, **kwargs: Any
    ) -> Union[np.ndarray, pd.Series]:
        """Loads and returns single column from dataset.

        Args:
            col_name: The name of the column which should be loaded.

        Returns:
            The column request as a series.
        """

        df: pd.DataFrame = self.get_data(**kwargs)
        return df[col_name]

    def get_dtypes(self, table_name: Optional[str] = None, **kwargs: Any) -> _Dtypes:
        """Loads and returns the columns and column types of the dataset.

        Returns:
            A mapping from column names to column types.
        """
        df: pd.DataFrame = self.get_data(**kwargs)
        return self._get_data_dtypes(df)

    def __len__(self) -> int:
        return len(self.get_data())


@delegates()
class SQLFileSystemIterableDataView(SQLDataView, _DataViewFromFileIterableSource):
    """A data view that presents filesystem iterable data with SQL query applied.

    Raises:
        ValueError: if the underlying datasource is not of
            FileSystemIterableSource type.
    """

    _datasource: FileSystemIterableSource

    def __init__(
        self,
        datasource: BaseSource,
        query: str,
        pod_name: str,
        source_dataset_name: str,
        connector: PodDbConnector,
        **kwargs: Any,
    ) -> None:
        if not isinstance(datasource, FileSystemIterableSource):
            raise ValueError(
                "Underlying datasource is not a `FileSystemIterableSource`, "
                "which is the only compatible datasource for this view."
            )

        super().__init__(
            datasource=datasource,
            query=query,
            pod_name=pod_name,
            source_dataset_name=source_dataset_name,
            connector=connector,
            **kwargs,
        )

    @property
    def selected_file_names(self) -> List[str]:
        """Returns `selected_file_names` for the view."""
        return [
            file
            for file in self._datasource.selected_file_names
            if file in self.file_names
        ]

    @cached_property
    def file_names(self) -> List[str]:
        """Get filenames for views generated from FileSystemIterableSource."""
        db_conn = self._connector.get_db_connection_from_name(self.pod_db_name)
        tables = self.get_tables()
        if not any(table in self.query for table in tables):
            logger.warning("The table specified in the query does not exist.")
        # We get the updated query that also includes the `_original_filename`
        # column, so we can obtain the list of filenames from the view.
        query_with_original_filename = self._get_updated_query_with_metadata()
        try:
            df = pd.read_sql_query(query_with_original_filename, db_conn)
            return df["_original_filename"].tolist()
        except Exception:
            logger.warning(
                "Could not obtain the filenames for the datasource. "
                "Make sure that your file-iterable datasource is properly defined."
            )
            return []

    @property
    def iterable(self) -> bool:
        """Returns `iterable` for the view and the parent datasource."""
        return self._datasource.iterable

    def yield_data(
        self, file_names: Optional[List[str]] = None, **kwargs: Any
    ) -> Iterator[pd.DataFrame]:
        """Returns `file_names` for the view and the parent datasource."""
        return self._datasource.yield_data(file_names=file_names, **kwargs)

    def _get_updated_query_with_metadata(self) -> str:
        """Get updated query with metadata columns included.

         For FileSystemIterableSource the `datapoint_hash`,
         `_original_filename` and `_last_modified`
        columns are added.
        """
        metadata_cols = ["datapoint_hash", "_original_filename", "_last_modified"]
        new_query = self.query
        for col in metadata_cols:
            if col not in self.query:
                new_query = new_query.replace("SELECT", f'SELECT "{col}",')
        return new_query


_DS = TypeVar("_DS", bound=BaseSource)


class ViewDatasourceConfig(ABC, Generic[_DS]):
    """A class dictating the configuration of a view.

    Args:
        source_dataset: The name of the underlying datasource.
    """

    def __init__(self, source_dataset: str, *args: Any, **kwargs: Any) -> None:
        self.source_dataset_name = source_dataset

    @abstractmethod
    def generate_schema(self, *args: Any, **kwargs: Any) -> BitfountSchema:
        """Schema generation for views."""

    @abstractmethod
    def build(
        self, underlying_datasource: _DS, connector: Optional[PodDbConnector] = None
    ) -> DataView:
        """Build a view instance corresponding to this config."""


@delegates()
class DropColViewConfig(ViewDatasourceConfig[BaseSource]):
    """Config class for DropColsDropColView.

    Args:
        drop_cols: The columns to drop.
    """

    def __init__(
        self, drop_cols: _SingleOrMulti[str], *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(**kwargs)
        self._drop_cols: List[str] = (
            [drop_cols] if isinstance(drop_cols, str) else list(drop_cols)
        )

    def generate_schema(
        self,
        underlying_datasource: BaseSource,
        name: str,
        force_stypes: Optional[
            MutableMapping[Union[_ForceStypeValue, _SemanticTypeValue], List[str]]
        ] = None,
        schema: Optional[BitfountSchema] = None,
    ) -> BitfountSchema:
        """Schema generation for DropColViewConfig.

        Args:
            underlying_datasource: The underlying datasource for the view.
            name: The name of the DropColViewConfig.
            force_stypes: A mapping of table names to a mapping of semantic types to
                a list of column names.
            schema: A BitfountSchema object. If provided, the schema will not be
                re-generated.

        Returns:
            A BitfountSchema object.
        """
        # Actually generate the schema
        if not schema:
            view = self.build(underlying_datasource)
            view_columns = view.get_dtypes().keys()
            if force_stypes:
                view_force_stypes = {}
                # adapt force stypes from underlying datasource to fit the drop view
                for k, v in force_stypes.items():
                    # We need special handling for `image_prefix`. This is because
                    # `image_prefix` is not part of the schema features, but just an
                    # easier way for a user to specify (especially in the YAML format).
                    # the image columns of a datasource.
                    if k not in ["image_prefix", "image"]:
                        # Extract only the columns present in the datasource.
                        view_force_stypes[k] = [col for col in v if col in view_columns]
                    elif k == "image_prefix":
                        # If `image_prefix` is in `force_stypes`, we need to add the
                        # columns that start with that prefix to the image features
                        # in the schema.
                        img_cols = [
                            col
                            for col in view_columns
                            if any(
                                col.startswith(stype)
                                for stype in force_stypes["image_prefix"]
                            )
                        ]
                        if len(img_cols) > 0:
                            # The image features might have processed so we don't
                            # want to overwrite them if that is the case
                            if "image" in view_force_stypes:
                                view_force_stypes["image"] = _add_this_to_list(
                                    img_cols, view_force_stypes["image"]
                                )
                            else:
                                view_force_stypes["image"] = img_cols
                    else:  # if k == "image"
                        # Similarly, image features might have been
                        # already added so we don't want to overwrite them
                        if "image" in view_force_stypes:
                            img_cols = [col for col in v if col in view_columns]
                            view_force_stypes["image"] = _add_this_to_list(
                                img_cols, view_force_stypes["image"]
                            )
                        else:
                            view_force_stypes["image"] = [
                                col for col in v if col in view_columns
                            ]
                view_force_stype = {name: view_force_stypes}
            else:
                view_force_stype = None
            logger.info(f"Generating schema for DropColView {name}")
            schema = BitfountSchema()
            schema.add_datasource_tables(
                datasource=view,
                table_name=name,
                force_stypes=cast(
                    Optional[
                        Mapping[
                            str,
                            MutableMapping[
                                Union[_SemanticTypeValue, _ForceStypeValue], List[str]
                            ],
                        ]
                    ],
                    view_force_stype,
                ),
            )
        return schema

    @overload
    def build(
        self,
        underlying_datasource: FileSystemIterableSource,
        connector: Optional[PodDbConnector] = None,
    ) -> DropColsFileSystemIterableDataview:
        ...

    @overload
    def build(
        self,
        underlying_datasource: BaseSource,
        connector: Optional[PodDbConnector] = None,
    ) -> DropColsDataview:
        ...

    def build(
        self,
        underlying_datasource: Union[BaseSource, FileSystemIterableSource],
        connector: Optional[PodDbConnector] = None,
    ) -> Union[DropColsDataview, DropColsFileSystemIterableDataview]:
        """Build a DropColsCSVDropColView from this configuration.

        Args:
            underlying_datasource: The underlying datasource for the view.
            connector: An optional PodDbConnector object.

        Returns:
            A DropColsDataview object.
        """
        klass = (
            DropColsFileSystemIterableDataview
            if isinstance(underlying_datasource, FileSystemIterableSource)
            else DropColsDataview
        )
        return klass(
            datasource=underlying_datasource,
            drop_cols=self._drop_cols,
            source_dataset_name=self.source_dataset_name,
        )


@delegates()
class SQLViewConfig(ViewDatasourceConfig[BaseSource]):
    """Config class for SQLDataViewConfig.

    Args:
        query: The SQL query for the view.

    Raises:
        ValueError: if the query does not start with SELECT.
    """

    def __init__(self, query: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        # Raise error at the beginning if query does not start with `SELECT`.
        # TODO: [NO_TICKET: Reason] Add better checking of the query after the query parser is built on the platform side. # noqa: B950
        if not query.lstrip().startswith("SELECT"):
            raise ValueError(
                "Unsupported query. We currently support only "
                "`SELECT ... FROM ...` queries for defining "
                "dataset views."
            )
        self.query = query

    def initialize(self, pod_name: str) -> None:
        """Initialize the view by providing the pod name for the database."""
        self.pod_name = pod_name

    def generate_schema(
        self,
        underlying_datasource: BaseSource,
        name: str,
        force_stypes: Optional[
            MutableMapping[Union[_ForceStypeValue, _SemanticTypeValue], List[str]]
        ] = None,
        schema: Optional[BitfountSchema] = None,
        connector: Optional[PodDbConnector] = None,
    ) -> BitfountSchema:
        """Schema generation for SQLDataViewConfig.

        Args:
            underlying_datasource: The underlying datasource for the view.
            name: The name of the SQLDataViewConfig.
            force_stypes: A mapping of table names to a mapping of semantic types to
                a list of column names.
            schema: A BitfountSchema object. If provided, the schema will not be
                re-generated.
            connector: An optional PodDbConnector object.

        Returns:
            A BitfountSchema object.
        """
        if not schema:
            view = self.build(underlying_datasource, connector)
            data = view.get_data()
            if data is not None:
                view_columns = data.columns.to_list()
            else:
                view_columns = []
            if force_stypes:
                view_force_stypes = {}
                # adapt force stypes from underlying datasource to fit the drop view
                for k, v in force_stypes.items():
                    # We need special handling for `image_prefix`. This is because
                    # `image_prefix` is not part of the schema features, but just an
                    # easier way for a user to specify (especially in the YAML format).
                    # the image columns of a datasource.
                    if k not in ["image_prefix", "image"]:
                        # Extract only the columns present in the datasource.
                        view_force_stypes[k] = [col for col in v if col in view_columns]
                    elif k == "image_prefix":
                        # If `image_prefix` is in `force_stypes`, we need to add the
                        # columns that start with that prefix to the image features
                        # in the schema.
                        img_cols = [
                            col
                            for col in view_columns
                            if any(
                                col.startswith(stype)
                                for stype in force_stypes["image_prefix"]
                            )
                        ]
                        if len(img_cols) > 0:
                            # The image features might have processed, so we don't
                            # want to overwrite them if that is the case
                            if "image" in view_force_stypes:
                                view_force_stypes["image"] = _add_this_to_list(
                                    img_cols, view_force_stypes["image"]
                                )
                            else:
                                view_force_stypes["image"] = img_cols
                    else:  # if k == "image"
                        # Similarly, image features might have been
                        # already added, so we don't want to overwrite them
                        if "image" in view_force_stypes:
                            img_cols = [col for col in v if col in view_columns]
                            view_force_stypes["image"] = _add_this_to_list(
                                img_cols, view_force_stypes["image"]
                            )
                        else:
                            view_force_stypes["image"] = [
                                col for col in v if col in view_columns
                            ]
                view_force_stype = {name: view_force_stypes}
            else:
                view_force_stype = None
            # Actually generate schema
            logger.info(f"Generating schema for SQLDataView {name}")
            schema = BitfountSchema()
            schema.add_datasource_tables(
                datasource=view,
                table_name=name,
                force_stypes=cast(
                    Optional[
                        Mapping[
                            str,
                            MutableMapping[
                                Union[_SemanticTypeValue, _ForceStypeValue], List[str]
                            ],
                        ]
                    ],
                    view_force_stype,
                ),
            )
        return schema

    @overload
    def build(
        self,
        underlying_datasource: FileSystemIterableSource,
        connector: Optional[PodDbConnector] = None,
    ) -> Union[SQLFileSystemIterableDataView, DataView]:
        ...

    @overload
    def build(
        self,
        underlying_datasource: BaseSource,
        connector: Optional[PodDbConnector] = None,
    ) -> Union[SQLDataView, DataView]:
        ...

    def build(
        self,
        underlying_datasource: Union[BaseSource, FileSystemIterableSource],
        connector: Optional[PodDbConnector] = None,
    ) -> Union[SQLDataView, SQLFileSystemIterableDataView, DataView]:
        """Build a SQLDataViewConfig from this configuration.

        Args:
            underlying_datasource: The underlying datasource for the view.
            connector: An optional PodDbConnector object.

        Returns:
            A SQLDataView when connector is provided or
            An empty DataView when connector is not provided.
        """
        # TODO: [BIT-3402]: Replace tmp return of EmptyDataview with exception
        # This currently causes the schema for the view to completely change
        # and match the parent datasource's schema instead when the schema is
        # updated after a task.
        if connector is None:
            logger.warning(
                "SQLViews are only supported with pods that "
                + "have the pod database enabled."
            )
            return _EmptyDataview(underlying_datasource, self.source_dataset_name)

        klass = (
            SQLFileSystemIterableDataView
            if isinstance(underlying_datasource, FileSystemIterableSource)
            else SQLDataView
        )

        return klass(
            datasource=underlying_datasource,
            source_dataset_name=self.source_dataset_name,
            query=self.query,
            pod_name=self.pod_name,
            connector=connector,
        )
