# List Comprehension es basicamente el manejo de listas mediante el uso de una sintaxis mas simplificada

# Creacion y agregar elementos a una lista de forma normal

nums = []

for i in range(1, 11):
    nums.append(i)

print(f"La lista formada de manera tradicional es: {nums}")

# Creacion y agregar elementos de una lista mediante list comprehension

nums_v2 = [i for i in range(1, 11)]
print(f"La lista creada y formada con list comprehension es: {nums_v2}")

# Generalmente se sigue la sintaxis de list comprenhension = [element to use for element in iterable structure]. Ademas se pueden usar condicionales en la estructura

# Crear una lista mediante list comprehension que solo agregue elemenos impares del 1 al 100

odd_nums_list = [i for i in range(1, 101) if i % 2 != 0]
print(f"La lista de elementos impares creada mediante list comprehension es: {odd_nums_list}")