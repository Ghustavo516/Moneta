import re

import requests
from bs4 import BeautifulSoup
from typing import Dict, Union
from Moneta.model.stocks_model import StocksModel

class MarketInfoExtractor:

    global headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    def extract_value_and_percentage(self, value:str) -> Dict[str, Union[str, None]]:
        match = re.match(r"([0-9,\.]+)\s?(bi|tri)?\s?(-?[\d,\.]+%)?", value.strip())
        if match:
            value = match.group(1).replace(',', '.')
            unit = match.group(2) if match.group(2) else None
            percentage = match.group(3) if match.group(3) else None
            return {"value": value, "unit": unit, "percentage":percentage}
        return {"value": None, "unit": None, "percentage":None}

    def clean_string(value: str) -> str:
        return value.encode('utf-8', 'ignore').decode('utf-8').replace('\xa0', '').strip()

    def map_stocks_model(self, values: Dict[str, str]) -> StocksModel:
        stocks_model = StocksModel(
            name = values.get("Nome"),
            price=values.get("Preco"),
            percentage_variation=values.get("Percentual Variacao"),
            value_variation=values.get("Valor Variação"),
            date_market=values.get("Data"),
            last_closing_value=values.get("Último fechamento"),
            today_variation=values.get("Variações de hoje"),
            year_variation=values.get("Variações do ano"),
            market_capitalization=values.get("Capitalização de mercado"),
            medium_volume=values.get("Volume médio"),
            pl_index=values.get("Índice P/L"),
            yield_dividends=values.get("Rend. de dividendos"),
            main_stock_exchange=values.get("Bolsa principal"),
            ceo=values.get("CEO"),
            foundation_date=values.get("Data da fundação"),
            site=values.get("Site"),
            employees=values.get("Empregados"),
            revenue=values.get("Receita", ""),
            operation_expenses=values.get("Gastos operacionais", ""),
            net_income=values.get("Renda líquida", ""),
            net_profit_margin=values.get("Margem de lucro líquida", ""),
            earnings_per_share=values.get("Lucros por ação", ""),
            ebitda=values.get("LAJIDA", ""),
            effective_tax_rate=values.get("Carga tributária efetiva", ""),
            short_term_investments=values.get("Dinheiro e investimentos de curto prazo", ""),
            total_assets=values.get("Total de ativos", ""),
            total_liabilities=values.get("Total de passivos", ""),
            equity=values.get("Capital próprio", ""),
            shares_outstanding=values.get("Ações em circulação", ""),
            asset_value=values.get("Preço/Valor Patrimonial", ""),
            return_assets=values.get("Retorno sobre ativos", ""),
            return_equity=values.get("Retorno sobre capital", ""),
            cash_operations=values.get("Dinheiro das operações", ""),
            cash_investments=values.get("Dinheiro de investimentos", ""),
            cash_financing=values.get("Dinheiro de financiamentos", ""),
            net_change_cash=values.get("Variação líquida em dinheiro", ""),
            free_cash_flow=values.get("Fluxo de caixa livre", "")
        )
        return stocks_model


    def get_market_data(self, name):
        specification = {}
        url = f"https://www.google.com/finance/quote/{name}:BVMF?hl=pt"

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return []

        #Basic Infomation about finance market
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('div', attrs={'class', 'YMlKec fxKbKc'}).text
        name = soup.find('div', attrs={'class', 'zzDege'}).text
        percentage_variation = soup.find('span', attrs={'class', 'V53LMb'}).text
        value_variation = soup.find('span', attrs={'class', 'P2Luy Ez2Ioe ZYVHBb'})
        date_market = soup.find('div', attrs={'class', 'ygUjEc'}).text

        specification["Nome"] = name
        specification["Preco"] = price
        specification["Percentual Variacao"] = percentage_variation
        specification["Valor Variação"] = value_variation
        specification["Data"] = date_market

        #More details about finance item
        information_market = soup.find_all('div', attrs={'class': 'gyFHrc'})
        for i in information_market:
            name_info = i.find('div', attrs={'class': 'mfs7Fc'}).text
            values_info = i.find('div', attrs={'class': 'P6K39c'}).text
            specification[name_info] = values_info

        about_company = soup.findAll('span', attrs={'class', 'w4txWc oJeWuf'})
        for b in about_company:
            about_text = b.find('div', attrs={'class': 'bLLb2d'})
            info = b.find('div', attrs={'class': 'gyFHrc'})

            if info:
                role_about_company = info.find('div', attrs={'class': 'mfs7Fc'}).text
                value_role_about_company = info.find('div', attrs={'class': 'P6K39c'}).text
                specification[role_about_company] = value_role_about_company

        finance_values = soup.findAll('tr', attrs={'class', 'roXhBd'})

        for f in finance_values:
            line_table_finance = f.find('div', attrs={'class', 'rsPbEe'})
            name_role_finance = line_table_finance.text if line_table_finance else ""

            value_line_finance = f.find('td', attrs={'class', 'QXDnM'})
            value_period = value_line_finance.text if value_line_finance else ""

            variation_year_to_year = f.find('span', attrs={'class', 'JwB6zf Ez2Ioe CnzlGc'})
            value_variation = variation_year_to_year.text if variation_year_to_year else ""

            specification[name_role_finance] = f"{value_period} - {value_variation}"
        build_model = self.map_stocks_model(specification)
        return build_model
