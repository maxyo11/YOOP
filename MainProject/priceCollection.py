import requests
import time
from MainProject.priceDao import priceDao

class priceCollection:

    def __init__(self):
        self.test = None

    def getPrice(self):
        cryptoID = ['1', '1027', '52', '2', '2010']
        for i, val in enumerate(cryptoID):
            tickerURL = "https://api.coinmarketcap.com/v2/ticker/%s/" % val
            print(tickerURL)
            response = requests.get(tickerURL).json()
            name = response['data']['website_slug']
            print(name)
            price = response['data']['quotes']['USD']['price']
            print(price)
            time_weird = response['metadata']['timestamp']
            readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_weird))
            priceDao().updatePrice(name, price, readable_time)


priceCollection().getPrice()