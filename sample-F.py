import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def check_even(n):
    return n % 2 == 0


def number_generator(limit):
    for i in range(limit):
        yield i


class Calculator:

    def __init__(self, value):
        self.value = value

    def square(self):
        return self.value ** 2

    def cube(self):
        return self.value ** 3


def run_operations(x, y):
    results = {
        "add": add(x, y),
        "subtract": subtract(x, y),
        "multiply": multiply(x, y),
        "divide": divide(x, y),
        "even": check_even(x)
    }
    return results
