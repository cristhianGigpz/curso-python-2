"""
Ejercicios de Expresiones Regulares
"""

import re

# Ejercicio 1: Validar contraseña
# Debe tener: 8+ caracteres, 1 mayúscula, 1 minúscula, 1 dígito, 1 especial
def validar_password(password):
    # Tu código aquí
    pass

# Ejercicio 2: Extraer hashtags de texto
def extraer_hashtags(texto):
    # Retorna lista de hashtags (#python, #coding, etc.)
    pass

# Ejercicio 3: Validar fecha en formato DD/MM/YYYY
def validar_fecha(fecha):
    # Valida formato y rangos razonables
    pass

# Ejercicio 4: Limpiar HTML tags
def remover_html(texto):
    # Remueve todas las etiquetas HTML
    pass

# Ejercicio 5: Extraer números de tarjeta de crédito
def extraer_tarjetas(texto):
    # Formato: 1234-5678-9012-3456 o 1234567890123456
    pass

# Ejercicio 6: Convertir snake_case a camelCase
def snake_to_camel(texto):
    # mi_variable -> miVariable
    pass

# Ejercicio 7: Validar dirección IP (IPv4)
def validar_ip(ip):
    # Formato: 192.168.1.1 (cada octeto 0-255)
    pass

# Ejercicio 8: Extraer menciones de Twitter
def extraer_menciones(texto):
    # Retorna lista de @usuario
    pass

# Ejercicio 9: Parsear logs de servidor
def parsear_log(linea_log):
    # Extrae IP, timestamp, método HTTP, URL, código de estado
    # Formato: 192.168.1.1 - - [15/Jan/2024:10:30:45] "GET /index.html HTTP/1.1" 200
    pass

# Ejercicio 10: Censurar palabras
def censurar_palabras(texto, palabras_prohibidas):
    # Reemplaza palabras prohibidas con asteriscos
    # Debe respetar mayúsculas/minúsculas
    pass

# Tests
if __name__ == "__main__":
    print("Implementa los ejercicios y prueba aquí")
    
    # Ejemplo test
    # print(validar_password("Pass123!"))  # True
    # print(validar_password("weak"))      # False
