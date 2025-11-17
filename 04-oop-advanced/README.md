# Programación Orientada a Objetos Avanzada

## Conceptos Avanzados de POO

### Herencia Múltiple y MRO

Python soporta herencia múltiple. El Method Resolution Order (MRO) determina el orden en que se buscan métodos en la jerarquía de clases.

- **MRO**: Algoritmo C3 Linearization
- Ver el MRO: `Clase.__mro__` o `Clase.mro()`

### Métodos Mágicos (Dunder Methods)

Son métodos especiales rodeados por doble guión bajo que Python invoca automáticamente.

**Categorías principales:**
- Construcción/Destrucción: `__init__`, `__del__`
- Representación: `__str__`, `__repr__`
- Comparación: `__eq__`, `__lt__`, `__gt__`, etc.
- Aritméticos: `__add__`, `__sub__`, `__mul__`, etc.
- Contenedores: `__len__`, `__getitem__`, `__setitem__`
- Contexto: `__enter__`, `__exit__`
- Llamables: `__call__`

### Properties

Permiten controlar el acceso a atributos mediante métodos getter, setter y deleter.

```python
@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self, value):
    self._nombre = value
```

### Descriptores

Objetos que controlan el acceso a atributos mediante `__get__`, `__set__` y `__delete__`.

### Clases Abstractas

Definen interfaces que las subclases deben implementar.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
```

### Metaclases

Clases que crean clases. Controlan la creación de clases.

```python
class Meta(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)
```

## Patrones de Diseño

- Singleton
- Factory
- Observer
- Decorator
- Strategy
