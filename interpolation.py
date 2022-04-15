#!/bin/env python3

"""Documentation

Just a script simple to test interpolation in Python
"""


email = """
Olá, %(nome)s

Informamos que voce recebeu um %(produto)s.

Click no link %(link)s e aproveite essa maravilha.

Caso houver duvidas, ligue no %(telefone)s
"""

clientes = ["Ana", "John", "Francisnaldo"]

for cliente in clientes:
    print(email % {"nome": cliente, "produto": "cigarro", "link": "https://kkk.com.br", "telefone": "0800 342 190"})
