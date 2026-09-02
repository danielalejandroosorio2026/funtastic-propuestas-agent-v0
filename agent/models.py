from __future__ import annotations

from enum import Enum
from math import isclose
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class Estado(str, Enum):
    BORRADOR = "BORRADOR"
    REQUIERE_DATOS = "REQUIERE_DATOS"
    NO_COTIZABLE = "NO_COTIZABLE"


class Paquete(str, Enum):
    BASICA = "Basica"
    COMPLETA = "Completa"
    SALUDABLE = "Saludable"


class Recomendacion(StrictModel):
    nombre: Paquete
    justificacion: str = Field(min_length=10, max_length=600)


class Alternativa(StrictModel):
    nombre: Paquete
    diferencia: str = Field(min_length=5, max_length=600)


class ItemCotizacion(StrictModel):
    concepto: str = Field(min_length=1, max_length=120)
    cantidad: float = Field(gt=0)
    precio_unitario: float = Field(ge=0)
    subtotal: float = Field(ge=0)
    fuente: str = Field(pattern=r"^datos/(catalogo_paquetes|adicionales)\.csv$")

    @model_validator(mode="after")
    def validar_subtotal(self) -> "ItemCotizacion":
        esperado = self.cantidad * self.precio_unitario
        if not isclose(self.subtotal, esperado, rel_tol=0, abs_tol=0.01):
            raise ValueError(f"subtotal inválido: {self.subtotal} != {esperado}")
        return self


class Cotizacion(StrictModel):
    moneda: str = Field(pattern=r"^ARS$")
    catalogo_validado: bool
    items: list[ItemCotizacion]
    total_estimado: float | None

    @model_validator(mode="after")
    def validar_total(self) -> "Cotizacion":
        suma = sum(item.subtotal for item in self.items)
        if self.total_estimado is None:
            if self.items:
                raise ValueError("total_estimado no puede ser null si hay ítems")
        elif not isclose(self.total_estimado, suma, rel_tol=0, abs_tol=0.01):
            raise ValueError(f"total inválido: {self.total_estimado} != {suma}")
        return self


class Propuesta(StrictModel):
    estado: Estado
    consulta_id: str = Field(min_length=1, max_length=80)
    confianza: float = Field(ge=0, le=1)
    datos_faltantes: list[str]
    paquete_recomendado: Recomendacion | None
    alternativa: Alternativa | None = None
    cotizacion: Cotizacion
    alertas: list[str]
    mensaje_whatsapp: str = Field(max_length=1800)
    resumen_interno: dict[str, Any]
    requiere_revision_humana: bool
    motivos_revision: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def controles_de_gobierno(self) -> "Propuesta":
        if self.requiere_revision_humana is not True:
            raise ValueError("requiere_revision_humana debe ser true")
        if self.estado == Estado.REQUIERE_DATOS and not self.datos_faltantes:
            raise ValueError("REQUIERE_DATOS exige datos_faltantes")
        texto = self.mensaje_whatsapp.lower()
        prohibidas = ("fecha confirmada", "reserva confirmada", "descuento aplicado")
        if any(frase in texto for frase in prohibidas):
            raise ValueError("el mensaje contiene una confirmación no autorizada")
        return self
