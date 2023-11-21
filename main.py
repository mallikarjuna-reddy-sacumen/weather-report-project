"""This file is entry of the project, we can get the weather report of the location"""
# standard library's
import ipaddress
import requests

from config import API_ID, LOCATION_URL, WEATHER_REPORT_URL, IP_ADDRESS


class WeatherReport:
    """
    Class to get the weather report of a specific location
    """
    def get_location_details(self):
        """
        This method to get the location details by passing
        IPAddress
        """
        try:
            ipaddress.ip_address(IP_ADDRESS)
            location_url = f"{LOCATION_URL}/{IP_ADDRESS}"
            location_data = requests.request("GET", location_url)
            city = location_data.json()["city"]
            return city
        except ValueError as err:
            return f"Invalid IPAddress due to {err.args}"
        except Exception as err:
            return f"Exception occurred due to {err.args}"

    def get_weather_report(self, city_name):
        """
        This method to fetch the weather report by passing location name
        """
        try:
            weather_url = f"{WEATHER_REPORT_URL}?q={city_name}&appid={API_ID}"
            weather_data = requests.request("GET", weather_url)
            return weather_data.json()
        except Exception as err:
            return f"Exception occurred due to {err.args}"


if __name__ == "__main__":
    weather_report = WeatherReport()
    city_name = weather_report.get_location_details()
    print(city_name)
    weather_response = weather_report.get_weather_report(city_name)
    print(weather_response)
