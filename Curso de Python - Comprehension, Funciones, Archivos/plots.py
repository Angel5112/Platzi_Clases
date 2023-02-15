# Usando la libreria/modulo de matplotlib es posible crear graficos mediante Python tomando datos
# Crearemos 2 de los tipos de graficos mas populares, de barra y de torta

import matplotlib.pyplot as plt

# Crear funcion para grafico de barras

def bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

# Crear funcion para grafico de torta

def pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['Jugos', 'Comida', 'Postres']
    values = [45, 211, 25]
    bar_chart(labels, values)
    pie_chart(labels, values)