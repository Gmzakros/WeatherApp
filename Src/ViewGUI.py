import customtkinter as ct
from tkinter import *
from PIL import Image
import sys
import os

data_path = os.path.join(os.path.dirname(__file__),'Model')
print (data_path)
sys.path.append(data_path)
from Model import Weather

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")
isDarkMode = True

root  = ct.CTk()
root.geometry("650x500")
root.title("Wild Weather")


WeatherPerDay = Weather.getWeatherPerDay()


CurrentTemp = Weather.getCurrentTemp()
CurHighAndLow = Weather.getHighLow()
CurHumidity = Weather.getHumidity()
CurWindSpeed = Weather.getWindSpeed()
CurWeather = Weather.getWeeklyWeatherCode()[0]



def weekForcast():
    makeNewWindow()
    weekForcastPage()
    root.mainloop()


def makeNewWindow():
    global root
    root.destroy()
    root =ct.CTk()
    root.geometry("650x475")
    root.title("Wild Weather")

def currentForcast():
    makeNewWindow()
    currentForcastPage()
    root.mainloop()
    


def currentForcastPage():
    global WeatherPerDay, CurrentTemp, CurHighAndLow, CurHumidity, CurWindSpeed,CurRainChance
    frame = ct.CTkFrame(master=root)
    frame.pack(padx=20, pady=20, fill= 'both', expand=True, side='right')

    sideFrame = ct.CTkFrame(master=root, width=50)
    sideFrame.pack(padx= 20, pady= 20, side= 'left',fill='both', expand=True)

    mainFrame = ct.CTkFrame(master= frame)
    mainFrame.pack(padx=10, pady=15, fill= 'both', expand=True, side='top')

    scrollFrame = ct.CTkScrollableFrame(master= frame, orientation='horizontal',height= 50)
    scrollFrame.pack(padx=10, pady=15, fill= 'both', expand=True, side='bottom')

    menuLabel = ct.CTkLabel(master= sideFrame, text= "Menu", text_color= 'orange')
    menuLabel.pack(padx=5, pady= 10)

    toCurrentForcast = ct.CTkButton(master= sideFrame,text= "Weekly Forcast", command= weekForcast )
    toCurrentForcast.pack(padx= 10, pady= 10)

    backToStartBtn = ct.CTkButton(master= sideFrame,text= "Back To Start", command= openStart )
    backToStartBtn.pack(padx = 10, pady= 20)

    darkModeButton = ct.CTkButton(master=sideFrame, command=changeMode, text= "Switch Mode")
    darkModeButton.pack(padx = 10, pady = 10)

    quitBtn = ct.CTkButton(master = sideFrame, text= 'Quit', command= root.destroy)
    quitBtn.pack(padx= 10, pady = 20)

    mainCurentTitle = ct.CTkLabel(master = mainFrame, text= 'Current Weather')
    mainCurentTitle.pack(padx= 10, pady= 15, side= 'top')

    curentTempLabel = ct.CTkLabel(master = mainFrame, text= CurrentTemp, font= ('', 20))
    curentTempLabel.pack(padx= 10, pady= 7, side= 'top')

    currentHighLabel = ct.CTkLabel(master = mainFrame, text= CurHighAndLow[1])
    currentHighLabel.pack(padx= (30, 10), pady= 7, side= 'left')

    curentLowLabel = ct.CTkLabel(master = mainFrame, text= CurHighAndLow[0])
    curentLowLabel.pack(padx= 10, pady= 7, side= 'left')

    curentHumidityLabel = ct.CTkLabel(master = mainFrame, text= CurHumidity)
    curentHumidityLabel.pack(padx= 10, pady= 7, side= 'left')

    curentWindSpeedLabel = ct.CTkLabel(master = mainFrame, text= CurWindSpeed)
    curentWindSpeedLabel.pack(padx= 10, pady= 7, side= 'left')




def changeMode():
    global isDarkMode
    if isDarkMode == True:
        ct.set_appearance_mode("light")
        isDarkMode = False
    else:
        ct.set_appearance_mode("dark")
        ct.AppearanceModeTracker.update()
        isDarkMode = True


