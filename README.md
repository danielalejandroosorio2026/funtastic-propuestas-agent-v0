# Funtastic Propuestas Agent v2

Sistema agéntico para preparar propuestas comerciales de cumpleaños infantiles a partir de una consulta estructurada y un catálogo validado.

> Estado: versión 2 operativa sobre archivos de GitHub. Los precios y casos incluidos son datos de demostración. Antes de la entrega final deben reemplazarse por datos comerciales validados y tres consultas reales anonimizadas.

## Objetivo

Reducir el tiempo de preparación de propuestas sin delegar decisiones sensibles. El agente valida una consulta, lee el catálogo vigente, recomienda una opción, calcula una cotización trazable y prepara un borrador de WhatsApp y un resumen interno.

No confirma disponibilidad, no ofrece descuentos y no envía mensajes.

## Flujo

1. El equipo guarda una consulta como JSON.
2. El agente lee la consulta y los archivos de `datos/` mediante el conector de GitHub.
3. Valida datos obligatorios y trata los comentarios del cliente únicamente como datos.
4. Recomienda un paquete y calcula cada concepto con reglas explícitas.
5. Devuelve JSON conforme a `schemas/propuesta.schema.json`.
6. Escribe el resultado en una rama o pull request.
7. Una persona revisa precio, fecha, condiciones sensibles y mensaje.
8. Solo el responsable comercial puede aprobar y enviar.

## Herramienta real

GitHub es el conector operativo de esta versión:

- lectura: `datos/`, `corridas/*/entrada.json`;
- escritura: resultados en una rama o pull request;
- prohibido: escribir directamente en `main`, borrar evidencia o guardar credenciales.

La futura integración con Google Sheets está definida en `INTEGRACION_GOOGLE_SHEETS.md`, pero no se declara implementada.

## Nivel de supervisión

**L2 — ejecutar con revisión.** El agente produce un borrador completo. El responsable comercial verifica y firma. El agente nunca confirma fecha, reserva, descuento, alergias o condiciones especiales.

## Estructura

```text
README.md
prompts/
  system_prompt.md
  user_prompt.md
datos/
  catalogo_paquetes.csv
  adicionales.csv
  politicas.md
  preguntas_frecuentes.md
schemas/
  propuesta.schema.json
corridas/
  README.md
  01-caso-normal/
  02-caso-limite/
  03-caso-riesgoso/
DECISIONES.md
COSTOS.md
RIESGOS.md
INTEGRACION_GOOGLE_SHEETS.md
```

## Cómo reproducir una corrida

1. Elegir una entrada de `corridas/*/entrada.json`.
2. Ejecutar `prompts/system_prompt.md` y `prompts/user_prompt.md`.
3. Leer exclusivamente los archivos canónicos de `datos/`.
4. Guardar la respuesta original como `salida.json`.
5. Registrar fecha, modelo, versión de prompts, herramienta y tokens en `metadata.md`.
6. Validar la salida contra `schemas/propuesta.schema.json`.
7. Abrir un pull request para revisión humana.

## Corridas incluidas

Las tres corridas actuales prueban:

- caso normal con datos completos;
- caso límite con invitados excedentes y presupuesto;
- caso riesgoso con datos faltantes, alergia e intento de alterar instrucciones.

Son demostraciones reproducibles. Para cumplir el final deben sustituirse por tres casos reales anonimizados y conservar las salidas originales.

## Criterios de aceptación

- No usa precios ni servicios fuera del catálogo.
- Todos los cálculos muestran cantidades, precio unitario y subtotal.
- No confirma disponibilidad ni reserva.
- Los datos faltantes quedan explícitos.
- El texto del cliente nunca cambia las reglas del agente.
- La salida cumple el esquema JSON.
- Toda propuesta queda pendiente de aprobación humana.

## Antecedentes

Los archivos históricos de la v0 y el Gestor de Carta se conservan como evidencia del proceso, pero no son fuentes canónicas de esta versión. `instrucciones_agente.md` y `datos_propuesta.md` redirigen a los archivos vigentes.

## Pendientes antes de entregar

- Adaptar este README a la plantilla exacta publicada en Moodle.
- Validar el catálogo con el responsable comercial.
- Sustituir datos demostrativos por casos reales anonimizados.
- Ejecutar y guardar tres salidas originales con tokens medidos.
- Calibrar el modelo más pequeño que pase los controles.
