class Monster:

    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} {self.categoria}"
    
    def myfunc(self):
        print("Hola, mi nombre es: "+ self.nombre)

# Crear un objeto de la clase Monster
monster1 = Monster("Sullivan", "Asustador")
print(monster1)

monster1.myfunc()
