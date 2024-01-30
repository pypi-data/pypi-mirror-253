# -*- coding: utf-8 -*-
"""Library to download KNMI weather data aggregated on a daily or hourly level.

https://www.daggegevens.knmi.nl/

"""

import io
import logging
from datetime import datetime, timedelta
from typing import Optional, Tuple

import mpu
import pandas as pd
import requests

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def import_daily_data(
    start: str, end: str, coord: Optional[Tuple[float, float]] = None
) -> pd.DataFrame:
    """Import daily aggregated KNMI data.

    Post a request to the KNMI url and parse the response content to a pandas dataframe.

    Parameters
    ----------
    start : str
        String containing starting date from which to get data in format YYYYMMDD.
    end : str
        String containing final date from which to get data in format YYYYMMDD.
    coord : Optional[Tuple[float, float]]
        Coordinate to search for nearest station in format (latitude, longitude). If
        left as None, all stations are returned.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing the parsed content of the post response.

    Examples
    --------
    .. code:: python

        from rws_knmi_lib.knmi_downloader import import_daily_data

        # Returns dataframe containing information on all KNMI stations.
        df_daily = import_daily_data(start="20220501", end="20220505")

        # Returns dataframe containing only information from the nearest KNMI station.
        df_daily_nearest = import_daily_data(start="20220501", end="20220505",
                                             coord=(52.460770, 4.625110))

    """
    return _import_data(
        start, end, "https://www.daggegevens.knmi.nl/klimatologie/daggegevens", coord
    )


def import_hourly_data(
    start: str, end: str, coord: Optional[Tuple[float, float]] = None
) -> pd.DataFrame:
    """Import hourly aggregated KNMI data.

    Post a request to the KNMI url and parse the response content to a pandas
    dataframe. If the timedelta between start and end is bigger than 30 days,
    the request is posted in batches to avoid a Query Error from the server for
    requesting too many values.

    Parameters
    ----------
    start : str
        String containing starting date from which to get data in format YYYYMMDD.
    end : str
        String containing final date from which to get data in format YYYYMMDD.
    coord : Optional[Tuple[float, float]]
        Coordinate to search for nearest station in format (latitude, longitude). If
        left as None, all stations are returned.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing the parsed content of the post response.

    Examples
    --------
    .. code:: python

        from rws_knmi_lib.knmi_downloader import import_hourly_data

        # Returns dataframe containing information on all KNMI stations.
        df_hourly = import_hourly_data(start="20220501", end="20220505")

        # Returns dataframe containing only information from the nearest KNMI station.
        df_hourly_nearest = import_hourly_data(start="20220501", end="20220505",
                                               coord=(52.460770, 4.625110))
    """
    start_time = datetime.strptime(start, "%Y%m%d")
    end_time = datetime.strptime(end, "%Y%m%d")
    if end_time - start_time > timedelta(days=30):

        start_dates = pd.date_range(start=start_time, end=end_time, freq="MS")
        end_dates = [sd + timedelta(days=30) for sd in start_dates]

        knmi_data = []

        for start_date, end_date in zip(start_dates, end_dates):
            logger.debug("Downloading weather data for %s - %s...", start, end)
            knmi_data += [
                _import_data(
                    start=start_date.strftime("%Y%m%d"),
                    end=end_date.strftime("%Y%m%d"),
                    url="https://www.daggegevens.knmi.nl/klimatologie/uurgegevens",
                    coord=coord,
                )
            ]
        df_hourly = pd.concat(knmi_data).reset_index(drop=True)
    else:
        df_hourly = _import_data(
            start,
            end,
            "https://www.daggegevens.knmi.nl/klimatologie/uurgegevens",
            coord,
        )

    df_hourly["HH"] = pd.to_timedelta(df_hourly["HH"], unit="hours")
    df_hourly["Datetime"] = df_hourly["YYYYMMDD"] + df_hourly["HH"]

    return df_hourly


