"""
Ejercicios de Decoradores
"""

import time
import functools

# Ejercicio 1: Decorador de depuración
# Crea un decorador que imprima el nombre de la función y sus argumentos
# antes de ejecutarla
def debug(func):
    # Tu código aquí
    pass

# Ejercicio 2: Decorador de conteo
# Crea un decorador que cuente cuántas veces se ha llamado a una función
def contador_llamadas(func):
    # Tu código aquí
    pass

# Ejercicio 3: Decorador de timeout
# Crea un decorador que limite el tiempo de ejecución de una función
# (Pista: usa threading o multiprocessing)
def timeout(segundos):
    # Tu código aquí
    pass

# Ejercicio 4: Decorador de tipo de retorno
# Crea un decorador que valide que el valor de retorno sea de un tipo específico
def validar_tipo_retorno(tipo_esperado):
    # Tu código aquí
    pass

# Ejercicio 5: Decorador de autenticación
# Simula un decorador que verifica si un usuario está autenticado
# antes de ejecutar una función
usuario_autenticado = False

def requiere_autenticacion(func):
    # Tu código aquí
    pass

# Ejercicio 6: Decorador de rate limiting
# Crea un decorador que limite cuántas veces se puede llamar a una función
# en un período de tiempo
def rate_limit(llamadas_max, periodo):
    # Tu código aquí
    # llamadas_max: número máximo de llamadas
    # periodo: período en segundos
    pass

# Ejercicio 7: Decorador de conversión de resultado
# Crea un decorador que convierta el resultado de una función a JSON
def to_json(func):
    # Tu código aquí
    pass

# Ejercicio 8: Decorador de excepciones
# Crea un decorador que capture excepciones específicas y retorne un valor
# por defecto
def manejar_excepcion(excepcion, valor_defecto):
    # Tu código aquí
    pass

# Ejercicio 9: Decorador que guarda resultados
# Crea un decorador que guarde todos los resultados de una función en una lista
def guardar_resultados(func):
    # Tu código aquí
    # Debe agregar un atributo 'resultados' a la función
    pass

# Ejercicio 10: Decorador de deprecación
# Crea un decorador que muestre un mensaje de advertencia cuando se use
# una función deprecada
def deprecated(mensaje="Esta función está deprecada"):
    # Tu código aquí
    pass

# Tests
if __name__ == "__main__":
    # Test ejercicio 1
    @debug
    def suma(a, b):
        return a + b
    
    print("Test ejercicio 1:")
    # Debería imprimir información de debug antes del resultado
    # suma(3, 5)
    
    # Test ejercicio 2
    @contador_llamadas
    def decir_hola():
        print("Hola")
    
    print("\nTest ejercicio 2:")
    # Debería contar las llamadas
    # decir_hola()
    # decir_hola()
    # print(f"Llamadas: {decir_hola.llamadas}")
    
    print("\nImplementa los ejercicios y descomenta los tests para probar")
