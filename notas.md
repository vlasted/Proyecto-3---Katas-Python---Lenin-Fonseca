# Notas del Proyecto 3 - Katas Python

## Ejercicio 8
- Usa `input()` para pedir dos números.
- Convierte con `float()` para aceptar decimales.
- Hay dos errores a controlar:
  - `ValueError` si el usuario escribe texto
  - `ZeroDivisionError` si divide entre 0
- Mejor probarlo manualmente, no dejarlo ejecutándose siempre al correr el archivo.

## Ejercicio 10
- Aquí aparece la excepción personalizada.
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

## Recordatorio general
- Los `print` de prueba van al final, dentro de `if __name__ == "__main__":`
- Los ejercicios con `input()` es mejor probarlos manualmente.