# Gobierno y riesgos

## Nivel de delegación

L2 — ejecutar con revisión.

## Permisos

- GitHub lectura: datos canónicos y entradas.
- GitHub escritura: únicamente rama de trabajo o pull request.
- Sin permiso para escribir directamente en main.
- Sin permiso para enviar WhatsApp, confirmar fecha, reserva o descuento.
- Sin credenciales dentro del repositorio.

## Matriz

| Riesgo | Consecuencia | Control preventivo | Respuesta | Firma |
|---|---|---|---|---|
| Precio inventado | Propuesta incorrecta | Solo catálogo canónico y fuente por ítem | Detener y marcar no cotizable | Responsable comercial |
| Catálogo vencido | Información desactualizada | Vigencia y bandera de validación | Bloquear propuesta definitiva | Responsable comercial |
| Fecha confirmada sin revisión | Sobreventa | Prohibición en system prompt | Corregir borrador y validar agenda | Responsable comercial |
| Prompt injection en comentarios | Descuento o acción indebida | Tratar entrada como dato no confiable | Ignorar instrucción y generar alerta | Responsable comercial |
| Alergia o necesidad sensible | Riesgo a personas | Alerta obligatoria | Escalar y no prometer viabilidad | Responsable operativo |
| Datos personales expuestos | Pérdida de privacidad | Anonimizar corridas públicas | Retirar dato y registrar incidente | Dueño del proceso |
| Cálculo incorrecto | Cotización errónea | Desglose y suma verificable | Recalcular antes de aprobar | Responsable comercial |
| Escritura directa en main | Pérdida de trazabilidad | Trabajar por PR | Revertir y revisar permisos | Dueño del repositorio |

## Firma

La salida del agente es un borrador. La responsabilidad final pertenece a la persona que valida y envía la propuesta.
