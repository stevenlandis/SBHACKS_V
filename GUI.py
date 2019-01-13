#!/usr/bin/python


# Code to add widgets will go here...


import tkinter
from tkinter import messagebox
from tkinter import *
from GPIOLibrary import GPIOProcessor
import time


#global theme
theme = 0

top = Tk()
top.title("Welcome to this demo")
top.geometry("600x400+300+200")
top.config(background = "black")
top.resizable(0,0)
label = Label( top, text='Click on the buttons to see the magic', bg = "white")
#top.iconbitmap('favicon.ico')


class HoverBinding:
   def __init__(self, button):
      self.button = button
   def on_enter(self, e):
       self.button['background'] = 'grey'

   def on_leave(self, e):
       self.button['background'] = 'SystemButtonFace'

   def enterLeaveBinding(self):
      print("in Enter and Leave")
      self.button.bind("<Enter>", self.on_enter)
      self.button.bind("<Leave>", self.on_leave)



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


def changeBackgroundColor():
   global theme
   if (theme % 2 ==0):
      theme+=1
      top.config(background = "white")
      return
   theme+=1
   top.config(background = "black")

helloButton = Button(top, text ="            Hello              ",fg = "red", command = helloCallBack)
touchButton = Button(top, text ="     Touch Sensor       ", fg = "orange", command = touchCallBack)
temperatureButton = Button(top, text ="Temperature Sensor", fg="green", command = temperatureCallBack)
LEDButton = Button(top, text ="               LED              ", fg="blue",command = LEDCallBack)
turnNobButton = Button(top, text ="          Turn Nob         ", fg="indigo", command = turnNobCallBack)
quitbutton = Button(top, text = "               Exit               ", fg="violet", command = quit)
themeButton = Button(top, text = "             Theme              ", fg="turquoise", command = changeBackgroundColor)

buttonList = []
buttonList.append(HoverBinding(helloButton))
buttonList.append(HoverBinding(touchButton))
buttonList.append(HoverBinding(temperatureButton))
buttonList.append(HoverBinding(LEDButton))
buttonList.append(HoverBinding(turnNobButton))
buttonList.append(HoverBinding(quitbutton))
buttonList.append(HoverBinding(themeButton))
for item in buttonList:
   print("something something")
   item.enterLeaveBinding()


label.pack()
helloButton.pack()
touchButton.pack()
temperatureButton.pack()
LEDButton.pack()
turnNobButton.pack()
quitbutton.pack()
themeButton.pack()

top.mainloop()
