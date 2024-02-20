from task import Task
from taskList import TaskList

class Menu:
    def __init__(self):
        self.lista_tareas = TaskList()

    def mostrar_menu(self):
        print("* "*21)
        print("*   SIS-213\t\t\t\t*")
        print("*   Aplicación de Lista de Tareas \t*")
        print("*   Integrantes: \t\t\t*")
        print("*   1. Marco Reynolds\t\t\t*")
        print("*   2. Max Pasten\t\t\t*")
        print("* "*21)
        print("1. Agregar nueva tarea")
        print("2. Marcar tarea como completada")
        print("3. Ver lista de tareas")
        print("4. Reporte de tareas completadas")
        print("5. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese su opción: ")
            if opcion == "1":
                nombre = input("Ingrese la descripción de la tarea: ")
                fecha_limite = input("Ingrese la fecha límite (DD/MM/AAAA): ")
                hora_limite = input("Ingrese la hora límite (HH:MM): ")
                prioridad = input("Ingrese la prioridad: ")
                tarea = Task(nombre, fecha_limite, hora_limite, prioridad)
                self.lista_tareas.agregar_tarea(tarea)
            elif opcion == "2":
                indice = int(input("Ingrese el índice de la tarea a marcar como completada: ")) - 1
                tarea = self.lista_tareas.tareas[indice]
                tarea.estado = "Completada"
            elif opcion == "3":
                self.lista_tareas.mostrar_tareas()
            elif opcion == "4":
                self.lista_tareas.reporte_tareas_completadas()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")
