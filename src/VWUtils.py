# VWUtils - contains utility functions.
# Packaged with VisorWare, a project by Liam Z. Charles.

#####################################################################################
#                                                                                   #
#    VWUtils.py - Module for provision of various utility functions for VisorWare.  #
#    Copyright (C) 2019  Liam Z. Charles                                            #
#                                                                                   #
#    This program is free software: you can redistribute it and/or modify           #
#    it under the terms of the GNU Affero General Public License as published       #
#    by the Free Software Foundation, either version 3 of the License, or           #
#    (at your option) any later version.                                            #
#                                                                                   #
#    This program is distributed in the hope that it will be useful,                #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of                 #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                  #
#    GNU Affero General Public License for more details.                            #
#                                                                                   #
#    You should have received a copy of the GNU Affero General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.         #
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



