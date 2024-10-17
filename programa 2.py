# Crear un diccionario vacío
diccionario = {}

# Solicitar las traducciones
entradas = input("Ingrese las traducciones en formato <palabra>:<traducción>, separadas por dos puntos: ")
pares = entradas.split(',')

# Llenar el diccionario
for par in pares:
    palabra_traduccion = par.split(':')
    if len(palabra_traduccion) == 2:
        palabra = palabra_traduccion[0].strip()
        traduccion = palabra_traduccion[1].strip()
        diccionario[palabra] = traduccion

print("Diccionario creado:", diccionario)

# Pedir una frase en español para traducir
frase = input("Ingrese una frase en español para traducir: ")
palabras = frase.split()

# Traducir palabra por palabra
traduccion = []
for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))  # Dejar sin traducir si no está en el diccionario

# Mostrar la frase traducida
frase_traducida = ' '.join(traduccion)
print("Frase traducida:", frase_traducida)
