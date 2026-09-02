# Integración futura con Google Sheets

Esta integración está diseñada, no implementada.

## Hojas

### consultas

`consulta_id | fecha_ingreso | datos_json | estado`

### catalogo

Versión privada y validada de paquetes, adicionales, precios y vigencias.

### resultados

`consulta_id | salida_json | estado_revision | revisor | fecha_revision`

## Flujo propuesto

1. El formulario agrega una fila con estado `PENDIENTE`.
2. El agente lee solo filas pendientes.
3. Lee el catálogo validado con acceso de solo lectura.
4. Escribe el resultado como `PENDIENTE_REVISION`.
5. Una persona aprueba o rechaza.
6. El envío por WhatsApp continúa manual.

## Permisos mínimos

- lectura de catálogo;
- lectura de consultas pendientes;
- escritura solo en resultados y estado;
- sin acceso al resto de Drive;
- sin permiso para enviar mensajes.

## Criterio de finalización

No declarar esta integración como herramienta real hasta guardar evidencia de tres lecturas y escrituras exitosas con datos anonimizados.
