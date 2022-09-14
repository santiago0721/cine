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
        self.clave_admin = "10111"



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

    def iniciar_sesion_opcion(self,opcion: str) -> Optional[str]:
        """
        chequea la opcion ingresada y devuelve el valor ingresado de este estar en el rango
        :param opcion: (str) es la opcion que se puede escoger en el meno de iniciar sesion
        :return: "1" si desea iniciar como admin<br>
        "2" si desea iniciar como un usuario <br>
        None si es una opcion por fuera del rango
        """
        if (opcion == "1") or (opcion == "2"):
            if opcion == "1":
                return "iniciar sesion admin"
            else:
                return "iniciar sesion usuario"
        else:
            return None


    def iniciar_sesion_usuario(self,cedula: str, clave:str) -> Optional[int]:
        if cedula in self.usuarios.keys():
            usuario= self.usuarios[cedula]
        else:
            return None
        if usuario.clave == clave:
            return 0
        else:
            return 1

    def iniciar_sesion_admin(self, clave: str) -> bool:
        if self.clave_admin == clave:
            return True
        else:
            return False














