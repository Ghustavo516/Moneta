from pydantic import BaseModel
from typing import Dict, Optional


class StocksModel(BaseModel):
    name: Optional[str]
    price: Optional[str]
    percentage_variation: Optional[str] = None
    value_variation: Optional[str] = None
    date_market: Optional[str] = None
    last_closing_value: Optional[str] = None
    today_variation: Optional[str] = None
    year_variation: Optional[str] = None
    market_capitalization: Optional[str] = None
    medium_volume: Optional[str] = None
    pl_index: Optional[str] = None
    yield_dividends: Optional[str] = None
    main_stock_exchange: Optional[str] = None
    ceo: Optional[str] = None
    foundation_date: Optional[str] = None
    site: Optional[str] = None
    employees: Optional[str] = None
    revenue: Optional[str] = None
    operation_expenses: Optional[str] = None
    net_income: Optional[str] = None
    net_profit_margin: Optional[str] = None
    earnings_per_share: Optional[str] = None
    ebitda: Optional[str] = None
    effective_tax_rate: Optional[str] = None
    short_term_investments: Optional[str] = None
    total_assets: Optional[str] = None
    total_liabilities: Optional[str] = None
    equity: Optional[str] = None
    shares_outstanding: Optional[str] = None
    asset_value: Optional[str] = None
    return_assets: Optional[str] = None
    return_equity: Optional[str] = None
    cash_operations: Optional[str] = None
    cash_investments: Optional[str] = None
    cash_financing: Optional[str] = None
    net_change_cash: Optional[str] = None
    free_cash_flow: Optional[str] = None



