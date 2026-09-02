# Decisiones del proyecto

## D1 — Separar v2 de la entrega anterior

La v0 mezclaba un asistente de propuestas y un Gestor de Carta. Se creó la rama `final-v2` para conservar la evidencia anterior y definir un único sistema principal.

## D2 — Elegir el agente comercial

Se eligió porque resuelve un proceso recurrente real, permite entradas y salidas claras y tiene puntos relevantes de supervisión y riesgo.

## D3 — Usar GitHub como primer conector real

El formulario de la v0 era visual y no enviaba datos. Para lograr una versión reproducible sin inventar credenciales, v2 usa GitHub para leer entradas y catálogo y guardar salidas mediante ramas y pull requests.

## D4 — No automatizar WhatsApp

Automatizar el envío agrega permisos y riesgo comercial. El agente produce un borrador; una persona revisa y envía. Nivel L2.

## D5 — Separar datos de instrucciones

La v0 concentraba reglas y datos en documentos generales. V2 separa catálogo, adicionales, políticas, preguntas frecuentes, prompts y esquema de salida.

## D6 — Agregar cálculo trazable

Cada precio tiene fuente, cantidad, valor unitario y subtotal. El total debe coincidir con la suma. Esto facilita auditoría y evita números sin explicación.

## D7 — Tratar texto del cliente como no confiable

Se agregó una prueba con instrucciones maliciosas en comentarios. El agente debe registrarlas como datos e ignorarlas.

## D8 — No inventar evidencia real

No contamos todavía con catálogo validado ni consultas reales anonimizadas. Las corridas se etiquetan como demostración y no se presentan como cumplimiento final.

## Próximas iteraciones reales

Registrar aquí, con texto original:

- error observado;
- entrada usada;
- versión del prompt;
- única pieza modificada;
- salida antes y después;
- decisión de mantener o revertir.
