from fastapi import FastAPI

from Moneta.model.real_estate_model import RealEstateModel
from Moneta.model.stocks_model import StocksModel
from Moneta.scrapper.stocks_scrapper import MarketInfoExtractor
from Moneta.scrapper.real_estate_scrapper import RealEstateScrapper

app = FastAPI(title="Moneta",
    description="API para consulta de dados do mercado financeiro",
    version="1.0.0")

@app.post("/stocks/by-name")
async def get_info_finance_market(model: StocksModel):
    finance = MarketInfoExtractor()
    info_finance = finance.get_market_data(model.name_company)
    return info_finance

@app.post("/stocks/by-name-ticket")
async def get_info_finance_market(model: StocksModel):
    finance = MarketInfoExtractor()
    info_finance = finance.get_market_data(model.name_ticket)
    return info_finance

@app.post("/fii/by-name-ticket")
async def get_info_real_estate(model:RealEstateModel):
    fiis = RealEstateScrapper()
    info_finance = fiis.get_real_estate_data(model.name_ticket)
    return info_finance


# [] Gerar o requeriments
# [] Documentar a api e gerar o swagger
# [] Finalizar read.me

# Desenvolver o intergrador para integrar todas as outras API para gerar o projeto completo





