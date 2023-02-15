# Igual que en List Comprehension, en Dict Comprehension se pueden usar condicionales

import random

# Reutilizacion de unos de los diccionarios de la clase anterior

countries = ['col', 'mex', 'arg', 'bol']
population_dict = {country: random.randint(1, 100) for country in countries}

# Crear un diccionario en base a otro diccionario mediante Dict Comprehension, agregar par solo si population > 50

result = {country: population for (country, population) in population_dict.items() if population > 50}
print(f"El diccionario es: {result}")

# Dado un texto, crear un diccionario que solo guarde las vocales que aparecen y su version en mayuscula

text = 'Hola, soy nicolas'

unique_vocals = {c: c.upper() for c in text if c in 'aeiou'}
print(f"El diccionario de vocales unicas es: {unique_vocals}")