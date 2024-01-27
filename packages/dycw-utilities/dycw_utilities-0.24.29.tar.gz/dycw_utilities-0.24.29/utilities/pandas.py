from __future__ import annotations

import datetime as dt
from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from dataclasses import dataclass
from functools import partial, reduce
from itertools import chain, permutations
from typing import TYPE_CHECKING, Any, Literal, TypeAlias, TypeVar, cast

from numpy import where
from pandas import (
    NA,
    BooleanDtype,
    CategoricalDtype,
    DataFrame,
    DatetimeTZDtype,
    Index,
    Int64Dtype,
    NaT,
    RangeIndex,
    Series,
    StringDtype,
    Timestamp,
)
from pandas.testing import assert_frame_equal, assert_index_equal
from typing_extensions import assert_never, override

from utilities.datetime import UTC
from utilities.errors import redirect_error
from utilities.functions import CheckNameError, check_name
from utilities.iterables import (
    CheckLengthError,
    CheckSetsEqualError,
    CheckSubSetError,
    CheckSuperSetError,
    check_length,
    check_sets_equal,
    check_subset,
    check_superset,
)
from utilities.numpy import NDArray1, dt64ns, has_dtype
from utilities.sentinel import Sentinel, sentinel
from utilities.zoneinfo import HONG_KONG

if TYPE_CHECKING:  # pragma: no cover
    IndexA: TypeAlias = Index[Any]
    IndexB: TypeAlias = Index[bool]
    IndexBn: TypeAlias = Index[BooleanDtype]
    IndexC: TypeAlias = Index[CategoricalDtype]
    IndexD: TypeAlias = Index[dt.datetime]
    IndexDhk: TypeAlias = Index[DatetimeTZDtype]
    IndexDutc: TypeAlias = Index[DatetimeTZDtype]
    IndexF: TypeAlias = Index[float]
    IndexI: TypeAlias = Index[int]
    IndexI64: TypeAlias = Index[Int64Dtype]
    IndexS: TypeAlias = Index[str]
    IndexSt: TypeAlias = Index[StringDtype]

    SeriesA: TypeAlias = Series[Any]
    SeriesB: TypeAlias = Series[bool]
    SeriesBn: TypeAlias = Series[BooleanDtype]
    SeriesC: TypeAlias = Series[CategoricalDtype]
    SeriesD: TypeAlias = Series[dt.datetime]
    SeriesDhk: TypeAlias = Series[DatetimeTZDtype]
    SeriesDutc: TypeAlias = Series[DatetimeTZDtype]
    SeriesF: TypeAlias = Series[float]
    SeriesI: TypeAlias = Series[int]
    SeriesI64: TypeAlias = Series[Int64Dtype]
    SeriesS: TypeAlias = Series[str]
    SeriesSt: TypeAlias = Series[StringDtype]
else:
    IndexA = (
        IndexB
    ) = (
        IndexBn
    ) = (
        IndexC
    ) = (
        IndexD
    ) = IndexDhk = IndexDutc = IndexF = IndexI = IndexI64 = IndexS = IndexSt = Index
    SeriesA = (
        SeriesB
    ) = (
        SeriesBn
    ) = (
        SeriesC
    ) = (
        SeriesD
    ) = (
        SeriesDhk
    ) = SeriesDutc = SeriesF = SeriesI = SeriesI64 = SeriesS = SeriesSt = Series


Int64 = "Int64"
boolean = "boolean"
category = "category"
string = "string"
datetime64nsutc = DatetimeTZDtype(tz=UTC)
datetime64nshk = DatetimeTZDtype(tz=HONG_KONG)


_Index = TypeVar("_Index", bound=Index)


def astype(df: DataFrame, dtype: Any, /) -> DataFrame:
    """Wrapper around `.astype`."""
    return cast(Any, df).astype(dtype)


def check_index(
    index: IndexA,
    /,
    *,
    length: int | tuple[int, float] | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    name: Hashable | Sentinel = sentinel,
    sorted: bool = False,  # noqa: A002
    unique: bool = False,
) -> None:
    """Check the properties of an Index."""
    _check_index_length(index, equal_or_approx=length, min=min_length, max=max_length)
    _check_index_name(index, name)
    if sorted:
        _check_index_sorted(index)
    if unique:
        _check_index_unique(index)


@dataclass(frozen=True, kw_only=True, slots=True)
class CheckIndexError(Exception):
    index: IndexA


def _check_index_length(
    index: IndexA,
    /,
    *,
    equal_or_approx: int | tuple[int, float] | None = None,
    min: int | None = None,  # noqa: A002
    max: int | None = None,  # noqa: A002
) -> None:
    try:
        check_length(index, equal_or_approx=equal_or_approx, min=min, max=max)
    except CheckLengthError as error:
        raise _CheckIndexLengthError(index=index) from error


