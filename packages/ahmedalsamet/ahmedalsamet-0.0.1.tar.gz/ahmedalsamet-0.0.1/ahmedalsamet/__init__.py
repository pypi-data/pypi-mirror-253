from tkinter import *
from tkinter import ttk
import os

def mainWindow():
    window =Tk()
    window.resizable(False,False)
    window.geometry("960x600+230+50")
    window.config(background='#22333B')
    style = ttk.Style()
    style.map('T2.TButton', foreground=[('pressed', '#22333B'),
                                            ('active', '#22333B'),
                                           ('disabled', '#22333B'), ('!disabled', '#22333B')],
                  background=[('pressed', '#22333B'), ('active', '#22333B'),
                              ('!disabled', '#22333B'), ('disabled', '#22333B')
                              ], )
    style.configure('T2.TButton', relief='flat', font=('tajwal', 30, 'italic'))
    ttk.Button(window,text="Hello Ahmed",width=200,cursor='man',style="T2.TButton").pack(padx=100,pady=200)
    window.mainloop()

mainWindow()
