class TaskList:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea, estado="En curso"):
        tarea.estado = estado
        self.tareas.append(tarea)

    def completar_tarea(self, indice):
        msg = False
        for t in self.tareas:
            if t.idT == indice:
                t.estado = "Completada"
                print()
                print("-"*30)
                print()
                print(f"Tarea {t.nombre} completada")
                print()
                print("-"*30)
                msg = True
                
        if msg==False:
            print()
            print("-"*30)
            print()
            print("Índice de tarea inválido o ya completado")
            print()
            print("-"*30)
        
        

    def reporte_tares_encurso (self):
        en_curso = [tarea for tarea in self.tareas if tarea.estado == "En curso"]
        if en_curso:
            print()
            print("-"*30)
            print()
            print("Tareas en curso:")
            for tarea in en_curso:
                print(tarea)
            print()
            print("-"*30)
        else:
            print()
            print("-"*30)
            print()
            print("No hay tareas en curso")
            print()
            print("-"*30)

    def mostrar_tareas(self):
        if len(self.tareas) != 0:
            print()
            print("-"*30)
            print()
            print("Tareas:")
            for tarea in self.tareas:
                print(tarea)
            print()
            print("-"*30)
        else:
            print()
            print("-"*30)
            print()
            print("No hay tareas")
            print()
            print("-"*30)
    def reporte_tareas_completadas(self):
        completadas = [tarea for tarea in self.tareas if tarea.estado == "Completada"]
        if completadas:
            print()
            print("-"*30)
            print()
            print("Tareas completadas:")
            for tarea in completadas:
                print(tarea)

            print()
            print("-"*30)
        else:
            print()
            print("-"*30)
            print()
            print("No hay tareas completadas")
            print()
            print("-"*30)