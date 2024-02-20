class TaskList:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea, estado="En curso"):
        tarea.estado = estado
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            print("Índice de tarea inválido")

    def mostrar_tareas(self):
        en_curso = [tarea for tarea in self.tareas if tarea.estado == "En curso"]
        if en_curso:
            print("Tareas en curso:")
            for tarea in en_curso:
                print(tarea)
        else:
            print("No hay tareas en curso")

    def reporte_tareas_completadas(self):
        completadas = [tarea for tarea in self.tareas if tarea.estado == "Completada"]
        if completadas:
            print("Tareas completadas:")
            for tarea in completadas:
                print(tarea)
        else:
            print("No hay tareas completadas")