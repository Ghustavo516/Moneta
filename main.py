from scrapper.market_info_extractor import MarketInfoExtractor
# [] ajustar o metodo e fazer com que os dados saiam no formato do modelo 


finance = MarketInfoExtractor()
info_finance = finance.get_market_data('ITUB4')
print(info_finance)