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
        "Paquete Saludable",
        "Refuerzo comida adultos",
    ]


def test_twins_case_respects_low_cost_preference() -> None:
    path = ROOT / "corridas/03-caso-riesgoso/salida.json"
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.paquete_recomendado is not None
    assert proposal.paquete_recomendado.nombre == Paquete.BASICA
    assert proposal.cotizacion.total_estimado is None
    assert proposal.cotizacion.conceptos_pendientes == ["Paquete Basica"]
    serialized = json.dumps(proposal.model_dump(mode="json"), ensure_ascii=False).lower()
    assert "descuento aplicado" not in serialized


def test_quote_stops_safely_when_prices_are_missing() -> None:
    quote = calculate_quote("Completa", children=38, adults=40, extras=[])
    assert quote["total_estimado"] is None
    assert quote["items"] == []
    assert quote["conceptos_pendientes"] == ["Paquete Completa", "Invitados adicionales"]


def test_capacity_limit_is_enforced() -> None:
    with pytest.raises(ValueError, match="capacidad máxima"):
        calculate_quote("Completa", children=60, adults=41, extras=[])


def test_unknown_extra_is_rejected() -> None:
    with pytest.raises(ValueError):
        calculate_quote("Completa", children=20, adults=20, extras=["Descuento libre"])
