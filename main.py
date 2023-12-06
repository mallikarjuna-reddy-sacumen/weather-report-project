"""This file is entry of the project, we can get the weather report of the respective IPAddress."""
# standard library's
import ipaddress
import json
import requests
from furl import furl

from config import (
    API_ID,
    JSON_FILE_NAME,
    IP_ADDRESS,
    LOCATION_URL,
    STATUS_OK,
    WEATHER_REPORT_URL,
)
from log import logger


class WeatherReport:
    """Class to get the weather report of a specific IPAddress."""

    def get_location_details(self) -> str:
        """Method to get location details by passing IPAddress."""
        try:
            logger.info(
                f"Initiating get_location_details method to get the location name of {IP_ADDRESS} IPAddress"
            )
            ipaddress.ip_address(IP_ADDRESS)
            location_url = f"{LOCATION_URL}/{IP_ADDRESS}"
            location_data = requests.request("GET", location_url)
            if location_data.status_code == STATUS_OK:
                city = location_data.json()["city"]
                return city
            else:
                location_data.raise_for_status()
        except ValueError as err:
            logger.exception(f"Exception occurred due to {err.args}")
        except Exception as err:
            logger.exception(f"Exception occurred due to {err.args}")

    def get_weather_report(self, city_name):
        """Method to fetch the weather report by passing location name."""
        try:
            logger.info(
                f"Initiating the get_weather_report method to get weather report of city {city_name}"
            )
            weather_url = furl(WEATHER_REPORT_URL)
            weather_url.args["q"] = city_name
            weather_url.args["appid"] = API_ID
            weather_data = requests.request("GET", weather_url)
            if weather_data.status_code == STATUS_OK:
                weather_info = weather_data.json()
                self.writing_to_json_file(weather_info)
            else:
                weather_data.raise_for_status()
        except Exception as err:
            logger.exception(f"Exception occurred due to {err.args}")

    def writing_to_json_file(self, weather_info):
        """This method store the weather report in json format."""
        try:
            logger.info(
                "Initiating the writing_to_json_file method to store the weather report"
            )
            with open(JSON_FILE_NAME, "w") as file_obj:
                json.dump(weather_info, file_obj, indent=4)
        except Exception as err:
            logger.exception(f"Exception occurred due to {err.args}")


if __name__ == "__main__":
    try:
        logger.info(
            f"Initiating the main method to get the weather report of {IP_ADDRESS} IPAdress"
        )
        weather_report = WeatherReport()
        city_name = weather_report.get_location_details()
        weather_report.get_weather_report(city_name)
    except Exception as err:
        logger.exception(f"Exception occurred due to {err.args}")
