import matplotlib.pyplot as plt

# Funciones para el proyecto

# Funcion para validar el numero de entradas de valores y etiquetas de la grafica

def validate_input(val, labels):
    if len(val) != len(labels):
        return False
    else:
        return True


# Funcion para generar el plot

def create_plot(values, labels):
    fig, ax = plt.subplots()
    plt.title("Grafica de los valores dados por el Usuario")
    plt.bar(labels, values)
    plt.show()





