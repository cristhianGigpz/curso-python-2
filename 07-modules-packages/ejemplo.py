"""
Ejemplos de Módulos y Paquetes
"""

import sys
import os
from pathlib import Path

# ============================================
# INFORMACIÓN DEL MÓDULO
# ============================================

print("=== Información del Módulo ===")
print(f"Nombre del módulo: {__name__}")
print(f"Archivo: {__file__}")
print()

# ============================================
# MÓDULOS BUILT-IN
# ============================================

# OS - Sistema Operativo
print("=== Módulo OS ===")
import os
print(f"Directorio actual: {os.getcwd()}")
print(f"Variables de entorno PATH: {os.environ.get('PATH', 'N/A')[:50]}...")
print()

# SYS - Sistema Python
print("=== Módulo SYS ===")
import sys
print(f"Versión de Python: {sys.version}")
print(f"Plataforma: {sys.platform}")
print(f"Path de módulos (primeros 3): {sys.path[:3]}")
print()

# DATETIME
print("=== Módulo Datetime ===")
from datetime import datetime, timedelta
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Fecha formateada: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")
manana = ahora + timedelta(days=1)
print(f"Mañana: {manana.strftime('%d/%m/%Y')}")
print()

# MATH
print("=== Módulo Math ===")
import math
print(f"Pi: {math.pi}")
print(f"e: {math.e}")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Seno de 90°: {math.sin(math.radians(90))}")
print()

# RANDOM
print("=== Módulo Random ===")
import random
print(f"Número aleatorio: {random.random()}")
print(f"Entero aleatorio (1-10): {random.randint(1, 10)}")
lista = [1, 2, 3, 4, 5]
print(f"Elemento aleatorio: {random.choice(lista)}")
random.shuffle(lista)
print(f"Lista mezclada: {lista}")
print()

# COLLECTIONS
print("=== Módulo Collections ===")
from collections import Counter, defaultdict, namedtuple
# Counter
palabras = "hola mundo hola python mundo mundo".split()
conteo = Counter(palabras)
print(f"Conteo de palabras: {conteo}")
print(f"Más comunes: {conteo.most_common(2)}")

# defaultdict
dd = defaultdict(list)
dd['frutas'].append('manzana')
dd['frutas'].append('banana')
print(f"defaultdict: {dict(dd)}")

# namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(10, 20)
print(f"Punto: {p}, x={p.x}, y={p.y}")
print()

# ============================================
# CREAR MÓDULO PROPIO
# ============================================

print("=== Crear Módulo Propio ===")
# Creamos un módulo temporal
modulo_path = Path('/tmp/mi_modulo.py')
modulo_path.write_text('''
"""Mi módulo de ejemplo"""

def saludar(nombre):
    """Saluda a una persona"""
    return f"Hola, {nombre}!"

def sumar(a, b):
    """Suma dos números"""
    return a + b

PI = 3.14159

class MiClase:
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return f"MiClase({self.valor})"
''')

# Agregar el directorio al path para importar
if '/tmp' not in sys.path:
    sys.path.insert(0, '/tmp')

# Importar y usar el módulo
import mi_modulo
print(f"Saludar: {mi_modulo.saludar('Python')}")
print(f"Sumar: {mi_modulo.sumar(5, 3)}")
print(f"PI: {mi_modulo.PI}")
obj = mi_modulo.MiClase(42)
print(f"Objeto: {obj}")
print()

# ============================================
# CREAR PAQUETE
# ============================================

print("=== Crear Paquete ===")
# Crear estructura de paquete
paquete_dir = Path('/tmp/mi_paquete')
paquete_dir.mkdir(exist_ok=True)

# __init__.py
(paquete_dir / '__init__.py').write_text('''
"""Mi paquete de ejemplo"""
__version__ = '1.0.0'
__all__ = ['utilidades', 'matematicas']

from .utilidades import formatear_texto
from .matematicas import factorial
''')

# modulo utilidades
(paquete_dir / 'utilidades.py').write_text('''
"""Módulo de utilidades"""

def formatear_texto(texto):
    """Formatea texto a título"""
    return texto.title()

def contar_vocales(texto):
    """Cuenta vocales en texto"""
    vocales = 'aeiouáéíóú'
    return sum(1 for c in texto.lower() if c in vocales)
''')

# modulo matematicas
(paquete_dir / 'matematicas.py').write_text('''
"""Módulo matemático"""

def factorial(n):
    """Calcula factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def es_primo(n):
    """Verifica si es primo"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
''')

# Importar y usar el paquete
import mi_paquete
print(f"Versión del paquete: {mi_paquete.__version__}")
print(f"Formatear texto: {mi_paquete.formatear_texto('hola mundo')}")
print(f"Factorial de 5: {mi_paquete.factorial(5)}")

# Importar módulos específicos
from mi_paquete.utilidades import contar_vocales
from mi_paquete.matematicas import es_primo
print(f"Vocales en 'python': {contar_vocales('python')}")
print(f"¿7 es primo?: {es_primo(7)}")
print()

# ============================================
# SUBPAQUETES
# ============================================

print("=== Subpaquetes ===")
# Crear subpaquete
subpaquete_dir = paquete_dir / 'avanzado'
subpaquete_dir.mkdir(exist_ok=True)

(subpaquete_dir / '__init__.py').write_text('''
"""Subpaquete avanzado"""
from .estadisticas import promedio
''')

(subpaquete_dir / 'estadisticas.py').write_text('''
"""Módulo de estadísticas"""

def promedio(numeros):
    """Calcula el promedio"""
    return sum(numeros) / len(numeros) if numeros else 0

def mediana(numeros):
    """Calcula la mediana"""
    sorted_nums = sorted(numeros)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]
''')

# Usar subpaquete
from mi_paquete.avanzado import promedio
from mi_paquete.avanzado.estadisticas import mediana
numeros = [1, 2, 3, 4, 5]
print(f"Promedio: {promedio(numeros)}")
print(f"Mediana: {mediana(numeros)}")
print()

# ============================================
# __name__ == "__main__"
# ============================================

print("=== Patrón __name__ == '__main__' ===")
modulo_ejecutable = Path('/tmp/ejecutable.py')
modulo_ejecutable.write_text('''
def main():
    print("Función principal")

if __name__ == "__main__":
    print("Ejecutando como script principal")
    main()
else:
    print("Importado como módulo")
''')

# Cuando se importa, no ejecuta el bloque if
import importlib.util
spec = importlib.util.spec_from_file_location("ejecutable", "/tmp/ejecutable.py")
ejecutable = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ejecutable)
print()

# ============================================
# DIR() - EXPLORAR MÓDULOS
# ============================================

print("=== Explorar Módulo con dir() ===")
import math
print(f"Primeras 10 funciones de math: {dir(math)[:10]}")
print()

# ============================================
# IMPORTLIB - IMPORTACIÓN DINÁMICA
# ============================================

print("=== Importación Dinámica ===")
import importlib

# Importar módulo dinámicamente
nombre_modulo = "datetime"
modulo = importlib.import_module(nombre_modulo)
print(f"Módulo importado: {modulo.__name__}")
print(f"Fecha actual: {modulo.datetime.now().strftime('%Y-%m-%d')}")
print()

# ============================================
# RELOAD DE MÓDULOS
# ============================================

print("=== Reload de Módulos ===")
# Modificar módulo
modulo_path.write_text('''
def saludar(nombre):
    return f"¡Hola, {nombre}! Versión 2"
''')

# Recargar
importlib.reload(mi_modulo)
print(f"Después de reload: {mi_modulo.saludar('Python')}")
