# Asistente Comercial Funtastic Playroom

## Qué construí

Construí una primera versión de un agente comercial para **Funtastic Playroom**, un salón infantil con cafetería y propuestas de cumpleaños. El agente ayuda al equipo a generar propuestas personalizadas a partir de los datos de cada familia y de la propuesta comercial existente.

La propuesta real ya está documentada en el PDF del salón, que contiene los paquetes, adicionales, condiciones de reserva y preguntas frecuentes. Este proyecto no busca reemplazar ese documento, sino utilizarlo como base comercial para orientar las recomendaciones del agente.

También construí un formulario web simple para relevar los datos necesarios del cliente. El formulario no intenta explicar toda la propuesta ni incluir toda la letra chica: su función es ordenar la consulta inicial de la familia.

En esta primera versión, la vinculación entre GitHub y el GPT es manual: **GitHub funciona como repositorio maestro del proyecto y ChatGPT funciona como entorno operativo del agente**.

## Cómo se lo pedí

Primero le pedí a ChatGPT que me ayudara a pensar ideas para un agente que asistiera en la generación de propuestas comerciales del salón:

```text
Mira, se me ocurrio crear un agente que me ayude con las propuestas del salon. Las propuestas son estandares pero personalizables. Se te ocurren ideas ?
```

Luego le pedí que me explicara cómo operaría el sistema con los clientes:

```text
Y yo q le pasaria al cliente, como operaria todo esto?
```

Después definimos que el cliente podría completar un formulario web con estética del salón:

```text
el formulario tipo un link de html? formulario web, estariba bueno q eso acompañe la estetica del local
```

Más adelante, para crear la estructura inicial del proyecto en GitHub usando Codex, usé este prompt:

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

Finalmente, creé un GPT personalizado en ChatGPT con estas instrucciones principales:

```text
Sos el “Asistente Comercial Funtastic”, un agente especializado en ayudar a Funtastic Playroom a generar propuestas comerciales personalizadas para cumpleaños infantiles.

Tu objetivo es asistir al equipo comercial del salón, no hablar directamente como dueño ni confirmar reservas por cuenta propia.

Funciones principales:
1. Analizar los datos de una consulta de cliente.
2. Recomendar el paquete más adecuado: Básica, Completa o Saludable.
3. Sugerir adicionales relevantes según edad, temática, cantidad de invitados y preferencias.
4. Generar mensajes listos para enviar por WhatsApp.
5. Generar una propuesta comercial breve y clara.
6. Responder preguntas frecuentes usando solo las reglas comerciales cargadas.
7. Crear un resumen interno operativo para el equipo del salón.
8. Detectar datos faltantes antes de armar una propuesta definitiva.
```

## Qué funciona

El repositorio está creado y el README documenta el proceso de construcción y prueba. También existen los archivos base `instrucciones_agente.md`, `datos_propuesta.md`, `formulario/index.html` y `formulario/styles.css`.

El formulario HTML/CSS funciona como una demostración visual y permite relevar nombre del adulto, WhatsApp, datos del cumpleañero, fecha, horario, invitados, temática, tipo de propuesta, adicionales de interés y comentarios. Se mantuvo breve a propósito y no contiene toda la información comercial.

El GPT personalizado **Asistente Comercial Funtastic** fue creado y probado con un caso simulado de un cumpleaños de 6 años, temática de princesas, con 25 niños y 25 adultos. Para una familia que quería resolver todo sin ocuparse demasiado, recomendó la **Opción Completa**, sugirió adicionales coherentes y generó un mensaje de WhatsApp utilizable.

En esa prueba, el agente respetó límites importantes: no inventó precios, no confirmó disponibilidad de fecha y no confirmó una reserva sin seña.

El flujo actual es manual y deliberadamente simple: el cliente completaría un formulario corto, el equipo revisaría la información y el agente ayudaría a recomendar una opción y redactar el mensaje. Esta simplicidad fue elegida para entender la herramienta antes de automatizar el proceso.

```text
Cliente
   ↓
Completa un formulario corto
   ↓
El equipo revisa la información
   ↓
El agente interpreta la necesidad
   ↓
Recomienda una opción y adicionales
   ↓
Genera un mensaje comercial
   ↓
El equipo revisa, ajusta y envía
```

## Qué falta o qué falló

La información comercial ya existe en el PDF de propuesta. Lo que falta es avanzar, en una etapa posterior, en una estructuración más completa y mantenible de esa información dentro del repositorio o en una fuente editable. Ya existe una primera versión estructurada en `datos_propuesta.md`, pero deberá mantenerse actualizada cuando cambie la propuesta comercial.

Los precios no se incluyen en esta primera versión porque pueden cambiar. En el futuro podrían administrarse desde una planilla, un archivo de datos o un sistema interno que funcione como fuente comercial vigente.

El formulario todavía no guarda información y no está conectado con Google Sheets, un CRM, WhatsApp ni el GPT personalizado. Tampoco valida disponibilidad ni genera propuestas o archivos PDF automáticamente.

Durante el trabajo, GitHub tuvo un problema temporal de carga, pero luego se resolvió y los archivos quedaron accesibles en el repositorio.

El GPT fue creado y probado, pero no pudo compartirse públicamente desde esta cuenta porque en la configuración solo aparece la opción **“Solo yo”**.

También falta probar el agente con más casos reales o simulados: alternativas económicas, propuestas saludables, mayor cantidad de invitados, decoración propia, dudas sobre seña o cancelación y consultas por disponibilidad.

## Qué aprendí

Aprendí que un agente no es solo un chat: necesita instrucciones claras, datos confiables, reglas comerciales y validación humana. Una respuesta bien redactada no es suficiente si la información de base no está ordenada o actualizada.

También entendí que GitHub funciona como repositorio maestro y documental del proyecto, mientras que ChatGPT funciona como entorno operativo del agente. En esta versión, la conexión entre ambos es manual y permite revisar cada cambio antes de utilizarlo.

Decidí mantener esta primera versión simple para entender en detalle cómo se combinan GitHub, Codex, un GPT personalizado, archivos de conocimiento y un flujo comercial. La idea no es hacer la automatización completa desde el inicio, sino validar primero el proceso básico y luego complejizarlo con más información, integraciones y automatización.

Por último, comprendí que automatizar un proceso desordenado puede acelerar el desorden. Antes de conectar Google Sheets, CRM, WhatsApp, validación de disponibilidad o generación automática de propuestas y PDFs, conviene definir y probar bien el flujo comercial.

## Links

- Repositorio GitHub: [funtastic-propuestas-agent-v0](https://github.com/danielalejandroosorio2026/funtastic-propuestas-agent-v0)
- GPT personalizado: fue creado y probado, pero actualmente no puede compartirse públicamente desde esta cuenta.
- Formulario web: pendiente de publicación con GitHub Pages.
