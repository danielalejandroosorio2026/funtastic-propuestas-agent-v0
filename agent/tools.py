from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FILES = {
    "datos/catalogo_paquetes.csv",
    "datos/adicionales.csv",
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
                "extras": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "Decoracion tematica",
                            "Mesa dulce",
                            "Animacion especial",
                            "Fotografia",
                            "Catering adultos",
                        ],
                    },
                    "maxItems": 5,
                },
            },
            "required": ["package", "children", "adults", "extras"],
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


def calculate_quote(package: str, children: int, adults: int, extras: list[str]) -> dict[str, Any]:
    packages = {row["nombre"]: row for row in _csv_rows("datos/catalogo_paquetes.csv")}
    additions = {row["nombre"]: row for row in _csv_rows("datos/adicionales.csv")}
    if package not in packages:
        raise ValueError("paquete inexistente")
    unknown = sorted(set(extras) - additions.keys())
    if unknown:
        raise ValueError(f"adicionales inexistentes: {unknown}")

    row = packages[package]
    items: list[dict[str, Any]] = []

    def add(concepto: str, cantidad: int, unitario: int, fuente: str) -> None:
        if cantidad > 0:
            items.append(
                {
                    "concepto": concepto,
                    "cantidad": cantidad,
                    "precio_unitario": unitario,
                    "subtotal": cantidad * unitario,
                    "fuente": fuente,
                }
            )

    add(f"Paquete {package}", 1, int(row["precio_base_ars"]), "datos/catalogo_paquetes.csv")
    add(
        "Niños excedentes",
        max(0, children - int(row["ninos_incluidos"])),
        int(row["precio_nino_excedente_ars"]),
        "datos/catalogo_paquetes.csv",
    )
    add(
        "Adultos excedentes",
        max(0, adults - int(row["adultos_incluidos"])),
        int(row["precio_adulto_excedente_ars"]),
        "datos/catalogo_paquetes.csv",
    )
    for extra in extras:
        add(extra, 1, int(additions[extra]["precio_ars"]), "datos/adicionales.csv")

    return {
        "moneda": "ARS",
        "catalogo_validado": row["catalogo_validado"].lower() == "true",
        "items": items,
        "total_estimado": sum(item["subtotal"] for item in items),
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
