# -*- coding: utf-8 -*-

"""Tests for the rws-knmi-lib module."""
import pandas as pd
import pytest

from rws_knmi_lib.knmi_downloader import (
    _format_dataframe,
    import_daily_data,
    import_hourly_data,
)


def test_correct_usage_all_stations():
    df = import_daily_data(start="20220531", end="20220602")
    assert isinstance(df, pd.DataFrame)
    assert len(df["STN"].value_counts()) > 1

    df_hour = import_hourly_data(start="20220531", end="20220602")
    assert isinstance(df_hour, pd.DataFrame)
    assert len(df_hour["STN"].value_counts()) > 1

    df_hour = import_hourly_data(start="20200131", end="20200331")
    assert isinstance(df_hour, pd.DataFrame)
    assert len(df_hour["STN"].value_counts()) > 1


def test_correct_usage_single_station():
    df = import_daily_data(
        start="20220531", end="20220602", coord=(51.820486, 4.706331)
    )
    assert isinstance(df, pd.DataFrame)
    assert len(df["STN"].value_counts()) == 1

    df_hour = import_hourly_data(
        start="20220531", end="20220602", coord=(51.820486, 4.706331)
    )
    assert isinstance(df_hour, pd.DataFrame)
    assert len(df_hour["STN"].value_counts()) == 1


def test_wrong_string_format_error():
    with pytest.raises(Exception):
        import_daily_data(start="05312022", end="06022022")


def test_wrong_string_format_error_hourly():
    with pytest.raises(Exception):
        import_hourly_data(start="05312022", end="06022022")


def test_negative_coord_error():
    with pytest.raises(Exception):
        import_daily_data(start="20220531", end="20220602", coord=(-1, -1))


def test_negative_coord_error_hourly():
    with pytest.raises(Exception):
        import_hourly_data(start="20220531", end="20220602", coord=(-1, -1))


def test_query_error_hourly():
    with pytest.raises(Exception):
        import_daily_data(start="20120101", end="20220101")


def test_empty_response_dataframe():
    with pytest.raises(Exception):
        empty_df = pd.DataFrame()
        _format_dataframe(empty_df)


# Fixture example
# @pytest.fixture
# def an_object():
#     return {}
#
#
# def test_example(an_object):
#     assert an_object == {}
