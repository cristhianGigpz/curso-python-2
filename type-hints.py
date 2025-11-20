from typing import Any

variable = 42  # type: int  
variable_str: str = "Hola, mundo!"
variable_int: int = 100

print(f"variable de tipo {type(variable)} con valor {variable}")
print(f"variable_str de tipo {type(variable_str)} con valor {variable_str}")
print(f"variable_int de tipo {type(variable_int)} con valor {variable_int}")

def sumar(a: int, b: int) -> int:
    return a + b

resultado = sumar(5, 10)
print(f"El resultado de la suma es: {resultado}")

user_id: int | None = None  # Indicando que user_id no debe ser None

user_id = 12345  # Asignando un valor entero válido
print(f"user_id de tipo {type(user_id)} con valor {user_id}")

frutas: list[str | int] = ["manzanas", "naranjas", "plátanos", 50]
print(f"frutas de tipo {type(frutas)} con valor {frutas}")

articulos: list[dict[str, str | float]] = [
    {"nombre": "libro", "precio": 12.99},
    {"nombre": "lápiz", "precio": 0.99},
]
print(f"articulos de tipo {type(articulos)} con valor {articulos}")

valor: Any = "Esto puede ser cualquier cosa"
print(f"valor de tipo {type(valor)} con valor {valor}")

valor = 3.14  # Cambiando el valor a un float
print(f"valor de tipo {type(valor)} con valor {valor}")
