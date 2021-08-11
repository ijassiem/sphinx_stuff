""" This module contains functions for displaying machine information.
"""
import socket

def host_name():
    """This function returns the hostname of computer
    :return: the hostname of computer
    :rtype: str
    """
    result = socket.gethostname()
    return c
