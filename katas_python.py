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


# EXCEPCIÓN PERSONALIZADA

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    pass


# CLASE ÁRBOL

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        pass

    def nueva_rama(self):
        pass

    def crecer_ramas(self):
        pass

    def quitar_rama(self, posicion):
        pass

    def info_arbol(self):
        pass


# CLASE USUARIOBANCO

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        pass

    def transferir_dinero(self, otro_usuario, cantidad):
        pass

    def agregar_dinero(self, cantidad):
        pass


# FUNCIÓN PROCESAR TEXTO

def contar_palabras(texto):
    pass


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    pass


def eliminar_palabra(texto, palabra):
    pass


def procesar_texto(texto, opcion, *args):
    pass


if __name__ == "__main__":
    print("Base del Proyecto 3 preparada correctamente.")