"""
Proyecto 3 - Katas Python
Autor: Lenin Fonseca

En este archivo se recogen los ejercicios resueltos del proyecto.
Cada ejercicio irá encabezado por un comentario con su enunciado.
"""

from functools import reduce


# EJERCICIO 1
# Escribe una función que reciba una cadena de texto como
# parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencia_letras(texto):
    frecuencias = {}
    texto_limpio = texto.replace(" ", "").lower()

    for letra in texto_limpio:
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1

    return frecuencias

# EJERCICIO 2
# Dada una lista de números, obtén una nueva lista con el
# doble de cada valor. Usa la función map().

def doblar_valores(lista):
    return list(map(lambda numero: numero * 2, lista))

# EJERCICIO 3
# Escribe una función que tome una lista de palabras y una
# palabra objetivo como parámetros. La función debe devolver
# una lista con todas las palabras de la lista original que
# contengan la palabra objetivo.

def buscar_palabras(lista_palabras, objetivo):
    objetivo = objetivo.lower()
    return [palabra for palabra in lista_palabras if objetivo in palabra.lower()]

# EJERCICIO 4
# Genera una función que calcule la diferencia entre los
# valores de dos listas. Usa la función map().

def diferencia_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Las dos listas deben tener la misma longitud.")
    return list(map(lambda x, y: x - y, lista1, lista2))

# EJERCICIO 5
# Escribe una función que tome una lista de números como
# parámetro y un valor opcional nota_aprobado (por defecto 5).
# La función debe calcular la media y devolver una tupla
# con la media y el estado.

def calcular_media_y_estado(lista_numeros, nota_aprobado=5):
    if len(lista_numeros) == 0:
        return (0, "suspenso")

    media = sum(lista_numeros) / len(lista_numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# EJERCICIO 6
# Escribe una función que calcule el factorial de un número
# de manera recursiva.

def factorial_recursivo(numero):
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial_recursivo(numero - 1)

# EJERCICIO 7
# Genera una función que convierta una lista de tuplas a una
# lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))

# EJERCICIO 8
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada y muestra un mensaje
# indicando si la división fue exitosa o no.

def dividir_con_excepciones():
    try:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        resultado = numero1 / numero2
        print(f"La división fue exitosa. Resultado: {resultado}")
    except ValueError:
        print("Error: debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")

# EJERCICIO 9
# Escribe una función que tome una lista de nombres de mascotas
# como parámetro y devuelva una nueva lista excluyendo ciertas
# mascotas prohibidas en España.
# La lista de mascotas a excluir es:
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Usa la función filter().

def filtrar_mascotas_permitidas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

# EJERCICIO 10
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja
# el error adecuadamente.

class ListaVaciaError(Exception):
    pass

def calcular_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        raise ListaVaciaError("La lista está vacía.")

    return sum(lista_numeros) / len(lista_numeros)

# EJERCICIO 11
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del
# rango esperado (por ejemplo, menor que 0 o mayor que 120),
# maneja las excepciones adecuadamente.

def validar_edad():
    try:
        edad = int(input("Introduce tu edad: "))

        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")

        print(f"Edad válida: {edad}")
    except ValueError as error:
        print(f"Error: {error}")

# EJERCICIO 12
# Genera una función que, al recibir una frase, devuelva una
# lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# EJERCICIO 13
# Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas
# y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map().

def letras_mayus_minus(caracteres):
    letras_unicas = list(set(caracteres))
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))

# EJERCICIO 14
# Crea una función que retorne las palabras de una lista que
# comiencen con una letra en específico. Usa la función filter().

def palabras_por_letra(lista_palabras, letra):
    letra = letra.lower()
    return list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))

# EJERCICIO 15
# Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: list(map(lambda numero: numero + 3, lista))

# EJERCICIO 16
# Escribe una función que tome una cadena de texto y un número
# entero n como parámetros y devuelva una lista de todas las
# palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas_que(texto, n):
    pass


# EJERCICIO 17
# Crea una función que tome una lista de dígitos y devuelva el
# número correspondiente. Por ejemplo, [5,7,2] corresponde al
# número 572. Usa la función reduce().

def digitos_a_numero(lista_digitos):
    pass


# EJERCICIO 18
# Escribe un programa en Python que cree una lista de diccionarios
# con información de estudiantes (nombre, edad, calificación) y use
# filter para extraer a los estudiantes con una calificación mayor
# o igual a 90.

def estudiantes_destacados(estudiantes):
    pass


# EJERCICIO 19
# Crea una función lambda que filtre los números impares
# de una lista dada.

filtrar_impares = lambda lista: None


# EJERCICIO 20
# Para una lista con elementos de tipo integer y string,
# obtén una nueva lista solo con los valores int.
# Usa la función filter().

def solo_enteros(lista_mixta):
    pass


if __name__ == "__main__":
    print("#1", frecuencia_letras("Hola mundo"))
    print("#2", doblar_valores([1, 2, 3, 4]))
    print("#3", buscar_palabras(["casa", "casco", "perro", "casual"], "cas"))
    print("#4", diferencia_listas([10, 20, 30], [1, 2, 3]))
    print("#5", calcular_media_y_estado([6, 7, 8]))
    print("#6", factorial_recursivo(5))
    print("#7", tuplas_a_strings([(1, 2), ("hola", "mundo"), ("Python", 3)]))
    print("#8 listo para probar con input manual(arreglar cuanto tenga la mitad hechos)")
    print("#9", filtrar_mascotas_permitidas(["Perro", "Mapache", "Gato", "Oso", "Loro"]))
    print("#11 listo para probar con input manual")
    print("#12", longitud_palabras("Hola mundo desde Python"))
    print("#13", letras_mayus_minus("abracadabra"))
    print("#14", palabras_por_letra(["casa", "coche", "perro", "camino"], "c"))
    print("#15", sumar_tres([1, 2, 3, 4]))

    try:
        print("#10", calcular_promedio([5, 10, 15]))
    except ListaVaciaError as error:
        print("#10", error)