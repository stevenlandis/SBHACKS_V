#!/usr/bin/python


# Code to add widgets will go here...


import tkinter
from tkinter import messagebox
from tkinter import *
from GPIOLibrary import GPIOProcessor
import time




top = Tk()
top.title("Welcome to this demo")
label = Label( top, text='Click on the buttons to see the magic', relief=RAISED )

top.iconbitmap('favicon.ico')

def helloCallBack():
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

helloButton = Button(top, text ="Hello", command = helloCallBack)
touchButton = Button(top, text ="Touch Sensor", command = touchCallBack)
temperatureButton = Button(top, text ="Temperature Sensor", command = temperatureCallBack)
LEDButton = Button(top, text ="LED", command = LEDCallBack)
turnNobButton = Button(top, text ="Turn Nob", command = turnNobCallBack)

label.pack()
helloButton.pack()
touchButton.pack()
temperatureButton.pack()
LEDButton.pack()
turnNobButton.pack()

top.mainloop()
