"""
Ejemplos de Manejo de Archivos y Excepciones
"""

import json
import csv
import pickle
from pathlib import Path

# ============================================
# LECTURA Y ESCRITURA DE ARCHIVOS
# ============================================

print("=== Escritura de Archivo ===")
# Escribir archivo de texto
with open('/tmp/ejemplo.txt', 'w', encoding='utf-8') as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.writelines(["Tercera línea\n", "Cuarta línea\n"])
print("Archivo escrito\n")

# Leer archivo completo
print("=== Lectura de Archivo ===")
with open('/tmp/ejemplo.txt', 'r', encoding='utf-8') as f:
    contenido = f.read()
    print(contenido)

# Leer línea por línea
print("=== Lectura Línea por Línea ===")
with open('/tmp/ejemplo.txt', 'r', encoding='utf-8') as f:
    for linea in f:
        print(linea.strip())
print()

# Leer todas las líneas en una lista
with open('/tmp/ejemplo.txt', 'r', encoding='utf-8') as f:
    lineas = f.readlines()
    print(f"Total de líneas: {len(lineas)}\n")

# ============================================
# PATHLIB
# ============================================

print("=== Uso de Pathlib ===")
ruta = Path('/tmp/ejemplo.txt')
print(f"Existe: {ruta.exists()}")
print(f"Es archivo: {ruta.is_file()}")
print(f"Tamaño: {ruta.stat().st_size} bytes")
print(f"Nombre: {ruta.name}")
print(f"Extensión: {ruta.suffix}\n")

# ============================================
# ARCHIVOS JSON
# ============================================

print("=== Archivos JSON ===")
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["programar", "leer", "viajar"]
}

# Escribir JSON
with open('/tmp/datos.json', 'w', encoding='utf-8') as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
print("JSON escrito")

# Leer JSON
with open('/tmp/datos.json', 'r', encoding='utf-8') as f:
    datos_leidos = json.load(f)
    print(f"Datos leídos: {datos_leidos}\n")

# ============================================
# ARCHIVOS CSV
# ============================================

print("=== Archivos CSV ===")
# Escribir CSV
with open('/tmp/datos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Nombre', 'Edad', 'Ciudad'])
    writer.writerow(['Ana', 25, 'Barcelona'])
    writer.writerow(['Bob', 30, 'Valencia'])
print("CSV escrito")

# Leer CSV
with open('/tmp/datos.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(fila)
print()

# CSV con DictReader/DictWriter
print("=== CSV con Diccionarios ===")
with open('/tmp/datos_dict.csv', 'w', newline='', encoding='utf-8') as f:
    campos = ['nombre', 'edad', 'ciudad']
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    writer.writerow({'nombre': 'Carlos', 'edad': 28, 'ciudad': 'Sevilla'})
    writer.writerow({'nombre': 'Diana', 'edad': 32, 'ciudad': 'Bilbao'})

with open('/tmp/datos_dict.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(f"{fila['nombre']}: {fila['edad']} años, {fila['ciudad']}")
print()

# ============================================
# ARCHIVOS BINARIOS
# ============================================

print("=== Archivos Binarios con Pickle ===")
# Serializar objeto
objeto = {'lista': [1, 2, 3], 'texto': 'hola', 'numero': 42}
with open('/tmp/objeto.pkl', 'wb') as f:
    pickle.dump(objeto, f)
print("Objeto serializado")

# Deserializar objeto
with open('/tmp/objeto.pkl', 'rb') as f:
    objeto_leido = pickle.load(f)
    print(f"Objeto deserializado: {objeto_leido}\n")

# ============================================
# MANEJO DE EXCEPCIONES BÁSICO
# ============================================

print("=== Manejo de Excepciones Básico ===")
try:
    numero = int("no es un número")
except ValueError as e:
    print(f"Error de conversión: {e}\n")

# ============================================
# TRY-EXCEPT-ELSE-FINALLY
# ============================================

print("=== Try-Except-Else-Finally ===")
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: División por cero")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Bloque finally siempre se ejecuta\n")

# ============================================
# MÚLTIPLES EXCEPCIONES
# ============================================

print("=== Múltiples Excepciones ===")
def procesar_dato(dato):
    try:
        numero = int(dato)
        resultado = 100 / numero
        return resultado
    except ValueError:
        print("Error: No es un número válido")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

procesar_dato("abc")
procesar_dato("0")
procesar_dato("5")
print()

# ============================================
# EXCEPCIONES PERSONALIZADAS
# ============================================

class ErrorValidacion(Exception):
    """Excepción personalizada para errores de validación"""
    pass

class ErrorRango(ErrorValidacion):
    """Error cuando un valor está fuera de rango"""
    def __init__(self, valor, minimo, maximo):
        self.valor = valor
        self.minimo = minimo
        self.maximo = maximo
        mensaje = f"Valor {valor} fuera de rango [{minimo}, {maximo}]"
        super().__init__(mensaje)

print("=== Excepciones Personalizadas ===")
def validar_edad(edad):
    if not isinstance(edad, int):
        raise ErrorValidacion("La edad debe ser un número entero")
    if edad < 0 or edad > 150:
        raise ErrorRango(edad, 0, 150)
    return edad

try:
    validar_edad(200)
except ErrorRango as e:
    print(f"Error: {e}")
print()

# ============================================
# RE-LANZAR EXCEPCIONES
# ============================================

print("=== Re-lanzar Excepciones ===")
def operacion_critica():
    try:
        # Simular operación que falla
        raise ValueError("Error en operación")
    except ValueError as e:
        print(f"Registrando error: {e}")
        raise  # Re-lanza la excepción

try:
    operacion_critica()
except ValueError:
    print("Excepción capturada en nivel superior\n")

# ============================================
# CONTEXT MANAGER PARA ARCHIVOS
# ============================================

print("=== Context Manager para Múltiples Archivos ===")
try:
    with open('/tmp/entrada.txt', 'w') as entrada, \
         open('/tmp/salida.txt', 'w') as salida:
        entrada.write("Datos de entrada\n")
        salida.write("Datos de salida\n")
    print("Archivos procesados correctamente\n")
except IOError as e:
    print(f"Error de E/S: {e}")

# ============================================
# EAFP vs LBYL
# ============================================

print("=== EAFP (Easier to Ask Forgiveness than Permission) ===")
# Estilo Python preferido
diccionario = {'a': 1, 'b': 2}
try:
    valor = diccionario['c']
except KeyError:
    valor = None
print(f"Valor (EAFP): {valor}")

print("\n=== LBYL (Look Before You Leap) ===")
# No tan pythónico
if 'c' in diccionario:
    valor = diccionario['c']
else:
    valor = None
print(f"Valor (LBYL): {valor}\n")

# ============================================
# SUPRESIÓN DE EXCEPCIONES
# ============================================

from contextlib import suppress

print("=== Supresión de Excepciones ===")
with suppress(FileNotFoundError):
    # Intenta eliminar archivo que puede no existir
    Path('/tmp/archivo_inexistente.txt').unlink()
print("Continuó sin error\n")

# ============================================
# TRACEBACK
# ============================================

import traceback

print("=== Traceback ===")
try:
    def funcion_a():
        funcion_b()
    
    def funcion_b():
        1 / 0
    
    funcion_a()
except ZeroDivisionError:
    print("Error capturado. Traceback:")
    traceback.print_exc()
