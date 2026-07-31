ventas = [
    {"producto": "Refresco",  "precio": 18,  "cantidad": 12},
    {"producto": "Pan",       "precio": 22,  "cantidad": 30},
    {"producto": "Leche",     "precio": 25,  "cantidad": 8},
    {"producto": "Chicles",   "precio": 5,   "cantidad": 40},
    {"producto": "Jabón",     "precio": 38,  "cantidad": 5},
    {"producto": "Agua",      "precio": 12,  "cantidad": 20},
    {"producto": "Galletas",  "precio": 32,  "cantidad": 15},
]

total_ingresos = sum(venta["precio"] * venta["cantidad"] for venta in ventas)
max_ingreso, p, pr, c = max((venta["precio"] * venta["cantidad"], venta["producto"], venta["precio"], venta["cantidad"]) for venta in ventas)
mayor_a_20 = sum(1 for venta in ventas if venta["precio"] > 20)

print("=== Reporte Nocturno de la Tienda ===\n")
print(f"Total de ingresos del día:         ${total_ingresos:,}")
print(f"Producto que más ingresó:          ${max_ingreso:,} ({p}: {pr} x {c})")
print(f"Productos con precio mayor a $20:  {mayor_a_20}")
