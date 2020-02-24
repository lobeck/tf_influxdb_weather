#!/usr/bin/python

from setuptools import setup

setup(
    name="tf_influxdb_weather",
    version="0.0.1",
    description="Send Tinkerforge outdoor weather data to InfluxDB",
    url="https://github.com/lobeck/tf_influxdb_weather",
    license="GPL",
    author="Christian Becker",
    author_email="python@beck.space",
    scripts=["tf_influxdb_weather"],
    install_requires=list(open("requirements.txt").read().strip().split("\n"))
)
