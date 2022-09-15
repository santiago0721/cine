import sys
from Trabajo.trabajo.mundo.cine import Cine

class Consola:
    def __init__(self):
        self.cine = Cine()
        self.usuario_app = " "
        self.opciones = {
            "1": self.registrarse,
            "2": self.ingresar_cuenta,
            "3": self.salir
        }
        self.menu_opciones_mostrar = {
            "1": self.reservar,
            "2": self.agregar_comestibles_bolsa,
            "3": self.ver_bolsa,
            "4": self.eliminar_item_de_bolsa,
            "5": self.comprar_bolsa,
            "6": self.ver_estadisticas,
            "7": self.salir
        }

    def mostrar_menu(self):
        print("""
        \n 
        ++++++++++++++++++++
        BIENVENIDO AL CINE
        ++++++++++++++++++++
        \n
        -------------------
        1: REGISTRARSE
        2: INGRESAR CUENTA
        3: SALIR
        -------------------
        """)

    def mostrar_menu_principal(self):
        print("""
        ++++++++++++++++++++
            MENU INICIAL
        ++++++++++++++++++++
        \n
        -------------------
        1: RESERVAR
        2: AGREGAR COMESTIBLES A LA BOLSA
        3: VER BOLSA
        4: ELIMINAR ITEM DE BOLSA
        5: COMPRAR BOLSA
        6: VER ESTADISTICAS
        7: SALIR
        -------------------
        """)



    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            funcion = self.opciones.get(opcion)
            if funcion is not None:
                funcion()
            else:
                print(f"{opcion} no es una opción válida")

    def ejecutar_menu_principal(self):
        while True:
            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")
            funcion = self.menu_opciones_mostrar.get(opcion)
            if funcion is not None:
                funcion()
            else:
                print(f"{opcion} no es una opción válida")

    def registrarse(self):
        print("\n REGISTRAR USUARIO")
        cedula = input("ingrese cedula: ")
        nombre = input("ingrese nombre: ")
        clave = input("ingrese su clave :")
        if self.cine.registrar_usuario(cedula, nombre, clave):
            print("EL REGISTRO SE HIZO EXITOSAMENTE")
        else:
            print("YA EXISTE UNA CUENTA CON ESTA CEDULA")


    def ingresar_cuenta(self):

        while True:
            print("""
            -----------------------------
                    \n INICIAR SESIÓN:
                
                    1:INICIAR COMO ADMIN
                    2:USUARIO
                    3:VOLVER
                    
                    """)
            opcion = input("ingrese la opcion : ")
            respuesta = self.cine.iniciar_sesion_opcion(opcion)
            if respuesta is not None:

                if respuesta == "iniciar sesion admin":
                    print(f"""
                    -----------------------
                    {respuesta}
                    -----------------------
                    """)
                    clave = input("ingrese a clave ")
                    if self.cine.iniciar_sesion_admin(clave):
                        print("melos")

                    else:
                        print("contraseña invalida")

                elif respuesta == "volver":
                    self.ejecutar()

                else:
                    print(f"""
                     -----------------------
                    {respuesta}
                    -----------------------
                    """)

                    cedula = input("ingrese cedula : ")
                    clave = input("ingrese su clave : ")
                    self.usuario_app = self.cine.iniciar_sesion_usuario(cedula, clave)

                    if self.usuario_app is not None:
                        if self.usuario_app == 0:
                            print("ingreso con exito")
                            self.ejecutar_menu_principal()

                        else:
                            print("contraseña invalida")

                    else: print("esta cuenta no esta registrada")

            else:
                print("INGRESE UNA OPCION CORRECTA")

    def reservar(self):
        print("no implementado aun")

    def agregar_comestibles_bolsa(self):


    def ver_bolsa(self):
        pass

    def eliminar_item_de_bolsa(self):
        pass
    def comprar_bolsa(self):
        pass
    def ver_estadisticas(self):
        pass

    def salir(self):

        print("GRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)