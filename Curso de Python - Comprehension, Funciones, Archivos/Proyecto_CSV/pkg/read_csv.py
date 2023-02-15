# Modulo donde se trabajaran las funciones de lectura del csv ademas de funciones para mejor lectura de 
# los datos de los libros en la terminal

import csv

# Funcion para leer el CSV

def read_csv_file(path):
    with open(path, 'r') as csv_file:                   # Abrimos el archivo
        reader = csv.reader(csv_file, delimiter=',')    # Creamos el lector del csv
        header = next(reader)                           # Conseguimos los titulos (keys) de los diccionarios
        books = []                                      # Creamos la lista de diccionarios
        cont_books = 0

        for row in reader:  
            book_info = zip(header, row)                # Unimos titulos con valores de fila
            book = {key: value for (key, value) in book_info}   # Creamos diccionario ya juntando todo
            books.append(book)
            cont_books += 1

        return books, cont_books                        # Retornamos el diccionario

# Funcion para leer mejor los datos

def read_data(dataset):
    for element in range(0, len(dataset)):
        print('\n' + '*****' * 22)
        print(dataset[element])

# Funcion para determinar la cantidad de libros que son ficcion y no ficcion

def category(dataset):
    cont_ficcion = 0
    cont_no_ficcion = 0
    values = []

    for element in dataset:
        if element['Genre'] == 'Fiction':
            cont_ficcion += 1
        else:
            cont_no_ficcion += 1

    values.append(cont_ficcion)
    values.append(cont_no_ficcion)

    return values