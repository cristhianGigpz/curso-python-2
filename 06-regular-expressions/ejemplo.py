"""
Ejemplos de Expresiones Regulares
"""

import re

# ============================================
# MATCH vs SEARCH
# ============================================

print("=== Match vs Search ===")
texto = "El código postal es 28001"

# match busca al inicio
match = re.match(r'\d+', texto)
print(f"Match: {match}")  # None, no empieza con dígito

# search busca en toda la cadena
search = re.search(r'\d+', texto)
print(f"Search: {search.group()}")  # 28001
print()

# ============================================
# FINDALL
# ============================================

print("=== Findall ===")
texto = "Juan tiene 25 años, María 30 y Pedro 28"
numeros = re.findall(r'\d+', texto)
print(f"Números encontrados: {numeros}")

palabras = re.findall(r'\b[A-Z][a-z]+\b', texto)
print(f"Nombres propios: {palabras}")
print()

# ============================================
# GRUPOS DE CAPTURA
# ============================================

print("=== Grupos de Captura ===")
texto = "Contacto: juan@email.com, teléfono: 123-456-7890"

# Capturar email
email_pattern = r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
match = re.search(email_pattern, texto)
if match:
    print(f"Email completo: {match.group(0)}")
    print(f"Usuario: {match.group(1)}")
    print(f"Dominio: {match.group(2)}")
print()

# ============================================
# GRUPOS NOMBRADOS
# ============================================

print("=== Grupos Nombrados ===")
patron = r'(?P<nombre>\w+)\s+(?P<apellido>\w+)'
texto = "Juan Pérez es el ganador"
match = re.search(patron, texto)
if match:
    print(f"Nombre: {match.group('nombre')}")
    print(f"Apellido: {match.group('apellido')}")
    print(f"Diccionario: {match.groupdict()}")
print()

# ============================================
# SUSTITUCIÓN
# ============================================

print("=== Sustitución ===")
texto = "La fecha es 2024-01-15"
# Cambiar formato de fecha
nuevo = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', texto)
print(f"Original: {texto}")
print(f"Modificado: {nuevo}")

# Función en sustitución
def convertir_mayuscula(match):
    return match.group(0).upper()

texto = "hola mundo python"
nuevo = re.sub(r'\b\w+\b', convertir_mayuscula, texto)
print(f"Mayúsculas: {nuevo}")
print()

# ============================================
# SPLIT CON REGEX
# ============================================

print("=== Split ===")
texto = "uno,dos;tres:cuatro|cinco"
partes = re.split(r'[,;:|]', texto)
print(f"Partes: {partes}")
print()

# ============================================
# VALIDACIÓN DE EMAIL
# ============================================

print("=== Validación de Email ===")
def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))

emails = ["test@example.com", "invalid.email", "user@domain.co.uk"]
for email in emails:
    print(f"{email}: {validar_email(email)}")
print()

# ============================================
# VALIDACIÓN DE TELÉFONO
# ============================================

print("=== Validación de Teléfono ===")
def validar_telefono(telefono):
    # Formato: (123) 456-7890 o 123-456-7890
    patron = r'^(\(\d{3}\)\s?|\d{3}-)?\d{3}-\d{4}$'
    return bool(re.match(patron, telefono))

telefonos = ["(123) 456-7890", "123-456-7890", "1234567890"]
for tel in telefonos:
    print(f"{tel}: {validar_telefono(tel)}")
print()

# ============================================
# VALIDACIÓN DE URL
# ============================================

print("=== Validación de URL ===")
def validar_url(url):
    patron = r'^https?://(www\.)?[\w.-]+\.\w{2,}(/.*)?$'
    return bool(re.match(patron, url))

urls = [
    "https://www.example.com",
    "http://example.com/path",
    "not a url"
]
for url in urls:
    print(f"{url}: {validar_url(url)}")
print()

# ============================================
# EXTRACCIÓN DE INFORMACIÓN
# ============================================

