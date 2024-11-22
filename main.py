from fastapi import FastAPI

from Moneta.model.stocks_model import StocksModel
from Moneta.scrapper.market_info_extractor import MarketInfoExtractor

app = FastAPI()
@app.post("/moneta-by-name")
async def get_info_finance_market(model: StocksModel):
    finance = MarketInfoExtractor()
    info_finance = finance.get_market_data(model.name_company)
    return info_finance

@app.post("/moneta-by-name-ticket")
async def get_info_finance_market(model: StocksModel):
    finance = MarketInfoExtractor()
    print(model.name_ticket)
    info_finance = finance.get_market_data('itub4')
    return info_finance


