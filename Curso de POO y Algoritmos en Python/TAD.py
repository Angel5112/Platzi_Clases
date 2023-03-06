# Los TAD tienen la ventaja de contar con descomposicion, abstraccion y encapsulamiento

# Descomposicion = Dividir el problema en problemas de menor escala para hacer el proceso mas satisfactorio para el programador y el usuario que leera el codigo
# Abstraccion = Manejo de menu o interfaces para "explicar" el proceso o operacion sin dar muchos detalles, simplemente se le da a entender al usuario, lo que deberia ocurrir
# Encapsulamiento = Agrupar valores, variables o datos para la seguridad del objeto, clase o usuario. Para eso se usan las variables o atributos privados "_attribute_name"

class Computer:

    def __init__(self, cpu, gpu, storage):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = None        # Claro ejemplo de Descomposicion
        self.storage = storage

    def add_ram(self, modules, gb, speed):
        self.ram = RAM(modules, gb, speed)


class RAM:

    def __init__(self, modules, gb, speed):
        self.modules = modules
        self.gb = gb
        self.speed = speed



if __name__ == '__main__':
    cpu, gpu, storage = input("Enter your CPU, GPU and Storage Capacity: ").split()
    modules, gb, speed = input("Enter the number of RAM modules, GB and Speed of the RAM: ").split()

    my_computer = Computer(cpu, gpu, storage)

    my_computer.add_ram(modules, gb, speed)

    print(f"RAM characteristics are: Number of Modules = {my_computer.ram.modules}, GBs = {my_computer.ram.gb}, Speed = {my_computer.ram.speed}")