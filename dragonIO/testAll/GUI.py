from tkinter import *
import Keyboard_Control as keyboard
import Windows_Control as windows
import Volume_Control as volume

Function_Dict = {"rot":volume.Change_Volume ,
                 "touch": volume.Change_Volume,
                 "light": volume.Change_Volume,
                 "button": volume.Change_Volume,
                 "click": volume.Change_Volume,
                 "encoder": volume.Change_Volume}

def GUI():
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

    rotVar.set("Volume")
    touchVar.set("YouTube")
    lightVar.set("Auto-Dim")
    buttonActVar.set("Tab")
    clickVar.set("Enter")
    encoderVar.set("Scroll Windows")


    def getRotItem(self):
        rotItem = rotVar.get()
        if (rotItem == "Volume"):
            Function_Dict["rot"] = volume.Change_Volume
        elif (rotItem == "Brightness"):
            "JUst clicked Brightness"
            Function_Dict["rot"] = windows.Change_Brightness
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
        elif (buttonActItem == "one"):
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
    Label(tk, text="Encoder:").grid(column=0,row=4)
    Label(tk, text="Encoder Click:").grid(column=0,row=5)

    rot = OptionMenu(tk, rotVar, "Volume", "Brightness", command=getRotItem).grid(column=1,row=0)
    touch = OptionMenu(tk, touchVar, "Youtube", "Toggle Brightness", command=getTouchItem).grid(column=1,row=1)
    light = OptionMenu(tk, lightVar, "Auto-Dim", command=getLightItem).grid(column=1,row=2)
    buttonAct = OptionMenu(tk, buttonActVar, "Tab", "Enter", command=getbuttonActItem).grid(column=1,row=3)
    click = OptionMenu(tk, clickVar, "Enter", "New Tab", command=getClickItem).grid(column=1,row=5)
    encoder = OptionMenu(tk, encoderVar, "Scroll Windows", "Scroll Tabs",  command=getEncoderItem).grid(column=1,row=4)


    button = Button(tk, text="OK", command=getRotItem)

    while True:
        tk.update_idletasks()
        tk.update()

def Call_Function(string):
    split_string = string.split(":")
    print("Got to here....")
    Function_Dict[split_string[0]](int(split_string[1]))
def Parse_String_From_Board(string):
    if "rot" in string:
        turnVal = round(int(string[4:])/1023*100)
        #windows.Adjust_Brightness(turnVal)
        volume.Set_Volume(turnVal)
    elif "button" in string:
        if "1" in string:
            windows.Open_Chrome()
    elif "encoder" in string:
        if "0" in string:
            keyboard.Alt_Tab()
        else:
            keyboard.Alt_Shift_Tab()
