# Errores en Python existen muchos, y estos cuando ocurren soltaran un Traceback mediante el interpretador
# Ahora vamos a descubrir como probar manualmente que una parte del codigo este libre de texto y ademas, crear nuestros propios errores

suma = lambda x, y: x + y
assert suma(2, 2) == 4      # assert basicamente prueba la condicion del caso siguiente y si regresa resultados esperados, no arrojara errores

age = int(input("Ingrese su edad: "))
if age < 18:
    raise Exception("Usted debe ser mayor de edad!")    # raise Exception nos permite crear un mensaje de error propia y parar la ejecucion del programa