# Todo archivo con extension .py es considerado un modulo, es por ello que se pueden crear nuestros propios modulos
# Solamente se deben crear en el mismo directorio y ser importados mediante import
# Finalmente para acceder a las operaciones, se maneja el nombre del modulo como un method

# Probemos con el siguiente programa que emula una calculadora basica

import utils

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: \n"))

print(f"La suma es: {utils.suma(x, y)}")
print(f"La resta es: {utils.resta(x, y)}")
print(f"La divison es: {utils.division(x, y)}")
print(f"El producto es: {utils.producto(x, y)}")

# Siempre recuerda que los modulos deben tener nombres significativos, utils es un standard de modulos de funciones
