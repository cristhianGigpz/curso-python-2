"""
Ejemplos de Programación Funcional
"""

from functools import reduce, partial, lru_cache
from itertools import chain, combinations, permutations, cycle, islice, groupby
from operator import add, mul, itemgetter
import operator

# ============================================
# FUNCIONES LAMBDA
# ============================================

print("=== Funciones Lambda ===")
# Lambda básica
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# Lambda con múltiples argumentos
suma = lambda x, y: x + y
print(f"Suma de 3 y 4: {suma(3, 4)}")

# Lambda en lista
operaciones = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]
valor = 5
for op in operaciones:
    valor = op(valor)
print(f"Resultado de aplicar operaciones: {valor}")
print()

# ============================================
# MAP
# ============================================

print("=== Map ===")
numeros = [1, 2, 3, 4, 5]

# Cuadrados con map
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrados: {cuadrados}")

# Map con función definida
def duplicar(x):
    return x * 2

duplicados = list(map(duplicar, numeros))
print(f"Duplicados: {duplicados}")

# Map con múltiples iterables
a = [1, 2, 3]
b = [10, 20, 30]
sumas = list(map(lambda x, y: x + y, a, b))
print(f"Sumas: {sumas}")
print()

# ============================================
# FILTER
# ============================================

print("=== Filter ===")
numeros = range(1, 11)

# Filtrar pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")

# Filtrar mayores que 5
mayores = list(filter(lambda x: x > 5, numeros))
print(f"Mayores que 5: {mayores}")

# Filtrar con función
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = list(filter(es_primo, range(2, 20)))
print(f"Primos: {primos}")
print()

# ============================================
# REDUCE
# ============================================

print("=== Reduce ===")
numeros = [1, 2, 3, 4, 5]

# Suma de todos
suma = reduce(lambda x, y: x + y, numeros)
print(f"Suma total: {suma}")

# Producto de todos
producto = reduce(lambda x, y: x * y, numeros)
print(f"Producto: {producto}")

# Máximo
maximo = reduce(lambda x, y: x if x > y else y, numeros)
print(f"Máximo: {maximo}")

# Con valor inicial
suma_con_inicial = reduce(lambda x, y: x + y, numeros, 100)
print(f"Suma con inicial 100: {suma_con_inicial}")
print()

# ============================================
# FUNCIONES PURAS
# ============================================

print("=== Funciones Puras ===")

# Función pura: mismo input = mismo output, sin efectos secundarios
def suma_pura(a, b):
    return a + b

print(f"Suma pura: {suma_pura(3, 4)}")

# Función NO pura (modifica estado externo)
lista_externa = []

def agregar_impuro(item):
    lista_externa.append(item)  # Efecto secundario
    return lista_externa

# Versión pura
def agregar_puro(lista, item):
    return lista + [item]  # Retorna nueva lista

lista = [1, 2, 3]
nueva_lista = agregar_puro(lista, 4)
print(f"Lista original: {lista}")
print(f"Nueva lista: {nueva_lista}")
print()

# ============================================
# INMUTABILIDAD
# ============================================

print("=== Inmutabilidad ===")

# Usar tuplas en lugar de listas
coordenadas = (10, 20)
# coordenadas[0] = 15  # Error: no se puede modificar

# Crear nuevos objetos en lugar de modificar
numeros = (1, 2, 3)
nuevos_numeros = numeros + (4, 5)
print(f"Números inmutables: {nuevos_numeros}")

# namedtuple para estructuras inmutables
from collections import namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
p1 = Punto(10, 20)
p2 = Punto(30, 40)
print(f"Puntos inmutables: {p1}, {p2}")
print()

# ============================================
# COMPOSICIÓN DE FUNCIONES
# ============================================

print("=== Composición de Funciones ===")

def componer(*funciones):
    """Compone múltiples funciones"""
    def composicion(x):
        for f in reversed(funciones):
            x = f(x)
        return x
    return composicion

# Funciones simples
def agregar_uno(x):
    return x + 1

def multiplicar_por_dos(x):
    return x * 2

def elevar_al_cuadrado(x):
    return x ** 2

# Componer funciones
operacion = componer(elevar_al_cuadrado, multiplicar_por_dos, agregar_uno)
resultado = operacion(3)  # ((3 + 1) * 2) ** 2
print(f"Composición: {resultado}")
print()

# ============================================
# PARTIAL - APLICACIÓN PARCIAL
# ============================================

print("=== Partial (Aplicación Parcial) ===")

def potencia(base, exponente):
    return base ** exponente

# Crear funciones especializadas
cuadrado_func = partial(potencia, exponente=2)
cubo_func = partial(potencia, exponente=3)

print(f"Cuadrado de 5: {cuadrado_func(5)}")
print(f"Cubo de 5: {cubo_func(5)}")

