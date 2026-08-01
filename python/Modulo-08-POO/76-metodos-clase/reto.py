class Pizzeria:
    pizzas_vendidas = 0

    def __init__(self, sabor):
        self.sabor = sabor
        Pizzeria.pizzas_vendidas += 1

    @classmethod
    def reporte_ventas(cls):
        print(f"¡Hemos vendido {cls.pizzas_vendidas} pizzas en total!")

pizza1 = Pizzeria("Pepperoni")
pizza2 = Pizzeria("Hawaiana")
pizza3 = Pizzeria("Queso")

Pizzeria.reporte_ventas()
