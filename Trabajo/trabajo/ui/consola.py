import sys
from Trabajo.trabajo.mundo.cine import Cine

class Consola:
    def __init__(self):
        self.cine = Cine()
        self.opciones = {
            "1": self.registrarse,
            "2": self.ingresar_cuenta,
            "3": self.salir
        }
        self.menu_opciones_mostrar = {
            "1": self.reservar,
            "2": self.ver_comestibles_disponibles,
            "3": self.agregar_comestibles_bolsa,
            "4": self.ver_bolsa,
            "5": self.eliminar_item_de_bolsa,
            "6": self.comprar_bolsa,
            "7": self.ver_estadisticas,
            "8": self.salir
        }

    def mostrar_menu(self):
        print(""" 
                ==✧･ﾟ: *✧･ﾟ:*  ───── ⋆⋅☆⋅⋆ ─────  ✧･ﾟ: *✧･ﾟ:*==
                |                                             |
                |      ‧͙⁺˚*･༓☾ BIENVENIDO AL CINE ☽༓･*˚⁺‧͙       |
                |                                             | 
                ✧･ﾟ: *✧･ﾟ:* ======================= ✧･ﾟ: *✧･ﾟ:*
                |                                             |
                |              MENU DE OPCIONES:              |
                |                                             |
                ====✧･ﾟ: *✧･ﾟ:*================================
                |                                             |
                |             1: REGISTRARSE                  |
                |             2: INGRESAR CUENTA              |
                |             3: SALIR                        |
                |                                             |
                ===============================✧･ﾟ: *✧･ﾟ:*=====
                
                """)

    def mostrar_menu_principal(self):
        print("""
                        ✧･ﾟ: *✧･ﾟ:* ======================= ✧･ﾟ: *✧･ﾟ:*
                        |                                             |
                        |                 MENU PRINCIPAL:             |
                        |                                             |
                        ====✧･ﾟ: *✧･ﾟ:*================================
                        |                                             |
                        |           1: RESERVAR                       |
                        |           2: COMESTIBLES DISPONIBLES        |
                        |           3: AGREGAR COMESTIBLES A LA BOLSA |
                        |           4: VER BOLSA                      |
                        |           5: ELIMINAR ITEM DE BOLSA         |
                        |           6: COMPRAR BOLSA                  |
                        |           7: VER ESTADISTICAS               |
                        |           8: SALIR                          |
                        |                                             |
                        ===============================✧･ﾟ: *✧･ﾟ:*=====
                        
                        """)



    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción : ")
            funcion = self.opciones.get(opcion)
            if funcion is not None:
                funcion()
            else:
                print(f"\n {opcion} no es una opción válida")

    def ejecutar_menu_principal(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción : ")
            funcion = self.menu_opciones_mostrar.get(opcion)
            if funcion is not None:
                funcion()
            else:
                print(f"\n {opcion} no es una opción válida")

    def registrarse(self):
        print("\n REGISTRAR USUARIO ")
        cedula = input("\n ingrese cedula : ")
        nombre = input("\n ingrese nombre : ")
        clave = input("\n ingrese su clave :")
        if self.cine.registrar_usuario(cedula, nombre, clave):
            print("\n EL REGISTRO SE HIZO EXITOSAMENTE")
        else:
            print("\n YA EXISTE UNA CUENTA CON ESTA CEDULA")


    def ingresar_cuenta(self):

        while True:
            print("""
                ✧･ﾟ: *✧･ﾟ:* ======================= ✧･ﾟ: *✧･ﾟ:*
                |                                             |
                |              MENU DE INGRESO:               |
                |                                             |
                ====✧･ﾟ: *✧･ﾟ:*================================
                |                                             |
                |             1: INGRESAR COMO ADMIN          |
                |             2: INGRESAR USUARIO             |
                |             3: VOLVER                       |
                |                                             |
                ===============================✧･ﾟ: *✧･ﾟ:*=====
                
                """)
                    

            opcion = input("ingrese la opcion : ")
            respuesta = self.cine.iniciar_sesion_opcion(opcion)
            if respuesta is not None:

                if respuesta == "iniciar sesion admin":
                    print(f"""
                    =========================
                     {respuesta}
                    =========================
                    """)
                    clave = input("\n ingrese la clave : ")
                    if self.cine.iniciar_sesion_admin(clave):
                        print("\n ingreso exitoso")

                    else:
                        print("\n contraseña invalida")

                elif respuesta == "volver":
                    self.ejecutar()

                else:
                    print(f"""
                     ========================
                      {respuesta}
                     ========================
                    """)

                    cedula = input("\n ingrese cedula : ")
                    clave = input("\n ingrese su clave : ")
                    self.usuario_app = self.cine.iniciar_sesion_usuario(cedula, clave)

                    if self.usuario_app is not None:
                        if self.usuario_app == 0:
                            print("\n ingreso con exito")
                            self.ejecutar_menu_principal()

                        else:
                            print("\n contraseña invalida")

                    else:
                        print("\n esta cuenta no esta registrada")

            else:
                print("\n INGRESE UNA OPCION CORRECTA")

    def reservar(self):
        print("no implementado aun")

    def ver_comestibles_disponibles(self):
        print("""
                =========================
                 COMESTIBLES DISPONIBLES
                =========================
                """)
        lista_comestibles = self.cine.mostrar_comestibles_disponibles()
        for i in range(len(lista_comestibles)):
            print(f"{i + 1}. {lista_comestibles[i][0]}")

    def agregar_comestibles_bolsa(self):
        nombre: str = input("\n ingrese el nombre del producto : ")
        cantidad: int = int(input("\n ingrese la cantidad que desea :"))
        resultado = self.cine.agregar_comestibles_bolsa(nombre, cantidad)
        if resultado == 0:
            print(f"\n se agregaron {cantidad} de {nombre} a la bolsa")
        elif resultado == 1:
            print(f"\n no hay suficientes unidades disponibles de {nombre} ")
        else:
            print(f"\n no se encontro el comestible {nombre}")



    def ver_bolsa(self):
        print("""
        ====================
         PRODUCTOS EN BOLSA
        ====================
        """)
        lista_items = self.cine.mostrar_items_bolsa()
        for i in range(len(lista_items)):
            print(f"\n {i+1}. {lista_items[i]}")

    def eliminar_item_de_bolsa(self):
        self.ver_bolsa()
        indice: int = int(input("\n ingrese el numero del elemento que desea eliminar : "))
        if self.cine.eliminar_item(indice) is True:
            print("\n ELEMENTO ELIMINADO")
        else:
            print("\n EL NUMERO INGRESADO NO ESTA EN LA LISTA")
    def comprar_bolsa(self):
        print("no implementado aun")
    def ver_estadisticas(self):
        print("no implementado aun")

    def salir(self):

        print("GRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)