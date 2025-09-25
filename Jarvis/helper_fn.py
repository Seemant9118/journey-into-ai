import socket

def isInternetActive():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False
