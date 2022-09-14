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

    def mostrar_menu(self):
        print("""
        \n 
        ++++++++++++++++++++
        BIENVENIDO AL CINE
        ++++++++++++++++++++
        \n
        MENU DE OPCIONES:
        \n
        -------------------
        1: REGISTRARSE
        2: INGRESAR CUENTA
        3: SALIR
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
        print("\n INICIAR SESIÓN")

        while True:
            print("""
                    1:INICIAR COMO ADMIN
                    2:USUARIO
                    
                    """)
            opcion = input("ingrese la opcion : ")
            respuesta = self.cine.iniciar_sesion_opcion(opcion)
            if respuesta is not None:
                #poner otro while
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
                else:
                    print(f"""
                     -----------------------
                    {respuesta}
                    -----------------------
                    """)
                    cedula = input("ingrese cedula : ")
                    clave = input("ingrese su clave : ")
                    iniciar_sesion = self.cine.iniciar_sesion_usuario(cedula, clave)
                    if iniciar_sesion is not None:
                        if iniciar_sesion == 0:
                            print("ingreso con exito")
                        else:
                            print("contraseña invalida")

                    else: print("esta cuenta no esta registrada")

            else:
                print("INGRESE UNA OPCION CORRECTA")





    def salir(self):

        print("GRACIAS POR USAR LA APLICACIÓN")
        print(self.cine.usuarios)
        sys.exit(0)