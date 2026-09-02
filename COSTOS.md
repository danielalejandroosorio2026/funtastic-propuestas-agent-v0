# Análisis económico

## Estado

Las corridas de construcción no exponen medición de tokens, por eso no se inventan cifras. Antes de entregar se deben registrar tokens reales o una estimación reproducible claramente identificada.

## Medición por corrida

| Campo | Valor |
|---|---:|
| Tokens de entrada | pendiente |
| Tokens de salida | pendiente |
| Precio por millón de tokens de entrada | pendiente según modelo |
| Precio por millón de tokens de salida | pendiente según modelo |
| Costo total | pendiente |

Fórmula:

```text
costo = entrada_tokens / 1.000.000 × precio_entrada
      + salida_tokens / 1.000.000 × precio_salida
```

## Proyección

Registrar:

- consultas promedio por semana;
- costo por corrida;
- costo semanal;
- costo anual;
- minutos humanos actuales por propuesta;
- minutos humanos esperados con el agente;
- ahorro anual estimado.

## Elección de modelo

Criterio: diseñar con un modelo capaz y operar con el modelo más pequeño que pase estos controles:

1. cero precios inventados;
2. cálculo correcto;
3. JSON válido;
4. detección de datos faltantes;
5. detección del comentario malicioso;
6. escalamiento de alergias;
7. prohibición de confirmar fecha o descuento.

Comparar al menos dos modelos sobre las mismas tres entradas y registrar precisión, costo y latencia.
