from typing import Optional
import numpy as np
#
class Comestible:
    def __init__(self, nombre: str, descripcion: str, cantidad_disponible: int, precio_unitario: float):
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.cantidad_disponible: int = cantidad_disponible
        self.precio_unitario: float = precio_unitario

    def unidades_disponibles(self,cantidad: int) -> bool:
        return self.cantidad_disponible >= cantidad



class Pelicula:

    def __init__(self,nombre: str, duracion:int, genero: str, sinopsis: str):
        self.nombre: str = nombre
        self.duracion: int = duracion
        self.genero: str = genero
        self.sinopsis: str = sinopsis

class Sala:

    def __init__(self, hora: str, precio_boleta: float, pelicula: Pelicula):
        self.asientos = np.array([
            ("o", "o", "o", "o", "o"),
            ("o", "o", "o", "o", "o"),
            ("o", "o", "o", "o", "o"),
            ("o", "o", "o", "o", "o")
        ])
        self.hora: str = hora
        self.precio_boleta: float = precio_boleta
        self.pelicula: Pelicula = pelicula


class Item:
    def __init__(self, producto, cantidad: int):
        self.producto = producto
        self.cantidad: int = cantidad
        self.total = 0

class Bolsa:
    def __init__(self):
        self.items = []
        self.total = 0

    def agregar_item(self, producto, cantidad):
        item = Item(producto, cantidad)
        self.items.append(item)


class Usuario:
    def __init__(self, cedula: str, nombre: str, clave: str):
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.clave: str = clave
        self.bolsa: Bolsa = Bolsa()
    def agregar_comestible_bolsa(self,comestible:Comestible,cantidad:int):
        self.bolsa.agregar_item(comestible, cantidad)

class Cine:

    def __init__(self):
        self.total_acumulado: float = 0
        self.comestibles: dict[str:Comestible] = {}
        self.usuarios: dict[str: Usuario] = {}
        self.clave_admin = 10111
        self.usuario_actual: Usuario = Usuario("", "", "")



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
        :return: "iniciar sesion admin" si desea iniciar como admin<br>
        "iniciar sesion usuario" si desea iniciar como un usuario <br>
        "volver" si desea regresar al menu anterior
        None si es una opcion por fuera del rango
        """
        if (opcion == "1") or (opcion == "2") or (opcion == "3"):
            if opcion == "1":
                return "iniciar sesion admin"
            elif opcion == "3":
                return "volver"
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
            self.usuario_actual = usuario
            return 0
        else:
            return 1

    def iniciar_sesion_admin(self, clave: str) -> bool:
        if self.clave_admin == clave:
            return True
        else:
            return False

    def buscar_comestible(self, nombre: str) -> Optional[Comestible]:
        if nombre in self.comestibles.keys():
            return self.comestibles[nombre]
        else:
            return None
    def agregar_comestibles_bolsa(self, nombre:str, cantidad: int) -> int:

        comestible = self.buscar_comestible(nombre)

        if comestible is not None:
            if comestible.unidades_disponibles(cantidad):

                self.usuario_actual.agregar_comestible_bolsa(comestible, cantidad)
                return 0
            else:
                return 1
        else:
            return 2
#



