"""This file consists configuration of logger"""
# standard library's
import logging

from config import FILE_MODE, LOG_FORMAT, WEATHER_REPORT_LOG

# Create and configure logger
logging.basicConfig(filename=WEATHER_REPORT_LOG,
                    format=LOG_FORMAT,
                    filemode=FILE_MODE)

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)

