mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Bogotá"
}

# print(mi_diccionario)
# print(type(mi_diccionario))

print(mi_diccionario["nombre"])  # Juan

nombre = mi_diccionario["nombre"]
print(nombre)  # Juan

edad = mi_diccionario["edad"]
print(edad)  # 25

mi_diccionario["edad"] = 30
print(mi_diccionario)  # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogotá'}

mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)  # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogotá', 'profesion': 'Ingeniero'}

for clave in mi_diccionario:
    print(clave)

# nombre
# ciudad
# profesion

for clave, valor in mi_diccionario.items():
    print(clave, valor)

# nombre Juan
# ciudad Bogotá
# profesion Ingeniero

if "nombre" in mi_diccionario:
    print("La clave 'nombre' se encuentra en el diccionario")

if "apellido" not in mi_diccionario:
    print("La clave 'apellido' no se encuentra en el diccionario")