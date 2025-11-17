# Programación Funcional en Python

## ¿Qué es la Programación Funcional?

Un paradigma de programación que trata la computación como la evaluación de funciones matemáticas, evitando estados mutables y datos mutables.

## Principios Clave

1. **Funciones Puras**: Sin efectos secundarios, mismo input = mismo output
2. **Inmutabilidad**: Los datos no se modifican después de crearse
3. **Funciones de Primera Clase**: Las funciones son objetos
4. **Composición de Funciones**: Combinar funciones simples
5. **Recursión**: Alternativa a loops

## Funciones Lambda

Funciones anónimas de una línea:
```python
lambda x: x * 2
lambda x, y: x + y
```

## Map, Filter, Reduce

### map()
Aplica una función a cada elemento:
```python
map(función, iterable)
```

### filter()
Filtra elementos que cumplen condición:
```python
filter(función, iterable)
```

### reduce()
Reduce iterable a un valor:
```python
from functools import reduce
reduce(función, iterable)
```

## Módulos Importantes

### functools
- `reduce()`: Reducir iterable
- `partial()`: Aplicación parcial
- `lru_cache()`: Caché de resultados
- `wraps()`: Preservar metadata

### itertools
- `chain()`: Concatenar iterables
- `combinations()`: Combinaciones
- `permutations()`: Permutaciones
- `cycle()`: Ciclo infinito
- `islice()`: Slice de iterador
- `groupby()`: Agrupar elementos

### operator
- Versiones de función de operadores
- `add`, `mul`, `lt`, `gt`, etc.

## Características Funcionales

- **List Comprehensions**: Transformaciones declarativas
- **Generator Expressions**: Evaluación perezosa
- **Closures**: Funciones que capturan entorno
- **Decoradores**: Transformar funciones

## Ventajas

- Código más conciso
- Más fácil de testear
- Menos bugs por inmutabilidad
- Paralelización más simple
- Código más declarativo
