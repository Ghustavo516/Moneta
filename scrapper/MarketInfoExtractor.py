import requests
from bs4 import BeautifulSoup

class MarketInfoExtractor:

    global headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    def get_market_data(name):
        url = f"https://www.google.com/finance/quote/BBAS3:BVMF?hl=pt"

        try:
            response = requests.get(url=url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return []

        text_finance = ""

        #Basic Infomation about finance market
        soup = BeautifulSoup(response.content, 'html.parser')
        price_market = soup.find('div', attrs={'class', 'YMlKec fxKbKc'}).text
        name_market = soup.find('div', attrs={'class', 'zzDege'}).text
        percentage_change = soup.find('span', attrs={'class', 'V53LMb'}).text
        value_money_change = soup.find('span', attrs={'class', 'P2Luy Ez2Ioe ZYVHBb'})
        date_market = soup.find('div', attrs={'class', 'ygUjEc'}).text

        text_finance = f"Preço:{price_market}, Nome:{name_market}, Percentual Variação:{percentage_change}, Valor Variação:{value_money_change}, Data:{date_market}"

        #More details about finance item
        information_market = soup.find_all('div', attrs={'class': 'gyFHrc'})
        for i in information_market:
            name_info = i.find('div', attrs={'class': 'mfs7Fc'}).text
            values_info = i.find('div', attrs={'class': 'P6K39c'}).text
            text_finance += f" {name_info}:{values_info}, "
            # print(name_info + ' - ' + values_info)

        about_company = soup.findAll('span', attrs={'class', 'w4txWc oJeWuf'})
        for b in about_company:
            about_text = b.find('div', attrs={'class': 'bLLb2d'})
            info = b.find('div', attrs={'class': 'gyFHrc'})

            if info:
                role_about_company = info.find('div', attrs={'class': 'mfs7Fc'}).text
                value_role_about_company = info.find('div', attrs={'class': 'P6K39c'}).text

                text_finance += f"Sobre Empresa:{about_text.get_text()}"
                text_finance += f" {role_about_company}:{value_role_about_company},"

        finance_values = soup.findAll('tr', attrs={'class', 'roXhBd'})

        for f in finance_values:
            line_table_finance = f.find('div', attrs={'class', 'rsPbEe'})
            name_role_finance = line_table_finance.text if line_table_finance else ""

            value_line_finance = f.find('td', attrs={'class', 'QXDnM'})
            value_period = value_line_finance.text if value_line_finance else ""

            variation_year_to_year = f.find('span', attrs={'class', 'JwB6zf Ez2Ioe CnzlGc'})
            value_variation = variation_year_to_year.text if variation_year_to_year else ""

            text_finance += f" {name_role_finance}:{value_period} - {value_variation}, "

        print(text_finance)

            # print(name_role_finance + " - " + value_period + " - " + value_variation)


    get_market_data('name')