class TaskList:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Índice de tarea inválido")

    def mostrar_tareas(self):
        if self.tareas:
            print("Tareas:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")
        else:
            print("No hay tareas")
