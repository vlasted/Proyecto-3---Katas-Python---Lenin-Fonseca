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
    pass


# EJERCICIO 2
# Dada una lista de números, obtén una nueva lista con el
# doble de cada valor. Usa la función map().

def doblar_valores(lista):
    pass


# EJERCICIO 3
# Escribe una función que tome una lista de palabras y una
# palabra objetivo como parámetros. La función debe devolver
# una lista con todas las palabras de la lista original que
# contengan la palabra objetivo.

def buscar_palabras(lista_palabras, objetivo):
    pass


# EJERCICIO 4
# Genera una función que calcule la diferencia entre los
# valores de dos listas. Usa la función map().

def diferencia_listas(lista1, lista2):
    pass


# EJERCICIO 5
# Escribe una función que tome una lista de números como
# parámetro y un valor opcional nota_aprobado (por defecto 5).
# La función debe calcular la media y devolver una tupla
# con la media y el estado.

def calcular_media_y_estado(lista_numeros, nota_aprobado=5):
    pass


# EJERCICIO 6
# Escribe una función que calcule el factorial de un número
# de manera recursiva.

def factorial_recursivo(numero):
    pass


# EJERCICIO 7
# Genera una función que convierta una lista de tuplas a una
# lista de strings. Usa la función map().

def tuplas_a_strings(lista_tuplas):
    pass


# EJERCICIO 8
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada y muestra un mensaje
# indicando si la división fue exitosa o no.

def dividir_con_excepciones():
    pass


# EJERCICIO 9
# Escribe una función que tome una lista de nombres de mascotas
# como parámetro y devuelva una nueva lista excluyendo ciertas
# mascotas prohibidas en España.
# La lista de mascotas a excluir es:
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
# Usa la función filter().

def filtrar_mascotas_permitidas(lista_mascotas):
    pass


# EJERCICIO 10
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja
# el error adecuadamente.

def calcular_promedio(lista_numeros):
    pass

# EXCEPCIÓN PERSONALIZADA

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    pass

# EJERCICIO 11
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del
# rango esperado (por ejemplo, menor que 0 o mayor que 120),
# maneja las excepciones adecuadamente.

def validar_edad():
    pass


# EJERCICIO 12
# Genera una función que, al recibir una frase, devuelva una
# lista con la longitud de cada palabra. Usa la función map().

def longitud_palabras(frase):
    pass


# EJERCICIO 13
# Genera una función que, para un conjunto de caracteres,
# devuelva una lista de tuplas con cada letra en mayúsculas
# y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map().

def letras_mayus_minus(caracteres):
    pass


# EJERCICIO 14
# Crea una función que retorne las palabras de una lista que
# comiencen con una letra en específico. Usa la función filter().

def palabras_por_letra(lista_palabras, letra):
    pass


# EJERCICIO 15
# Crea una función lambda que sume 3 a cada número de una lista dada.

sumar_tres = lambda lista: None


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
    print("Hola Antonio")