from __future__ import print_function
import websocket
import asyncio

ip = "http://169.231.141.17"

async def main():
    websocket.enableTrace(True)
    ws = websocket.create_connection(ip)
    print("Receiving...")
    result = await ws.recv()
    print("Received '%s'" % result)
    ws.close()




if __name__ == "__main__":
    main()