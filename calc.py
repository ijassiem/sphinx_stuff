""" This module contains functions performing mathematical operations.
"""

def adder(a, b):
    """This function adds two integer numbers

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: sum of two integer numbers
    :rtype: int
    """
    c = a + b
    return c

def square(a):
    """This function squares an integer number

    :param a: first number
    :type a: int
    :return: square of the first number
    :rtype: int
    """
    b = a**2
    return b

def subtract(a, b):
    """This function calculates the difference between two integer numbers

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: difference of two integer numbers
    :rtype: int
    """
    result = a - b
    return result

def multiply(a, b, c):
    """This function calculates the product of three integer numbers

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :param b: third number
    :type b: int
    :return: product of three integer numbers
    :rtype: int
    """
    result = a*b*c
    return result

def divide(a, b):
    """This function calculates the quotient of two integer numbers

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: quotient of two integer numbers
    :rtype: int
    """
    result = a/b
    return result

def modulo(a, b):
    """This function calculates the modulo of two integer numbers

    :param a: first number
    :type a: int
    :param b: second number
    :type b: int
    :return: modulo of two integer numbers
    :rtype: int
    """
    result = a%b
    return result
