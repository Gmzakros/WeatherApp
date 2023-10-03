import requests


def getData():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.0379&longitude=-76.3055&hourly=temperature_2m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timeformat=unixtime&timezone=America%2FNew_York")
    dict = response.json()
    return dict


