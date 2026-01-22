"""
This module provides basic mathematical operations and a calculator class.

It demonstrates full compliance with PEP-257 documentation standards.
"""


def add(a, b):
    """
    Add two numbers.

    Args:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: The sum of the two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first.

    Args:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: The result of subtraction.
    """
    return a - b


def check_even(number):
    """
    Check whether a number is even.

    Args:
        number (int): Input number.

    Returns:
        bool: True if the number is even, otherwise False.
    """
    return number % 2 == 0


class Calculator:
    """
    Perform basic calculator operations.
    """

    def __init__(self, value):
        """
        Initialize the calculator with a value.

        Args:
            value (int | float): Initial value.
        """
        self.value = value

    def square(self):
        """
        Return the square of the stored value.

        Returns:
            int | float: Squared value.
        """
        return self.value ** 2

    def cube(self):
        """
        Return the cube of the stored value.

        Returns:
            int | float: Cubed value.
        """
        return self.value ** 3
