import ParseData
import datetime
import time


def getHourlyData():
    dict = ParseData.getData1Day()['hourly']
    timesAndTemps = {}
    for i in range(len(dict['time'])):
        estTime = datetime.datetime.fromtimestamp(dict['time'][i]).strftime('%H')
        timesAndTemps[estTime] = (str(int(dict['temperature_2m'][i])), str(dict['rain'][i] / 100))
    return timesAndTemps


def getWindSpeed():
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    windSpeed = ParseData.getData1Day()['hourly']['windspeed_10m'][int(currentTime)]
    return str(int(windSpeed))

def getCurrentTemp():
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    dict = getHourlyData()

    return int(dict[currentTime][0])

def getHighLow():
    units = ParseData.getData1Day()['daily_units']
    data = ParseData.getData1Day()['daily']
    minStr = ''
    minStr += str(int(data['temperature_2m_min'][0]))
    minStr += units['temperature_2m_min']

    maxStr = ''
    maxStr += str(int(data ['temperature_2m_max'][0]))
    maxStr += units['temperature_2m_max']

    return maxStr, minStr

def getHumidity():
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    Humidity = ParseData.getData1Day()['hourly']['relativehumidity_2m'][int(currentTime)]
    return str(int(Humidity))


def getHourlyWeatherFromTime():
    t = time.localtime()
    currentTime = time.strftime('%H', t)

    dict = {}
    HourlyWeather = getHourlyData()
    for i in HourlyWeather:
        if i >= currentTime:
            dict[i] = HourlyWeather[i]

    return dict


def getPrecipitationPerDay():
    lst = ParseData.getData7Days()['hourly']['precipitation_probability']
    res = []

    for i in range(len(lst) // 24):
        res.append(max(lst[0:24]))
        lst = lst[24:(len(lst))]

    return res

def getWeatherPerDay():
    dict = ParseData.getData7Days()['daily']
    precpitation = getPrecipitationPerDay()
    res = {}
    for i in range(len(dict["temperature_2m_max"])):
        res[i] = (str(int(dict["temperature_2m_max"][i])), str(int(dict["temperature_2m_min"][i])), str(precpitation[i]))
    return res

