class DivisionError(Exception):
    """Excepción personalizada para errores de división."""
    pass

try:    
    a = int(input("Ingrese un número entero: "))
    b = int(input("Ingrese otro número entero: "))
    
    # if b == 2:
    #     raise DivisionError("El programa no permite dividir por 2.")
    resultado = a / b
    print(f"El resultado de {a} dividido por {b} es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Entrada inválida. Por favor, ingrese números enteros válidos.")
except Exception as e:
    print("Ha ocurrido un error, tipo:", type(e))
else:
    print("La división se realizó correctamente.")
finally:
    print("Ejecución finalizada.")
