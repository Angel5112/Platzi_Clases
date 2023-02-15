# La funcion reduce() es una funcion que permite reducir a un unico elemento una lista dada mediante la operacion
# o comportamiento definido por la lambda

# Se debe importar antes de usar

import functools

# Reducir una lista a un unico elemento (Suma de todos los elementos)

nums = [1, 3, 6, 14]
result = functools.reduce(lambda counter, item: counter + item, nums)   # Counter = contador interno de la operacion
print(f"La suma de todos los elementos de la lista es: {result}")