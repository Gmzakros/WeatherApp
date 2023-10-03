
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
def printTable():
    str = '{0: ^15}{1: ^15}{2: ^15}{3: ^15}{4: ^15}'.format('Current Tempature', 'Low', 'High', 'Humidity', 'Wind Speed')
    data = '  {0: ^15}{1: ^15}{2: ^15}{3: ^15}{4: ^15}'.format(Weather.getCurrentTemp(), Weather.getHighLow()[1], Weather.getHighLow()[0], Weather.getHumidity() + '%', Weather.getWindSpeed() + ' mph')
    print(str)
    print('------------------------------------------------------------------------------------')
    print(data)

def main():
    printStart()
    printTable()

main()
    