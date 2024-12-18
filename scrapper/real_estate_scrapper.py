
import requests
from typing import Dict
from bs4 import BeautifulSoup

from Moneta.model.real_estate_model import RealEstateModel
from Moneta.util.moneta_utils import MonetaUtils


class RealEstateScrapper():
    global headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    def real_estate_map(self, values: Dict[str, str]) -> RealEstateModel:
        real_estate = RealEstateModel(
            name_ticket = values.get("name_ticket"),
            name_company = values.get("name_company"),
            cotacao = values.get("cotacao"),
            dividend_yield = values.get("dividend_yield"),
            dividend_yield_per_year = values.get("dividend_yield_ano"),
            pv = values.get("pv"),
            liquidez_diaria = values.get("liquidez_diaria"),
            razao_social = values.get("razãoSocial"),
            cnpj = values.get("cnpj"),
            publico_alvo = values.get("públicoAlvo"),
            mandato = values.get("mandato"),
            segmento = values.get("segmento"),
            tipo_fundo = values.get("tipoDefundo"),
            prazo_duracao = values.get("prazoDeduração"),
            tipo_gestao = values.get("tipoDegestão"),
            taxa_administracao = values.get("taxaDeadministração"),
            vacancia = values.get("vacância"),
            numero_cotistas = values.get("numeroDecotistas"),
            cotas_emitidas = values.get("cotasEmitidas"),
            valor_patrimonial_cota = values.get("valPatrimonialpcota"),
            valor_patrimonial = values.get("valorPatrimonial"),
            ultimo_rendimento = values.get("últimoRendimento")
        )
        return real_estate

    def get_real_estate_data(self, name_ticket):
        real_estate_info = {}
        url = f"https://investidor10.com.br/fiis/{name_ticket}/"

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return []

        # Basic Infomation about finance market
        soup = BeautifulSoup(response.content, 'html.parser')

        name_ticket = soup.find('div', attrs={'class', 'name-ticker'}).find('h1').get_text()
        name_company = soup.find('h2', attrs={'class', 'name-company'}).get_text()
        cotacao = soup.find('div', attrs={'class', '_card cotacao'}).find('div', class_='_card-body').get_text().strip()
        dividend_yield = soup.find('div', attrs={'class', '_card dy'}).find('div', class_='_card-body').get_text()
        pv = soup.find('div', attrs={'class', '_card vp'}).find('div', class_='_card-body').get_text()
        liquidez_diaria = soup.find('div', attrs={'class', '_card val'}).find('div', class_='_card-body').get_text()
        dividend_yield_ano = soup.find('div', attrs={'class', '_card dy'}).find('div', class_='_card-body').get_text()

        real_estate_info["name_ticket"] = MonetaUtils.formmater_value_item(name_ticket)
        real_estate_info['name_company'] = MonetaUtils.formmater_value_item(name_company)
        real_estate_info['cotacao'] = MonetaUtils.formmater_value_item(cotacao)
        real_estate_info['dividend_yield'] = MonetaUtils.formmater_value_item(dividend_yield)
        real_estate_info['pv'] = MonetaUtils.formmater_value_item(pv)
        real_estate_info['liquidez_diaria'] = MonetaUtils.formmater_value_item(liquidez_diaria)
        real_estate_info['dividend_yield_ano'] = MonetaUtils.formmater_value_item(dividend_yield_ano)

        # Information Real Estate
        information_real = soup.find('div', id='table-indicators')
        lines_table = information_real.find_all('div', attrs={'class', 'cell'})

        for i in lines_table:
            name_itens = i.find('span', attrs={'class', 'd-flex justify-content-between align-items-center name'}).get_text()
            value_itens = i.find('div', attrs={'class', 'value'}).get_text()
            real_estate_info[MonetaUtils.formmater_label_itens(name_itens)] = MonetaUtils.formmater_value_item(value_itens)

        real_estate_model = self.real_estate_map(real_estate_info)
        return real_estate_model
