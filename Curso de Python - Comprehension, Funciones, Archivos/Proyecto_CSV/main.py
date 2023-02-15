# Proyecto de lectura de CSV de los libros mas vendidos de Amazon desde 2009 a 2019
# Objetivo: Listar la cantidad de libros, mostrarlos como titulos del plot y mostrar la cantidad que son
# libros de ficcion y no ficcion

from pkg import plots, read_csv

def run():
    path = './info/best_sellers.csv'                # Path del csv
    best_books, num_books = read_csv.read_csv_file(path)       # Leemos el csv y lo organizamos en una lista de diccionarios
    read_csv.read_data(best_books)                  # Mostramos el CSV en pantalla de terminal
    categories = ['Ficcion', 'No-Ficcion']
    values = read_csv.category(best_books)
    plots.pie_chart(categories, values, num_books)


if __name__ == '__main__':
    run()