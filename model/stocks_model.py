from pydantic import BaseModel
from typing import Optional

class StocksModel(BaseModel):
    # Informações gerais da empresa
    name_ticket: str
    name_company: str
    cnpj: str
    ano_estreia_bolsa: Optional[int]
    ano_fundacao: Optional[int]
    numero_funcionarios: Optional[int]
    setor: str
    segmento: str
    segmento_listagem: str

    # Informações financeiras básicas
    cotacao: Optional[float]
    variation: Optional[float]
    valor_mercado: Optional[float]  # em bilhões, por exemplo
    valor_firma: Optional[float]  # em bilhões, por exemplo
    patrimonio_liquido: Optional[float]
    total_papeis: Optional[int]

    # Indicadores financeiros
    pl: Optional[float]  # Preço/Lucro
    pvp: Optional[float]  # Preço/Valor Patrimonial
    dividend_yield: Optional[float]  # Dividend Yield em %
    payout: Optional[float]  # Payout ratio em %
    margem_liquida: Optional[float]
    margem_bruta: Optional[float]
    margem_ebit: Optional[float]
    margem_ebitda: Optional[float]
    ev_ebit: Optional[float]
    p_ebit: Optional[float]
    p_receita_psr: Optional[float]  # Preço/Receita
    p_ativo: Optional[float]
    p_cap_giro: Optional[float]
    p_ativo_circ_liq: Optional[float]
    vpa: Optional[float]  # Valor Patrimonial por Ação
    lpa: Optional[float]  # Lucro por Ação
    giro_ativos: Optional[float]
    roe: Optional[float]  # Return on Equity em %
    roic: Optional[float]  # Return on Invested Capital em %
    roa: Optional[float]  # Return on Assets em %
    patrimonio_ativos: Optional[float]
    passivos_ativos: Optional[float]
    liquidez_corrente: Optional[float]

    # Indicadores de crescimento
    cagr_receita_cinco_anos: Optional[float]  # Taxa de crescimento anual composta em %
    cagr_lucros_cinco_anos: Optional[float]  # Taxa de crescimento de lucros em %

    # Informações de ativos
    ativos: Optional[float]
    ativo_circulante: Optional[float]
    disponibilidade: Optional[float]  # Caixa e equivalentes

    # Outros
    free_float: Optional[float]  # Percentual de ações em circulação no mercado
    tag_along: Optional[float]  # Direito de venda conjunto em %

    # Liquidez
    liquidez_media_diaria: Optional[float]  # Volume médio diário em milhões
