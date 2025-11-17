"""
Ejemplos de Decoradores en Python
"""

import time
import functools
from typing import Callable

# ============================================
# DECORADOR BÁSICO
# ============================================

def mi_decorador(func):
    """Decorador básico que envuelve una función"""
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

print("=== Decorador Básico ===")
saludar()

# ============================================
# DECORADOR CON ARGUMENTOS
# ============================================

def decorador_con_args(func):
    """Decorador que acepta funciones con argumentos"""
    def wrapper(*args, **kwargs):
        print(f"Argumentos: {args}, {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@decorador_con_args
def sumar(a, b):
    return a + b

print("\n=== Decorador con Argumentos ===")
sumar(5, 3)

# ============================================
# DECORADOR QUE MIDE TIEMPO
# ============================================

def medir_tiempo(func):
    """Decorador que mide el tiempo de ejecución"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def calcular_factorial(n):
    """Calcula el factorial de n"""
    if n <= 1:
        return 1
    return n * calcular_factorial(n - 1)

print("\n=== Medir Tiempo ===")
calcular_factorial(10)

# ============================================
# DECORADOR CON PARÁMETROS
# ============================================

def repetir(veces):
    """Decorador que repite la ejecución n veces"""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resultados = []
            for _ in range(veces):
                resultado = func(*args, **kwargs)
                resultados.append(resultado)
            return resultados
        return wrapper
    return decorador

@repetir(3)
def generar_numero():
    import random
    return random.randint(1, 10)

print("\n=== Decorador con Parámetros ===")
print("Números generados:", generar_numero())

# ============================================
# DECORADOR DE CACHÉ (MEMOIZACIÓN)
# ============================================

def cache(func):
    """Decorador simple de caché"""
    memo = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(*args)
            print(f"Calculando {func.__name__}{args}")
        else:
            print(f"Usando caché para {args}")
        return memo[args]
    return wrapper

@cache
def fibonacci(n):
    """Calcula el n-ésimo número de Fibonacci"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n=== Caché/Memoización ===")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(5) = {fibonacci(5)}")  # Segunda vez usa caché

# ============================================
# DECORADOR DE VALIDACIÓN
# ============================================

def validar_positivo(func):
    """Valida que los argumentos sean positivos"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"El argumento debe ser positivo, recibido: {arg}")
        return func(*args, **kwargs)
    return wrapper

@validar_positivo
def raiz_cuadrada(n):
    return n ** 0.5

print("\n=== Validación ===")
print(f"Raíz de 16: {raiz_cuadrada(16)}")
try:
    raiz_cuadrada(-4)
except ValueError as e:
    print(f"Error: {e}")

# ============================================
# DECORADORES APILADOS
# ============================================

def hacer_mayusculas(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado.upper()
    return wrapper

def agregar_signos(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return f"¡¡¡ {resultado} !!!"
    return wrapper

@agregar_signos
@hacer_mayusculas
def obtener_mensaje():
    return "hola mundo"

print("\n=== Decoradores Apilados ===")
print(obtener_mensaje())

# ============================================
# DECORADOR DE CLASE
# ============================================

def singleton(cls):
    """Decorador que convierte una clase en singleton"""
    instancias = {}
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Creando conexión a base de datos")
        self.connected = True

print("\n=== Singleton ===")
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"db1 es db2: {db1 is db2}")

# ============================================
# USO DE FUNCTOOLS.LRU_CACHE
# ============================================

@functools.lru_cache(maxsize=128)
def fibonacci_optimizado(n):
    """Fibonacci con caché automático de Python"""
    if n < 2:
        return n
    return fibonacci_optimizado(n - 1) + fibonacci_optimizado(n - 2)

print("\n=== LRU Cache ===")
print(f"fibonacci(30) = {fibonacci_optimizado(30)}")
print(f"Cache info: {fibonacci_optimizado.cache_info()}")

# ============================================
# DECORADOR DE LOGGING
# ============================================

def log_llamadas(func):
    """Registra cada llamada a la función"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Llamando a {func.__name__}({signature})")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__!r} retornó {resultado!r}")
        return resultado
    return wrapper

@log_llamadas
def multiplicar(a, b):
    return a * b

print("\n=== Logging ===")
multiplicar(3, 4)

# ============================================
# DECORADOR DE RETRY
# ============================================

def retry(max_intentos=3, delay=1):
    """Reintenta la función en caso de excepción"""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(max_intentos):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if intento == max_intentos - 1:
                        raise
                    print(f"Intento {intento + 1} falló: {e}. Reintentando...")
                    time.sleep(delay)
        return wrapper
    return decorador

@retry(max_intentos=3, delay=0.5)
def operacion_inestable():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Conexión fallida")
    return "¡Éxito!"

print("\n=== Retry ===")
try:
    resultado = operacion_inestable()
    print(resultado)
except ConnectionError as e:
    print(f"Falló después de todos los intentos: {e}")
