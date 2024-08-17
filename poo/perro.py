class Perro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} de {self.age}"
    
    def ladrar(self):
        print(f"{self.name} ladra fuerte")
    
perro_1 = Perro("Wolf", 7)
print(perro_1)
print(perro_1.age)
print(perro_1.name)
# print(perro_1.__str__())
perro_1.ladrar()