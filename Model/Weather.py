import ParseData


def hourlyData():
    dict = ParseData.getData()
    return dict['hourly']


def getWindSpeed():
    dict = ParseData.getData()
    return dict
