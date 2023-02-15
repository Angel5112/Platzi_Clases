# Diferentes operaciones con el tipo de estructura de dato conjunto mediante el uso de metodos y funciones

# Creamos un set vacio

test_set = set()

# Cantidad de elementos del conjunto

size = len(test_set)
print(f"La cantidad de elementos es: {size}")

# Agregar un elemento al conjunto

test_set.add(1)
print(f"Ahora el conjunto es: {test_set}")

# Agregar elementos de un subconjunto en el conjunto original

sub_set = {3, 4, 1, 32, 5}
test_set.update(sub_set)
print(f"El nuevo conjunto ahora es: {test_set}")

# Buscar elemento, retorna True (1) si lo encuentra o False (0) si no lo consigue

print(3 in test_set)

# Eliminar un elemento en un conjunto NOTA: Debe existir o de lo contrario arrojara un Traceback

test_set.remove(32)
print(f"El nuevo conjunto con 32 eliminado es: {test_set}")

# Eliminar un elemento sin miedo a que no este en el conjunto

test_set.discard(37)
print(f"37 no estaba en el conjunto y aun asi no hubo Traceback alguno, el conjunto sigue siendo: {test_set}")

# Eliminar un conjunto

test_set.clear()
print(f"Eliminado el conjunto!")