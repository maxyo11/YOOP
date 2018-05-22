import requests
import time
from MainProject.priceDao import priceDao
import sys
import pandas as pd
import numpy as np


class priceCollection:

    def __init__(self):
        self.test = None
        """This method calls the Coinmarketcap Api and stores the prices of the 5 currencies in the database using the
        priceDao."""

    def collectPrice(self):
        cryptoID = ['1', '1027', '52', '2', '2010']
        for i, val in enumerate(cryptoID):
            tickerURL = "https://api.coinmarketcap.com/v2/ticker/%s/" % val
            response = requests.get(tickerURL).json()
            name = response['data']['website_slug']
            price = response['data']['quotes']['USD']['price']
            time_weird = response['metadata']['timestamp']
            readable_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_weird))
            priceDao().updatePrice(name, price, readable_time)
            print(f"The price of {name} right now is ${price}.")


    def getPrice(self, cryptoName):
        df = priceDao().selectPrice(cryptoName)
        df[f'readable_{cryptoName}_time'] = pd.to_datetime(df[f'readable_{cryptoName}_time'])
        df[f'readable_{cryptoName}_time'] = df[f'readable_{cryptoName}_time'].values.astype('datetime64[D]')
        result = df.groupby(f'readable_{cryptoName}_time').describe()
        my_list = result[f"{cryptoName}_data"].values
        list_of_list = my_list.tolist()
        listSelect = [row[2] for row in list_of_list]
        # cryptoValue = map(lambda x: x.encode('ascii'), listSelect)
        cryptoValue = np.array(listSelect).astype(np.float)
        print(cryptoValue)
        return cryptoValue

    def getActualPrice(self, value):
        # get the actual value of crypto currencies
        tickerURL = "https://api.coinmarketcap.com/v2/ticker/%s/" % value
        response = requests.get(tickerURL).json()
        actual_data = response['data']['quotes']['USD']['price']
        return actual_data