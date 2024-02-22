class TaskList:
    def __init__(self):
        self.tareas = []

    # Funcion para agregar una tarea
    def agregar_tarea(self, tarea, estado="En curso"):
        tarea.estado = estado
        self.tareas.append(tarea)

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

    def reporte_tareas_en_curso(self):
        en_curso = [tarea for tarea in self.tareas if tarea.estado == "En curso"]
        if en_curso:
            print("\n" + "-"*60)
            print("Tareas en curso:")
            print("{:<20} {:<15} {:<15} {:<10} {:<10}".format("Descripcion", "Fecha límite", "Hora límite", "Prioridad", "Estado"))
            for tarea in en_curso:
                print("{:<20} {:<15} {:<15} {:<10} {:<10}".format(tarea.nombre, tarea.fecha_limite, tarea.hora_limite, tarea.prioridad, tarea.estado))
            print()
        else:
            print("\n" + "-"*60)
            print("No hay tareas en curso\n")

    def mostrar_tareas(self):
        if self.tareas:
            print("\n" + "-"*60)
            print("Tareas:")
            print("{:<20} {:<15} {:<15} {:<10} {:<10}".format("Descripcion", "Fecha límite", "Hora límite", "Prioridad", "Estado"))
            for tarea in self.tareas:
                print("{:<20} {:<15} {:<15} {:<10} {:<10}".format(tarea.nombre, tarea.fecha_limite, tarea.hora_limite, tarea.prioridad, tarea.estado))
            print()
        else:
            print("\n" + "-"*60)
            print("No hay tareas\n")

    def reporte_tareas_completadas(self):
        completadas = [tarea for tarea in self.tareas if tarea.estado == "Completada"]
        if completadas:
            print("\n" + "-"*60)
            print("Tareas completadas:")
            print("{:<20} {:<15} {:<15} {:<10} {:<10}".format("Descripcion", "Fecha límite", "Hora límite", "Prioridad", "Estado"))
            for tarea in completadas:
                print("{:<20} {:<15} {:<15} {:<10} {:<10}".format(tarea.nombre, tarea.fecha_limite, tarea.hora_limite, tarea.prioridad, tarea.estado))
            print()
        else:
            print("\n" + "-"*60)
            print("No hay tareas completadas\n")