# Asistente Comercial Funtastic Playroom

## Qué construí

Construí una primera versión de un agente comercial para **Funtastic Playroom**, un salón infantil con cafetería y propuestas de cumpleaños.

El agente sirve para ayudar al equipo del salón a generar propuestas comerciales personalizadas a partir de paquetes estándar: **Básica, Completa y Saludable**.

También permite sugerir adicionales, responder preguntas frecuentes y preparar mensajes listos para enviar por WhatsApp.

Está pensado para reducir tareas repetitivas, ordenar la información comercial y mejorar la velocidad de respuesta a las familias.

En esta primera versión, la vinculación entre GitHub y el GPT es manual: **GitHub funciona como repositorio maestro del proyecto** y **ChatGPT funciona como entorno operativo del agente**.

---

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

---

## Qué funciona

Se creó el repositorio público en GitHub y se cargó una estructura inicial del proyecto.

El repositorio contiene estos archivos:

```text
.
├── README.md
├── instrucciones_agente.md
├── datos_propuesta.md
└── formulario/
    ├── index.html
    └── styles.css
```

También se creó un formulario web inicial en HTML/CSS. El formulario releva datos básicos del cumpleaños, como nombre del adulto, WhatsApp, nombre del cumpleañero/a, edad, fecha, horario, cantidad de niños, cantidad de adultos, temática, tipo de propuesta deseada, adicionales de interés y comentarios.

El proyecto no incluye todavía JavaScript, backend, base de datos ni integración automática. Por ahora el formulario funciona como una demostración visual del proceso.

Además, se creó una primera versión del GPT personalizado llamado **Asistente Comercial Funtastic** dentro de ChatGPT.

Se probó el agente con un caso simulado:

```text
Tengo una consulta para un cumpleaños de 6 años, temática princesas, con 25 niños y 25 adultos. La familia quiere resolver todo sin ocuparse demasiado. ¿Qué paquete recomendarías, qué adicionales sugerís y qué mensaje puedo mandar por WhatsApp?
```

La respuesta fue adecuada: el agente recomendó la **Opción Completa**, sugirió adicionales coherentes con la temática de princesas, como animación, ambientación temática, mesa dulce y fotografía/fotocabina, y generó un mensaje de WhatsApp usable.

También respetó restricciones importantes: no inventó precios, no confirmó disponibilidad de fecha y no confirmó la reserva sin seña.

El flujo pensado es:

```text
Cliente
   ↓
Completa el formulario del cumpleaños
   ↓
El equipo recibe la información
   ↓
El agente interpreta la necesidad
   ↓
Recomienda paquete y adicionales
   ↓
Genera un mensaje comercial
   ↓
El equipo revisa, ajusta y envía
   ↓
El agente genera un resumen interno operativo
```

---

## Qué falta o qué falló

La propuesta comercial real de Funtastic ya existe en el PDF cargado y contiene paquetes, adicionales, condiciones de reserva y preguntas frecuentes. En esta etapa, esa información fue trasladada también al repositorio en formato editable dentro de `datos_propuesta.md`, para facilitar mantenimiento, futuras automatizaciones y uso por el agente.

Los precios no se incluyen en esta primera versión porque pueden cambiar. En una etapa futura podrían administrarse desde una fuente editable y vigente, como una planilla, un archivo de datos o un sistema interno.

El formulario web todavía es solamente visual. No guarda información, no envía mensajes, no está conectado con Google Sheets, CRM, WhatsApp ni con el GPT personalizado.

También falta publicar el formulario usando GitHub Pages. El problema temporal de carga que apareció durante el trabajo ya se resolvió y los archivos se encuentran accesibles en el repositorio.

El GPT fue creado y probado, pero actualmente no puede compartirse públicamente desde esta cuenta. En la pantalla de compartir solo aparecía la opción **“Solo yo”** y el mensaje:

```text
Ya no se pueden compartir GPT con el público.
```

Todavía falta probar el agente con más casos reales o simulados, por ejemplo:

- familias que buscan algo más económico;
- familias que quieren llevar decoración propia;
- cumpleaños con más invitados;
- consultas sobre seña;
- consultas sobre cancelación;
- clientes indecisos entre Básica y Completa;
- consultas por disponibilidad de fecha;
- familias que quieren una propuesta saludable;
- clientes que preguntan por torta, piñata o ingreso anticipado.

---

## Qué aprendí

Aprendí que un agente no es solo “un chat que responde”, sino una combinación de instrucciones, datos, reglas, pruebas y flujo de trabajo.

También entendí que GitHub no es donde vive el agente, sino donde se documenta y ordena el proyecto: archivos, versiones, instrucciones, formulario y datos comerciales.

El GPT personalizado funciona como entorno operativo para generar respuestas, mientras que GitHub funciona como repositorio maestro y evidencia del proceso.

También comprobé que una buena instrucción no alcanza por sí sola: hay que probar el agente con casos reales, revisar si inventa información, ajustar reglas y validar el resultado antes de usarlo con clientes.

Por último, entendí que conviene avanzar por etapas. Primero hay que ordenar el proceso comercial y crear una versión simple. Después se puede pensar en automatizaciones, integración con planillas, CRM, WhatsApp o generación automática de propuestas.

---

## Links

- Repositorio GitHub: [funtastic-propuestas-agent-v0](https://github.com/danielalejandroosorio2026/funtastic-propuestas-agent-v0)
- GPT personalizado: fue creado y probado en ChatGPT, pero actualmente no puede compartirse públicamente desde esta cuenta.
- Formulario web: pendiente de publicación con GitHub Pages.

---

## Próximas etapas

1. Mantener `datos_propuesta.md` actualizado cuando cambie la propuesta comercial del salón.
2. Probar el agente con más casos comerciales.
3. Ajustar las instrucciones del GPT según los errores detectados.
4. Publicar el formulario con GitHub Pages y verificar su acceso público.
5. Conectar el formulario con Google Sheets, CRM o una base de datos.
6. Evaluar una integración futura con WhatsApp o generación automática de PDF.
