import urllib
import requests
import json

#URLs to call API


tickerURL = "https://api.coinmarketcap.com/v2/ticker/"


# Get data from URL
#request = requests.get(tickerURL)
#json_data = request.json.load()
# currentPrice = data['price']
# currentDate = data['timestamp']

def getPrice():
    tickerURL = "https://api.coinmarketcap.com/v2/ticker/"
    tickerURL += '/1/'
    json_data = requests.get(tickerURL).json()

    for item in json_data['data']:
        print(item)


def getHistoric():
    historicUrl = "https://coinmarketcap.northpole.ro/history.json?coin=bitcoin&period=14days&format=array"
    json_history = requests.get(historicUrl).json()

    for item2 in json_history['history']['20-24-04-2018']['price']:
        print(item2)

if __name__ == '__main__':
    #getPrice()
    getHistoric()

