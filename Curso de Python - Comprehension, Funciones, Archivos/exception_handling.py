# Cuando salen errores en Python, la ejecucion del programa se detiene por completo, esto puede ser alterado

# Usando try: se podra probar una parte del codigo y con except Error_Type: se podra continuar la ejecucion

# Creemos una funcion que divida dos numeros, vamos a capturar el error ZeroDivisionError

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:       # En casos normales arrojaria Traceback que no pemitiria la ejecucion, esto sera util para probar codigo que no estemos seguros que sirva
        result = 'No se permiten divisiones con 0'
    return result


if __name__ == '__main__':
    print("Caso de prueba 10 / 0 : ")
    result = division(10, 0)
    print(result)