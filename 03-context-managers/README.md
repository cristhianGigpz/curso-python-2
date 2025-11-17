# Context Managers en Python

## ¿Qué es un Context Manager?

Un context manager es un objeto que define el contexto de ejecución que debe establecerse al ejecutar una declaración `with`. Se encarga de la configuración y limpieza automática de recursos.

## El Protocolo `with`

El protocolo de context manager requiere dos métodos:
- `__enter__()`: Se ejecuta al entrar al bloque `with`
- `__exit__()`: Se ejecuta al salir del bloque `with`

## Sintaxis

```python
with context_manager as variable:
    # Código que usa el recurso
    pass
# Aquí el recurso ya se ha limpiado
```

## Ventajas

1. **Garantía de limpieza**: Los recursos se liberan incluso si hay excepciones
2. **Código más limpio**: No necesitas try/finally explícitos
3. **Pythónico**: Es el estándar para manejar recursos

## Usos Comunes

- Manejo de archivos
- Conexiones a bases de datos
- Locks y semáforos
- Manejo de transacciones
- Contextos temporales

## Formas de Crear Context Managers

1. **Clase con `__enter__` y `__exit__`**: Control total
2. **Decorador `@contextmanager`**: Más conciso usando generadores
3. **Context managers built-in**: Como `open()`, `threading.Lock()`, etc.

## Métodos Especiales

- `__enter__(self)`: Retorna el recurso o self
- `__exit__(self, exc_type, exc_val, exc_tb)`: 
  - exc_type: Tipo de excepción (None si no hubo)
  - exc_val: Valor de la excepción
  - exc_tb: Traceback
  - Retorna True para suprimir la excepción
