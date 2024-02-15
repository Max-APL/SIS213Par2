## Enunciado

- Ejercicio: Desarrollo de una Aplicación de Lista de Tareas
- Descripción del Proyecto:
Crear una aplicación de lista de tareas que permita a los usuarios agregar nuevas tareas, marcarlas como completadas, eliminarlas de la lista, generar reportes por estados de tareas en curso y tareas completadas.
La aplicación debe ser implementada utilizando un lenguaje de programación de su elección (por ejemplo, Python, Java o JavaScript) y debe incluir una interfaz de línea de comandos (CLI) para interactuar con ella (Menú de Opciones).
Se debe usar Programación Orientada a Objetos o Programación Modular o ambos
- Pasos del Ejercicio:
1. Planificación y Diseño: Como equipo, discutan y diseñen la estructura general de la aplicación. Decidan qué funcionalidades incluir y cómo organizar el código.
2. Configuración del Repositorio Git: Creen un nuevo repositorio en GitHub para el proyecto. Uno de los miembros del equipo puede crear el repositorio y agregar al otro miembro como colaborador.
3. Creación de Ramas: Cada pareja de programadores crea una rama nueva en el repositorio para trabajar en su parte del proyecto. Por ejemplo, una rama podría ser "feature/agregar-tareas" para implementar la funcionalidad de agregar tareas.
4. Desarrollo de Funcionalidades: Las parejas trabajan juntas en sus respectivas ramas para implementar las funcionalidades asignadas. Utilicen técnicas de programación por pares, como el piloto-copiloto, para escribir código de manera colaborativa.
5. Revisión de Código: Una vez que una pareja haya completado una parte del trabajo, crean un pull request para fusionar sus cambios con la rama principal. La otra pareja revisa el código y ofrece sugerencias o correcciones si es necesario.
6. Pruebas y Depuración: Después de que los cambios se hayan fusionado con la rama principal, todas las parejas realizan pruebas exhaustivas para asegurarse de que la funcionalidad implementada funcione correctamente. Si se encuentran errores, trabajan juntos para solucionarlos.
7. Documentación y Comentarios: A medida que avanzan, asegúrense de documentar el código y agregar comentarios descriptivos para facilitar la comprensión del mismo por parte de otros miembros del equipo. Así mismo crear un archivo readme en el repositorio para describir la Planificación y Diseño, Ramas creadas, Descripción de funcionalidades y asignación de tareas.
8. Finalización y Revisión: Una vez que todas las funcionalidades estén implementadas y probadas, realicen una revisión final del código y asegúrense de que la aplicación funcione como se espera.

Notas Adicionales:
- Durante todo el ejercicio, las parejas deben colaborar estrechamente y asegurarse de comunicarse de manera efectiva para evitar conflictos y mantenerse al tanto del progreso.
- Utilicen herramientas de Git, como ramas, pull requests y comentarios en el código, para gestionar el flujo de trabajo de manera eficiente y mantener un registro claro de los cambios realizados.
- Al finalizar el ejercicio, realicen una sesión de retroalimentación para discutir lo que aprendieron y cualquier área que puedan mejorar en futuros proyectos.
- Agregar al repositorio al docente katia.mansilla@ucb.edu.bo
- Subir a NEO el link del repositorio

## Análisis del Problema

El problema propuesto implica el desarrollo de una aplicación de lista de tareas que tenga las siguientes características:

- **Agregar Nuevas Tareas:** Los usuarios deben poder agregar nuevas tareas a la lista.
- **Marcar Tareas como Completadas:** Debe ser posible marcar las tareas como completadas una vez que se han realizado.
- **Eliminar Tareas:** Los usuarios deben poder eliminar tareas de la lista.
- **Generar Reportes:** La aplicación debe ser capaz de generar reportes que muestren el estado de las tareas, tanto las en curso como las completadas.
- **Interfaz de Línea de Comandos:** La interacción con la aplicación se realizará a través de una interfaz de línea de comandos, presentando al usuario un menú de opciones.

Para abordar este problema, es necesario diseñar una estructura que permita gestionar eficientemente las tareas y su estado, así como manejar la interacción con el usuario de manera intuitiva y clara.

## Solución

Para resolver este problema, se puede implementar una aplicación utilizando el lenguaje de programación Python y aprovechando la Programación Orientada a Objetos (POO) para modelar las tareas y la lógica de la aplicación. Además, se puede utilizar la Programación Modular para organizar el código de manera más legible y mantenible.

La aplicación constará de las siguientes clases principales:

- **Task:** Esta clase representará una tarea individual. Tendrá atributos como descripción y estado (pendiente o completada), así como métodos para marcar la tarea como completada y obtener su estado.
- **TaskList:** Esta clase será responsable de gestionar la lista de tareas. Tendrá métodos para agregar nuevas tareas, marcar tareas como completadas, eliminar tareas y generar reportes de estado.
- **Menu:** Esta clase manejará la interfaz de línea de comandos, mostrando al usuario un menú de opciones y gestionando la entrada del usuario para ejecutar las acciones correspondientes.

El desarrollo de la aplicación se realizará iterativamente, implementando cada funcionalidad paso a paso y realizando pruebas para garantizar su correcto funcionamiento. Una vez completada, la aplicación proporcionará una forma eficiente y fácil de administrar listas de tareas, brindando al usuario la capacidad de agregar, completar y eliminar tareas, así como generar informes sobre su estado.
