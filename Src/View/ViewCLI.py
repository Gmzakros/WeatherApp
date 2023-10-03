
def printStart():
    print()
    print('Welcome to Wild Weather')
    print('Here is the forcast for today:\n')


    #Place Holder Values
def printTable():
    str = '{0: ^15}{1: ^15}{2: ^15}{3: ^15}{4: ^15}'.format('Current Tempature', 'Low', 'High', 'Humidity', 'Wind Speed')
    data = '  {0: ^15}{1: ^15}{2: ^15}{3: ^15}{4: ^15}'.format(Model.getCurrentTemp(), '58', '80', '75%', '12 mph')
    print(str)
    print('------------------------------------------------------------------------------------')
    print(data)

def main():
    printStart()
    printTable()

printTable()
    