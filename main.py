from scrapper.market_info_extractor import MarketInfoExtractor

finance = MarketInfoExtractor()
info_finance = finance.get_market_data('ITUB4')
print(info_finance)

# [] formatar os valores de acordo com os atribuitos e deixar pronto para o proximo passo