"""This file consists unit test cases of the development code"""
from main import WeatherReport
from .test_data import CITY, OK_STATUS_CODE, FAILURE_STATUS_CODE, WEATHER_REPORT_DATA


def test_location_details_1(mocker) -> None:
    """
    Test case to test the get_location_details function when
    fetching the location details successful
    """

    json_mock = mocker.MagicMock(return_value=CITY)
    status_code_mock = mocker.MagicMock(status_code=OK_STATUS_CODE, json=json_mock)
    request_mock = mocker.patch("main.requests.request", return_value=status_code_mock)
    response = WeatherReport().get_location_details()
    assert response == CITY["city"]
    request_mock.assert_called_once()
    json_mock.assert_called_once()


def test_location_details_2(mocker) -> None:
    """
    Test case to test the get_location_details function when
    status code is not 200
    """

    raise_for_status_mock = mocker.MagicMock(
        side_effect=[ValueError("Failed to fetch the data")]
    )
    status_code_mock = mocker.MagicMock(
        status_code=FAILURE_STATUS_CODE, raise_for_status=raise_for_status_mock
    )
    request_mock = mocker.patch("main.requests.request", return_value=status_code_mock)
    response = WeatherReport().get_location_details()
    assert response is None
    request_mock.assert_called_once()
    raise_for_status_mock.assert_called_once()


def test_location_details_3(mocker) -> None:
    """
    Test case to test the get_location_details function when
    Exception occurs
    """

    request_mock = mocker.patch(
        "main.requests.request", side_effect=[Exception("Invalid request")]
    )
    response = WeatherReport().get_location_details()
    assert response is None
    request_mock.assert_called_once()


def test_get_weather_report_1(mocker) -> None:
    """
    Test case to test the get_weather_report function when
    fetching the weather report successful
    """

    furl_mock = mocker.patch("main.furl")
    json_mock = mocker.MagicMock(return_value=WEATHER_REPORT_DATA)
    status_code_mock = mocker.MagicMock(status_code=OK_STATUS_CODE, json=json_mock)
    request_mock = mocker.patch("main.requests.request", return_value=status_code_mock)
    writing_to_json_file_mock = mocker.patch("main.WeatherReport.writing_to_json_file")
    response = WeatherReport().get_weather_report(city_name=CITY["city"])
    assert response is None
    request_mock.assert_called_once()
    json_mock.assert_called_once()
    furl_mock.assert_called_once()
    writing_to_json_file_mock.assert_called_once()


def test_get_weather_report_2(mocker) -> None:
    """
    Test case to test the get_weather_report function when
    Exception occurs
    """

    furl_mock = mocker.patch("main.furl")
    raise_for_status_mock = mocker.MagicMock(
        side_effect=[Exception("Failed to fetch the weather data")]
    )
    status_code_mock = mocker.MagicMock(
        status_code=FAILURE_STATUS_CODE, raise_for_status=raise_for_status_mock
    )
    request_mock = mocker.patch("main.requests.request", return_value=status_code_mock)
    response = WeatherReport().get_weather_report(city_name=CITY["city"])
    assert response is None
    request_mock.assert_called_once()
    raise_for_status_mock.assert_called_once()
    furl_mock.assert_called_once()
