import customtkinter as ct
from tkinter import *
from PIL import Image
def weekForcast():
    print('7day')


def currentForcast():
    print('current')

ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")


root  = ct.CTk()
root.geometry("500x350")

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












root.mainloop()
