"""local api client used to obtain
IoT service credentials for iot mqtt communication

"""

import os
import logging
import requests

API_APPS_CONFIG_URL = "http://localhost:{}/api/apps"
API_DEVICE_CONFIG_URL = "http://localhost:{}/api/device"


def get_app_config_api(appId, port=5000):
    """get app configuration from local HTTP server"""
    return local_http_api(
        API_APPS_CONFIG_URL, query_param={"applicationId": appId}, port=port
    )


def get_device_config_api(port=5000):
    """get app configuration from local HTTP server"""
    return local_http_api(API_DEVICE_CONFIG_URL, port=port)


def local_http_api(url, query_param=None, port=5000):
    """local HTTP server API"""
    env_port = os.getenv("PORT")
    if env_port:
        port = env_port
    try:
        result = requests.get(url.format(port), params=query_param, timeout=30)
        result.raise_for_status()
        if result.status_code == 200:
            data = result.json()
            logging.info(
                f"{__name__}: signalsdk:HTTP request "
                f"local HTTP server success. Data: {data}"
            )
            return data
    except Exception as e:
        logging.error(
            f"{__name__}: signalsdk:HTTP request "
            f"local HTTP server failed. Error: {e}"
        )
    return None
