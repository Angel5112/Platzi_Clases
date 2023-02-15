# Las funciones lambda son funciones anonimas que permiten dar mas versatilidad a funciones con una sintaxis sencilla

# Creacion de una funcion que suma dos numeros de forma tradicional

def sum(a, b):
    return a + b

result = sum(14, 2)
print(f"La suma es: {result}")

# Creacion de la funcion anterior pero mediante lambda

sum_v2 = lambda a, b: a + b

result = sum_v2(14, 2)
print(f"La suma mediante lambda es: {result}")

# La sintaxis sera, funct_name = lambda funct_args: return_value/s