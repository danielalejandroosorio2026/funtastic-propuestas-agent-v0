from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FILES = {
    "datos/catalogo_paquetes.csv",
    "datos/precios_diciembre_2026.csv",
    "datos/adicionales.csv",
    "datos/servicios_paquetes.md",
    "datos/politicas.md",
    "datos/preguntas_frecuentes.md",
}

TOOLS = [
    {
        "type": "function",
        "name": "read_business_file",
        "description": "Lee una fuente comercial canónica del repositorio.",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string", "enum": sorted(ALLOWED_FILES)}},
            "required": ["path"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "calculate_quote",
        "description": "Calcula de manera determinística paquete, excedentes y adicionales.",
        "parameters": {
            "type": "object",
            "properties": {
                "package": {"type": "string", "enum": ["Basica", "Completa", "Saludable"]},
                "children": {"type": "integer", "minimum": 1, "maximum": 300},
                "adults": {"type": "integer", "minimum": 0, "maximum": 300},
                "day_type": {
                    "type": "string",
                    "enum": ["Lun-Jue", "Vie-Dom-Fer", "Sin definir"],
                    "description": "Tipo de día del evento. Usar Sin definir si falta la fecha o no se verificó si es feriado.",
                },
                "extras": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "Hora adicional",
                            "Animacion especial",
                            "Fotografia",
                            "Talleres",
                            "Spa de niñas",
                            "Mesa dulce tematica",
                            "Ambientacion",
                            "Foto cabina",
                            "Helados",
                            "Refuerzo comida adultos",
                            "Torta",
                            "Menu cafeteria",
                        ],
                    },
                    "maxItems": 13,
                },
            },
            "required": ["package", "children", "adults", "day_type", "extras"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


def read_business_file(path: str) -> dict[str, Any]:
    if path not in ALLOWED_FILES:
        raise ValueError("ruta no autorizada")
    content = (ROOT / path).read_text(encoding="utf-8")
    return {"path": path, "content": content}


def _csv_rows(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def calculate_quote(
    package: str,
    children: int,
    adults: int,
    day_type: str,
    extras: list[str],
) -> dict[str, Any]:
    packages = {row["nombre"]: row for row in _csv_rows("datos/catalogo_paquetes.csv")}
    additions = {row["nombre"]: row for row in _csv_rows("datos/adicionales.csv")}
    prices = {
        (row["nombre"], row["tipo_dia"]): row
        for row in _csv_rows("datos/precios_diciembre_2026.csv")
    }
    if package not in packages:
        raise ValueError("paquete inexistente")
    unknown = sorted(set(extras) - additions.keys())
    if unknown:
        raise ValueError(f"adicionales inexistentes: {unknown}")

    row = packages[package]
    price_row = prices.get((package, day_type))
    items: list[dict[str, Any]] = []
    pending: list[str] = []

    def add(concepto: str, cantidad: int, raw_price: str, fuente: str) -> None:
        if cantidad <= 0:
            return
        if not raw_price.strip():
            pending.append(concepto)
        else:
            unitario = int(raw_price)
            items.append(
                {
                    "concepto": concepto,
                    "cantidad": cantidad,
                    "precio_unitario": unitario,
                    "subtotal": cantidad * unitario,
                    "fuente": fuente,
                }
            )

    if children + adults > 100:
        raise ValueError("la cantidad total supera la capacidad máxima de 100 personas")

    if price_row is None:
        pending.append(f"Tipo de día/fecha para cotizar Paquete {package}")
    else:
        add(
            f"Paquete {package}",
            1,
            price_row["precio_base_ars"],
            "datos/precios_diciembre_2026.csv",
        )
    excess_children = max(0, children - int(row["ninos_incluidos"]))
    excess_adults = max(0, adults - int(row["adultos_incluidos"]))
    if excess_children:
        add(
            "Niños adicionales",
            excess_children,
            "" if price_row is None else price_row["precio_nino_excedente_ars"],
            "datos/precios_diciembre_2026.csv",
        )
    if excess_adults:
        add(
            "Adultos adicionales",
            excess_adults,
            "" if price_row is None else price_row["precio_adulto_excedente_ars"],
            "datos/precios_diciembre_2026.csv",
        )
    for extra in extras:
        if extra == "Hora adicional":
            add(
                extra,
                1,
                "" if price_row is None else price_row["precio_hora_adicional_ars"],
                "datos/precios_diciembre_2026.csv",
            )
        else:
            add(extra, 1, additions[extra]["precio_ars"], "datos/adicionales.csv")

    return {
        "moneda": "ARS",
        "catalogo_validado": price_row is not None
        and price_row["precios_validados"].lower() == "true",
        "vigencia": None if price_row is None else price_row["vigencia"],
        "tipo_dia": None if price_row is None else price_row["tipo_dia"],
        "items": items,
        "conceptos_pendientes": pending,
        "total_estimado": None if pending else sum(item["subtotal"] for item in items),
    }


def execute_tool(name: str, arguments_json: str) -> str:
    arguments = json.loads(arguments_json)
    if name == "read_business_file":
        result = read_business_file(**arguments)
    elif name == "calculate_quote":
        result = calculate_quote(**arguments)
    else:
        raise ValueError(f"herramienta desconocida: {name}")
    return json.dumps(result, ensure_ascii=False)
