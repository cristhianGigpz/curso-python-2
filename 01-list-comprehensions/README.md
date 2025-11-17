# List Comprehensions y Generadores

## ¿Qué son las List Comprehensions?

Las list comprehensions son una forma concisa y elegante de crear listas en Python. Permiten crear nuevas listas aplicando una expresión a cada elemento de una secuencia.

### Sintaxis Básica

```python
[expresion for item in iterable]
[expresion for item in iterable if condicion]
```

## Ventajas

- Código más conciso y legible
- Generalmente más rápidas que loops tradicionales
- Expresivas y pythónicas

## Tipos de Comprehensions

1. **List Comprehensions**: Crean listas
2. **Dict Comprehensions**: Crean diccionarios
3. **Set Comprehensions**: Crean conjuntos
4. **Generator Expressions**: Crean generadores (lazy evaluation)

## Generadores

Los generadores son iteradores que generan valores bajo demanda, sin almacenar toda la secuencia en memoria.

### Ventajas de Generadores

- Eficientes en memoria
- Ideales para secuencias grandes o infinitas
- Evaluación perezosa (lazy evaluation)

## Conceptos Clave

- `yield` vs `return`
- Generator expressions vs list comprehensions
- Cuándo usar cada uno