print("=== Extracción de Información ===")
log = """
2024-01-15 10:30:45 INFO User login successful
2024-01-15 10:31:22 ERROR Database connection failed
2024-01-15 10:32:10 WARNING Low memory
"""

patron = r'(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)'
for linea in log.strip().split('\n'):
    match = re.match(patron, linea)
    if match:
        fecha, hora, nivel, mensaje = match.groups()
        print(f"[{fecha} {hora}] {nivel}: {mensaje}")
print()

# ============================================
# LOOKAHEAD Y LOOKBEHIND
# ============================================

print("=== Lookahead y Lookbehind ===")
# Positive lookahead (?=...)
texto = "precio: $100, descuento: $20"
precios = re.findall(r'\$(?=\d+)', texto)  # $ seguido de dígitos
print(f"Símbolos de dólar: {precios}")

# Lookbehind (?<=...)
numeros = re.findall(r'(?<=\$)\d+', texto)  # dígitos precedidos de $
print(f"Cantidades: {numeros}")
print()

# ============================================
# FLAGS
# ============================================

print("=== Flags ===")
texto = "Python es GENIAL"

# Sin flag
print(f"Sin flag: {re.findall(r'python', texto)}")

# Con IGNORECASE
print(f"IGNORECASE: {re.findall(r'python', texto, re.IGNORECASE)}")

# MULTILINE
texto_multi = """Primera línea
Segunda línea
Tercera línea"""
print(f"Líneas que empiezan con palabra: {re.findall(r'^\\w+', texto_multi, re.MULTILINE)}")
print()

# ============================================
# VERBOSE (COMENTADO)
# ============================================

print("=== Verbose ===")
patron_verbose = re.compile(r'''
    ^                   # Inicio de línea
    [a-zA-Z0-9._%+-]+  # Usuario
    @                   # Arroba
    [a-zA-Z0-9.-]+     # Dominio
    \.                  # Punto
    [a-zA-Z]{2,}       # TLD
    $                   # Fin de línea
''', re.VERBOSE)

email = "test@example.com"
print(f"Email válido: {bool(patron_verbose.match(email))}")
print()

# ============================================
# COMPILAR PATRONES
# ============================================

print("=== Patrones Compilados ===")
# Más eficiente si se usa múltiples veces
patron = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')

textos = [
    "SSN: 123-45-6789",
    "Código: 987-65-4321",
    "No hay SSN aquí"
]

for texto in textos:
    if patron.search(texto):
        print(f"SSN encontrado en: {texto}")
print()

# ============================================
# FINDITER
# ============================================

print("=== Finditer ===")
texto = "Python 3.9, Java 11, JavaScript ES6"
patron = r'(\w+)\s+([\d.]+|ES\d+)'

for match in re.finditer(patron, texto):
    print(f"Lenguaje: {match.group(1)}, Versión: {match.group(2)}")
    print(f"  Posición: {match.start()}-{match.end()}")
print()

# ============================================
# NO CAPTURAR GRUPO
# ============================================

print("=== Grupo No Capturado ===")
# (?:...) no captura
texto = "2024-01-15"
# Con captura
match = re.match(r'(\d{4})-(\d{2})-(\d{2})', texto)
print(f"Con captura: {match.groups()}")

# Sin captura del año
match = re.match(r'(?:\d{4})-(\d{2})-(\d{2})', texto)
print(f"Sin captura de año: {match.groups()}")
print()

# ============================================
# ESCAPAR CARACTERES ESPECIALES
# ============================================

print("=== Escapar Caracteres ===")
texto = "El precio es $100.50"
# Sin escapar (error)
# match = re.search(r'$\d+', texto)  # $ es especial

# Escapado
match = re.search(r'\$\d+', texto)
print(f"Precio: {match.group()}")

# re.escape para escapar automáticamente
caracteres = "$100.50"
patron = re.escape(caracteres)
print(f"Patrón escapado: {patron}")
