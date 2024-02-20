class Task:
    def __init__(self, nombre, fecha_limite, hora_limite, prioridad, estado="En curso"):
        self.nombre = nombre
        self.fecha_limite = fecha_limite
        self.hora_limite = hora_limite
        self.prioridad = prioridad
        self.estado = estado

    def __str__(self):
        return f"{self.nombre} - Fecha límite: {self.fecha_limite} {self.hora_limite}, Prioridad: {self.prioridad}, Estado: {self.estado}"

