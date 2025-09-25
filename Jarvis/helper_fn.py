import socket

# check is internet active of not
def isInternetActive():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False
