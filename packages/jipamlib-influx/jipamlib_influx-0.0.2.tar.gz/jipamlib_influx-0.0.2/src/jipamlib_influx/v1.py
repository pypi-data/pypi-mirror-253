import datetime
import time
import pandas as pd
import logging
from influxdb import InfluxDBClient
logging.disable(logging.DEBUG)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def log(m):
    logging.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ; {m}")
