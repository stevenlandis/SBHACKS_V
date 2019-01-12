from __future__ import print_function
import websocket

ip = "http://169.231.141.17"

def main():
    websocket.enableTrace(True)
    ws = websocket.create_connection(ip)
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    ws.close()


if __name__ == "__main__":
    main()