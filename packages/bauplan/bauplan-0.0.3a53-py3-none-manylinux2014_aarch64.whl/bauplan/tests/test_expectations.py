import pyarrow as pa
import pytest

from bauplan.standard_expectations import (
    expect_column_all_null,
    expect_column_all_unique,
    expect_column_no_nulls,
    expect_column_not_unique,
    expect_column_some_null,
)


@pytest.fixture
def table_int():
    c0 = pa.array([2, 4, 5, 100])
    c1 = pa.array([2, 4, None, 100])
    c2 = pa.array([None, None, None, None])
    c3 = pa.array([1, 2, 3, 4])
    c4 = pa.array([1, 2, 3, 3])
    return pa.Table.from_arrays(
        [ c0, c1, c2, c3, c4 ],
        names=['no_null', 'some_null', 'all_null', 'all_unique', 'not_unique']
    )


def test_not_null(table_int):
    assert expect_column_no_nulls(table_int, 'no_null')

def test_null(table_int):
    assert expect_column_some_null(table_int, 'some_null')

def test_all_null(table_int):
    assert expect_column_all_null(table_int, 'all_null')

def test_unique(table_int):
    assert expect_column_all_unique(table_int, 'all_unique')

def test_not_unique(table_int):
    assert expect_column_not_unique(table_int, 'not_unique')
