# Las funciones son fundamentales para evitar escribir un bloque de codigo una y otra vez en programas

# Python permite la creacion de funciones de la siguiente forma

def my_function(text):      # text es lo conocido como "parametro/s de la funcion"
    for i in text:
        print(i)


# Fuera de la funcion, podemos "invocarla" o "llamarla" para tener acceso a dicho bloque de codigo

my_text = 'Hola, yo soy Angel'
my_function(my_text)    # Llamada a la funcion con el "argumento" my_text