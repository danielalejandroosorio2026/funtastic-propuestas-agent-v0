# Asistente Comercial Funtastic Playroom

## Agente GPT personalizado

Este proyecto se complementa con un GPT personalizado creado en ChatGPT:

**Asistente Comercial Funtastic**

El agente utiliza como base las instrucciones comerciales, la información de paquetes, adicionales, condiciones y preguntas frecuentes documentadas en este repositorio.

En esta primera versión, la vinculación entre GitHub y el GPT es manual: GitHub funciona como repositorio maestro del proyecto y ChatGPT funciona como entorno operativo del agente.

Link del GPT: https://chatgpt.com/g/g-6a830bc3c9988191957cee988d00db8e-asistente-comercial-funtastic-v0

## Objetivo del proyecto

Este proyecto propone una primera versión de un asistente comercial para **Funtastic Playroom**, orientado a la preparación de propuestas personalizadas para cumpleaños infantiles.

El asistente, llamado **“Asistente Comercial Funtastic”**, combinará la información que brinda cada familia con una base de paquetes, adicionales, condiciones y preguntas frecuentes. A partir de esos datos podrá recomendar una opción adecuada y redactar una propuesta clara, cálida y fácil de enviar.

Esta versión inicial incluye:

- La definición funcional del asistente.
- Una plantilla editable para la información comercial.
- Un formulario web simple para relevar los datos del evento.
- Un estilo visual infantil, pastel y adaptable a celulares.

Por ahora no hay backend, base de datos ni envío automático. El formulario funciona como una demostración visual del proceso.

## Problema que resuelve

Preparar propuestas de manera manual puede demandar tiempo y producir respuestas poco uniformes. Además, cada consulta tiene variables distintas: fecha, edad, cantidad de invitados, temática, presupuesto y servicios adicionales.

El proyecto busca resolver cuatro necesidades:

1. **Ordenar la información** recibida de cada potencial cliente.
2. **Reducir el tiempo de respuesta** del equipo comercial.
3. **Mantener consistencia** en precios, condiciones y tono de comunicación.
4. **Personalizar cada propuesta** sin tener que redactarla desde cero.

## Flujo propuesto

```text
Cliente
   ↓
Completa el formulario del cumpleaños
   ↓
El agente interpreta la necesidad y consulta los datos comerciales
   ↓
Recomienda un paquete y adicionales relevantes
   ↓
Genera la propuesta y un mensaje listo para WhatsApp
   ↓
El equipo revisa, ajusta y envía
   ↓
El agente crea un resumen interno para la operación
```

### 1. Cliente

La familia comparte los datos principales del festejo y sus preferencias.

### 2. Formulario

El formulario estandariza la consulta y evita omitir información importante, como cantidad de invitados, horario o temática.

### 3. Agente

El asistente analiza la solicitud, identifica datos faltantes, recomienda alternativas y utiliza únicamente la información comercial vigente.

### 4. Propuesta

El resultado incluye una recomendación personalizada, adicionales sugeridos, condiciones de reserva, respuesta a dudas frecuentes y un mensaje para WhatsApp. También genera un resumen interno para facilitar la coordinación del evento.

## Beneficios esperados

- Respuestas comerciales más rápidas.
- Menos tareas repetitivas para el equipo.
- Propuestas consistentes y fáciles de revisar.
- Mejor experiencia para las familias.
- Mayor visibilidad sobre preferencias y oportunidades de venta adicional.
- Información operativa más ordenada para el salón.
- Base simple para futuras automatizaciones.

## Estructura del proyecto

```text
.
├── README.md
├── instrucciones_agente.md
├── datos_propuesta.md
└── formulario/
    ├── index.html
    └── styles.css
```

## Cómo ver el formulario

Abrí `formulario/index.html` con cualquier navegador. No requiere instalación ni conexión a internet.

## Próximas etapas posibles

- Completar los paquetes, precios y condiciones reales.
- Conectar el formulario con una base de datos o planilla.
- Integrar el asistente con WhatsApp o un CRM.
- Generar propuestas en PDF.
- Incorporar validación de disponibilidad de fechas.
- Medir consultas, conversiones y adicionales más elegidos.

> Importante: antes de utilizar el asistente con clientes reales, el equipo debe completar y validar toda la información de `datos_propuesta.md`.
