def sumar_todos(*args):
    """Suma todos los argumentos posicionales proporcionados."""
    return sum(args)

print(sumar_todos(1, 2, 3, 4))  # Salida: 10

# def ejemplo_args(a, b, *args):
#     """Ejemplo de uso de *args."""
#     print(f"a: {a}, b: {b}, args: {args}")

def ejemplo_args(*args):
    """Ejemplo de uso de *args."""
    print("Argumentos posicionales adicionales:", args)
    print(type(args))
    #print(f"a: {a}, b: {b}, args: {args}")


ejemplo_args(1, 2, 3, 4, 5, 7, 10)  # Salida: a: 1, b: 2, args: (3, 4, 5)

def ejemplo_kwargs(**kwargs):
    """Ejemplo de uso de **kwargs."""
    print("Argumentos clave y valor:", kwargs)
    print(type(kwargs))
    #print(f"a: {a}, b: {b}, kwargs: {kwargs}")


ejemplo_kwargs(nombre="Cristhian", edad=33, ciudad="Lima")


def informacion_personal(**kwargs):
    """Imprime información personal a partir de argumentos clave y valor."""
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
    
informacion_personal(nombre="Cristhian", edad=33, ciudad="Lima", profesion="Desarrollador")
informacion_personal(nombre="Jose", edad=38, ciudad="ICA", profesion="Diseñador", hobby="Fotografía")

def combinar_args_kwargs(api_key, *args, **kwargs):
    """Combina argumentos posicionales y clave-valor."""
    print("Argumentos obligatorios:", api_key)
    print("Argumentos posicionales:", args)
    print("Argumentos clave y valor:", kwargs)

combinar_args_kwargs("mi_api_key_123", 1, 2, nombre="Cristhian", edad=33)
combinar_args_kwargs("otra_api_key_456", "a", "b", "c",nombre="Cristhian", ciudad="Lima", pais="Perú")
