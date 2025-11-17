"""
Ejercicios de List Comprehensions y Generadores
"""

# Ejercicio 1: Filtrar números
# Crea una list comprehension que genere una lista de números del 1 al 50
# que sean divisibles por 3 o por 5
def ejercicio_1():
    # Tu código aquí
    pass

# Ejercicio 2: Diccionario de caracteres
# Dada una cadena, crea un diccionario donde las claves sean los caracteres
# únicos y los valores sean el número de veces que aparece cada carácter
def ejercicio_2(cadena):
    # Tu código aquí
    pass

# Ejercicio 3: Transponer matriz
# Dada una matriz (lista de listas), transponla usando list comprehensions
def ejercicio_3(matriz):
    # Tu código aquí
    # Ejemplo: [[1,2,3], [4,5,6]] -> [[1,4], [2,5], [3,6]]
    pass

# Ejercicio 4: Generador de primos
# Crea una función generadora que produzca números primos
def generador_primos(limite):
    # Tu código aquí
    pass

# Ejercicio 5: Validar emails
# Dada una lista de strings, filtra solo los que parezcan emails válidos
# (contienen @ y .)
def ejercicio_5(lista_emails):
    # Tu código aquí
    pass

# Ejercicio 6: Fibonacci con generador
# Crea un generador que produzca números Fibonacci menores a un límite dado
def fibonacci_hasta(limite):
    # Tu código aquí
    pass

# Ejercicio 7: Aplanar lista anidada de cualquier profundidad
# Crea una función que aplane una lista anidada de cualquier nivel
def aplanar(lista):
    # Tu código aquí (puede usar recursión)
    pass

# Ejercicio 8: Generar todas las combinaciones
# Dados dos listas, genera todas las tuplas posibles
def ejercicio_8(lista1, lista2):
    # Tu código aquí
    # Ejemplo: [1,2], ['a','b'] -> [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
    pass

# Ejercicio 9: Set comprehension con palabras
# Dada una lista de palabras, crea un set con todas las letras únicas
def ejercicio_9(palabras):
    # Tu código aquí
    pass

# Ejercicio 10: Pipeline de procesamiento
# Crea un pipeline de generadores que:
# 1. Lea números del 1 al 1000
# 2. Filtre solo los múltiplos de 7
# 3. Calcule su raíz cuadrada
# 4. Retorne solo los primeros 10
def ejercicio_10():
    # Tu código aquí
    pass

# Tests básicos
if __name__ == "__main__":
    print("Ejecuta cada ejercicio y verifica los resultados")
    print("Ejemplo de solución para ejercicio 1:")
    solucion_1 = [x for x in range(1, 51) if x % 3 == 0 or x % 5 == 0]
    print(solucion_1)
