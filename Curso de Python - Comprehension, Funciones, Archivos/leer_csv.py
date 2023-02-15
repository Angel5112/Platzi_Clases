# Los archivos csv son los mas importantes en proyectos de analisis o ciencia de datos
# Python permite la lectura de dichos archivos para extraer la informacion y poder luego manejarla
# o incluso graficarla

import csv

# Funcion para leer el csv y retornar su informacion en una lista

def read_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')    # csv,reder() un metodo del modulo csv
        header = next(reader)                           # Usamos next() en reader para acceder a los titulos
        books = []                                      # Lista donde se guardara cada diccionario
        for row in reader:
            book_info = zip(header, row)                # Juntamos titulo con informacion de libro por tuplas
            book = {key: value for (key, value) in book_info}   # Creamos diccionario por tuplas 
            books.append(book)                          # Agregamos el diccionario a la lista
        return books

# Funcion para leer informacion de libro por libro

def read_book_info(dataset):
    for i in range(0, len(dataset)):            # Leemos diccionario por diccionario en vez de todo el dataset completo
        print('\n' + '******' * 22 + '\n')
        print(dataset[i])


if __name__ == '__main__':
    path = './app/best_sellers.csv'         # Path del csv con el que se trabajo
    data = read_csv(path)
    read_book_info(data)
    