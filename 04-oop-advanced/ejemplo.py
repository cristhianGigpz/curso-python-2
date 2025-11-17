"""
Ejemplos de POO Avanzada en Python
"""

from abc import ABC, abstractmethod
from typing import Any

# ============================================
# MÉTODOS MÁGICOS (DUNDER METHODS)
# ============================================

class Vector:
    """Clase que implementa un vector 2D con métodos mágicos"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """Representación para desarrolladores"""
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        """Representación para usuarios"""
        return f"Vector de ({self.x}, {self.y})"
    
    def __add__(self, other):
        """Suma de vectores"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Resta de vectores"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, escalar):
        """Multiplicación por escalar"""
        return Vector(self.x * escalar, self.y * escalar)
    
    def __eq__(self, other):
        """Comparación de igualdad"""
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):
        """Magnitud del vector"""
        return (self.x**2 + self.y**2)**0.5
    
    def __bool__(self):
        """Verdadero si no es vector cero"""
        return bool(abs(self))

print("=== Métodos Mágicos ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 2: {v1 * 2}")
print(f"|v1|: {abs(v1)}")
print(f"v1 == v2: {v1 == v2}\n")

# ============================================
# PROPERTIES
# ============================================

class Persona:
    """Clase con properties para validación de atributos"""
    
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        """Getter para nombre"""
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        """Setter para nombre con validación"""
        if not isinstance(value, str):
            raise TypeError("El nombre debe ser un string")
        if len(value) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        self._nombre = value
    
    @property
    def edad(self):
        """Getter para edad"""
        return self._edad
    
    @edad.setter
    def edad(self, value):
        """Setter para edad con validación"""
        if not isinstance(value, int):
            raise TypeError("La edad debe ser un entero")
        if value < 0 or value > 150:
            raise ValueError("La edad debe estar entre 0 y 150")
        self._edad = value
    
    @property
    def mayor_de_edad(self):
        """Property de solo lectura calculada"""
        return self._edad >= 18

print("=== Properties ===")
p = Persona("Juan", 25)
print(f"Nombre: {p.nombre}")
print(f"Edad: {p.edad}")
print(f"¿Mayor de edad?: {p.mayor_de_edad}")
p.edad = 30
print(f"Nueva edad: {p.edad}\n")

# ============================================
# HERENCIA MÚLTIPLE Y MRO
# ============================================

class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")
        super().metodo()

class C(A):
    def metodo(self):
        print("Método de C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("Método de D")
        super().metodo()

print("=== Herencia Múltiple y MRO ===")
d = D()
d.metodo()
print(f"MRO de D: {[c.__name__ for c in D.__mro__]}\n")

# ============================================
# DESCRIPTORES
# ============================================

class ValidadorPositivo:
    """Descriptor que valida números positivos"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.nombre, 0)
    
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError(f"{self.nombre} debe ser positivo")
        obj.__dict__[self.nombre] = value
    
    def __delete__(self, obj):
        del obj.__dict__[self.nombre]

class Producto:
    precio = ValidadorPositivo('precio')
    cantidad = ValidadorPositivo('cantidad')
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def total(self):
        return self.precio * self.cantidad

print("=== Descriptores ===")
prod = Producto("Laptop", 1000, 5)
print(f"Producto: {prod.nombre}")
print(f"Total: ${prod.total}")
try:
    prod.precio = -100
except ValueError as e:
    print(f"Error: {e}\n")

# ============================================
# CLASES ABSTRACTAS
# ============================================

class Figura(ABC):
    """Clase abstracta para figuras geométricas"""
    
    @abstractmethod
    def area(self):
        """Calcula el área de la figura"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """Calcula el perímetro de la figura"""
        pass
    
    def descripcion(self):
        """Método concreto"""
        return f"Soy una {self.__class__.__name__}"

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

print("=== Clases Abstractas ===")
rect = Rectangulo(5, 3)
print(f"{rect.descripcion()}: área={rect.area()}, perímetro={rect.perimetro()}")
circ = Circulo(4)
print(f"{circ.descripcion()}: área={circ.area():.2f}, perímetro={circ.perimetro():.2f}\n")

# ============================================
# METACLASES
# ============================================

class SingletonMeta(type):
    """Metaclase que implementa el patrón Singleton"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Creando instancia de Database")
        self.connection = "Connected"

