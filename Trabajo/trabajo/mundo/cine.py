from typing import Optional

class Producto:
    def __init__(self, nombre: str, resumen: str, tipo: str, cantidad_disponible: int, precio_unitario: float):
        self.nombre: str = nombre
        self.resumen: str = resumen
        self.tipo: str = tipo
        self.cantidad_disponible: int = cantidad_disponible
        self.precio_unitario: float = precio_unitario


class Item:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto: Producto = producto
        self.cantidad: int = cantidad


class Bolsa:
    def __init__(self):
        self.items = []
        self.total = 0


class Usuario:
    def __init__(self, cedula: str, nombre: str, clave: str):
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.clave: str = clave
        self.bolsa: Bolsa = Bolsa()


class Cine:

    def __init__(self):
        self.total_acumulado: float = 0
        self.productos: list[Producto] = []
        self.usuarios: dict[str: Usuario] = {}


    def registrar_usuario(self, cedula: str, nombre: str, clave: str)-> bool:

        if self.buscar_usuario(cedula) is None:
            usuario = Usuario(cedula, nombre, clave)
            self.usuarios[cedula] = usuario
            return True
        else:
            return False

    def buscar_usuario(self, cedula: str) -> Optional[Usuario]:
        if cedula in self.usuarios.keys():
            return self.usuarios[cedula]

        else:
            return None







