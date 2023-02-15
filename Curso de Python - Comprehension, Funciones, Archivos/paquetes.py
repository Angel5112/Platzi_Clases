# Los paquetes/packages o pkg son carpetas que contienen modulos con diferente contenido
# Para importar cierto modulo de un paquete se usa from pkg_name import module_name
# Ademas, se recomienda que cada paquete tenga un modulo __init__.py en donde se dejara instrucciones que siempre
# se ejecutaran, y este modulo le indica a Python que se trata de un paquete y no de una carpeta normal

# Importando los modulos

from pkg import aritmetica, mensaje

# Codigo base

def run():
    x = int(input('Ingrese el primer numero: '))
    y = int(input('Ingrese el segundo numero: '))

    print(f"\nLa suma es: {aritmetica.suma(x, y)}")
    print(f"La resta es: {aritmetica.resta(x, y)}")
    print(f"La division es: {aritmetica.division(x, y)}")
    print(f"El producto es: {aritmetica.producto(x, y)}")

    mensaje.message()


if __name__ == '__main__':
    run()