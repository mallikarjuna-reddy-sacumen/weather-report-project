"""This file consists test data, this file will be used while executing the test cases"""

WEATHER_REPORT_DATA = {
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

CITY = {"city": "Watertown"}

OK_STATUS_CODE = 200

FAILURE_STATUS_CODE = 422