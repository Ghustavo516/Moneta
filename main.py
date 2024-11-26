from fastapi import FastAPI

from Moneta.model.real_estate_model import RealEstateModel
from Moneta.model.stocks_model import StocksModel
from Moneta.scrapper.market_info_extractor import MarketInfoExtractor
from Moneta.scrapper.real_estate_scrapper import RealEstateScrapper

app = FastAPI()
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



