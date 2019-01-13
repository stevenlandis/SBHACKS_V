#!/usr/bin/python


# Code to add widgets will go here...


import tkinter
from tkinter import messagebox
from tkinter import *
import time


#global theme


top = Tk()
top.title("Welcome to this demo")
top.geometry("600x400+300+200")
top.config(background = "black")
top.resizable(0,0)
label = Label( top, text='Click on the buttons to see the magic', bg = "white")
#top.iconbitmap('favicon.ico')
theme = 0
chosen = ''
chosenButton = Button()

class HoverBinding:
   def __init__(self, button):
      self.button = button
   def on_enter(self, e):
      if(self.button != chosenButton):
         self.button['background'] = 'grey'

   def on_leave(self, e):
      if(self.button != chosenButton):
         self.button['background'] = 'SystemButtonFace'

   def enterLeaveBinding(self):
      print("in Enter and Leave")
      self.button.bind("<Enter>", self.on_enter)
      self.button.bind("<Leave>", self.on_leave)


def chosenButtonColor(button):
   print("in buttno color",button)
   button['background'] = 'SystemButtonFace'

def callFunction(string):
   func = string.split(':')
   if (len(func) < 2):
      print("String sent has errors!")
      return
   elif (func[0] == "temperature"):
      temperatureCallBack(func[1])
   elif (func[0] == "LED"):
      LEDCallBack(func[1])
   elif (func[0] == "turnNob"):
      turnNobCallBack(func[1])
   elif (func[0] == "light"):
      lightCallBack(func[1])

def helloCallBack():
   messagebox.showinfo( "Hello Python", "Hello World")

def touchCallBack():
   # Add code for touch sensor here
   print("sss")

def temperatureCallBack():
   # Add code for temperature here
   chosen = "temperature"
   temperatureButton['background'] = 'yellow'
   global chosenButton
   print("aaa",chosenButton)
   chosenButtonColor(chosenButton)
   chosenButton = temperatureButton



def LEDCallBack():
   # Add code light sensor here
   chosen = "LED"
   LEDButton['background'] = 'yellow'
   global chosenButton
   chosenButtonColor(chosenButton)
   chosenButton = LEDButton

def turnNobCallBack():
   # Add code for volume here
   chosen =  "turnNob"
   turnNobButton['background'] = 'yellow'
   global chosenButton
   chosenButtonColor(chosenButton)
   chosenButton = turnNobButton

def changeBackgroundColor():
   global theme
   if (theme % 2 ==0):
      theme+=1
      top.config(background = "white")
   else:
      theme+=1
      top.config(background = "black")
   themeButton['background'] = 'yellow'
   global chosenButton
   chosenButtonColor(chosenButton)
   chosenButton = themeButton

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
callFunction(chosen)
top.mainloop()
