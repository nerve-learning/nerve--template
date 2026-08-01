import json
import os

ARCHIVO_INVENTARIO = "inventario.json"

class Categoria:
    def __init__(self, nombre, descripcion=""):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"Categoría: {self.nombre}"
        
    def to_dict(self):
        return {"nombre": self.nombre, "descripcion": self.descripcion}

class Producto:
    def __init__(self, id_prod, nombre, precio, cantidad, categoria):
        self.id_prod = str(id_prod)
        self.nombre = nombre
        self._precio = float(precio)
        self.cantidad = int(cantidad)
        self.categoria = categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = float(valor)

    def valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"[{self.id_prod}] {self.nombre} - ${self.precio} (Stock: {self.cantidad}) - {self.categoria.nombre}"

    def to_dict(self):
        return {
            "tipo": "Normal",
            "id_prod": self.id_prod,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "categoria": self.categoria.to_dict()
        }

class ProductoPerecedero(Producto):
    def __init__(self, id_prod, nombre, precio, cantidad, categoria, dias_caducidad):
        super().__init__(id_prod, nombre, precio, cantidad, categoria)
        self.dias_caducidad = int(dias_caducidad)

    def __str__(self):
        return super().__str__() + f" [Caduca en {self.dias_caducidad} días]"

    def to_dict(self):
        d = super().to_dict()
        d["tipo"] = "Perecedero"
        d["dias_caducidad"] = self.dias_caducidad
        return d

class Inventario:
    def __init__(self):
        self.productos = {}
        self.cargar_datos()

    def agregar(self, producto):
        self.productos[producto.id_prod] = producto
        self.guardar_datos()

    def eliminar(self, id_prod):
        if str(id_prod) in self.productos:
            del self.productos[str(id_prod)]
            self.guardar_datos()
            return True
        return False

    def buscar(self, nombre):
        resultados = []
        for p in self.productos.values():
            if nombre.lower() in p.nombre.lower():
                resultados.append(p)
        return resultados

    def actualizar(self, id_prod, cantidad=None, precio=None):
        if str(id_prod) in self.productos:
            if cantidad is not None:
                self.productos[str(id_prod)].cantidad = int(cantidad)
            if precio is not None:
                self.productos[str(id_prod)].precio = float(precio)
            self.guardar_datos()
            return True
        return False

    def calcular_valor_total(self):
        return sum(p.valor_total() for p in self.productos.values())

    def verificar_stock_bajo(self, limite=5):
        bajos = []
        for p in self.productos.values():
            if p.cantidad <= limite:
                bajos.append(p)
        return bajos

    def __str__(self):
        return f"Inventario con {len(self.productos)} productos registrados."

    def guardar_datos(self):
        datos = [p.to_dict() for p in self.productos.values()]
        try:
            with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as f:
                json.dump(datos, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def cargar_datos(self):
        if not os.path.exists(ARCHIVO_INVENTARIO):
            return
        try:
            with open(ARCHIVO_INVENTARIO, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for d in datos:
                    cat = Categoria(d["categoria"]["nombre"], d["categoria"]["descripcion"])
                    if d["tipo"] == "Perecedero":
                        prod = ProductoPerecedero(d["id_prod"], d["nombre"], d["precio"], d["cantidad"], cat, d["dias_caducidad"])
                    else:
                        prod = Producto(d["id_prod"], d["nombre"], d["precio"], d["cantidad"], cat)
                    self.productos[prod.id_prod] = prod
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

if __name__ == "__main__":
    inv = Inventario()
    print(inv)
    
    cat_elec = Categoria("Electrónica", "Aparatos")
    cat_alim = Categoria("Alimentos", "Comida fresca")
    
    inv.agregar(Producto("1", "Laptop", 1200.0, 10, cat_elec))
    inv.agregar(ProductoPerecedero("2", "Manzanas", 1.5, 3, cat_alim, 7))
    inv.agregar(Producto("3", "Mouse", 25.0, 4, cat_elec)) 
    
    print("\n--- Productos en Inventario ---")
    for p in inv.productos.values():
        print(p)
        
    print(f"\nValor Total del Inventario: ${inv.calcular_valor_total():.2f}")
    
    print("\n--- Alertas de Stock Bajo (<= 5) ---")
    bajos = inv.verificar_stock_bajo(5)
    for b in bajos:
        print(f"ALERTA: {b.nombre} tiene solo {b.cantidad} unidades.")
