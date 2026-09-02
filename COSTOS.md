# Análisis económico

## Modelo operativo de referencia

La configuración predeterminada usa `gpt-5.6-luna`, elegido para cargas sensibles a costo. Tarifas de referencia al 01/09/2026:

- entrada: USD 0,20 por millón de tokens;
- entrada cacheada: USD 0,02 por millón;
- salida: USD 1,20 por millón;
- escritura explícita de caché: 1,25 veces la tarifa de entrada no cacheada.

Verificar nuevamente las tarifas oficiales antes de entregar.

## Supuesto base

- 5.000 tokens de entrada;
- 1.000 tokens de salida;
- 100 propuestas por semana;
- 52 semanas;
- 80% de la entrada reutilizable cuando la caché acierta.

| Escenario | Costo/corrida | Semanal | Anual |
|---|---:|---:|---:|
| Sin caché | USD 0,00220 | USD 0,220 | USD 11,44 |
| Con 80% de entrada cacheada | USD 0,00148 | USD 0,148 | USD 7,70 |
| Pico 5× sin caché | USD 0,00220 | USD 1,100 | USD 57,20 |
| Pico 5× con caché | USD 0,00148 | USD 0,740 | USD 38,48 |

Ahorro estimado con 80% de caché: 32,7%.

## SLO y picos de carga

SLO inicial:

- 95% de corridas válidas sin intervención técnica;
- latencia p95 menor a 30 segundos;
- error de proveedor menor a 1%;
- cero propuestas persistidas sin validación Pydantic.

En picos 5×, el costo crece linealmente. El runner aplica backoff con jitter ante 429/503; esto protege estabilidad, pero puede elevar la latencia. Si p95 supera 30 segundos durante tres mediciones consecutivas:

1. reducir concurrencia;
2. priorizar consultas pendientes más antiguas;
3. revisar tamaño del contexto;
4. degradar de manera segura a cola manual.

## Medición real

Cada ejecución genera metadata con:

- tokens de entrada;
- tokens cacheados;
- tokens de salida;
- costo estimado;
- latencia;
- modelo;
- hashes de prompts.

Las cifras de esta matriz son sensibilidad, no sustituyen las tres mediciones reales.
