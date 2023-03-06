# Clase del modelado de un Humano

class Human:

    def __init__(self, nombre, edad, profesion, pais):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.pais = pais
        self._presupuesto = 0

    def greetings(self, other_person):
        return f"Hello {other_person.nombre}, my name is {self.nombre}"
    
    def profession_explanation(self, other_person):
        return f"{other_person.nombre}, yo trabajo como un {self.profesion}"
    
    def _define_budget(self, person_budget):
        self._presupuesto = person_budget
    


if __name__ == '__main__':
    
    name, age, profession, country = input("Ingresa tu nombre, edad, profesion y pais: ").split()
    age = int(age)

    first_person = Human(name, age, profession, country)
    
    name, age, profession, country = input("Ingresa el nombre, edad, profesion y pais de la otra persona: ").split()
    age = int(age)

    second_person = Human(name, age, profession, country)

    budget, other_budget = input("Ingresa el presupuesto de ambas personas por separado: ").split()
    first_person._define_budget(int(budget))
    second_person._define_budget(int(other_budget))

    greet = first_person.greetings(second_person)
    print(greet)

    profession_explain = first_person.profession_explanation(second_person)
    print(profession_explain)
    
    print(f"El presupuesto de {first_person.nombre} es de {first_person._presupuesto}, mientras que el presupuesto de {second_person.nombre} es de {second_person._presupuesto}")