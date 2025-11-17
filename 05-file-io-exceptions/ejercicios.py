"""
Ejercicios de Manejo de Archivos y Excepciones
"""

# Ejercicio 1: Leer archivo y contar palabras
def contar_palabras(nombre_archivo):
    # Debe retornar un diccionario con la frecuencia de cada palabra
    # Maneja FileNotFoundError
    pass

# Ejercicio 2: Copiar archivo con manejo de errores
def copiar_archivo(origen, destino):
    # Copia el contenido de un archivo a otro
    # Maneja todas las excepciones posibles
    pass

# Ejercicio 3: Procesar archivo JSON con validación
def procesar_json(archivo_json):
    # Lee un archivo JSON y valida que tenga ciertos campos
    # Lanza excepciones personalizadas si falta información
    pass

# Ejercicio 4: Escribir log de errores
def escribir_log(mensaje, nivel='INFO'):
    # Escribe mensajes en un archivo de log con timestamp
    # Formato: [TIMESTAMP] NIVEL: mensaje
    pass

# Ejercicio 5: Leer CSV y convertir a diccionario
def csv_a_dict(archivo_csv):
    # Lee un CSV y retorna lista de diccionarios
    # Maneja errores de formato
    pass

# Ejercicio 6: Crear excepción personalizada para validación
class ErrorUsuario(Exception):
    # Crea una jerarquía de excepciones para validar usuarios
    # - ErrorUsuarioInvalido
    # - ErrorEdadInvalida
    # - ErrorEmailInvalido
    pass

# Ejercicio 7: Context manager para backup de archivo
class BackupArchivo:
    # Context manager que hace backup antes de modificar
    # y restaura si hay error
    pass

# Ejercicio 8: Procesar múltiples archivos
def procesar_directorio(directorio):
    # Lee todos los .txt de un directorio
    # Concatena su contenido en un solo archivo
    # Maneja archivos que no se puedan leer
    pass

# Ejercicio 9: Deserializar objeto con validación
def cargar_configuracion(archivo):
    # Carga archivo JSON de configuración
    # Valida que tenga todos los campos requeridos
    # Retorna objeto con valores por defecto si algo falla
    pass

# Ejercicio 10: Retry con exponential backoff
def operacion_con_retry(operacion, max_intentos=3):
    # Ejecuta operación con reintentos
    # Usa exponential backoff entre intentos
    # Registra cada intento fallido
    pass

# Tests
if __name__ == "__main__":
    print("Implementa los ejercicios y prueba aquí")
