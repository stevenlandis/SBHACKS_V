from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import Keyboard_Control as keyboard
import Volume_Control as volume
import Windows_Control as windows
import Youtube_Control as youtube
import GUI
import sys
import wmi
import _thread as thread
import pythoncom

DataString = ''
port = 22

def Socket_Function():
    pythoncom.CoInitialize()
    server = SimpleWebSocketServer('', port, SimpleEcho)
    server.serveforever()

class SimpleEcho(WebSocket):
    def handleMessage(self):
        # echo message back to client
        DataString = self.data
        GUI.Call_Function(DataString)
       # print(DataString)
        self.sendMessage(self.data)
    def handleConnected(self):
        print(self.address, 'Connected')
    def handleClose(self):
        print(self.address, 'Disconnected')

thread.start_new_thread(Socket_Function, ())
GUI.GUI()

