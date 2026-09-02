# Funtastic Propuestas Agent v2

Sistema agéntico reproducible para preparar propuestas comerciales de cumpleaños infantiles a partir de una consulta estructurada y un catálogo validado.

> Estado: la arquitectura y el runner están implementados. Los precios y casos incluidos siguen siendo demostrativos; deben reemplazarse por datos validados y tres consultas reales anonimizadas antes de la entrega final.

## Qué hace

1. Recibe una consulta JSON.
2. Usa function calling para leer fuentes comerciales y calcular una cotización.
3. Valida datos faltantes, riesgos e instrucciones maliciosas.
4. Devuelve JSON estricto.
5. Valida la salida con Pydantic antes de guardarla.
6. Registra tokens, caché, costo, latencia y hashes de prompts.
7. Deja la propuesta en revisión humana L2.

No confirma disponibilidad, reservas ni descuentos. No envía WhatsApp.

## Componentes

```text
agent/
  runner.py       runner de Responses API, herramientas y guardas
  tools.py        lectura de fuentes y cálculo determinístico
  models.py       contrato Pydantic estricto
prompts/
datos/
schemas/
corridas/
tests/
README.md
DECISIONES.md
COSTOS.md
RIESGOS.md
requirements.txt
.env.example
```

## Herramientas reales

- `read_business_file`: lee exclusivamente las cuatro fuentes autorizadas.
- `calculate_quote`: calcula paquete, excedentes y adicionales de forma determinística.

Las herramientas usan schemas cerrados. El modelo no calcula precios por su cuenta.

## Instalación reproducible

Requiere Python 3.11 o superior.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Cargar `OPENAI_API_KEY` en el entorno. Nunca subir la clave al repositorio.

## Comando único de ejecución

```bash
python -m agent.runner \
  --input corridas/01-caso-normal/entrada.json \
  --output /tmp/propuesta.json \
  --metadata /tmp/metadata.json
```

Modelo predeterminado: `gpt-5.6-luna`. Se puede cambiar con `OPENAI_MODEL`.

## Validación sin API

```bash
python -m agent.runner --validate-only corridas/01-caso-normal/salida.json
```

## Tests de regresión

```bash
pytest -q
```

Los tests validan las tres salidas, la aritmética, el caso riesgoso y el rechazo de adicionales inexistentes.

## Resiliencia

- Hasta 5 intentos ante 429, 503, timeout o error de conexión.
- Backoff exponencial con jitter.
- Timeout configurable.
- Máximo de 8 iteraciones.
- Guard de 30.000 tokens totales.
- Máximo de 3.000 tokens de salida por llamada.
- Límite de tamaño de entrada y comentarios.
- Pydantic estricto antes de persistir.
- Escritura solo después de validación.

## Prompt caching y costos

Se usa una clave estable de caché y se registran tokens de entrada, tokens cacheados y salida. Las tarifas predeterminadas están documentadas en `COSTOS.md` y pueden configurarse por variables de entorno.

## Corridas incluidas

Las tres corridas actuales son demostraciones:

- normal;
- límite de capacidad/presupuesto;
- riesgosa con alergia e intento de prompt injection.

No se presentan como casos reales. Deben reemplazarse antes de entregar.

## Supervisión

L2: el agente genera el borrador y una persona revisa catálogo, precio, disponibilidad, alergias y texto final. Solo el responsable comercial firma y envía.

## Integración con Sheets

`INTEGRACION_GOOGLE_SHEETS.md` describe la etapa futura. No está declarada como implementada.
