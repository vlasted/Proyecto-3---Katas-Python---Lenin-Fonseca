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

if __name__ == "__main__":
    print("Hola Antonio.")