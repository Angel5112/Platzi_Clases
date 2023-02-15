# Leer archivos de texto en Python es muy simple, solamente debes agregar la direccio del archivo a una variable
# Abrirlo mediante with y open, luego leerlo de linea a linea mediante file_name.readline() o con un for loop

# Leamos un archivo de texto encontrado en el mismo directorio

with open('./text.txt') as file:
    for i in file:
        print(i)