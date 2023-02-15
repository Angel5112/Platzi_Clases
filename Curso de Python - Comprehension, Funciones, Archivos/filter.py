# La funcion filter() permite filtrar los elementos de una lista existente en una nueva cumplida una condicion
# establecida por la lambda, en caso de ser True, pasara a la nueva lista

# Filtrar los numeros pares de una lista de numeros

nums = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x: x % 2 == 0, nums))
print(f"La lista de numeros pares de la lista: {nums} es: {new_numbers}")