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

__version__ = "0.1.2"
__author__ = "Fabricio Fagundes"
__license__ = "Unlicense"


import os


current_language = os.getenv("LANG", "en_US")
print(current_language)

msg = {
        "eng_US": "Hello Python!!!",
        "pt_BR": "Olá Python!!!",
        "it_IT": "Ciao Python!!!",
        "es_SP": "Hola Python!!!",
        "fr_FR": "Bonjour Python!!!",
        }


# Print the message
print(msg[current_language])



