# Iteración 01 — Regla de redondeo

## Qué falló

El agente recibió el pedido de aumentar precios un 5%, pero indicó que no tenía una regla de redondeo cargada o no aplicó un criterio comercial consistente para los precios finales.

## Fallo textual

> “El agente no tenía una regla definida para redondear precios al aplicar un aumento porcentual.”

## Pieza del contrato tocada

Restricciones.

## Cambio aplicado

Se agregó una regla de actualización porcentual de precios:

Cuando el usuario pida aumentar o disminuir precios por porcentaje, el agente debe calcular el nuevo precio aplicando el porcentaje indicado y luego redondear siempre hacia arriba al múltiplo de $100 más cercano.

Ejemplos:

- $3.200 + 5% = $3.360 → $3.400
- $4.500 + 5% = $4.725 → $4.800
- $6.900 + 5% = $7.245 → $7.300

## Qué cambió en la salida

Después del ajuste, el agente puede calcular precios finales sin decimales ni valores intermedios, usando precios comerciales comparables y consistentes.
