# Las operaciones de la teora de conjuntos se pueden realizar dados dos conjuntos A y B

set_a = {1, 5, 32, 21, 345}
set_b = {2, 6, 8, 212, 21, 4, 5}

# Union de conjuntos = Se unen todos los elementos de A y B en un conjunto C

set_c = set_a.union(set_b)
set_d = set_a | set_b
print(f"El conjunto C formado con la union de A y B es: {set_c}")
print(f"El conjunto C formado con la union de A y B (Usando el simbolo | ) es: {set_d}")

# Interseccion de conjuntos = Se agregan los elementos que esten en A y B al mismo tiempo en un conjunto C

set_c = set_a.intersection(set_b)
set_d = set_a & set_b
print(f"El conjunto C formado con la interseccion de A y B es: {set_c}")
print(f"El conjunto C formado con la interseccion de A y B (Usando el simbolo & ) es: {set_d}")

# Diferencia de conjuntos = Elementos de A que no se encuentran en B

set_c = set_a.difference(set_b)
set_d = set_a - set_b
print(f"El conjunto C formado con la diferencia de A y B es: {set_c}")
print(f"El conjunto C formado con la diferencia de A y B (Usando el simbolo - ) es: {set_d}")

# Diferencia simetrica de conjuntos = Elementos de A y B que no estan en ambos conjuntos a la vez

set_c = set_a.symmetric_difference(set_b)
set_d = set_a ^ set_b
print(f"El conjunto C formado con la diferencia simetrica de A y B es: {set_c}")
print(f"El conjunto C formado con la diferencia simetrica de A y B (Usando el simbolo ^ ) es: {set_d}")

