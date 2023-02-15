# Modulo donde se trabajaran las funciones para la creacion de la grafica de torta donde se va a 
# mostrar el porcentaje de libros de ficcion vs no-ficcion y la cantidad de libros como titulo del plot

import matplotlib.pyplot as plt

# Funcion para crear el grafico de torta de ficcion vs no-ficcion

def pie_chart(labels, values, num_books):
    fig, ax = plt.subplots()
    plt.title(f'Categoria de los {num_books} mas vendidos en Amazon durante 2009 - 2019', fontdict={'fontsize':16}, pad=20)
    ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'fontsize':14})
    ax.axis('equal')
    plt.show()
