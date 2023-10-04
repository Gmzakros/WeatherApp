
import sys
import os

data_path = os.path.join(os.path.dirname(__file__),'Model')
print (data_path)
sys.path.append(data_path)
from Model import Weather

def printStart():
    print()
    print('Welcome to Wild Weather')
    print('Here is the forcast for today:\n')


    #Place Holder Values
def printTable(currentTemp, high, low, humidity, windSpeed, day):
    str = '{0: ^20}{1: ^20}{2: ^20}{3: ^20}{4: ^20}{5: ^20}'.format('Days From Today','Current Tempature', 'Low', 'High', 'Humidity', 'Wind Speed')
    data = '{0: ^20}{1: ^20}{2: ^20}{3: ^20}{4: ^20}{5: ^20}'.format(day, currentTemp, low, high, humidity + '%', windSpeed + ' mph')
    print(str)
    print('--------------------------------------------------------------------------------------------------------------------------------')
    print(data)


def printToday():
    printStart()
    printTable(Weather.getCurrentTemp(), Weather.getHighLow()[0], Weather.getHighLow()[1], Weather.getHumidity(), Weather.getWindSpeed(), 0)

def printHourly():
    print()
    print('THIS IS THE WEATHER FOR THE REST OF TODAY\n')
   
    dict = Weather.getHourlyWeatherFromTime()
    str = '{0: ^20}{1: ^20}{2: ^20}'.format('Time','Tempature','Precipitation Probability')
    data = ''
    for i in dict:
        data += '{0: ^20}{1: ^20}            {2}%\n'.format(i, dict[i][0] + '°F', dict[i][1])
    print(str)
    print('-----------------------------------------------------------------------')
    print(data)



def print7day():
    print()

    dict = Weather.getWeatherPerDay()
    str ='{0: ^20}{1: ^20}{2: ^20}{3:^20}'.format('Days From Today','High Temp','LowTemp', 'Precipitation')
    data =''

    for i in dict:
        data += '{0: ^20}{1: ^20}{2: ^20}        {3}%\n'.format(i, dict[i][0], dict[i][1], dict[i][2])

    print(str)
    print('------------------------------------------------------------------------------')
    print(data)

    
def handleInput():
    ip = input("type '!hourly' for an hourly forcast today or type '!7day' for a 7 day forcast:")
    
    match ip:
        case '!hourly':
            printHourly()
        case '!7day':
            print7day()
        case _:
            print('invalid input')
            handleInput()

def main():
    printToday()
    handleInput()
    

    



if __name__ == '__main__':
    main()

    