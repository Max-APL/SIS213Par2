class Task:
    def __init__(self, idT, nombre, fecha_limite, hora_limite, prioridad, estado="En curso"):
        self.idT = idT
        self.nombre = nombre
        self.fecha_limite = fecha_limite
        self.hora_limite = hora_limite
        self.prioridad = prioridad
        self.estado = estado

    # Funcion para mostrar los datos de la tarea
    def __str__(self):
        return f"{self.idT} {self.nombre} - Fecha límite: {self.fecha_limite} {self.hora_limite}, Prioridad: {self.prioridad}, Estado: {self.estado}"

