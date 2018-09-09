# VWCoreUtil - contains utility functions.
# Packaged with VisorWare, a project by Liam Z. Charles.

import socket

def connCheck(): # Checks for availability of internet connection.
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


