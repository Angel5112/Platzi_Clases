# Proyecto para probar lo aprendido del curso de PIP y entornos virtuales

from pkg import charts

def run():
    print("Ingrese los valores que desea poner en el grafico: \n")
    values = list(map(int, input().split()))
    print("\nIngrese los nombres de las etiquetas que desea poner en el grafico: \n")
    labels = input().split()

    if charts.validate_input(values, labels) == True:
        charts.create_plot(values, labels)
    else:
        print("\nERROR: El numero de valores debe coincidir con el numero de etiquetas")


if __name__ == '__main__':
    run()