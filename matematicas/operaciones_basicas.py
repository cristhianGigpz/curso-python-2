from .funciones_geometricas import area_cuadrado

def suma(a: float, b: float) -> float:
    return a + b
def resta(a: float, b: float) -> float:
    return a - b
def multiplicacion(a: float, b: float) -> float:
    return a * b
def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
def calcular_area_cuadrado(lado: float) -> float:
    return area_cuadrado(lado)
