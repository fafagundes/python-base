#!/usr/bin/env python3

"""
Here we have documentation about the app below

Usage:

    You must have the environment variable LANG configured ex:

        export LANG=C.UTF-8

Exec:

    python3 hello.py
    or
    ./hello.py

"""

__version__ = "0.0.1"
__author__ = "Fabricio Fagundes"
__license__ = "Unlicense"


import os


current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello Pytho!!!"

if current_language == "pt_BR":
    msg = "Olá Python!!!"
elif current_language == "it_IT":
    msg = "Ciao Mondo!!!"
elif current_language == "es_SP":
    msg = "Hola Mundo!!!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!!!"

# Print the message
print(msg)



