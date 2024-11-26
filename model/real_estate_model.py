from decimal import Decimal

from pydantic import BaseModel
from typing import Optional


class RealEstateModel(BaseModel):

    name_ticket: Optional[str] = None
    name_company:Optional[str] = None
    cotacao:Optional[float] = None
    dividend_yield: Optional[float] = None
    dividend_yield_per_year: Optional[float] = None
    pv: Optional[float] = None
    liquidez_diaria: Optional[float] = None
    razao_social: Optional[str] = None
    cnpj: Optional[str] = None
    publico_alvo: Optional[str] = None
    mandato: Optional[str] = None
    segmento: Optional[str] = None
    tipo_fundo: Optional[str] = None
    prazo_duracao: Optional[str] = None
    tipo_gestao: Optional[str] = None
    taxa_administracao: Optional[str] = None
    vacancia: Optional[float] = None
    cotas_emitidas: Optional[int] = None
    valor_patrimonial_cota: Optional[Decimal] = None
    valor_patrimonial: Optional[str] = None
    ultimo_rendimento: Optional[float] = None


