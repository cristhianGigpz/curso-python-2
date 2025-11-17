"""
Ejercicios de Módulos y Paquetes
"""

# Ejercicio 1: Crear módulo de conversiones
# Crea un módulo 'conversiones.py' con funciones para:
# - celsius_a_fahrenheit
# - fahrenheit_a_celsius
# - km_a_millas
# - millas_a_km

# Ejercicio 2: Crear módulo de validaciones
# Crea un módulo 'validaciones.py' con funciones para validar:
# - email
# - teléfono
# - DNI/NIF
# - código postal

# Ejercicio 3: Crear paquete 'calculadora'
# Estructura:
# calculadora/
#   __init__.py
#   basicas.py (suma, resta, multiplicación, división)
#   avanzadas.py (potencia, raíz, logaritmo)
#   estadisticas.py (promedio, mediana, moda)

# Ejercicio 4: Implementar lazy loading
# Crea un módulo que solo importe componentes pesados cuando se usen

# Ejercicio 5: Crear módulo configurable
# Crea un módulo que lea configuración de un archivo .env o config.ini

# Ejercicio 6: Paquete con namespace
# Crea un paquete que use __all__ para controlar qué se exporta

# Ejercicio 7: Módulo con singleton
# Crea un módulo que implemente un patrón singleton para configuración

# Ejercicio 8: Plugin system
# Crea un sistema que cargue plugins dinámicamente desde un directorio

# Ejercicio 9: Módulo de utilidades de strings
# Funciones: snake_case, camelCase, PascalCase, kebab-case

# Ejercicio 10: Crear paquete distribuible
# Crea un paquete completo con:
# - setup.py
# - README.md
# - requirements.txt
# - tests/

# Ejemplo de solución para ejercicio 1
"""
# conversiones.py
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def km_a_millas(km):
    return km * 0.621371

def millas_a_km(millas):
    return millas / 0.621371
"""

if __name__ == "__main__":
    print("Implementa los ejercicios creando archivos separados")
