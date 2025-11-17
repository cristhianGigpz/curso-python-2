# Módulos y Paquetes en Python

## Módulos

Un módulo es un archivo `.py` que contiene código Python reutilizable.

### Importar Módulos

```python
import modulo
from modulo import funcion
from modulo import *  # No recomendado
import modulo as alias
```

### Módulos Built-in

Python incluye muchos módulos útiles:
- `os`: Sistema operativo
- `sys`: Sistema Python
- `datetime`: Fechas y horas
- `math`: Matemáticas
- `random`: Números aleatorios
- `json`: Manejo de JSON
- `re`: Expresiones regulares

## Paquetes

Un paquete es un directorio que contiene módulos y un archivo `__init__.py`.

### Estructura de Paquete

```
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
    subpaquete/
        __init__.py
        modulo3.py
```

### `__init__.py`

- Define qué se importa con `from paquete import *`
- Inicializa el paquete
- Puede estar vacío

### Importaciones Relativas

```python
# Dentro de un paquete
from . import modulo          # mismo nivel
from .. import modulo         # nivel superior
from .subpaquete import mod   # subpaquete
```

### Importaciones Absolutas

```python
from mi_paquete.subpaquete import modulo
```

## Variables Especiales

- `__name__`: Nombre del módulo
- `__file__`: Ruta del archivo
- `__package__`: Nombre del paquete
- `__all__`: Lista de nombres públicos

## Best Practices

1. Un módulo = una responsabilidad
2. Nombres descriptivos
3. Documentar módulos (docstrings)
4. Evitar importaciones circulares
5. Usar importaciones absolutas cuando sea posible
6. `if __name__ == "__main__":` para código ejecutable

## Instalación de Paquetes

```bash
pip install paquete
pip install -r requirements.txt
pip freeze > requirements.txt
```
