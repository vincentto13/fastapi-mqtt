__author__ = "Sabuhi Shukurov"

__email__ = 'sabuhi.shukurov@gmail.com'

credits = ["Sabuhi Shukurov","Hasan Aliyev", "Tural Muradov"]

__version__ = "0.0.5"

from sys import modules as imported_modules
if not "setuptools" in imported_modules.keys():
    from fastapi_mqtt.fastmqtt import FastMQTT
    from fastapi_mqtt.config import  MQQTConfig

    __all__ = ["FastMQTT", "MQQTConfig"]