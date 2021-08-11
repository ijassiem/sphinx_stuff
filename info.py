""" This module contains functions for displaying machine information.
"""
import socket
import os

def host_name():
    """This function returns the hostname of computer
    :return: the hostname of computer
    :rtype: str
    """
    result = socket.gethostname()
    return c

def machine_os():
    """This function returns the name of the operating system running on machine
    :return: the operating system of computer
    :rtype: str
    """
    result = os.name
    return result
