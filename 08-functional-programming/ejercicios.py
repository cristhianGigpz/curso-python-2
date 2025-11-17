"""
Ejercicios de Programación Funcional
"""

from functools import reduce
from itertools import combinations, permutations

# Ejercicio 1: Implementar map sin usar map()
def mi_map(funcion, iterable):
    # Tu código aquí
    pass

# Ejercicio 2: Implementar filter sin usar filter()
def mi_filter(predicado, iterable):
    # Tu código aquí
    pass

# Ejercicio 3: Implementar reduce sin usar reduce()
def mi_reduce(funcion, iterable, inicial=None):
    # Tu código aquí
    pass

# Ejercicio 4: Flatten (aplanar) lista anidada usando reduce
def flatten(lista_anidada):
    # Ejemplo: [[1,2], [3,4], [5]] -> [1,2,3,4,5]
    # Usa reduce
    pass

# Ejercicio 5: Implementar composición de funciones
def compose(*funciones):
    # Debe retornar una función que aplique todas las funciones
    # de derecha a izquierda
    pass

# Ejercicio 6: Crear un decorador de memoización
def memoize(func):
    # Implementa tu propia versión de lru_cache
    pass

# Ejercicio 7: Pipeline de procesamiento de datos
# Dado una lista de diccionarios de productos, crea un pipeline que:
# 1. Filtre productos con precio > 100
# 2. Aplique 10% de descuento
# 3. Ordene por precio
# 4. Retorne solo nombres y precios
def procesar_productos(productos):
    # Tu código aquí
    pass

# Ejercicio 8: Implementar curry
def curry(func):
    # Transforma función de n argumentos en n funciones de 1 argumento
    # Ejemplo: suma(a,b,c) -> suma(a)(b)(c)
    pass

# Ejercicio 9: Generador infinito de Fibonacci
def fibonacci_infinito():
    # Generador que produce números Fibonacci indefinidamente
    pass

# Ejercicio 10: Validador funcional
# Crea un sistema de validación usando composición de funciones
def crear_validador(*validaciones):
    # Cada validación es una función que retorna True/False
    # El validador debe aplicar todas las validaciones
    pass

# Ejercicio 11: Transposición de matriz usando zip
def transponer(matriz):
    # [[1,2,3], [4,5,6]] -> [[1,4], [2,5], [3,6]]
    pass

# Ejercicio 12: Implementar groupBy
def agrupar_por(iterable, key_func):
    # Agrupa elementos según el resultado de key_func
    # Retorna diccionario
    pass

# Ejercicio 13: Partición de lista
def partir(predicado, iterable):
    # Divide iterable en dos listas: las que cumplen y las que no
    # Retorna tupla (cumple, no_cumple)
    pass

# Ejercicio 14: Implementar take y drop
def take(n, iterable):
    # Toma los primeros n elementos
    pass

def drop(n, iterable):
    # Omite los primeros n elementos
    pass

# Ejercicio 15: Calculadora funcional
# Crea una calculadora que use solo funciones puras
class CalculadoraFuncional:
    # Todas las operaciones deben ser funciones puras
    # No debe mantener estado
    pass

# Tests
if __name__ == "__main__":
    print("Implementa los ejercicios y prueba aquí")
    
    # Ejemplo test
    # numeros = [1, 2, 3, 4, 5]
    # cuadrados = list(mi_map(lambda x: x**2, numeros))
    # print(f"Cuadrados: {cuadrados}")