# Partial con múltiples argumentos
def multiplicar(a, b, c):
    return a * b * c

multiplicar_por_2 = partial(multiplicar, 2)
print(f"2 * 3 * 4 = {multiplicar_por_2(3, 4)}")
print()

# ============================================
# LRU_CACHE - MEMOIZACIÓN
# ============================================

print("=== LRU Cache (Memoización) ===")

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Fibonacci(50): {fibonacci(50)}")
print(f"Cache info: {fibonacci.cache_info()}")
print()

# ============================================
# ITERTOOLS
# ============================================

print("=== Itertools ===")

# chain - concatenar iterables
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenado = list(chain(lista1, lista2))
print(f"Chain: {concatenado}")

# combinations - combinaciones
combinaciones = list(combinations([1, 2, 3, 4], 2))
print(f"Combinaciones de 2: {combinaciones}")

# permutations - permutaciones
permutaciones = list(permutations([1, 2, 3], 2))
print(f"Permutaciones de 2: {permutaciones}")

# cycle - ciclo infinito
ciclo = cycle([1, 2, 3])
primeros_10 = list(islice(ciclo, 10))
print(f"Primeros 10 del ciclo: {primeros_10}")

# groupby - agrupar elementos
datos = [
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Bob', 'edad': 25},
    {'nombre': 'Carlos', 'edad': 30},
]
for edad, grupo in groupby(datos, key=itemgetter('edad')):
    print(f"Edad {edad}: {list(grupo)}")
print()

# ============================================
# OPERATOR MODULE
# ============================================

print("=== Operator Module ===")

# Usar funciones de operadores
numeros = [1, 2, 3, 4, 5]
suma = reduce(add, numeros)
producto = reduce(mul, numeros)
print(f"Suma con operator.add: {suma}")
print(f"Producto con operator.mul: {producto}")

# itemgetter para acceder a elementos
personas = [
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Bob', 'edad': 30},
    {'nombre': 'Carlos', 'edad': 20}
]
ordenados = sorted(personas, key=itemgetter('edad'))
print(f"Ordenados por edad: {ordenados}")
print()

# ============================================
# CLOSURES
# ============================================

print("=== Closures ===")

def crear_multiplicador(factor):
    """Retorna una función que multiplica por factor"""
    def multiplicar(x):
        return x * factor
    return multiplicar

duplicar = crear_multiplicador(2)
triplicar = crear_multiplicador(3)

print(f"Duplicar 5: {duplicar(5)}")
print(f"Triplicar 5: {triplicar(5)}")

# Closure con estado
def contador():
    count = 0
    def incrementar():
        nonlocal count
        count += 1
        return count
    return incrementar

c1 = contador()
print(f"Contador: {c1()}, {c1()}, {c1()}")
print()

# ============================================
# RECURSIÓN
# ============================================

print("=== Recursión ===")

def factorial(n):
    """Factorial recursivo"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial de 5: {factorial(5)}")

# Recursión con tail call (simulado)
def suma_recursiva(numeros, acumulador=0):
    if not numeros:
        return acumulador
    return suma_recursiva(numeros[1:], acumulador + numeros[0])

print(f"Suma recursiva: {suma_recursiva([1, 2, 3, 4, 5])}")
print()

# ============================================
# PIPELINE FUNCIONAL
# ============================================

print("=== Pipeline Funcional ===")

def pipeline(valor, *funciones):
    """Aplica secuencia de funciones"""
    for funcion in funciones:
        valor = funcion(valor)
    return valor

# Procesar datos funcionalmente
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = pipeline(
    datos,
    lambda x: filter(lambda n: n % 2 == 0, x),  # Filtrar pares
    lambda x: map(lambda n: n ** 2, x),          # Elevar al cuadrado
    lambda x: list(x)                             # Convertir a lista
)
print(f"Pipeline: {resultado}")
print()

# ============================================
# ALL Y ANY
# ============================================

print("=== All y Any ===")

numeros = [2, 4, 6, 8, 10]
print(f"¿Todos pares?: {all(n % 2 == 0 for n in numeros)}")

numeros = [1, 3, 5, 6, 7]
print(f"¿Alguno par?: {any(n % 2 == 0 for n in numeros)}")
print()

# ============================================
# ZIP
# ============================================

print("=== Zip ===")

nombres = ['Ana', 'Bob', 'Carlos']
edades = [25, 30, 35]
ciudades = ['Madrid', 'Barcelona', 'Valencia']

personas = list(zip(nombres, edades, ciudades))
print(f"Personas: {personas}")

# Desempaquetar con zip
pares = [(1, 2), (3, 4), (5, 6)]
x, y = zip(*pares)
print(f"Desempaquetado: x={x}, y={y}")
