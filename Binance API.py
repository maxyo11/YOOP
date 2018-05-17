import urllib
import requests
import json
import datetime
import time
import os
import mysql.connector
from mysql.connector import errorcode
import config



#URLs to call API
tickerURL = "https://api.coinmarketcap.com/v2/ticker/"


# 1 = bitcoin
# 1027 = Ethereum
# 52 = rippleURL
# 2 = litecoinURL
# 2010 = CardanoURL





def getPrice():
    #Connect to the database using the config.py file
    cnx = mysql.connector.connect(user=config.User, password=config.password,
                                  host=config.host,
                                  database=config.database,
                                  charset=config.charset)
    cursor = cnx.cursor()

    #get the bitcoin prices
    bitcoinURL = "https://api.coinmarketcap.com/v2/ticker/1/"
    bictoin_data = requests.get(bitcoinURL).json()['data']['quotes']['USD']['price']
    bictoin_time_weird = requests.get(bitcoinURL).json()['metadata']['timestamp']
    readable_bictoin_time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(bictoin_time_weird))

#insert it to the db
    cursor.execute(
        "INSERT INTO bitcoinData (bictoin_data,readable_bictoin_time) VALUES (%s,%s)",
        (bictoin_data,readable_bictoin_time))
    cnx.commit()

    print((bictoin_data,readable_bictoin_time))

#get the ethereum prices
    ethereumURL = "https://api.coinmarketcap.com/v2/ticker/1027/"
    ethereum_data = requests.get(ethereumURL).json()['data']['quotes']['USD']['price']
    ethereum_time_weird = requests.get(ethereumURL).json()['metadata']['timestamp']
    readable_ethereum_time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ethereum_time_weird))

#insert it to the db
    cursor.execute(
        "INSERT INTO ethereumData (ethereum_data,readable_ethereum_time) VALUES (%s,%s)",
        (ethereum_data,readable_ethereum_time))
    cnx.commit()

    print((ethereum_data,readable_ethereum_time))

#get the ripple prices
    rippleURL = "https://api.coinmarketcap.com/v2/ticker/52/"
    ripple_data = requests.get(rippleURL).json()['data']['quotes']['USD']['price']
    ripple_time_weird = requests.get(rippleURL).json()['metadata']['timestamp']
    readable_ripple_time= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ripple_time_weird))

#insert it to the db
    cursor.execute(
        "INSERT INTO rippleData (ripple_data,readable_ripple_time) VALUES (%s,%s)",
        (ripple_data,readable_ripple_time))
    cnx.commit()

    print((ripple_data,readable_ripple_time))

#get the litecoin prices
    litecoinURL = "https://api.coinmarketcap.com/v2/ticker/2/"
    litecoin_data = requests.get(litecoinURL).json()['data']['quotes']['USD']['price']
    litecoin_time_weird = requests.get(litecoinURL).json()['metadata']['timestamp']
    readable_litecoin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(litecoin_time_weird))

#insert it to the db
    cursor.execute(
        "INSERT INTO litecoinData (litecoin_data,readable_litecoin_time) VALUES (%s,%s)",
        (litecoin_data,readable_litecoin_time))
    cnx.commit()

    print((litecoin_data,readable_litecoin_time))

#get the cardano prices
    cardanoURL = "https://api.coinmarketcap.com/v2/ticker/2010/"
    cardano_data = requests.get(cardanoURL).json()['data']['quotes']['USD']['price']
    cardano_time_weird = requests.get(cardanoURL).json()['metadata']['timestamp']
    readable_cardano_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(cardano_time_weird))

#insert it to the db
    cursor.execute(
        "INSERT INTO cardanoData (cardano_data,readable_cardano_time) VALUES (%s,%s)",
        (cardano_data,readable_cardano_time))
    cnx.commit()

    print((cardano_data,readable_cardano_time))





if __name__ == '__main__':
    getPrice()
