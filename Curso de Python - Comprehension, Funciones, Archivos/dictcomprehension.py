# Dictionary comprehension sigue el mismo concepto de list comprehension: La creacion de un diccionario con una
# sintaxis abreviada en una simple linea

import random

# Creacion de un diccionario de forma normal

dict = {}

for i in range(1, 5):
    dict[i] = i * 2

print(f"El diccionario es: {dict}")

# Creacion del mismo diccionario mediante Dict. Comprehension

dict_v2 = {i: i * 2 for i in range(1, 5)}
print(f"El diccionario mediante dict. comprehension es: {dict_v2}")

# Creacion de un diccionario de poblacion desde una lista de paises (Sintaxis Normal)

population = {}
countries = ['col', 'mex', 'arg', 'bol']

for country in countries:
    population[country] = random.randint(1, 100)

print(f"El diccionario es: {population}")

# Creacion del mismo diccionario pero mediante dict. comprehension

countries = ['col', 'mex', 'arg', 'bol']
population_v2 = {country: random.randint(1, 100) for country in countries}
print(f"El diccionario pero con Dict. Comprehension es: {population_v2}")

# Creacion de un diccionario partiendo de dos listas mediante dict comprehension

names = ['nicolas', 'julio', 'santiago']
ages = [16, 58, 11]

combination = {name: age for (name, age) in zip(names, ages)}   # Zip comprime dos listas en una lista de tuplas
print(f"El diccionario es: {combination}")
