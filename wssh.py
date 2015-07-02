#!/usr/bin/python

import websocket
import sys

def on_message(ws, message):
    print message
def on_error(ws, error):
    print error
    exit(2)

def on_close(ws):
    print "Session Closed"

def on_open(ws):
    print "Session Open"
    ws.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Need Host!"
        exit(1)
    host = sys.argv[1]
    ws = websocket.WebSocketApp(host,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
