#!/usr/bin/python
# Code to add widgets will go here...

import tkinter
from tkinter import messagebox
from tkinter import *
from GPIOLibrary import GPIOProcessor
import time

top = Tk()
top.title("Welcome to this demo")
top.geometry("600x400+300+200")
top.config(background = "white")

top.resizable(0,0)
label = Label( top, text='Click on the buttons to see the magic', bg = "white")

#top.iconbitmap('favicon.ico')

def helloCallBack(self):
   messagebox.showinfo( "Hello Python", "Hello World")

def touchCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

def temperatureCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

def LEDCallBack():
   GP = GPIOProcessor()
   try:
    Pin27 = GP.getPin27()
    Pin27.out()

    Pin29 = GP.getPin29()
    Pin29.input()

    for i in range(0,20):
         pinValue = Pin29.getValue();
         if pinValue == 1:
            Pin27.high()
         else:
            Pin27.low()
            time.sleep(1)

   finally:
      GP.cleanup()
   #messagebox.showinfo( "Hello Python", "Hello World")

def turnNobCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

helloButton = Button(top, text ="            Hello              ",fg = "red", command = helloCallBack)
touchButton = Button(top, text ="     Touch Sensor       ", fg = "orange", command = touchCallBack)
temperatureButton = Button(top, text ="Temperature Sensor", fg="green", command = temperatureCallBack)
LEDButton = Button(top, text ="               LED              ", fg="blue",command = LEDCallBack)
turnNobButton = Button(top, text ="          Turn Nob         ", fg="indigo", command = turnNobCallBack)

def quitter(self):
   top.destroy()


top.bind('h', helloCallBack)
top.bind('q', quitter)
top.bind('<Escape>', quitter)

mainframe = Frame(top)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

tkvar = StringVar(top)
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza')
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

label.pack()
helloButton.pack()
touchButton.pack()
temperatureButton.pack()
LEDButton.pack()
turnNobButton.pack()
top.mainloop()