print("=== Metaclases (Singleton) ===")
db1 = Database()
db2 = Database()
print(f"db1 is db2: {db1 is db2}\n")

# ============================================
# __CALL__ - OBJETOS LLAMABLES
# ============================================

class Multiplicador:
    """Clase que actúa como función"""
    
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

print("=== Objetos Llamables ===")
duplicar = Multiplicador(2)
triplicar = Multiplicador(3)
print(f"duplicar(5): {duplicar(5)}")
print(f"triplicar(5): {triplicar(5)}\n")

# ============================================
# GETATTR, SETATTR, DELATTR
# ============================================

class AtributosDinamicos:
    """Clase con atributos dinámicos"""
    
    def __init__(self):
        self._datos = {}
    
    def __getattr__(self, nombre):
        """Se llama cuando no se encuentra el atributo"""
        if nombre in self._datos:
            return self._datos[nombre]
        raise AttributeError(f"Atributo '{nombre}' no encontrado")
    
    def __setattr__(self, nombre, valor):
        """Se llama al asignar un atributo"""
        if nombre == '_datos':
            super().__setattr__(nombre, valor)
        else:
            self._datos[nombre] = valor
    
    def __delattr__(self, nombre):
        """Se llama al eliminar un atributo"""
        if nombre in self._datos:
            del self._datos[nombre]
        else:
            raise AttributeError(f"Atributo '{nombre}' no encontrado")

print("=== Atributos Dinámicos ===")
obj = AtributosDinamicos()
obj.nombre = "Python"
obj.version = 3.11
print(f"Nombre: {obj.nombre}")
print(f"Versión: {obj.version}\n")

# ============================================
# CONTENEDORES PERSONALIZADOS
# ============================================

class MiLista:
    """Implementa protocolo de secuencia"""
    
    def __init__(self, *items):
        self._items = list(items)
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __delitem__(self, index):
        del self._items[index]
    
    def __iter__(self):
        return iter(self._items)
    
    def __contains__(self, item):
        return item in self._items
    
    def __repr__(self):
        return f"MiLista{tuple(self._items)}"

print("=== Contenedores Personalizados ===")
ml = MiLista(1, 2, 3, 4, 5)
print(f"Lista: {ml}")
print(f"Longitud: {len(ml)}")
print(f"Primer elemento: {ml[0]}")
print(f"¿3 está en la lista?: {3 in ml}")
print(f"Iteración: {[x for x in ml]}\n")

# ============================================
# COMPARACIONES PERSONALIZADAS
# ============================================

from functools import total_ordering

@total_ordering
class Estudiante:
    """Clase con comparaciones basadas en calificación"""
    
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
    
    def __eq__(self, other):
        return self.calificacion == other.calificacion
    
    def __lt__(self, other):
        return self.calificacion < other.calificacion
    
    def __repr__(self):
        return f"Estudiante('{self.nombre}', {self.calificacion})"

print("=== Comparaciones Personalizadas ===")
e1 = Estudiante("Ana", 95)
e2 = Estudiante("Bob", 87)
e3 = Estudiante("Carlos", 92)
estudiantes = [e2, e3, e1]
print(f"Estudiantes ordenados: {sorted(estudiantes)}\n")

# ============================================
# CONTEXT MANAGER CON CLASE
# ============================================

class Transaccion:
    """Context manager para transacciones"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        print(f"Iniciando transacción: {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"Transacción {self.nombre} completada con éxito")
        else:
            print(f"Transacción {self.nombre} falló: {exc_val}")
        return False

print("=== Context Manager con Clase ===")
with Transaccion("Pago"):
    print("Procesando pago...")
