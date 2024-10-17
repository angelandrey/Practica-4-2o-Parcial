#diccionario vacío
persona = {}

# aqui agrego los datos al diccionario
def agregar_dato(clave, valor):
    persona[clave] = valor
    print(f"Contenido actual del diccionario: {persona}")

# en esta opcion le pido los datos al usuario

#aqui pido su nombre
nombre = input("Ingrese su nombre: ")
agregar_dato("Nombre", nombre)

#aqui el usuario ingresa su edad
edad = input("Ingrese su edad: ")
agregar_dato("Edad", edad)

#aqui ingresa su genero
genero = input("Ingrese su genero: ")
agregar_dato("genero", genero)

#ingrese su num celular
telefono = input("Ingrese su teléfono: ")
agregar_dato("Teléfono", telefono)

#por ultimo el correo electronico
correo = input("Ingrese su correo electrónico: ")
agregar_dato("Correo Electrónico", correo)

print("Información completa de la persona:", persona)
