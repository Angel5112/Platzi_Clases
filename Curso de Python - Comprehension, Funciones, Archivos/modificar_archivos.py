# Para modificar archivos, debemos cambiar el tipo de permiso a uno de escritura y lectura
# r+ nos dejara escribir sobre lo existente y leer, nunca se perdera la informacion
# w+ sobreescribira el archivo cada vez que se corra el programa

# Abramos el archivo de la clase anterior

with open('./text.txt', 'r+') as file:
    file.write("\nAgregando nueva linea al final!\n")    # con el metodo write() se puede agregar texto al archivo
    for line in file:
        print(line)
