from tkinter import *

rotItem = ''
touchItem = ''
lightItem = ''
buttonActItem = ''
clickItem = ''
encoderItem = ''


tk = Tk()
tk.title("Sensors and Actions")
tk.geometry("600x400+300+200")
rotVar = StringVar(tk)
touchVar = StringVar(tk)
lightVar= StringVar(tk)
buttonActVar = StringVar(tk)
clickVar = StringVar(tk)
encoderVar = StringVar(tk)

rotVar.set("one")
touchVar.set("one")
lightVar.set("one")
buttonActVar.set("one")
clickVar.set("one")
encoderVar.set("one")


def getRotItem(self):
    rotItem = rotVar.get()
    if (rotItem == "one"):
        print("action one here")
    elif (rotItem == "two"):
        print("action two here")
    elif (rotItem == "three"):
        print("action three here")
        data = ""
def getTouchItem(self):
    touchItem = touchVar.get()
    if (touchItem == "one"):
        print("action one here")
    elif (touchItem == "two"):
        print("action two here")
    elif (touchItem == "three"):
        print("action three here")
        data = ""
def getLightItem(self):
    lightItem = lightVar.get()
    if (lightItem == "one"):
        print("action one here")
    elif (lightItem == "two"):
        print("action two here")
    elif (lightItem == "three"):
        print("action three here")
        data = ""
def getbuttonActItem(self):
    buttonActItem = buttonActVar.get()
    if (buttonActItem == "one"):
        print("action one here")
    elif (buttonActItem == "two"):
        print("action two here")
    elif (buttonActItem == "three"):
        print("action three here")
        data = ""
def getClickItem(self):
    clickItem = clickVar.get()
    if (clickItem == "one"):
        print("action one here")
    elif (clickItem == "two"):
        print("action two here")
    elif (clickItem == "three"):
        print("action three here")
        data = ""
def getEncoderItem(self):
    encoderItem = encoderVar.get()
    if (encoderItem == "one"):
        print("action one here")
    elif (encoderItem == "two"):
        print("action two here")
    elif (encoderItem == "three"):
        print("action three here")
        data = ""
        sendData(data)
def sendData(data):
    print("send data")


Label(tk, text="Rot:").grid(column=0,row=0)
Label(tk, text="Touch:").grid(column=0,row=1)
Label(tk, text="Light:").grid(column=0,row=2)
Label(tk, text="Button:").grid(column=0,row=3)
Label(tk, text="Click:").grid(column=0,row=4)
Label(tk, text="Encoder:").grid(column=0,row=5)

rot = OptionMenu(tk, rotVar, "one", "two", "three", command=getRotItem).grid(column=1,row=0)
touch = OptionMenu(tk, touchVar, "one", "two", "three", command=getTouchItem).grid(column=1,row=1)
light = OptionMenu(tk, lightVar, "one", "two", "three", command=getLightItem).grid(column=1,row=2)
buttonAct = OptionMenu(tk, buttonActVar, "one", "two", "three", command=getbuttonActItem).grid(column=1,row=3)
click = OptionMenu(tk, clickVar, "one", "two", "three", command=getClickItem).grid(column=1,row=4)
encoder = OptionMenu(tk, encoderVar, "one", "two", "three", command=getEncoderItem).grid(column=1,row=5)


button = Button(tk, text="OK", command=getRotItem)

mainloop()
