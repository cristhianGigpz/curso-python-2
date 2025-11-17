"""
Ejercicios de Context Managers
"""

from contextlib import contextmanager
import time

# Ejercicio 1: Context Manager para Timer
# Crea un context manager que mida y muestre el tiempo de ejecución
class Timer:
    # Tu código aquí
    pass

# Ejercicio 2: Context Manager usando @contextmanager
# Crea un context manager que guarde y restaure el directorio actual
@contextmanager
def working_directory(path):
    # Tu código aquí
    pass

# Ejercicio 3: Context Manager para archivo temporal
# Crea un context manager que cree un archivo temporal y lo elimine al salir
class TempFile:
    # Tu código aquí
    pass

# Ejercicio 4: Context Manager con supresión de excepciones
# Crea un context manager que capture y registre excepciones sin propagarlas
class CatchExceptions:
    # Tu código aquí
    pass

# Ejercicio 5: Context Manager para variables de entorno
# Crea un context manager que establezca variables de entorno temporalmente
@contextmanager
def env_vars(**kwargs):
    # Tu código aquí
    pass

# Ejercicio 6: Context Manager para logging
# Crea un context manager que active/desactive logging en un bloque
class LoggingContext:
    # Tu código aquí
    pass

# Ejercicio 7: Context Manager para abrir múltiples archivos
# Crea un context manager que abra varios archivos y los cierre todos
@contextmanager
def open_files(*filenames, mode='r'):
    # Tu código aquí
    pass

# Ejercicio 8: Context Manager para retry
# Crea un context manager que reintente código que falla
@contextmanager
def retry_context(max_attempts=3):
    # Tu código aquí
    pass

# Ejercicio 9: Context Manager para medir memoria
# Crea un context manager que muestre el uso de memoria antes y después
class MemoryMonitor:
    # Tu código aquí
    pass

# Ejercicio 10: Context Manager para cambiar atributos temporalmente
# Crea un context manager que cambie atributos de un objeto temporalmente
@contextmanager
def temp_attr(obj, **attrs):
    # Tu código aquí
    pass

# Tests
if __name__ == "__main__":
    print("Implementa los ejercicios y prueba aquí")
    
    # Ejemplo de test para ejercicio 1
    print("\n=== Test Timer ===")
    # with Timer():
    #     time.sleep(0.1)
    
    print("\nDescomenta los tests cuando implementes los ejercicios")
