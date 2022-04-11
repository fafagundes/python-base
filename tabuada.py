#!/usr/bin/env python3

"""Description:
    Print the multiplication table
"""
__version__ = "0.1.0"
__author__ = "Fabricio Fagundes"


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

# Iterable

for number in numbers:
    print("Multiplication Table: ", number)
    for other_number in numbers:
        print(number * other_number)
    print("-------------")
