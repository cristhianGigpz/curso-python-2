# Manejo de Archivos y Excepciones

## Manejo de Archivos

### Modos de Apertura
- `'r'`: Lectura (default)
- `'w'`: Escritura (sobrescribe)
- `'a'`: Append (añade al final)
- `'x'`: Creación exclusiva
- `'b'`: Modo binario
- `'t'`: Modo texto (default)
- `'+'`: Lectura y escritura

### Best Practices
- Usar `with` para manejo automático
- Especificar encoding (UTF-8)
- Cerrar archivos correctamente
- Manejar excepciones

## Excepciones

### Jerarquía de Excepciones
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError
    ├── TypeError
    ├── FileNotFoundError
    └── ...
```

### Try-Except-Else-Finally
```python
try:
    # Código que puede fallar
except TipoExcepcion as e:
    # Manejo de excepción
else:
    # Se ejecuta si no hay excepción
finally:
    # Siempre se ejecuta
```

### Excepciones Personalizadas
```python
class MiExcepcion(Exception):
    pass
```

## Conceptos Clave
- EAFP vs LBYL
- Capturar excepciones específicas
- Re-lanzar excepciones
- Context managers para recursos
