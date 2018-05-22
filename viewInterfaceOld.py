# -*- coding: utf-8 -*-
from __future__ import division
#We import everything from tkInter for the user interface
from tkinter import *
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import config
import mysql.connector
import requests
import sys
import pandas as pd
from MainProject.priceCollection import priceCollection
from MainProject.tweetCollection import tweetCollection





cryptoValueBitcoin = [1, 1, 7, 7, 11, 112]




def getActualPrice(value):

    #get the actual value of crypto currencies
    tickerURL = "https://api.coinmarketcap.com/v2/ticker/%s/" % value
    response = requests.get(tickerURL).json()
    actual_data = response['data']['quotes']['USD']['price']
    return actual_data


def compute_coef(xNb, yNb):
    #Linear regression with function --> Y = b1*X + b0
    #determine the slope b1
    x = np.array(xNb)
    y = np.array(yNb)
    b1 = (((np.mean(x)*np.mean(y)) - np.mean(x*y))/
         ((np.mean(x)*np.mean(x)) - np.mean(x*x)))
    b1= round(b1, 2)
    #determine the intercept b0
    b0=(np.mean(y) - np.mean(x)*b1)
    b0 = round(b0, 2)
    return b1, b0


def regressionCrypto(currency, cryptoVal, cryptoNum):
    cryptoList = priceCollection().getPrice(cryptoVal)
    twitList = tweetCollection().getAnalysis2(cryptoVal)
    new_tweets = tweetCollection().get_last_tweets(cryptoVal)
    b1, b0 = compute_coef(twitList, cryptoList)
    actual_data = getActualPrice(cryptoNum)

    print(b1, b0)
    # create the regression caclulation
    regressionFunc = [(b1*x) + b0 for x in twitList]
    # The prediction calculation
    bitcoinPredict = b1 * new_tweets + b0


    # create the regression graph and the view after the calculation
    upperTitle = plt.figure()
    upperTitle.canvas.set_window_title('%s Prediction' % currency)
    plt.scatter(cryptoList, twitList, color="red")
    plt.plot(cryptoList, regressionFunc)
    plt.ylabel("%s value in $" % currency)
    plt.xlabel("Tweets per day")

    plt.title('''Now 1 %s costs $ %s.-
              We predict it will be worth $ %s .- tomorrow.''' % (currency, actual_data, bitcoinPredict))
    plt.show()



# create the user interface
class appView():

#Create GUI
    root = Tk()
    def window(main):
        main.title('Crypto Prediction')

        # 500x500 pixels
        # and centered for all sizes of user's screen
        main.update_idletasks()
        width = 500
        height = 500
        x = (main.winfo_screenwidth() // 2 ) - (width // 2)
        y = (main.winfo_screenheight() // 2) - (height // 2)

        main.geometry('{}x{}+{}+{}'.format(width,height, x, y))


        firstText = Label(main, text="Hi! please select a currency:", font = ("Helvetica", 30, "bold"))
        firstText.place(relx=0.5, rely=0.15, anchor=CENTER)

        #Create buttons and commands
        bitcoinButton = Button(main, text="Bitcoin", font = ("Helvetica", 15, "bold"),
                               command = lambda: regressionCrypto(currency="Bitcoin",
                                                                  cryptoVal="bitcoin",
                                                                  cryptoNum= "1"))
        bitcoinButton.place(relx=0.5, rely=0.3, anchor=CENTER)

        rippleButton = Button(main, text="Ripple", font = ("Helvetica", 15, "bold"),
                              command = lambda: regressionCrypto(currency="Ripple",
                                                                 cryptoVal="ripple",
                                                                 cryptoNum= "52"))
        rippleButton.place(relx=0.5, rely=0.4, anchor=CENTER)

        ethereumButton = Button(main, text="Ethereum", font=("Helvetica", 15, "bold"),
                                command = lambda: regressionCrypto(currency="Ethereum",
                                                                   cryptoVal="ethereum",
                                                                   cryptoNum= "1027"))
        ethereumButton.place(relx=0.5, rely=0.5, anchor=CENTER)

        cardanoButton = Button(main, text="Cardano", font=("Helvetica", 15, "bold"),
                               command = lambda: regressionCrypto(currency="Cardano",
                                                                  cryptoVal="cardano",
                                                                  cryptoNum= "2010"))
        cardanoButton.place(relx=0.5, rely=0.6, anchor=CENTER)

        litecoinButton = Button(main, text="Litecoin", font=("Helvetica", 15, "bold"),
                                command = lambda: regressionCrypto(currency="Litecoin",
                                                                   cryptoVal="litecoin",
                                                                   cryptoNum= "2"))
        litecoinButton.place(relx=0.5, rely=0.7, anchor=CENTER)


    window(root)
    mainloop()
