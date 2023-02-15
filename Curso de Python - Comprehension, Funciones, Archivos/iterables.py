# Los iterables son objetos con valores contables que pueden ser recorridos uno a uno y que contienen elementos en forma de estructura de datos

my_list = [1, 64, 21, 23, 12]   # Ejemplo de iterable: Lista

# Recorrer un iterable mediante loops

for i in range(1, 5):
    continue

# Recorrer un iterable manualmente mediante la creacion de un objeto iterable con iter() e iteracion manual con next()

my_list = iter(my_list)

# El primer elemento sera el primer uso del next()

print(f"El primer elemento mediante el uso de next es: {next(my_list)}")