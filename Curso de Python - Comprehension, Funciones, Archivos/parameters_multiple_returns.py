# Una funcion a la cual no se le envien la misma cantidad de parametros que argumentos soltara un Traceback

# Una forma de evitar esto seria dandole valores predeterminados a los parametros en caso de que el usuario
# no envie cierto parametro por error o por decision propia

# Funcion para hallar el volumen

def find_volume(length = 1, width = 1, depth = 1):          # Esos valores seran tomados si no se recibe dicho parametro
    return length * width * depth

# Probemos unicamente enviando el width y el depth

result = find_volume(width = 10, depth = 20)        # En estos casos se repetiran los nombre de parametros y argumentos
print(f"El resultado sin el length es: {result}")

# Ademas de eso, en Python es posible retornar mas de un resultado por funcion, puede ser mediante tuplas o varias variables

def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'hola, yo soy Angel'


result = find_volume(width = 10, depth = 20)
print(f"De esta forma, result se volvera una tupla de 3 elementos: {result}")

result, width, text = find_volume(width = 10, depth = 20)
print(f"Ahora, result: {result}, width: {width} y text: {text} fueron retornados de funcion como diferentes variables")