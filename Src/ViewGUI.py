import customtkinter
from tkinter import *
from PIL import Image


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


root  = customtkinter.CTk()
root.geometry("500x350")

def login():
    print('test')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12,padx=10)

img = Image.open(".\\Assets\\new.png")

label2 = customtkinter.CTkLabel(master=frame, image=img, text="")
label2.pack(pady=12, padx=10)

root.mainloop()
