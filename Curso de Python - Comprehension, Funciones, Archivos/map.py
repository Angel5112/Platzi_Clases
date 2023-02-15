# La funcion map() permite transformar elementos de un iterable en uno nuevo mediante el concepto de HOF y lambdas

# Transformacion de elementos de una lista de numeros de forma tradicional

nums = [1, 2, 3, 4]
nums_v2 = [i * 2 for i in nums]
print(f"La lista original era: {nums} y la transformada es: {nums_v2}")

# Transformacion de elementos de una lista mediante map()

nums_v3 = list(map(lambda i: i *2, nums))
print(f"La lista transformada mediante la funcion map() es: {nums_v3}")

# Crear una nueva lista con la suma de los elementos de 2 listas mediante map()

nums = [1, 2, 3, 4]
nums_v2 = [5, 6, 7]

nums_v3 = list(map(lambda x, y: x + y, nums, nums_v2))
print(f"La suma de los elementos de la lista {nums} con los de la lista {nums_v2} mediante map() es: {nums_v3}")
print("Como se puede apreciar, map() no considera los elementos sobrantes, trabajarla con precaucion")