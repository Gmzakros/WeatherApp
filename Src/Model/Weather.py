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

def getSunriseSunset():
    dict = ParseData.getData1Day()['daily']
    return (dict['sunrise'][0], dict['sunset'][0])

def getWeeklyWeatherCode():
    weatherCodes = ParseData.getData1Day()['daily']['weathercode']
    weatherLst = []
    for i in range(len(weatherCodes)):
        if i == 0:
            weatherLst.append(processWeatherCode(weatherCodes[i], False))
        else:
            weatherLst.append(processWeatherCode(weatherCodes[i], True))
        
    print(weatherLst)
    return weatherLst




def processWeatherCode(code, weekly):
    t = time.localtime()
    currentTime = time.strftime('%H', t)
    sunriseSunset = getSunriseSunset()
    sunSet = False
    if int(currentTime) < sunriseSunset[0] and int(currentTime) >= sunriseSunset[1]:
        sunSet = True

    match code:
        case 0:
            if not sunSet or weekly:
                return 'Sunny'
            else:
                return 'Clear'
        case 1:
            if not sunSet or weekly:
                return 'Mainly Sunny'
            else:
                return 'Mainly Clear'
        case 2:
            return 'Partly Cloudly'
        case 3:
            return 'Cloudy'
        case 45:
            return 'Foggy'
        case 48:
            return 'Rime Fog'
        case 51:
            return 'Light Drizzle'
        case 53:
            return 'Drizzle'
        case 55:
            return 'Heavy Drizzle'
        case 56:
            return "Light Freezing Drizzle"
        case 57:
            return "Freezing Drizzle"
        case 61:
            return "Light Rain"
        case 63:
            return "Rain"
        case 65:
            return "Heavy Rain"
        case 66:
            return "Light Freezing Rain"
        case 67:
            return "Freezing Rain"
        case 71:
            return "Light Snow"
        case 73:
            return "Snow"
        case 75:
            return "Heavy Snow"
        case 77:
            return "Snow Grains"
        case 80:
            return "Light Showers"
        case 81:
            return "Showers"
        case 82:
            return "Heavy Showers"
        case 85:
            return "Light Snow Showers"
        case 86:
            return "Snow Showers"
        case 95:
            return "Thunderstorm"
        case 96:
            return "Light Thunderstorms With Hail"
        case 99:
            return "Thunderstorm With Hail"
        case _:
            return "Whoops"


getWeeklyWeatherCode()