@dataclass(frozen=True, kw_only=True, slots=True)
class _CheckIndexLengthError(CheckIndexError):
    @override
    def __str__(self) -> str:
        return "Index {} must satisfy the length requirements.".format(self.index)


def _check_index_name(index: IndexA, name: Any, /) -> None:
    if not isinstance(name, Sentinel):
        try:
            check_name(index, name)
        except CheckNameError as error:
            raise _CheckIndexNameError(index=index) from error


@dataclass(frozen=True, kw_only=True, slots=True)
class _CheckIndexNameError(CheckIndexError):
    @override
    def __str__(self) -> str:
        return "Index {} must satisfy the name requirement.".format(self.index)


def _check_index_sorted(index: IndexA, /) -> None:
    try:
        assert_index_equal(index, sort_index(index))
    except AssertionError as error:
        raise _CheckIndexSortedError(index=index) from error


@dataclass(frozen=True, kw_only=True, slots=True)
class _CheckIndexSortedError(CheckIndexError):
    @override
    def __str__(self) -> str:
        return "Index {} must be sorted.".format(self.index)


def _check_index_unique(index: IndexA, /) -> None:
    if index.has_duplicates:
        raise _CheckIndexUniqueError(index=index)


@dataclass(frozen=True, kw_only=True, slots=True)
class _CheckIndexUniqueError(CheckIndexError):
    @override
    def __str__(self) -> str:
        return "Index {} must be unique.".format(self.index)


def check_pandas_dataframe(
    df: DataFrame,
    /,
    *,
    standard: bool = False,
    columns: Sequence[Hashable] | None = None,
    dtypes: Mapping[Hashable, Any] | None = None,
    length: int | tuple[int, float] | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    sorted: Hashable | Sequence[Hashable] | None = None,  # noqa: A002
    unique: Hashable | Sequence[Hashable] | None = None,
) -> None:
    """Check the properties of a DataFrame."""
    if standard:
        if not isinstance(df.index, RangeIndex):
            msg = f"{df.index=}"
            raise CheckPandasDataFrameError(msg)
        with redirect_error(
            CheckRangeIndexError, CheckPandasDataFrameError(f"{df.index=}, {length=}")
        ):
            check_range_index(df.index, start=0, step=1, name=None)
        with redirect_error(
            CheckIndexError, CheckPandasDataFrameError(f"{df.index=}, {length=}")
        ):
            check_index(df.columns, name=None, unique=True)
    if (columns is not None) and (list(df.columns) != columns):
        msg = f"{df=}, {columns=}"
        raise CheckPandasDataFrameError(msg)
    if (dtypes is not None) and (dict(df.dtypes) != dict(dtypes)):
        msg = f"{df=}, {dtypes=}"
        raise CheckPandasDataFrameError(msg)
    if length is not None:
        with redirect_error(
            CheckLengthError, CheckPandasDataFrameError(f"{df=}, {length=}")
        ):
            check_length(df, equal_or_approx=length)
    if min_length is not None:
        with redirect_error(
            CheckLengthError, CheckPandasDataFrameError(f"{df=}, {min_length=}")
        ):
            check_length(df, min=min_length)
    if max_length is not None:
        with redirect_error(
            CheckLengthError, CheckPandasDataFrameError(f"{df=}, {max_length=}")
        ):
            check_length(df, max=max_length)
    if sorted is not None:
        df_sorted: DataFrame = df.sort_values(by=sorted).reset_index(drop=True)  # type: ignore
        with redirect_error(AssertionError, CheckPandasDataFrameError(f"{df=}")):
            assert_frame_equal(df, df_sorted)
    if (unique is not None) and df.duplicated(subset=unique).any():
        msg = f"{df=}, {unique=}"
        raise CheckPandasDataFrameError(msg)


class CheckPandasDataFrameError(Exception):
    ...


