#!/usr/bin/env python3

"""Exibi relatorio de criancas por atividade.

Imprimir a lista de criancas agrupadas por sala que 
frequentam cada uma das atividades.
"""

__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]


# criar um lista e colocar todas as listas de atividades dentro e adicionar tupla para termos as atividades com uma tag

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Danca", aula_danca),
]


# Listar alunos em cada atividade por sala

for name, alunos in atividades: # um loop para interar em cada lista
    # desempacotar a tupla colocando em duas variaveis onde a primeira e a tag e a segunda e a lista

    sala1_atividades = []
    sala2_atividades = []

    for aluno in alunos: # um loop para interar dentro das listas
        if aluno in sala1:
            sala1_atividades.append(aluno)
        if aluno in sala2:
            sala2_atividades.append(aluno)

    print(f"Sala 1 - Atividade de {name}", sala1_atividades)
    print(f"Sala 2 - Atividade de {name}", sala2_atividades)
    print()


