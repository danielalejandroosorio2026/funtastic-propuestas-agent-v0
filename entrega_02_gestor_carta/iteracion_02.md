# Iteración 02 — Fidelidad al formato de referencia

## Qué falló

El agente generó un PDF con estética alineada al manual de marca, pero no respetó el formato de la carta de referencia cargada. Rediseñó la carta en lugar de mantener la estructura original con los cambios solicitados.

## Fallo textual

> “El agente generó un PDF con estética del manual de marca, pero no siguió el ejemplo de carta que se le pasó.”

## Pieza del contrato tocada

Formato.

## Cambio aplicado

Se agregó una regla de prioridad de fuentes y fidelidad al formato de referencia:

1. La carta de referencia visual define layout y formato.
2. La carta base actual define contenido comercial.
3. El manual de marca define identidad visual.
4. El pedido puntual del usuario define solamente los cambios a aplicar.

También se agregó que el agente no debe rediseñar desde cero si el usuario pidió actualizar la carta existente.

## Qué cambió en la salida

El agente debe mantener el formato, estructura, orden visual, bloques, categorías y estilo general de la carta de referencia. El manual de marca se usa como apoyo visual, no como autorización para rediseñar.
