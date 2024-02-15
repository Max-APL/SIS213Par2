

def mostrar_menu():
    print("* "*21)
    print("*   SIS-213\t\t\t\t*")
    print("*   Aplicación de Lista de Tareas \t*")
    print("*   Integrantes: \t\t\t*")
    print("*   1. Marco Reynolds\t\t\t*")
    print("*   2. Max Pasten\t\t\t*")
    print("* "*21)
    print("1. Ver lista de tareas")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")

def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("=== Lista de Tareas ===")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
        elif opcion == "2":
            nueva_tarea = input("Ingresa la nueva tarea: ")
            tareas.append(nueva_tarea)
            print("¡Tarea agregada correctamente!")
        elif opcion == "3":
            if tareas:
                tarea_completada = int(input("Ingresa el número de la tarea completada: "))
                if 1 <= tarea_completada <= len(tareas):
                    del tareas[tarea_completada - 1]
                    print("¡Tarea marcada como completada!")
                else:
                    print("Número de tarea inválido.")
            else:
                print("No hay tareas para marcar como completadas.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
