# Decoradores en Python

## ¿Qué es un Decorador?

Un decorador es una función que toma otra función como argumento y extiende su comportamiento sin modificarla explícitamente. Es una aplicación del patrón de diseño Decorator.

## Conceptos Fundamentales

### Funciones de Primera Clase

En Python, las funciones son objetos de primera clase:
- Se pueden asignar a variables
- Se pueden pasar como argumentos
- Se pueden retornar desde otras funciones
- Se pueden almacenar en estructuras de datos

## Sintaxis

```python
@decorador
def funcion():
    pass

# Es equivalente a:
def funcion():
    pass
funcion = decorador(funcion)
```

## Tipos de Decoradores

1. **Decoradores de función**: Modifican funciones
2. **Decoradores con argumentos**: Aceptan parámetros
3. **Decoradores de clase**: Modifican clases
4. **Decoradores apilados**: Múltiples decoradores en una función

## Usos Comunes

- Logging y debugging
- Validación de permisos
- Caché y memoización
- Medición de tiempo de ejecución
- Validación de argumentos
- Registro de llamadas

## Decoradores Built-in

- `@property`
- `@staticmethod`
- `@classmethod`
- `@functools.wraps`
- `@functools.lru_cache`
