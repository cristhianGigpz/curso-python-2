from datetime import datetime

name = "Cristhian"
team = "Gigpz"
year = 1990

text_format = "HOla, {} bienvenido al equipo de {}.".format(name, team)
print(text_format)

text_fstring = f"Hola, {name} bienvenido al equipo de {team}."
print(text_fstring)

print(f"la suma de 2 + 3 es igual a {2 + 3}")

print(f"tu nombre es {name.upper()} y tienes {2025-year} años.")

edad = 35
text_if = f"{'Eres mayor de edad' if edad >= 18 else 'Eres menor de edad'}"
print(text_if)

# fstrings para formato numerico
precio = 49.9923
impuesto = 0.075
total = precio * (1 + impuesto)
print(f"El precio total con impuesto es: {total:.2f}")

stock_producto = 15.6789
print(f"El stock disponible es: {stock_producto:.1f} unidades")

id_producto = 27
print(f"El ID del producto es: {id_producto:05d}")

now = datetime.now()
print(f"Fecha y hora actual: {now:%Y-%m-%d %H:%M:%S}")
dia_semana = now.strftime("%A")
print(f"Hoy es: {dia_semana}")  # Día de la semana en texto completo