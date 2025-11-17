"""
Ejercicios de POO Avanzada
"""

from abc import ABC, abstractmethod

# Ejercicio 1: Implementa una clase Fraccion con métodos mágicos
# Debe soportar suma, resta, multiplicación, división, comparaciones
class Fraccion:
    # Tu código aquí
    pass

# Ejercicio 2: Crea una clase Temperature con properties
# Debe tener propiedades celsius, fahrenheit y kelvin que se conviertan
# automáticamente entre sí
class Temperature:
    # Tu código aquí
    pass

# Ejercicio 3: Implementa un descriptor para validar rangos
class RangoValidador:
    # Debe validar que el valor esté entre min_value y max_value
    # Tu código aquí
    pass

# Ejercicio 4: Crea una jerarquía de clases para un sistema de empleados
# - Clase base abstracta Empleado
# - EmpleadoTiempoCompleto (salario fijo)
# - EmpleadoHora (paga por hora trabajada)
# - Cada uno debe implementar calcular_salario()
class Empleado(ABC):
    # Tu código aquí
    pass

# Ejercicio 5: Implementa una metaclase que registre todas las clases
# creadas con ella
class RegistroMeta(type):
    # Tu código aquí
    pass

# Ejercicio 6: Crea una clase Contador que sea iterable y funcione como
# generador infinito
class Contador:
    # Tu código aquí
    pass

# Ejercicio 7: Implementa una clase DiccionarioOrdenado que mantenga
# el orden de inserción (antes de Python 3.7 los dict no ordenaban)
class DiccionarioOrdenado:
    # Tu código aquí
    pass

# Ejercicio 8: Crea una clase Matrix con operaciones matriciales
# Debe soportar suma, multiplicación, transposición
class Matrix:
    # Tu código aquí
    pass

# Ejercicio 9: Implementa el patrón Observer
class Observable:
    # Tu código aquí
    pass

class Observer(ABC):
    @abstractmethod
    def update(self, observable, *args, **kwargs):
        pass

# Ejercicio 10: Crea una clase que implemente __getitem__ para
# soportar slicing y acceso por índice negativo
class MiSecuencia:
    # Tu código aquí
    pass

# Tests
if __name__ == "__main__":
    print("Implementa los ejercicios y prueba aquí")
    
    # Ejemplo para ejercicio 1
    # f1 = Fraccion(1, 2)
    # f2 = Fraccion(1, 3)
    # print(f"1/2 + 1/3 = {f1 + f2}")
