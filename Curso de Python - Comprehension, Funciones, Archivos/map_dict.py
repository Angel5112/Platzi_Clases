# La funcion map() tambien se puede usar en diccionarios, siempre teniendo cuidado de no alterar el array original

# Dada una lista de diccionarios, transformar las key 'price' en una nueva lista

items = [{'product': 'camisa', 'price': 100},
        {'product': 'pantalon', 'price': 300},
        {'product': 'reloj', 'price': 200}]

prices_list = list(map(lambda item: item['price'], items))
print(f"La lista de los precios de productos es: {prices_list}")