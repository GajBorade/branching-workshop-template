"""
length_converter.py

This module provides functions to convert values related to length measurements.
Currently implemented:
- meters_to_kilometers(value): Converts meters to kilometers.

Each function is designed to take a numeric input and return the converted value.
"""


def meters_to_kilometers(value_in_meters):
    """
    Convert a length from meters to kilometers.

    :param value_in_meters:
        value_in_meters(float or int): The length in meters to convert.
    :return:
        value_in_kilometers(float): The converted length in kilometers.
    """
    return value_in_meters / 1000
