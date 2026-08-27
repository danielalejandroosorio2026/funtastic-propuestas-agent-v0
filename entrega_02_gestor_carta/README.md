# Gestor de Carta Funtastic

## Qué construí

Construí el contrato de un agente para una tarea recurrente: actualizar la carta de cafetería de Funtastic Playroom a partir de instrucciones simples.

El agente está pensado para aplicar cambios de precios, productos y formato, manteniendo una salida estructurada y comparable entre corridas. También puede generar un PDF descargable cuando el usuario lo solicita.

## Cómo se lo pedí

Se diseñó un system prompt y un user prompt que cubren las seis piezas vistas en clase:

- Rol.
- Contexto.
- Tarea.
- Restricciones.
- Formato.
- Ejemplos.

Los archivos principales son:

- [system_prompt.md](./system_prompt.md)
- [user_prompt.md](./user_prompt.md)

## Qué funciona

Se realizaron tres corridas:

- [salida_01.md](./salida_01.md)
- [salida_02.md](./salida_02.md)
- [salida_03.md](./salida_03.md)

La salida es estructurada y comparable porque siempre usa las mismas secciones:

1. Estado de la corrida.
2. Carta actualizada.
3. Cambios realizados.
4. Pendientes o dudas.
5. Mensaje breve para uso interno.
6. PDF descargable cuando corresponde.

## Qué falta o qué falló

Se documentaron dos iteraciones de mejora.

**Iteración 1**

- Fallo: no había una regla clara de redondeo para aumentos porcentuales.
- Pieza tocada: restricciones.
- Cambio: se agregó redondeo siempre hacia arriba al múltiplo de $100.
- Resultado: los precios finales quedan consistentes y comparables.

**Iteración 2**

- Fallo: el PDF generado respetaba la estética de marca, pero no el formato de la carta de referencia.
- Pieza tocada: formato.
- Cambio: se agregó prioridad de fuentes, donde la carta de referencia define el layout y el manual de marca solamente acompaña la identidad visual.
- Resultado: el agente debe actualizar la carta existente sin rediseñarla desde cero.

En esta versión todavía no se conectó el agente con Canva, Google Sheets, WhatsApp ni una base de datos. La idea fue mantener simple el flujo para entender el contrato del agente antes de automatizar.

## Qué aprendí

Aprendí que un agente necesita un contrato claro, no solo una instrucción general.

También entendí que la salida estructurada permite comparar una corrida con la siguiente y detectar mejoras concretas.

Trabajar una pieza por vez ayuda a entender qué parte del contrato mejora realmente el comportamiento del agente.

Además, mantener simple la primera versión permite validar el proceso antes de sumar automatizaciones, diseño avanzado o integraciones.

## Archivos de la entrega

- README.md
- system_prompt.md
- user_prompt.md
- salida_01.md
- salida_02.md
- salida_03.md
- iteracion_01.md
- iteracion_02.md