def check_range_index(
    index: RangeIndex,
    /,
    *,
    start: int | None = None,
    stop: int | None = None,
    step: int | None = None,
    length: int | tuple[int, float] | None = None,
    min_length: int | None = None,
    max_length: int | None = None,
    name: Hashable | Sentinel = sentinel,
) -> None:
    """Check the properties of a RangeIndex."""
    if (start is not None) and (cast(int, index.start) != start):
        msg = f"{index=}, {start=}"
        raise CheckRangeIndexError(msg)
    if (stop is not None) and (cast(int, index.stop) != stop):
        msg = f"{index=}, {stop=}"
        raise CheckRangeIndexError(msg)
    if (step is not None) and (cast(int, index.step) != step):
        msg = f"{index=}, {step=}"
        raise CheckRangeIndexError(msg)
    if length is not None:
        with redirect_error(
            CheckIndexError, CheckRangeIndexError(f"{index=}, {length=}")
        ):
            check_index(index, length=length)
    if min_length is not None:
        with redirect_error(
            CheckIndexError, CheckRangeIndexError(f"{index=}, {min_length=}")
        ):
            check_index(index, min_length=min_length)
    if max_length is not None:
        with redirect_error(
            CheckIndexError, CheckRangeIndexError(f"{index=}, {max_length=}")
        ):
            check_index(index, max_length=max_length, name=name)
    if not isinstance(name, Sentinel):
        with redirect_error(
            CheckIndexError, CheckRangeIndexError(f"{index=}, {name=}")
        ):
            check_index(index, name=name)


class CheckRangeIndexError(Exception):
    ...


@contextmanager
def redirect_empty_pandas_concat() -> Iterator[None]:
    """Redirect to the `EmptyPandasConcatError`."""
    with redirect_error(
        ValueError, EmptyPandasConcatError, match="No objects to concatenate"
    ):
        yield


class EmptyPandasConcatError(Exception):
    ...


def rename_index(index: _Index, name: Hashable, /) -> _Index:
    """Wrapper around `.rename`."""
    return cast(_Index, index.rename(name))


def reindex_to_set(index: _Index, target: Iterable[Any], /) -> _Index:
    """Re-index an Index to a strict permutation of its elements."""
    target_as_list = list(target)
    try:
        check_sets_equal(index, target_as_list)
    except CheckSetsEqualError as error:
        raise ReindexToSetError(index=index, target=target_as_list) from error
    new_index, _ = index.reindex(target_as_list)
    return new_index


@dataclass(frozen=True, kw_only=True, slots=True)
class ReindexToSetError(Exception):
    index: IndexA
    target: list[Any]

    @override
    def __str__(self) -> str:
        return "Index {} and {} must be equal as sets.".format(self.index, self.target)


def reindex_to_subset(index: _Index, target: Iterable[Any], /) -> _Index:
    """Re-index an Index to a strict subset of its elements."""
    target_as_list = list(target)
    try:
        check_superset(index, target_as_list)
    except CheckSuperSetError as error:
        raise ReindexToSubSetError(index=index, target=target_as_list) from error
    new_index, _ = index.reindex(target_as_list)
    return new_index


@dataclass(frozen=True, kw_only=True, slots=True)
class ReindexToSubSetError(Exception):
    index: IndexA
    target: list[Any]

    @override
    def __str__(self) -> str:
        return "Index {} must be a superset of {}.".format(self.index, self.target)


def reindex_to_superset(index: _Index, target: Iterable[Any], /) -> _Index:
    """Re-index an Index to a strict superset of its elements."""
    target_as_list = list(target)
    try:
        check_subset(index, target_as_list)
    except CheckSubSetError as error:
        raise ReindexToSuperSetError(index=index, target=target_as_list) from error
    new_index, _ = index.reindex(target_as_list)
    return new_index


@dataclass(frozen=True, kw_only=True, slots=True)
class ReindexToSuperSetError(Exception):
    index: IndexA
    target: list[Any]

    @override
    def __str__(self) -> str:
        return "Index {} must be a subset of {}.".format(self.index, self.target)


def series_max(*series: SeriesA) -> SeriesA:
    """Compute the maximum of a set of Series."""
    return reduce(partial(_series_minmax, kind="lower"), series)


def series_min(*series: SeriesA) -> SeriesA:
    """Compute the minimum of a set of Series."""
    return reduce(partial(_series_minmax, kind="upper"), series)


def _series_minmax(
    x: SeriesA, y: SeriesA, /, *, kind: Literal["lower", "upper"]
) -> SeriesA:
    """Compute the minimum/maximum of a pair of Series."""
    assert_index_equal(x.index, y.index)
    if not (has_dtype(x, y.dtype) and has_dtype(y, x.dtype)):
        raise SeriesMinMaxError(x=x, y=y)
    out = x.copy()
    for first, second in permutations([x, y]):
        i = first.notna() & second.isna()
        out.loc[i] = first.loc[i]
    i = x.notna() & y.notna()
    out.loc[i] = x.loc[i].clip(**{kind: cast(Any, y.loc[i])})
    out.loc[x.isna() & y.isna()] = NA
    return out


@dataclass(frozen=True, kw_only=True, slots=True)
class SeriesMinMaxError(Exception):
    x: SeriesA
    y: SeriesA

    @override
    def __str__(self) -> str:
        return "Series {} and {} must have the same dtype; got {} and {}.".format(
            self.x, self.y, self.x.dtype, self.y.dtype
        )


