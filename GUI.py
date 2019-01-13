from tkinter import *

rotItem = ''


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



Label(tk, text="Rot:").grid(column=0,row=0)
Label(tk, text="Touch:").grid(column=0,row=1)
Label(tk, text="Light:").grid(column=0,row=2)
Label(tk, text="Button:").grid(column=0,row=3)
Label(tk, text="Click:").grid(column=0,row=4)
Label(tk, text="Encoder:").grid(column=0,row=5)

rot = OptionMenu(tk, rotVar, "one", "two", "three", command=getRotItem).grid(column=1,row=0)
touch = OptionMenu(tk, touchVar, "one", "two", "three").grid(column=1,row=1)
light = OptionMenu(tk, lightVar, "one", "two", "three").grid(column=1,row=2)
buttonAct = OptionMenu(tk, buttonActVar, "one", "two", "three").grid(column=1,row=3)
click = OptionMenu(tk, clickVar, "one", "two", "three").grid(column=1,row=4)
encoder = OptionMenu(tk, encoderVar, "one", "two", "three").grid(column=1,row=5)


button = Button(tk, text="OK", command=getRotItem)

mainloop()
