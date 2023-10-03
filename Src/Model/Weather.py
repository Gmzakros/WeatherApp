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
    dict = ParseData.getData()
    return dict

def getCurrentTemp():
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    dict = getHourlyData()

    return int(dict[currentTime])


