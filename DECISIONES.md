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


## D9 — Convertir el feedback técnico en controles ejecutables

El informe pedagógico asignó 53/100 y recomendó runner, reintentos, guardas, dependencias fijadas, validación estricta y tests. Parte de la evidencia citada no correspondía con la rama (mencionaba diez corridas y un runner inexistente), por lo que se verificó cada hallazgo antes de implementarlo.

Cambio técnico: commit [49cd8f1](https://github.com/danielalejandroosorio2026/funtastic-propuestas-agent-v0/commit/49cd8f1dff37b0f5f492146be8edff16b99c7136).

Métrica diferencial:

| Control | Antes | Después |
|---|---:|---:|
| Runner API | 0 | 1 |
| Herramientas con schema | 0 | 2 |
| Validación Pydantic | 0 | 1 frontera estricta |
| Tests automatizados | 0 | 6 |
| Reintentos 429/503 | 0 | hasta 5 |
| Guard de iteraciones | 0 | máximo 8 |
| Guard de tokens | 0 | máximo 30.000 |

Latencia y tokens antes/después quedan pendientes hasta ejecutar con una API key y casos reales. No se fabrican mediciones.

## D10 — Corregir un fallo real de reproducibilidad

La primera ejecución de `pytest -q` falló durante la colección porque la raíz del repositorio no estaba en el import path. Se agregó `pytest.ini` y se fijó Python 3.12.

Cambio técnico: commit [4615f88](https://github.com/danielalejandroosorio2026/funtastic-propuestas-agent-v0/commit/4615f88743974f78902e87fbcfeb2392948ff537).

Resultado verificado:

- antes: 0 tests ejecutados; error `ModuleNotFoundError: No module named 'agent'`;
- después: 6 tests aprobados en 0,49 segundos;
- validación sin API: `OK: corridas/01-caso-normal/salida.json`.


## D11 — Sustituir escenarios inventados por consultas reales reconstruidas

El propietario aportó tres consultas comerciales reales de Funtastic. Se eliminaron nombres, teléfonos, fechas e identificadores, y se conservaron las necesidades comerciales relevantes.

Decisión:

- registrar `es_caso_real=true`;
- describir el origen como “consulta reconstruida y anonimizada”;
- no afirmar que los precios sean reales mientras el catálogo siga sin validar;
- permitir que el agente se detenga y pida información cuando la consulta original esté incompleta.

Esto mejora la honestidad de la evidencia: entradas reales, privacidad protegida y cotizaciones explícitamente preliminares.
