# Asistente Comercial Funtastic Playroom

## Qué construí

Construí una primera versión de un agente comercial para Funtastic Playroom, un salón infantil con cafetería y propuestas de cumpleaños.

El agente sirve para ayudar al equipo del salón a generar propuestas comerciales personalizadas a partir de paquetes estándar: Básica, Completa y Saludable.

También permite sugerir adicionales, responder preguntas frecuentes y preparar mensajes listos para enviar por WhatsApp.

Está pensado para reducir tareas repetitivas, ordenar la información comercial y mejorar la velocidad de respuesta a las familias.

## Cómo se lo pedí

Primero le pedí a ChatGPT que me ayudara a pensar ideas para un agente que asistiera en la generación de propuestas comerciales del salón:

```text
Mira, se me ocurrio crear un agente que me ayude con las propuestas del salon. Las propuestas son estandares pero personalizables. Se te ocurren ideas ?
```

Después le pedí que armara la estructura inicial del proyecto con la siguiente instrucción:

```text
Quiero armar la estructura inicial de un proyecto para un agente comercial de Funtastic Playroom.

El objetivo del proyecto es crear un asistente que ayude a generar propuestas comerciales personalizadas para cumpleaños infantiles, basado en paquetes estándar pero personalizables.

Creá o actualizá estos archivos:

1. README.md
Explicando el objetivo del proyecto, el problema que resuelve, cómo funcionaría el flujo cliente-formulario-agente-propuesta, y qué beneficios aporta.

2. instrucciones_agente.md
Con instrucciones claras para un futuro GPT personalizado llamado “Asistente Comercial Funtastic”. Debe recomendar paquetes, sugerir adicionales, generar mensajes de WhatsApp, responder preguntas frecuentes y crear un resumen interno operativo.

3. datos_propuesta.md
Con una estructura editable para cargar paquetes, adicionales, condiciones de reserva y preguntas frecuentes. Por ahora dejá placeholders claros donde luego vamos a completar la información real.

4. formulario/index.html
Un formulario web simple para solicitar datos de cumpleaños: nombre del adulto, WhatsApp, nombre del cumpleañero/a, edad, fecha, horario, cantidad de niños, cantidad de adultos, temática, tipo de propuesta deseada, adicionales de interés y comentarios.

5. formulario/styles.css
Estilo visual infantil, prolijo y pastel, alineado con una marca de salón infantil: colores suaves, tarjetas redondeadas, diseño mobile friendly.

No uses backend todavía. Solo HTML y CSS.
El proyecto debe ser simple, entendible para principiantes y apto para mostrar en una materia de MBA.
```

## Qué funciona

Se crearon los cinco archivos solicitados y se verificó que todos estén presentes. El formulario contiene los campos requeridos, utiliza controles HTML adecuados y está vinculado correctamente con su hoja de estilos.

También se comprobó que el proyecto no incorpore JavaScript, backend ni servicios externos. Los archivos fueron subidos a una rama de GitHub y se verificó que el contenido remoto coincida con la versión local. El pull request permite revisar los cambios antes de incorporarlos a la rama principal.

## Qué falta o qué falló

Todavía falta reemplazar los placeholders de `datos_propuesta.md` por los paquetes, precios, adicionales, condiciones de reserva y respuestas reales de Funtastic. Aunque se mencionan los paquetes Básica, Completa y Saludable, sus características comerciales aún deben cargarse y validarse.

El formulario es solamente visual: no guarda información, no envía mensajes y no está conectado con el agente. Tampoco se probó todavía el flujo completo con consultas reales de familias.

Durante la primera transferencia a GitHub apareció un error de codificación que dejó el texto remoto ilegible. El problema se detectó al comparar y leer los archivos subidos, y luego se corrigió con una nueva transferencia verificada. La rama principal no fue afectada.

## Qué aprendí

Aprendí que trabajar con un agente requiere definir con claridad el objetivo, las fuentes de información y los límites de lo que puede responder. También entendí que una buena instrucción no reemplaza la validación: es necesario revisar tanto el contenido generado como el resultado técnico. Separar los datos comerciales de las instrucciones facilita actualizar el proyecto sin rehacerlo. Por último, comprobé que conviene avanzar por etapas, empezando con una versión simple antes de agregar automatizaciones.
