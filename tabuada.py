#!/usr/bin/env python3

"""Description:
    Print the multiplication table
"""
__version__ = "0.1.1"
__author__ = "Fabricio Fagundes"



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

# Iterable

for n1 in numbers:
    print("{:-^30}".format(f" Multiplication Table {n1} "))
    print("")
    for n2 in numbers:
        resultado = n1 * n2
        print(f"{n1:>10} x {n2} = {resultado}")
    print("")
    print("#" * 30)

