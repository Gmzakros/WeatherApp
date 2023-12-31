import requests


def getData1Day():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.0379&longitude=-76.3055&hourly=temperature_2m,relativehumidity_2m,precipitation_probability,rain,visibility,windspeed_10m&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timeformat=unixtime&timezone=America%2FNew_York&past_days=7&forecast_days=1")
    dict = response.json()
    return dict

def getData7Days():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=39.9979&longitude=-76.3541&hourly=temperature_2m,precipitation_probability&daily=temperature_2m_max,temperature_2m_min&temperature_unit=fahrenheit&timeformat=unixtime&timezone=America%2FNew_York&past_days=1")
    dict = response.json()
    return dict


