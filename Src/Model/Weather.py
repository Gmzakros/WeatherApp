import ParseData
import datetime
import time


def getHourlyData():
    dict = ParseData.getData()['hourly']
    timesAndTemps = {}
    for i in range(len(dict['time'])):
        estTime = datetime.datetime.fromtimestamp(dict['time'][i]).strftime('%H')
        timesAndTemps[estTime] = dict['temperature_2m'][i]
    return timesAndTemps


def getWindSpeed():
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    windSpeed = ParseData.getData()['hourly']['windspeed_10m'][int(currentTime)]
    return str(int(windSpeed))

def getCurrentTemp():
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    dict = getHourlyData()

    return int(dict[currentTime])

def getHighLow():
    units = ParseData.getData()['daily_units']
    data = ParseData.getData()['daily']
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
    Humidity = ParseData.getData()['hourly']['relativehumidity_2m'][int(currentTime)]
    return str(int(Humidity))
