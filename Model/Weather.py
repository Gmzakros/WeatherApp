import ParseData
import datetime


def hourlyData():
    dict = ParseData.getData()['hourly']
    timesAndTemps = {}
    for i in range(len(dict['time'])):
        estTime = datetime.datetime.fromtimestamp(dict['time'][i]).strftime('%H')
        timesAndTemps[estTime] = dict['temperature_2m'][i]
    return timesAndTemps


def getWindSpeed():
    dict = ParseData.getData()
    return dict

print(hourlyData())
