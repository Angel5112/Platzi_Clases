# Return es una instruccion que se utiliza para retornar resultados de funciones en forma de valor o variable

# Funcion de suma

def sums(a, b):
    result = a + b
    return result       # Cada vez que se llegue a un return, la funcion finaliza su ciclo y vuelve al main

# Invocacion de la funcion

answer = sums(5, 7)     # Gracias al return, se puede asignar el valor obtenido en la funcion a una variable en main
print(f"La suma es: {answer}")