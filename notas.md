# Notas del Proyecto 3 - Katas Python

## Ejercicio 8
- Usa `input()` para pedir dos números.
- Convierte con `float()` para aceptar decimales.
- Hay dos errores a controlar:
  - `ValueError` si el usuario escribe texto
  - `ZeroDivisionError` si divide entre 0
- Mejor probarlo manualmente.

## Ejercicio 10
- Excepción personalizada
- `ListaVaciaError` hereda de `Exception`.
- Se usa `raise ListaVaciaError(...)` cuando la lista está vacía.
- Luego se puede manejar con `try/except` al probar la función.

## Ejercicio 11
- Similar al 8 porque usa `input()` y `try/except`.
- Además valida que la edad esté entre 0 y 120.
- Aunque el usuario escriba un número, si está fuera de rango también debe dar error.

## Ejercicio 13
- Hay que evitar letras repetidas.
- Se usa `set(caracteres)` para quitar duplicados.
- Luego se transforma cada letra en una tupla:
  - mayúscula
  - minúscula

## Ejercicio 16
- Se usa `filter()` para quedarnos solo con las palabras cuya longitud sea mayor que `n`.
- Primero se separa el texto con `split()`.

## Ejercicio 17
- Usa `reduce()`.
- La lógica es ir construyendo el número así:
  - acumulado * 10 + dígito

## Ejercicio 18
- Se usa `filter()` sobre una lista de diccionarios.
- La condición es que `calificacion >= 90`.
- Hay que acceder a la clave del diccionario correctamente.

## Ejercicio 19
- Es una lambda que filtra impares.
- Un número es impar si `numero % 2 != 0`.

## Ejercicio 20
- Se usa `isinstance(elemento, int)` para comprobar si un valor es entero.
- La lista puede mezclar strings, floats y enteros.

## Recordatorio general
- Los `print` de prueba van al final, dentro de `if __name__ == "__main__":`
- Los ejercicios con `input()` es mejor probarlos manualmente.