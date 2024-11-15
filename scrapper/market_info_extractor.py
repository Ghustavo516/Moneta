import re
from calendar import firstweekday

import requests
from bs4 import BeautifulSoup
from typing import Dict, Union

from pygments.lexer import words

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
            name_ticket = values.get("Nome"),
            name_company=values.get("Preco"),
            cnpj=values.get("Percentual Variacao"),
            ano_estreia_bolsa=values.get("Valor Variação"),
            ano_fundacao=values.get("Data"),
            numero_funcionarios=values.get("Último fechamento"),
            setor=values.get("Variações de hoje"),
            segmento=values.get("Variações do ano"),
            segmento_listagem=values.get("Capitalização de mercado"),
            cotacao=values.get("Volume médio"),
            variation=values.get("Índice P/L"),
            valor_mercado=values.get("Rend. de dividendos"),
            valor_firma=values.get("Bolsa principal"),
            patrimonio_liquido=values.get("CEO"),
            total_papeis=values.get("Data da fundação"),
            pl=values.get("Site"),
            pvp=values.get("Empregados"),
            dividend_yield=values.get("Receita", ""),
            payout=values.get("Gastos operacionais", ""),
            margem_liquida=values.get("Renda líquida", ""),
            margem_bruta=values.get("Margem de lucro líquida", ""),
            margem_ebit=values.get("Lucros por ação", ""),
            margem_ebitda=values.get("LAJIDA", ""),
            ev_ebit=values.get("Carga tributária efetiva", ""),
            p_ebit=values.get("Dinheiro e investimentos de curto prazo", ""),
            p_receita_psr=values.get("Total de ativos", ""),
            p_ativo=values.get("Total de passivos", ""),
            p_cap_giro=values.get("Capital próprio", ""),
            p_ativo_circ_liq=values.get("Ações em circulação", ""),
            vpa=values.get("Preço/Valor Patrimonial", ""),
            lpa=values.get("Retorno sobre ativos", ""),
            giro_ativos=values.get("Retorno sobre capital", ""),
            roe=values.get("Dinheiro das operações", ""),
            roic=values.get("Dinheiro de investimentos", ""),
            roa=values.get("Dinheiro de financiamentos", ""),
            patrimonio_ativos=values.get("Variação líquida em dinheiro", ""),
            passivos_ativos=values.get("Fluxo de caixa livre", ""),
            liquidez_corrente=values.get("Fluxo de caixa livre", ""),
            cagr_receita_cinco_anos=values.get("Fluxo de caixa livre", ""),
            cagr_lucros_cinco_anos=values.get("Fluxo de caixa livre", ""),
            ativos=values.get("Fluxo de caixa livre", ""),
            ativo_circulante=values.get("Fluxo de caixa livre", ""),
            disponibilidade=values.get("Fluxo de caixa livre", ""),
            free_float=values.get("Fluxo de caixa livre", ""),
            tag_along=values.get("Fluxo de caixa livre", ""),
            liquidez_media_diaria=values.get("Fluxo de caixa livre", "")
        )
        return stocks_model

    def formmater_label_itens(self, name_item):
        if not words:
            return ""

        formatter_word = re.sub(r'[/.()\-\']', ' ', name_item).split()
        first_word = formatter_word[0].lower()
        other_words = ''.join(formatter_word[1:]).lower().capitalize()
        camel_case_text = first_word + other_words
        return camel_case_text

    def get_market_data(self, name_ticket):
        investor_info = {}
        url = f"https://investidor10.com.br/acoes/{name_ticket}/"

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return []

        #Basic Infomation about finance market
        soup = BeautifulSoup(response.content, 'html.parser')

        name_ticket = soup.find('div', attrs={'class', 'name-ticker'}).find('h1').get_text()
        name_company = soup.find('h2', attrs={'class', 'name-company'}).get_text()
        cotacao = soup.find('div', attrs={'class', '_card cotacao'}).find('div', class_='_card-body').get_text().strip()
        variacao = soup.find('div', attrs={'class', '_card pl'}).find('div', class_='_card-body').get_text().strip()
        pl = soup.find('div', attrs={'class', '_card val'}).find('div', class_='_card-body').get_text().strip()
        pvp = soup.find('div', attrs={'class', '_card vp'}).find('div', class_='_card-body').get_text().strip()
        dy = soup.find('div', attrs={'class', '_card dy'}).find('div', class_='_card-body').get_text().strip()

        investor_info["name_ticket"] = name_ticket
        investor_info['name_company'] = name_company
        investor_info['cotacao'] = cotacao
        investor_info['variation'] = variacao
        investor_info['pl'] = pl
        investor_info['pvp'] = pvp
        investor_info['dy'] = dy

        fundamental_indicators = soup.find('div', id =  'table-indicators')
        itens = fundamental_indicators.findAll('div', attrs={'class', 'cell'})
        # print(itens)

        for i in itens:
            name_itens = i.find('span', attrs={'class', 'd-flex justify-content-between align-items-center'}).get_text()
            value_itens = i.find('div', attrs={'class', 'value d-flex justify-content-between align-items-center'}).find('span').get_text().strip()
            investor_info[self.formmater_label_itens(name_itens)] = value_itens
            # print(f"{name_itens} - {value_itens}")

        information_company = soup.find('div', id = 'table-indicators-company')
        information_cells = information_company.findAll('div', attrs={'class', 'cell'})

        for info in information_cells:
            name_info = info.find('span', attrs={'class', 'title'}).get_text()

            if(info.find('div', attrs={'class', 'detail-value'}) != None):
                simple_value_info = info.find('div', attrs={'class', 'detail-value'}).get_text().strip()
            else:
                simple_value_info = info.find('span', attrs={'value'}).get_text().strip()
            investor_info[self.formmater_label_itens(name_info)] = simple_value_info
            # print(self.formmater_label_itens(name_info))
            # print(f"{name_info} - {simple_value_info}")

        basic_info_company = soup.find('div', id = 'data_about')
        lines_info = basic_info_company.findAll('tr')

        for basic_info in lines_info:
            label_info = basic_info.find('td').get_text()
            value_label_info = basic_info.find('td', attrs={'class', 'value'}).get_text()
            investor_info[self.formmater_label_itens(label_info)] = value_label_info
            # print(f"{label_info} - {value_label_info}")
        return investor_info



        # [] Terminar de desenvolver o mapeamento dos dados coletados para api

        



        # percentage_variation = soup.find('span', attrs={'class', 'V53LMb'}).text
        # value_variation = soup.find('span', attrs={'class', 'P2Luy Ez2Ioe ZYVHBb'})
        # date_market = soup.find('div', attrs={'class', 'ygUjEc'}).text
        #
        # investor_info["Nome"] = name
        # investor_info["Preco"] = price
        # investor_info["Percentual Variacao"] = percentage_variation
        # investor_info["Valor Variação"] = value_variation
        # investor_info["Data"] = date_market
        #
        # #More details about finance item
        # information_market = soup.find_all('div', attrs={'class': 'gyFHrc'})
        # for i in information_market:
        #     name_info = i.find('div', attrs={'class': 'mfs7Fc'}).text
        #     values_info = i.find('div', attrs={'class': 'P6K39c'}).text
        #     investor_info[name_info] = values_info
        #
        # about_company = soup.findAll('span', attrs={'class', 'w4txWc oJeWuf'})
        # for b in about_company:
        #     about_text = b.find('div', attrs={'class': 'bLLb2d'})
        #     info = b.find('div', attrs={'class': 'gyFHrc'})
        #
        #     if info:
        #         role_about_company = info.find('div', attrs={'class': 'mfs7Fc'}).text
        #         value_role_about_company = info.find('div', attrs={'class': 'P6K39c'}).text
        #         investor_info[role_about_company] = value_role_about_company
        #
        # finance_values = soup.findAll('tr', attrs={'class', 'roXhBd'})
        #
        # for f in finance_values:
        #     line_table_finance = f.find('div', attrs={'class', 'rsPbEe'})
        #     name_role_finance = line_table_finance.text if line_table_finance else ""
        #
        #     value_line_finance = f.find('td', attrs={'class', 'QXDnM'})
        #     value_period = value_line_finance.text if value_line_finance else ""
        #
        #     variation_year_to_year = f.find('span', attrs={'class', 'JwB6zf Ez2Ioe CnzlGc'})
        #     value_variation = variation_year_to_year.text if variation_year_to_year else ""
        #
        #     investor_info[name_role_finance] = f"{value_period} - {value_variation}"
        # build_model = self.map_stocks_model(investor_info)
        # return build_model




































