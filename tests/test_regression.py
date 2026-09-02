import json
from pathlib import Path

import pytest

from agent.models import Estado, Paquete, Propuesta
from agent.tools import calculate_quote


ROOT = Path(__file__).resolve().parents[1]
RUNS = sorted((ROOT / "corridas").glob("0*/salida.json"))


@pytest.mark.parametrize("path", RUNS)
def test_real_anonymized_outputs_pass_strict_validation(path: Path) -> None:
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.requiere_revision_humana is True


def test_multifamily_case_stops_when_children_are_missing() -> None:
    path = ROOT / "corridas/01-caso-normal/salida.json"
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.estado == Estado.REQUIERE_DATOS
    assert "cantidad_ninos" in proposal.datos_faltantes
    assert proposal.cotizacion.total_estimado is None


def test_healthy_case_has_auditable_total() -> None:
    path = ROOT / "corridas/02-caso-limite/salida.json"
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.paquete_recomendado is not None
    assert proposal.paquete_recomendado.nombre == Paquete.SALUDABLE
    assert proposal.cotizacion.total_estimado is None
    assert proposal.cotizacion.items == []
    assert proposal.cotizacion.conceptos_pendientes == [
        "Fecha y tipo de día para cotizar Paquete Saludable",
        "Refuerzo comida adultos",
    ]


def test_twins_case_respects_low_cost_preference() -> None:
    path = ROOT / "corridas/03-caso-riesgoso/salida.json"
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.paquete_recomendado is not None
    assert proposal.paquete_recomendado.nombre == Paquete.BASICA
    assert proposal.cotizacion.total_estimado is None
    assert proposal.cotizacion.conceptos_pendientes == [
        "Fecha y tipo de día para cotizar Paquete Basica"
    ]
    serialized = json.dumps(proposal.model_dump(mode="json"), ensure_ascii=False).lower()
    assert "descuento aplicado" not in serialized


def test_december_weekend_quote_is_deterministic_and_auditable() -> None:
    quote = calculate_quote(
        "Completa",
        children=38,
        adults=40,
        day_type="Vie-Dom-Fer",
        extras=[],
    )
    assert quote["vigencia"] == "2026-12"
    assert quote["tipo_dia"] == "Vie-Dom-Fer"
    assert quote["total_estimado"] == 2_270_000
    assert sum(item["subtotal"] for item in quote["items"]) == 2_270_000
    assert quote["conceptos_pendientes"] == []


def test_quote_stops_when_day_type_is_unknown() -> None:
    quote = calculate_quote(
        "Basica", children=20, adults=15, day_type="Sin definir", extras=[]
    )
    assert quote["total_estimado"] is None
    assert quote["conceptos_pendientes"] == [
        "Tipo de día/fecha para cotizar Paquete Basica"
    ]


def test_hour_additional_uses_package_and_day_rate() -> None:
    quote = calculate_quote(
        "Basica",
        children=20,
        adults=15,
        day_type="Lun-Jue",
        extras=["Hora adicional"],
    )
    assert quote["total_estimado"] == 1_452_000


def test_children_and_adult_quotas_are_not_mixed() -> None:
    quote = calculate_quote(
        "Basica",
        children=30,
        adults=20,
        day_type="Lun-Jue",
        extras=[],
    )
    assert quote["total_estimado"] == 1_190_000
    children_item = next(
        item for item in quote["items"] if item["concepto"] == "Niños adicionales"
    )
    assert children_item["cantidad"] == 5
    assert not any(item["concepto"] == "Adultos adicionales" for item in quote["items"])


def test_capacity_limit_is_enforced() -> None:
    with pytest.raises(ValueError, match="capacidad máxima"):
        calculate_quote(
            "Completa",
            children=60,
            adults=41,
            day_type="Lun-Jue",
            extras=[],
        )


def test_unknown_extra_is_rejected() -> None:
    with pytest.raises(ValueError):
        calculate_quote(
            "Completa",
            children=20,
            adults=20,
            day_type="Lun-Jue",
            extras=["Descuento libre"],
        )
