"""
Ejemplos de List Comprehensions y Generadores
"""

# ============================================
# LIST COMPREHENSIONS
# ============================================

# Ejemplo básico: cuadrados de números
cuadrados = [x**2 for x in range(10)]
print("Cuadrados:", cuadrados)

# Con condición: solo números pares
pares = [x for x in range(20) if x % 2 == 0]
print("Pares:", pares)

# Transformación de strings
palabras = ["python", "java", "javascript"]
mayusculas = [palabra.upper() for palabra in palabras]
print("Mayúsculas:", mayusculas)

# List comprehension anidada (matriz)
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz 3x3:")
for fila in matriz:
    print(fila)

# ============================================
# DICT COMPREHENSIONS
# ============================================

# Crear diccionario de cuadrados
cuadrados_dict = {x: x**2 for x in range(6)}
print("\nDiccionario de cuadrados:", cuadrados_dict)

# Invertir un diccionario
original = {"a": 1, "b": 2, "c": 3}
invertido = {v: k for k, v in original.items()}
print("Diccionario invertido:", invertido)

# Con condición
numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
pares_dict = {k: v for k, v in numeros.items() if v % 2 == 0}
print("Solo pares:", pares_dict)

# ============================================
# SET COMPREHENSIONS
# ============================================

# Conjunto de longitudes únicas
palabras = ["hola", "mundo", "python", "code"]
longitudes = {len(palabra) for palabra in palabras}
print("\nLongitudes únicas:", longitudes)

# ============================================
# GENERATOR EXPRESSIONS
# ============================================

# Generator expression (similar a list comprehension pero con paréntesis)
gen = (x**2 for x in range(10))
print("\nGenerador:", gen)
print("Primeros 3 valores:", [next(gen) for _ in range(3)])

# Comparación de memoria
import sys
lista = [x**2 for x in range(1000)]
generador = (x**2 for x in range(1000))
print(f"\nTamaño de lista: {sys.getsizeof(lista)} bytes")
print(f"Tamaño de generador: {sys.getsizeof(generador)} bytes")

# ============================================
# FUNCIONES GENERADORAS
# ============================================

def fibonacci(n):
    """Generador de números Fibonacci"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\nPrimeros 10 números Fibonacci:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# Generador infinito
def contador(inicio=0):
    """Generador infinito que cuenta desde un número inicial"""
    num = inicio
    while True:
        yield num
        num += 1

# Usar con itertools.islice para limitar
from itertools import islice
print("\nPrimeros 5 números del contador:")
for num in islice(contador(100), 5):
    print(num, end=" ")
print()

# ============================================
# PIPELINE DE GENERADORES
# ============================================

def leer_numeros():
    """Simula lectura de números"""
    for i in range(100):
        yield i

def filtrar_pares(numeros):
    """Filtra solo números pares"""
    for num in numeros:
        if num % 2 == 0:
            yield num

def cuadrados(numeros):
    """Calcula cuadrados"""
    for num in numeros:
        yield num ** 2

# Pipeline eficiente
pipeline = cuadrados(filtrar_pares(leer_numeros()))
primeros_5 = list(islice(pipeline, 5))
print("\nPrimeros 5 cuadrados de pares:", primeros_5)

# ============================================
# EXPRESIONES COMPLEJAS
# ============================================

# Aplanar lista de listas
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [item for sublista in lista_anidada for item in sublista]
print("\nLista aplanada:", aplanada)

# Combinaciones
colores = ["rojo", "azul"]
objetos = ["auto", "casa"]
combinaciones = [f"{color} {objeto}" for color in colores for objeto in objetos]
print("Combinaciones:", combinaciones)
