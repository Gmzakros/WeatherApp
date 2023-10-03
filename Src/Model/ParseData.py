import requests


def getData():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=39.9979&longitude=-76.3541&hourly=temperature_2m,relativehumidity_2m,rain,showers,visibility,windspeed_10m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timeformat=unixtime&timezone=America%2FNew_York&forecast_days=1")
    dict = response.json()
    return dict


