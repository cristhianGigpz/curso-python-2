"""
Ejemplos de Context Managers en Python
"""

import time
from contextlib import contextmanager
import os

# ============================================
# CONTEXT MANAGER CON CLASE
# ============================================

class GestorArchivo:
    """Context manager básico para manejo de archivos"""
    
    def __init__(self, nombre_archivo, modo):
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        print(f"Abriendo archivo: {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, self.modo)
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Cerrando archivo: {self.nombre_archivo}")
        if self.archivo:
            self.archivo.close()
        # Retornar False propaga la excepción, True la suprime
        return False

print("=== Context Manager con Clase ===")
with GestorArchivo('/tmp/test.txt', 'w') as f:
    f.write("Hola desde context manager\n")
print("Archivo cerrado automáticamente\n")

# ============================================
# CONTEXT MANAGER CON CONTEXTMANAGER
# ============================================

@contextmanager
def temporizador(nombre):
    """Mide el tiempo de ejecución de un bloque"""
    print(f"Iniciando: {nombre}")
    inicio = time.time()
    try:
        yield
    finally:
        fin = time.time()
        print(f"Finalizando: {nombre}")
        print(f"Tiempo transcurrido: {fin - inicio:.4f} segundos")

print("=== Context Manager con @contextmanager ===")
with temporizador("Operación lenta"):
    time.sleep(0.5)
    print("Procesando...")
print()

# ============================================
# CONTEXT MANAGER PARA CAMBIAR DIRECTORIO
# ============================================

@contextmanager
def cambiar_directorio(nuevo_dir):
    """Cambia temporalmente el directorio de trabajo"""
    directorio_actual = os.getcwd()
    print(f"Directorio actual: {directorio_actual}")
    print(f"Cambiando a: {nuevo_dir}")
    try:
        os.chdir(nuevo_dir)
        yield
    finally:
        print(f"Volviendo a: {directorio_actual}")
        os.chdir(directorio_actual)

print("=== Cambiar Directorio ===")
with cambiar_directorio('/tmp'):
    print(f"Dentro del context: {os.getcwd()}")
print(f"Fuera del context: {os.getcwd()}\n")

# ============================================
# CONTEXT MANAGER PARA MANEJO DE EXCEPCIONES
# ============================================

class ManejadorExcepciones:
    """Context manager que maneja excepciones específicas"""
    
    def __init__(self, *excepciones):
        self.excepciones = excepciones
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if issubclass(exc_type, self.excepciones):
                print(f"Excepción capturada: {exc_type.__name__}: {exc_val}")
                return True  # Suprime la excepción
        return False

print("=== Manejo de Excepciones ===")
with ManejadorExcepciones(ValueError, TypeError):
    print("Intentando operación...")
    int("no es un número")  # Esto lanzará ValueError
print("Continuando después de la excepción\n")

# ============================================
# CONTEXT MANAGER PARA BASE DE DATOS (SIMULADO)
# ============================================

class ConexionDB:
    """Simula una conexión a base de datos con transacciones"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
        self.transaction = False
    
    def __enter__(self):
        print(f"Conectando a {self.db_name}")
        self.connected = True
        print("Iniciando transacción")
        self.transaction = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Commit de transacción")
        else:
            print("Rollback de transacción")
        print(f"Cerrando conexión a {self.db_name}")
        self.connected = False
        self.transaction = False
        return False
    
    def ejecutar(self, query):
        if not self.connected:
            raise RuntimeError("No hay conexión a la base de datos")
        print(f"Ejecutando: {query}")

print("=== Conexión a Base de Datos ===")
with ConexionDB("mi_base_datos") as db:
    db.ejecutar("INSERT INTO usuarios VALUES ('Juan')")
    db.ejecutar("UPDATE usuarios SET nombre='Pedro'")
print()

# ============================================
# CONTEXT MANAGER ANIDADO
# ============================================

@contextmanager
def recursos_multiples(*recursos):
    """Maneja múltiples recursos"""
    gestores = []
    try:
        for recurso in recursos:
            gestor = recurso.__enter__()
            gestores.append((recurso, gestor))
        yield [g for _, g in gestores]
    finally:
        for recurso, _ in reversed(gestores):
            recurso.__exit__(None, None, None)

print("=== Context Managers Anidados ===")
with recursos_multiples(
    GestorArchivo('/tmp/file1.txt', 'w'),
    GestorArchivo('/tmp/file2.txt', 'w')
) as (f1, f2):
    f1.write("Contenido archivo 1\n")
    f2.write("Contenido archivo 2\n")
print()

# ============================================
# CONTEXT MANAGER PARA SUPRIMIR SALIDA
# ============================================

@contextmanager
def suprimir_salida():
    """Suprime la salida estándar temporalmente"""
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield
    finally:
        sys.stdout = old_stdout

print("=== Suprimir Salida ===")
print("Esto se verá")
with suprimir_salida():
    print("Esto NO se verá")
    print("Tampoco esto")
print("Esto se verá nuevamente\n")

# ============================================
# CONTEXT MANAGER PARA MEDIR MEMORIA
# ============================================

@contextmanager
def medir_memoria(nombre):
    """Mide el uso de memoria de un bloque (simplificado)"""
    import sys
    print(f"Iniciando medición de memoria: {nombre}")
    # En un caso real usarías tracemalloc o psutil
    inicio = 0  # Simplificado
    try:
        yield
    finally:
        fin = 0  # Simplificado
        print(f"Medición completada: {nombre}")

print("=== Medir Memoria ===")
with medir_memoria("Creación de lista grande"):
    lista = [i for i in range(10000)]
print()

# ============================================
# CONTEXT MANAGER REUTILIZABLE
# ============================================

class Lock:
    """Simula un lock thread-safe"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.locked = False
    
    def __enter__(self):
        print(f"Adquiriendo lock: {self.nombre}")
        self.locked = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Liberando lock: {self.nombre}")
        self.locked = False
        return False

print("=== Lock Reutilizable ===")
mi_lock = Lock("recurso_compartido")

with mi_lock:
    print("Usando recurso protegido 1")

# El mismo lock puede reutilizarse
with mi_lock:
    print("Usando recurso protegido 2")
print()

# ============================================
# CONTEXT MANAGER PARA REDIRECCIÓN
# ============================================

@contextmanager
def redirigir_stdout(nuevo_destino):
    """Redirige stdout temporalmente"""
    import sys
    old_stdout = sys.stdout
    sys.stdout = nuevo_destino
    try:
        yield
    finally:
        sys.stdout = old_stdout

print("=== Redirección de Salida ===")
from io import StringIO
buffer = StringIO()
with redirigir_stdout(buffer):
    print("Este texto va al buffer")
    print("Este también")

print(f"Capturado: {buffer.getvalue()}")

# ============================================
# CONTEXT MANAGER CON PARÁMETROS
# ============================================

class ConfigTemporal:
    """Cambia configuración temporalmente"""
    
    def __init__(self, configuraciones):
        self.nuevas_config = configuraciones
        self.config_anterior = {}
        self.config_global = {"debug": False, "verbose": False}
    
    def __enter__(self):
        print(f"Configuración original: {self.config_global}")
        for key, value in self.nuevas_config.items():
            self.config_anterior[key] = self.config_global.get(key)
            self.config_global[key] = value
        print(f"Configuración temporal: {self.config_global}")
        return self.config_global
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        for key, value in self.config_anterior.items():
            if value is None:
                self.config_global.pop(key, None)
            else:
                self.config_global[key] = value
        print(f"Configuración restaurada: {self.config_global}")
        return False

print("\n=== Configuración Temporal ===")
with ConfigTemporal({"debug": True, "verbose": True}) as config:
    print(f"Dentro del contexto: {config}")
print()
