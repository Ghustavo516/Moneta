import requests
from bs4 import BeautifulSoup
from typing import Dict

from Moneta.model.stocks_model import StocksModel
from Moneta.util.moneta_utils import MonetaUtils


class MarketInfoExtractor:

    global headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    def map_stocks_model(self, values: Dict[str, str]) -> StocksModel:
        print(values)
        stocks_model = StocksModel(
            name_ticket = values.get("name_ticket"),
            name_company=values.get("name_company"),
            cnpj=values.get("cnpj"),
            ano_estreia_bolsa=values.get("anoDeestreianabolsa"),
            ano_fundacao=values.get("anoDefundação"),
            numero_funcionarios=values.get("númeroDefuncionários"),
            setor=values.get("setor"),
            segmento=values.get("segmento"),
            segmento_listagem=values.get("segmentoDelistagem"),
            cotacao=values.get("cotacao"),
            variation=values.get("variation"),
            valor_mercado=values.get("valorDemercado"),
            valor_firma=values.get("valorDefirma"),
            patrimonio_liquido=values.get("patrimônioLíquido"),
            total_papeis=values.get("nºTotaldepapeis"),
            pl=values.get("pl"),
            pvp=values.get("pvp"),
            dividend_yield=values.get("dy"),
            payout=values.get("payout"),
            margem_liquida=values.get("margemLíquida"),
            margem_bruta=values.get("margemBruta"),
            margem_ebit=values.get("margemEbit"),
            margem_ebitda=values.get("margemEbitda"),
            ev_ebit=values.get("evEbit"),
            p_ebit=values.get("pEbit"),
            p_receita_psr=values.get("pAtivo"),
            p_ativo=values.get("pCapgiro"),
            p_cap_giro=values.get("pCapgiro"),
            p_ativo_circ_liq=values.get("pAtivocircliq"),
            vpa=values.get("vpa"),
            lpa=values.get("lpa"),
            giro_ativos=values.get("giroAtivos"),
            roe=values.get("roe"),
            roic=values.get("roic"),
            roa=values.get("roa"),
            patrimonio_ativos=values.get("patrimônioAtivos"),
            passivos_ativos=values.get("passivosAtivos"),
            liquidez_corrente=values.get("liquidezCorrente"),
            cagr_receita_cinco_anos=values.get("cagrReceitas5anos"),
            cagr_lucros_cinco_anos=values.get("cagrLucros5anos"),
            ativos=values.get("ativos"),
            ativo_circulante=values.get("ativoCirculante"),
            disponibilidade=values.get("disponibilidade"),
            free_float=values.get("freeFloat"),
            tag_along=values.get("tagAlong"),
            liquidez_media_diaria=values.get("liquidezMédiadiária")
        )
        return stocks_model

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

        investor_info["name_ticket"] = MonetaUtils.formmater_value_item(name_ticket)
        investor_info['name_company'] = MonetaUtils.formmater_value_item(name_company)
        investor_info['cotacao'] = MonetaUtils.formmater_value_item(cotacao)
        investor_info['variation'] = MonetaUtils.formmater_value_item(variacao)
        investor_info['pl'] = MonetaUtils.formmater_value_item(pl)
        investor_info['pvp'] = MonetaUtils.formmater_value_item(pvp)
        investor_info['dy'] = MonetaUtils.formmater_value_item(dy)

        fundamental_indicators = soup.find('div', id = 'table-indicators')
        itens = fundamental_indicators.findAll('div', attrs={'class', 'cell'})

        for i in itens:
            name_itens = i.find('span', attrs={'class', 'd-flex justify-content-between align-items-center'}).get_text()
            value_itens = i.find('div', attrs={'class', 'value d-flex justify-content-between align-items-center'}).find('span').get_text().strip()
            investor_info[MonetaUtils.formmater_label_itens(name_itens)] = MonetaUtils.formmater_value_item(value_itens)

        information_company = soup.find('div', id = 'table-indicators-company')
        information_cells = information_company.findAll('div', attrs={'class', 'cell'})

        for info in information_cells:
            name_info = info.find('span', attrs={'class', 'title'}).get_text()

            if(info.find('div', attrs={'class', 'detail-value'}) != None):
                simple_value_info = info.find('div', attrs={'class', 'detail-value'}).get_text().strip()
            else:
                simple_value_info = info.find('span', attrs={'value'}).get_text().strip()
            investor_info[MonetaUtils.formmater_label_itens(name_info)] = MonetaUtils.formmater_value_item(simple_value_info)

        basic_info_company = soup.find('div', id = 'data_about')
        lines_info = basic_info_company.findAll('tr')

        for basic_info in lines_info:
            label_info = basic_info.find('td').get_text()
            value_label_info = basic_info.find('td', attrs={'class', 'value'}).get_text()
            investor_info[MonetaUtils.formmater_label_itens(label_info)] = MonetaUtils.formmater_value_item(value_label_info)

        finance_model = self.map_stocks_model(investor_info)
        return finance_model