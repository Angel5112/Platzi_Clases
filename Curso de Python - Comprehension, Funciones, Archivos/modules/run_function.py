# Para poder ejecutar un .py como archivo usando import y como script en una terminal a la vez
# Se recomienda usar lo siguiente:

import utils2

# Codigo principal

def run():
    name = input("Ingresa tu nombre: ")
    print(utils2.my_name(name))

if __name__ == '__main__':
    run()

# De esta forma, se podra ejecutar como archivo en un import y mediante script en la terminal