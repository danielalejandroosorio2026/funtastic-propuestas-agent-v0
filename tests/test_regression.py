import json
from pathlib import Path

import pytest

from agent.models import Estado, Propuesta
from agent.tools import calculate_quote


ROOT = Path(__file__).resolve().parents[1]
RUNS = sorted((ROOT / "corridas").glob("0*/salida.json"))


@pytest.mark.parametrize("path", RUNS)
def test_sample_outputs_pass_strict_validation(path: Path) -> None:
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.requiere_revision_humana is True


def test_quote_is_deterministic_and_auditable() -> None:
    quote = calculate_quote("Completa", children=38, adults=40, extras=[])
    assert quote["total_estimado"] == 329_000
    assert sum(item["subtotal"] for item in quote["items"]) == 329_000


def test_risky_case_stops_and_does_not_discount() -> None:
    path = ROOT / "corridas/03-caso-riesgoso/salida.json"
    proposal = Propuesta.model_validate_json(path.read_text(encoding="utf-8"))
    assert proposal.estado == Estado.REQUIERE_DATOS
    assert "fecha_preferida" in proposal.datos_faltantes
    serialized = json.dumps(proposal.model_dump(mode="json"), ensure_ascii=False).lower()
    assert "20%" not in serialized
    assert proposal.cotizacion.total_estimado is None


def test_unknown_extra_is_rejected() -> None:
    with pytest.raises(ValueError):
        calculate_quote("Completa", children=20, adults=20, extras=["Descuento libre"])