def sort_index(index: _Index, /) -> _Index:
    return cast(_Index, index.sort_values())


def timestamp_to_date(timestamp: Any, /, *, warn: bool = True) -> dt.date:
    """Convert a timestamp to a date."""
    return timestamp_to_datetime(timestamp, warn=warn).date()


def timestamp_to_datetime(timestamp: Any, /, *, warn: bool = True) -> dt.datetime:
    """Convert a timestamp to a datetime."""
    if timestamp is NaT:
        msg = f"{timestamp=}"
        raise TimestampToDateTimeError(msg)
    datetime = cast(dt.datetime, timestamp.to_pydatetime(warn=warn))
    if datetime.tzinfo is None:
        return datetime.replace(tzinfo=UTC)
    return datetime


class TimestampToDateTimeError(Exception):
    ...


def _timestamp_minmax_to_date(timestamp: Timestamp, method_name: str, /) -> dt.date:
    """Get the maximum Timestamp as a date."""
    method = getattr(timestamp, method_name)
    rounded = cast(Timestamp, method("D"))
    return timestamp_to_date(rounded)


TIMESTAMP_MIN_AS_DATE = _timestamp_minmax_to_date(Timestamp.min, "ceil")
TIMESTAMP_MAX_AS_DATE = _timestamp_minmax_to_date(Timestamp.max, "floor")


def _timestamp_minmax_to_datetime(
    timestamp: Timestamp, method_name: str, /
) -> dt.datetime:
    """Get the maximum Timestamp as a datetime."""
    method = getattr(timestamp, method_name)
    rounded = cast(Timestamp, method("us"))
    return timestamp_to_datetime(rounded)


TIMESTAMP_MIN_AS_DATETIME = _timestamp_minmax_to_datetime(Timestamp.min, "ceil")
TIMESTAMP_MAX_AS_DATETIME = _timestamp_minmax_to_datetime(Timestamp.max, "floor")


def to_numpy(series: SeriesA, /) -> NDArray1:
    """Convert a series into a 1-dimensional `ndarray`."""
    if has_dtype(series, (bool, dt64ns, int, float)):
        return series.to_numpy()
    if has_dtype(series, (boolean, Int64, string)):
        return where(
            series.notna(), series.to_numpy(dtype=object), cast(Any, None)
        ).astype(object)
    msg = f"{series=}"  # pragma: no cover
    raise ToNumpyError(msg)  # pragma: no cover


class ToNumpyError(Exception):
    ...


def union_indexes(
    index: IndexA,
    *more_indexes: IndexA,
    names: Literal["first", "last", "raise"] = "raise",
) -> IndexA:
    """Take the union of an arbitrary number of indexes."""
    indexes = chain([index], more_indexes)

    def func(left: IndexA, right: IndexA, /) -> IndexA:
        lname, rname = left.name, right.name
        if (lname == rname) or ((lname is not None) and (rname is None)):
            name = lname
        elif (lname is None) and (rname is not None):
            name = rname
        else:
            match names:
                case "first":
                    name = lname
                case "last":
                    name = rname
                case "raise":
                    raise UnionIndexesError(left=left, right=right)
                case _ as never:  # type: ignore
                    assert_never(never)
        return left.union(right).rename(name)

    return reduce(func, indexes)


@dataclass(frozen=True, kw_only=True, slots=True)
class UnionIndexesError(Exception):
    left: IndexA
    right: IndexA

    @override
    def __str__(self) -> str:
        return "Indexes {} and {} must have the same name; got {} and {}.".format(
            self.left, self.right, self.left.name, self.right.name
        )


__all__ = [
    "CheckIndexError",
    "CheckPandasDataFrameError",
    "CheckRangeIndexError",
    "EmptyPandasConcatError",
    "Int64",
    "ReindexToSetError",
    "ReindexToSubSetError",
    "ReindexToSuperSetError",
    "SeriesMinMaxError",
    "TIMESTAMP_MAX_AS_DATE",
    "TIMESTAMP_MAX_AS_DATETIME",
    "TIMESTAMP_MIN_AS_DATE",
    "TIMESTAMP_MIN_AS_DATETIME",
    "TimestampToDateTimeError",
    "UnionIndexesError",
    "astype",
    "boolean",
    "category",
    "check_index",
    "check_pandas_dataframe",
    "check_range_index",
    "datetime64nshk",
    "datetime64nsutc",
    "redirect_empty_pandas_concat",
    "reindex_to_set",
    "reindex_to_subset",
    "reindex_to_superset",
    "rename_index",
    "series_max",
    "series_min",
    "sort_index",
    "string",
    "timestamp_to_date",
    "timestamp_to_datetime",
    "to_numpy",
    "union_indexes",
]
