from task import Task
from taskList import TaskList
import datetime

class Menu:
    def __init__(self):
        self.lista_tareas = TaskList()

    # Funcion para mostrar la presentacion de la aplicacion
    def presentacion(self):
        print("* "*21)
        print("*   SIS-213\t\t\t\t*")
        print("*   Aplicación de Lista de Tareas \t*")
        print("*   Integrantes: \t\t\t*")
        print("*   1. Marco Reynolds\t\t\t*")
        print("*   2. Max Pasten\t\t\t*")
        print("* "*21)

    # Funcion para mostrar el menú de opciones
    def mostrar_menu(self):
        print("-"*30)
        print("Menú de opciones:")
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Ver lista de tareas")
        print("3. Reporte de tareas en curso")
        print("4. Reporte de tareas completadas")
        print("5. Salir")
        print("-"*30)

    # Funcion para validar el formato de la fecha
    def validar_fecha(self, fecha):
        try:
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    # Funcion para validar el formato de la hora
    def validar_hora(self, hora):
        try:
            datetime.datetime.strptime(hora, '%H:%M')
            return True
        except ValueError:
            return False

    # Funcion para ejecutar la aplicacion
    def ejecutar(self):
        self.presentacion()
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese su opción: ")

            # Agregar nueva tarea
            if opcion == "1":
                idT = len(self.lista_tareas.tareas) + 1
                nombre = input("Ingrese la descripción de la tarea: ")
                fecha_limite = input("Ingrese la fecha límite (DD/MM/AAAA): ")

                # Valida el formato de la fecha
                while not self.validar_fecha(fecha_limite):
                    print("Formato de fecha incorrecto. Por favor, ingrese la fecha en el formato DD/MM/AAAA.")
                    fecha_limite = input("Ingrese la fecha límite (DD/MM/AAAA): ")

                # Valida el formato de la hora
                hora_limite = input("Ingrese la hora límite (HH:MM): ")
                while not self.validar_hora(hora_limite):
                    print("Formato de hora incorrecto. Por favor, ingrese la hora en el formato HH:MM.")
                    hora_limite = input("Ingrese la hora límite (HH:MM): ")

                prioridad = input("Ingrese la prioridad: ")
                # Crea un objeto de tipo tarea
                tarea = Task(idT, nombre, fecha_limite, hora_limite, prioridad)
                self.lista_tareas.agregar_tarea(tarea)

            # Marcar tarea como completada
            elif opcion == "2":
                # Valida que existan tareas en la lista
                if len(self.lista_tareas.tareas) != 0:
                    idT = int(input("Ingrese el Id de la tarea a marcar como completada: "))
                    self.lista_tareas.completar_tarea(idT)
                else:
                    print()
                    print("-"*30)
                    print()
                    print("No hay tareas para marcar como completadas")
                    print()

                
            # Ver lista de tareas
            elif opcion == "3":
                self.lista_tareas.mostrar_tareas()

            # Reporte de tareas en curso
            elif opcion == "4":
                self.lista_tareas.reporte_tares_encurso()

            # Reporte de tareas completadas
            elif opcion == "5":
                self.lista_tareas.reporte_tareas_completadas()

            # Salir del programa
            elif opcion == "6":
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
