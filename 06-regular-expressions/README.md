# Expresiones Regulares en Python

## ¿Qué son las Regex?

Las expresiones regulares (regex) son patrones para buscar y manipular texto. Python proporciona el módulo `re` para trabajar con ellas.

## Sintaxis Básica

### Caracteres Especiales
- `.`: Cualquier carácter (excepto nueva línea)
- `^`: Inicio de cadena
- `$`: Fin de cadena
- `*`: 0 o más repeticiones
- `+`: 1 o más repeticiones
- `?`: 0 o 1 repetición
- `{n}`: Exactamente n repeticiones
- `{n,m}`: Entre n y m repeticiones
- `[]`: Conjunto de caracteres
- `|`: OR lógico
- `()`: Grupo de captura
- `\`: Escape

### Clases de Caracteres
- `\d`: Dígito [0-9]
- `\D`: No dígito
- `\w`: Palabra [a-zA-Z0-9_]
- `\W`: No palabra
- `\s`: Espacio en blanco
- `\S`: No espacio

## Funciones del Módulo re

- `re.match()`: Busca al inicio
- `re.search()`: Busca en toda la cadena
- `re.findall()`: Encuentra todas las coincidencias
- `re.finditer()`: Iterator de coincidencias
- `re.sub()`: Sustituir
- `re.split()`: Dividir

## Flags

- `re.IGNORECASE` o `re.I`: Ignorar mayúsculas/minúsculas
- `re.MULTILINE` o `re.M`: ^ y $ para cada línea
- `re.DOTALL` o `re.S`: . coincide con nueva línea
- `re.VERBOSE` o `re.X`: Permite comentarios

## Grupos

- `()`: Grupo de captura
- `(?:...)`: Grupo sin captura
- `(?P<name>...)`: Grupo nombrado
- `\1, \2`: Referencias a grupos

## Usos Comunes

- Validación de emails, URLs, teléfonos
- Extracción de información
- Limpieza y formateo de texto
- Parsing de logs
