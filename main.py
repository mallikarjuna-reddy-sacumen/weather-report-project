"""This file is entry of the project, we can get the weather report of the respective IPAddress"""
# standard library's
import ipaddress
import json
import requests
from furl import furl

from config import API_ID, LOCATION_URL, WEATHER_REPORT_URL, IP_ADDRESS


class WeatherReport:
    """Class to get the weather report of a specific IPAddress"""

    json_file_name = "weather-report.json"

    def get_location_details(self) -> str:
        """
        This method to get the location details by
        passing IPAddress
        """

        try:
            ipaddress.ip_address(IP_ADDRESS)
            location_url = f"{LOCATION_URL}/{IP_ADDRESS}"
            location_data = requests.request("GET", location_url)
            if location_data.status_code == 200:
                city = location_data.json()["city"]
                return city
            else:
                raise Exception("Failed to fetch")
        except ValueError as err:
            return f"Invalid IPAddress due to {err.args}"
        except Exception as err:
            return f"Exception occurred due to {err.args}"

    def get_weather_report(self, city_name):
        """
        This method to fetch the weather report by passing location name
        """
        try:
            weather_url = furl(WEATHER_REPORT_URL)
            weather_url.args["q"] = city_name
            weather_url.args["appid"] = API_ID
            weather_data = requests.request("GET", weather_url)
            if weather_data.status_code == 200:
                weather_info = weather_data.json()
                with open(WeatherReport.json_file_name, "w") as file_obj:
                    json.dump(weather_info, file_obj, indent=4)
            else:
                raise Exception("Failed to fetch")

        except Exception as err:
            return f"Exception occurred due to {err.args}"


if __name__ == "__main__":
    weather_report = WeatherReport()
    city_name = weather_report.get_location_details()
    print(city_name)
    weather_response = weather_report.get_weather_report(city_name)
    print(weather_response)
