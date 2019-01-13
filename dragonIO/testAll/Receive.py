from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import Keyboard_Control as keyboard
import Volume_Control as volume

import sys
def Parse_String_From_Board(string):
    if "rot" in string:
        turnVal = round(int(string[4:])/1023*100)
        volume.Set_Volume(turnVal)
    elif "button" in string:
        keyboard.Tab()


#port = int(sys.argv[1])
port = 22

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message back to client
        Parse_String_From_Board(self.data)
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', port, SimpleEcho)
server.serveforever()