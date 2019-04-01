# VWUtils - contains utility functions.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VWUtils.py - Module for provision of various utility functions for VisorWare.  #
#    Copyright (C) 2019  Liam Z. Charles | All Rights Reserved.                     #
#                                                                                   #
#  >>> UNAUTHORIZED DISTRIBUTION and UNAUTHORIZED MODIFICATION                      #
#      of this software is NOT ALLOWED.                                             #
#                                                                                   #
#####################################################################################

import socket
from termCol import *

def connCheck(): # Checks for availability of internet connection.
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False



