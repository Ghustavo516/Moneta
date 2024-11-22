from pydantic import BaseModel
from typing import Optional

class StocksModel(BaseModel):
    # Informações gerais da empresa
    name_ticket: str
    name_company: Optional[str] = None
    cnpj: Optional[str] = None
    ano_estreia_bolsa: Optional[int] = None
    ano_fundacao: Optional[int] = None
    numero_funcionarios: Optional[float] = None
    setor: Optional[str] = None
    segmento: Optional[str] = None
    segmento_listagem: Optional[str] = None

    # Informações financeiras básicas
    cotacao: Optional[float] = None
    variation: Optional[float] = None
    valor_mercado: Optional[float] = None  # em bilhões, por exemplo
    valor_firma: Optional[float] = None  # em bilhões, por exemplo
    patrimonio_liquido: Optional[float] = None
    total_papeis: Optional[int] = None

    # Indicadores financeiros
    pl: Optional[float] = None  # Preço/Lucro
    pvp: Optional[float] = None  # Preço/Valor Patrimonial
    dividend_yield: Optional[float] = None  # Dividend Yield em %
    payout: Optional[float] = None  # Payout ratio em %
    margem_liquida: Optional[float] = None
    margem_bruta: Optional[float] = None
    margem_ebit: Optional[float] = None
    margem_ebitda: Optional[float] = None
    ev_ebit: Optional[float] = None
    p_ebit: Optional[float] = None
    p_receita_psr: Optional[float] = None # Preço/Receita
    p_ativo: Optional[float] = None
    p_cap_giro: Optional[float] = None
    p_ativo_circ_liq: Optional[float] = None
    vpa: Optional[float] = None  # Valor Patrimonial por Ação
    lpa: Optional[float] = None  # Lucro por Ação
    giro_ativos: Optional[float] = None
    roe: Optional[float] = None # Return on Equity em %
    roic: Optional[float] = None # Return on Invested Capital em %
    roa: Optional[float] = None # Return on Assets em %
    patrimonio_ativos: Optional[float] = None
    passivos_ativos: Optional[float] = None
    liquidez_corrente: Optional[float] = None

    # Indicadores de crescimento
    cagr_receita_cinco_anos: Optional[float] = None # Taxa de crescimento anual composta em %
    cagr_lucros_cinco_anos: Optional[float] = None # Taxa de crescimento de lucros em %

    # Informações de ativos
    ativos: Optional[float]= None
    ativo_circulante: Optional[float]= None
    disponibilidade: Optional[float] = None # Caixa e equivalentes

    # Outros
    free_float: Optional[float] = None # Percentual de ações em circulação no mercado
    tag_along: Optional[float] = None # Direito de venda conjunto em %

    # Liquidez
    liquidez_media_diaria: Optional[float] = None  # Volume médio diário em milhões
