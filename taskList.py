class TaskList:
    def __init__(self):
        self.tareas = []

    # Funcion para agregar una tarea
    def agregar_tarea(self, tarea, estado="En curso"):
        tarea.estado = estado
        self.tareas.append(tarea)

    # Funcion para eliminar una tarea
    def eliminar_tarea(self, indice):
        msg = False
        for t in self.tareas:
            if t.idT == indice:
                self.tareas.remove(t)
                msg = True
                print()
                print("-"*30)
                print()
                print(f"Tarea {t.nombre} eliminada")
                print()
        if msg==False:
            print()
            print("-"*30)
            print()
            print("No se encontró la tarea con el índice ingresado")
            print()

    # Funcion para completar tarea
    def completar_tarea(self, indice):
        msg = False
        #Selecciona de la lista de tareas la tarea con el id seleccionado y la marca como completada
        for t in self.tareas:
            if t.idT == indice:
                t.estado = "Completada"
                print()
                print("-"*30)
                print()
                print(f"Tarea {t.nombre} completada")
                print()
                msg = True
                
        if msg==False:
            print()
            print("-"*30)
            print()
            print("Índice de tarea inválido o ya completado")
            print()

    # Funcion para mostrar tareas en curso
    def reporte_tares_encurso (self):
        # Agraga a la lista solo las tareas con el estado en curso
        en_curso = [tarea for tarea in self.tareas if tarea.estado == "En curso"]
        if en_curso:
            print()
            print("-"*30)
            print()
            print("Tareas en curso:")
            for tarea in en_curso:
                print(tarea)
            print()
        else:
            print()
            print("-"*30)
            print()
            print("No hay tareas en curso")
            print()

    # Funcion para mostrar todas las tareas
    def mostrar_tareas(self):
        # Valida que existan tareas en la lista
        if len(self.tareas) != 0:
            print()
            print("-"*30)
            print()
            print("Tareas:")
            for tarea in self.tareas:
                print(tarea)
            print()
        else:
            print()
            print("-"*30)
            print()
            print("No hay tareas")
            print()

     # Funcion para mostrar tareas completadas       
    def reporte_tareas_completadas(self):
        # Agraga a la lista solo las tareas con el estado completado
        completadas = [tarea for tarea in self.tareas if tarea.estado == "Completada"]
        if completadas:
            print()
            print("-"*30)
            print()
            print("Tareas completadas:")
            for tarea in completadas:
                print(tarea)

            print()
        else:
            print()
            print("-"*30)
            print()
            print("No hay tareas completadas")
            print()