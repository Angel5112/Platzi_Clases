# Clase del modelado de un Humano

class Human:

    def __init__(self, nombre, edad, profesion, pais):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.pais = pais
        self._presupuesto = 0

    def greetings(self, other_person):
        return f"Hello {other_person}, my name is {self.nombre}"
    
    def profession_explanation(self, other_person):
        return f"{other_person.nombre}, yo trabajo como un {self.profesion}"
    
    def _define_budget(self, person_budget):
        self._presupuesto = person_budget
        print(self._presupuesto)
    


if __name__ == '__main__':
    
    name, age, profession, country = input("Ingresa tu nombre, edad, profesion y pais: ")
    age = int(age)

    first_person = Human(name, age, profession, country)
    
    name, age, profession, country = input("Ingresa el nombre, edad, profesion y pais de la otra persona: ")
    age = int(age)

    second_person = Human(name, age, profession, country)

    budget, other_budget = int(input("Ingresa el presupuesto de ambas personas por separado: "))
    first_person._define_budget(budget)
    second_person._define_budget(other_budget)