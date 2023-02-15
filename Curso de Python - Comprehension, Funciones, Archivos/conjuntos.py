# Los conjuntos (Sets) son un tipo de estructura de dato que se rige por los fundamentos de la Teoria de Conjuntos, siendo un conjunto un grupo de elementos no duplicados sin orden especifico

# Creacion de un conjunto de numeros

nums_set = {1, 2, 3, 4, 5, 5, 5, 1, 3, 4}

# Imprimir un conjunto

print(nums_set)     # Como se puede observar, los elementos repetidos no se consideran

# Transformar un conjunto a otro tipo de estructura de dato

nums_list = list(nums_set)
nums_tuples = tuple(nums_set)

# Imprimir las estructuras creadas a traves del conjunto de numeros

print(nums_list)
print(nums_tuples)