def _import_data(
    start: str,
    end: str,
    url: str,
    coord: Optional[Tuple[float, float]] = None,
) -> pd.DataFrame:
    """Import KNMI data from the given URL which can be hourly or daily aggregated.

    Parameters
    ----------
    start : str
        String containing starting date from which to get data in format YYYYMMDD.
    end : str
        String containing final date from which to get data in format YYYYMMDD.
    coord : Optional[Tuple[float, float]]
        Coordinate to search for nearest station in format (latitude, longitude). If
        left as None, all stations are returned.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing the parsed content of the post response.
    """
    logger.debug("Posting request.")
    response = requests.post(url=url, data={"start": start, "end": end}, timeout=60)

    if response.status_code != 200:
        logger.error("Unable to retrieve download url for file.")
        logger.error(response.text)
        raise Exception("Unable to retrieve download url for file.")
    logger.debug("Response received.")

    decoded_response = response.content.decode("utf-8")

    if "Query Error" in decoded_response:
        logger.error(
            "Probably a Query Error. Too many values returned. Adjust "
            "time range in order to request less values."
        )
        raise Exception(
            "Probably a Query Error. Too many values returned. Adjust "
            "time range in order to request less values."
        )
    dataframe = _parse_knmi_response(decoded_response, coord)
    return dataframe


def _parse_knmi_response(
    dec_response: str, coord: Optional[Tuple[float, float]]
) -> pd.DataFrame:
    """Parse the decoded KNMI response object.

    Parameters
    ----------
    dec_response : str
        UTF-8 decoded response in raw text format.
    coord : Optional[Tuple[float, float]]
        Coordinate to search for nearest station in format (latitude, longitude). If
        left as None, all stations are returned.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing the parsed content of the post response.
    """
    try:
        # Find starting point of values for in the dataframe
        pos_df = dec_response.find("STN,YYYYMMDD")
        dataframe_response = dec_response[pos_df:]
        dataframe = pd.read_csv(io.StringIO(dataframe_response), skipinitialspace=True)
        dataframe = _format_dataframe(dataframe)

        if coord is not None:
            logger.debug("Finding nearest station.")
            df_stations = _parse_station_locations(dec_response)
            nearest_station = _find_nearest_station(df_stations, coord)
            logger.debug("Nearest station is station %d", nearest_station)
            dataframe = dataframe[dataframe["STN"].astype(int) == nearest_station]
        dataframe["YYYYMMDD"] = pd.to_datetime(dataframe["YYYYMMDD"], format="%Y%m%d")
        return dataframe
    except Exception as exc:
        logger.exception(exc)
        raise


def _find_nearest_station(dataframe: pd.DataFrame, coord: Tuple[float, float]) -> int:
    """Calculate nearest KNMI station to given coordinate.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Formatted dataframe which can be used for further calculations.
    coord : Tuple[float, float]
        Coordinate to search for nearest station in format (latitude, longitude).
        Can't be None, as this method would not be called otherwise.

    Returns
    -------
    int
        Integer value corresponding to the nearest station in the STN column.
    """
    if coord[0] < 0 or coord[1] < 0:
        raise ValueError("Negative longitude or latitude not allowed.")

    dataframe["haversine_distance"] = dataframe.apply(
        lambda x: mpu.haversine_distance(coord, (x["LAT(north)"], x["LON(east)"])),
        axis=1,
    )
    nearest = dataframe[
        dataframe["haversine_distance"] == dataframe["haversine_distance"].min()
    ]["STN"]
    return int(nearest.item())


def _parse_station_locations(dec_response: str) -> pd.DataFrame:
    """Parse station location part of the KNMI response.

    Parameters
    ----------
    dec_response : str
        UTF-8 decoded response in raw text format.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame containing the parsed content of the response.
    """
    pos_station = min(
        position
        for position in [dec_response.find("# DD"), dec_response.find("# YYYYMMDD")]
        if position > 0
    )
    station_response = dec_response[:pos_station]
    stations_df = pd.read_csv(
        io.StringIO(station_response),
        header=5,
        sep=r"\s{2,}",
        skipinitialspace=True,
        engine="python",
    )
    stations_df = _format_dataframe(stations_df)
    stations_df["STN"] = stations_df["STN"].str.replace("# ", "")
    return stations_df


def _format_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Format dataframe by changing names and selecting columns.

    Parameters
    ----------
    dataframe : pd.DataFrame
        Dataframe coming from the read_csv method on the raw response.

    Returns
    -------
    pd.DataFrame
        Formatted dataframe which is easier to work with and has unused columns removed.
    """
    alter_headers = {"# STN": "STN"}
    dataframe = dataframe.rename(columns=alter_headers)
    dataframe = dataframe.replace("# ", "")
    dataframe = dataframe.dropna(how="all", axis=1)
    if dataframe.empty:
        raise Exception("No data found in the constructed dataframe.")
    return dataframe
