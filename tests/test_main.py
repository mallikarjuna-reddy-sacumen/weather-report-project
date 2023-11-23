"""This file consists unit test cases of the development code"""
from unittest.mock import Mock, patch
from main import WeatherReport


weather_report_data = {
    "coord": {"lon": -71.1828, "lat": 42.3709},
    "weather": [
        {"id": 8000, "main": "Clear", "description": "clear sky", "icon": "01n"}
    ],
    "base": "stations",
    "main": {
        "temp": 269.79,
        "feels_like": 265.06,
        "temp_min": 267.31,
        "temp_max": 271.96,
        "pressure": 1034,
        "humidity": 66,
    },
    "visibility": 10000,
    "wind": {"speed": 3.6, "deg": 330},
    "clouds": {"all": 0},
    "dt": 1700549404,
    "sys": {
        "type": 2,
        "id": 2013673,
        "country": "US",
        "sunrise": 1700566964,
        "sunset": 1700601522,
    },
    "timezone": -18000,
    "id": 4954611,
    "name": "Watertown",
    "cod": 200,
}


@patch("main.ipaddress")
@patch("main.requests")
def test_location_details_1(request_mock, ipaddress_mock):
    """
    Test case to test the get_location_details function when
    fetching the location details successful
    """
    ipaddress_mock.ip_address.return_value = Mock()
    location = {"city": "Delhi"}
    json_mock = Mock(status_code=200)
    json_mock.json.return_value = location
    request_mock.request.return_value = json_mock
    weather_report = WeatherReport()
    response = weather_report.get_location_details()
    assert response == location["city"]
    ipaddress_mock.ip_address.assert_called_once()
    request_mock.request.assert_called_once()
    json_mock.json.assert_called_once()


@patch("main.ipaddress")
def test_location_details_2(ipaddress_mock):
    """
    Test case to test the get_location_details function when
    ip_address method returning ValueError
    """
    ipaddress_mock.ip_address.side_effect = [ValueError("pass valid ipaddress")]
    weather_report = WeatherReport()
    response = weather_report.get_location_details()
    assert response == "Invalid IPAddress due to ('pass valid ipaddress',)"
    ipaddress_mock.ip_address.assert_called_once()


@patch("main.ipaddress")
@patch("main.requests")
def test_location_details_3(request_mock, ipaddress_mock):
    """
    Test case to test the get_location_details function when
    KeyError occurs
    """
    ipaddress_mock.ip_address.return_value = Mock()
    location = {"country": "US"}
    json_mock = Mock(status_code=200)
    json_mock.json.return_value = location
    request_mock.request.return_value = json_mock
    weather_report = WeatherReport()
    response = weather_report.get_location_details()
    assert response == "Exception occurred due to ('city',)"
    ipaddress_mock.ip_address.assert_called_once()
    request_mock.request.assert_called_once()
    json_mock.json.assert_called_once()


@patch("main.requests")
def test_get_weather_report_1(request_mock):
    """
    Test case to test the get_weather_report function while
    fetching the weather report successfully
    """
    json_mock = Mock(status_code=200)
    json_mock.json.return_value = weather_report_data
    request_mock.request.return_value = json_mock
    weather_report = WeatherReport()
    response = weather_report.get_weather_report("Watertown")
    assert response is None
    request_mock.request.assert_called_once()
    json_mock.json.assert_called_once()


@patch("main.requests")
def test_get_weather_report_2(request_mock):
    """
    Test case to test the get_weather_report function while
    getting exception
    """
    request_mock.request.side_effect = [Exception("invalid url")]
    weather_report = WeatherReport()
    response = weather_report.get_weather_report("Watertown")
    assert response == "Exception occurred due to ('invalid url',)"
    request_mock.request.assert_called_once()