def weekForcastPage():
    global WeatherPerDay
    frame = ct.CTkCanvas(master=root,background= "#66574d")
    frame.pack(padx=20, pady=30, fill= 'both', expand=True, side='right')

    label = ct.CTkLabel(master=frame, text='This Weeks Weather', text_color='White')
    label.grid(row=0, column=2)

    headerLabel = ct.CTkLabel(master= frame, text= 'Days From Today', text_color='White')
    headerLabel.grid(row= 1, column= 1, sticky= 'ew',padx = 8)

    headerLabel = ct.CTkLabel(master= frame, text= 'High', text_color='White')
    headerLabel.grid(row= 1, column= 2, sticky= 'ew', padx = 8)

    headerLabel = ct.CTkLabel(master= frame, text= 'Low', text_color='White')
    headerLabel.grid(row= 1, column= 3, sticky= 'ew', padx = 8)

    headerLabel = ct.CTkLabel(master= frame, text= 'Humidity', text_color='White')
    headerLabel.grid(row= 1, column= 4, sticky= 'ew', padx = 8)

    for i in range(8):
        dayLabel = ct.CTkLabel(master= frame, text= str(i), text_color='White')
        dayLabel.grid(row= i + 2, column= 1, sticky= 'ew', padx = 8, pady= 8)
    
    for i in range(8):
        for j in range(3):
            if j == 2:
                l = ct.CTkLabel(master= frame, text= WeatherPerDay[i][j] + '%', text_color='White')
            else:
                l = ct.CTkLabel(master= frame, text= WeatherPerDay[i][j] + '°F', text_color='White')

            l.grid(row= i + 2, column= j + 2, sticky= 'ew', padx = 8, pady= 8)


    sideFrame = ct.CTkFrame(master=root, width=50)
    sideFrame.pack(padx= 20, pady= 20, side= 'left',fill='both', expand=True)

    
    menuLabel = ct.CTkLabel(master= sideFrame, text= "Menu", text_color= 'orange')
    menuLabel.pack(padx=5, pady= 10)

    toCurrentForcast = ct.CTkButton(master= sideFrame,text= "Current Forcast", command= currentForcast )
    toCurrentForcast.pack(padx= 10, pady= 10)

    backToStartBtn = ct.CTkButton(master= sideFrame,text= "Back To Start", command= openStart )
    backToStartBtn.pack(padx = 10, pady= 20)

    darkModeButton = ct.CTkButton(master=sideFrame, command=changeMode, text= "Switch Mode")
    darkModeButton.pack(padx = 10, pady = 10)

    quitBtn = ct.CTkButton(master = sideFrame, text= 'Quit', command= root.destroy)
    quitBtn.pack(padx= 10, pady = 20)


def openStart():
    makeNewWindow()
    startPage()
    root.mainloop()


def startPage():

    frameStartPage = ct.CTkFrame(master=root)
    frameStartPage.pack(padx=20, pady=40, fill='both', expand=True)

    label = ct.CTkLabel(master=frameStartPage, text='Welcome to Wild Weather', text_color="orange")
    label.pack(padx=10, pady=10)

    img = ct.CTkImage(Image.open('./Assets/noBackroundStartPage.png'))
    img._size = [100, 100]

    imgLabel = ct.CTkLabel(master=frameStartPage, text='', image= img)
    imgLabel.pack(padx=10, pady=10)


    currentForcastBtn = ct.CTkButton(master=frameStartPage, text="View Current Forcast",command= currentForcast)
    currentForcastBtn.pack(padx=10,pady=10)

    weekForcastBtn = ct.CTkButton(master=frameStartPage, text="View 7 Day Forcast",command=weekForcast)
    weekForcastBtn.pack(padx=10,pady=10)
    
    darkModeButton = ct.CTkButton(master=frameStartPage, command=changeMode, text= "Switch Mode")
    darkModeButton.pack(padx = 10, pady = 10)

    quitBtn = ct.CTkButton(master = frameStartPage, text= 'Quit', command= root.destroy)
    quitBtn.pack(padx= 10, pady = 10)


def main():
    
    startPage()
    root.mainloop()

    global WeatherPerDay, CurrentTemp, CurHighAndLow, CurHumidity, CurWindSpeed,CurRainChance
    WeatherPerDay = Weather.getWeatherPerDay()
    CurrentTemp = Weather.getCurrentTemp()
    CurHighAndLow = Weather.getHighLow()
    CurHumidity = Weather.getHumidity()
    CurWindSpeed = Weather.getWindSpeed()
    CurRainChance = Weather.getPrecipitationPerDay()[0]


if __name__ == "__main__":
    main()