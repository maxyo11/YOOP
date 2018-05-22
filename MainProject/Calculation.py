# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from MainProject.priceCollection import priceCollection
from MainProject.tweetCollection import tweetCollection

class Calculation:
    def __init__(self):
        self.Test = None

    def compute_coef(self, xNb, yNb):
        # Linear regression with function --> Y = b1*X + b0
        # determine the slope b1
        x = np.array(xNb)
        y = np.array(yNb)
        b1 = (((np.mean(x)*np.mean(y)) - np.mean(x*y))/
             ((np.mean(x)*np.mean(x)) - np.mean(x*x)))
        b1= round(b1, 2)
        #determine the intercept b0
        b0=(np.mean(y) - np.mean(x)*b1)
        b0 = round(b0, 2)
        return b1, b0

    """
    m = b1
    c = b0
    Y = b1x+ b0

    x= independant = tweets
    y= dependant = Crypto value

    The mathematical formula to calculate slope (m) is:

    (mean(x) * mean(y) – mean(x*y)) / ( mean (x)^2 – mean( x^2))

    The formula to calculate intercept (c) is:

    mean(y) – mean(x) * m

    """
    def regressionCrypto(self, currency, cryptoVal, cryptoNum):
        cryptoList = priceCollection().getPrice(cryptoVal)
        twitList = tweetCollection().getAnalysis(cryptoVal)
        new_tweets = tweetCollection().get_last_tweets(cryptoVal)
        b1, b0 = Calculation().compute_coef(twitList, cryptoList)
        actual_data = priceCollection().getActualPrice(cryptoNum)

        print(b1, b0)
        # create the regression caclulation
        regressionFunc = [(b1 * x) + b0 for x in twitList]
        # The prediction calculation
        bitcoinPredict = b1 * new_tweets + b0
        print(bitcoinPredict)
        print(regressionFunc)
        # create the regression graph and the view after the calculation
        upperTitle = plt.figure()
        upperTitle.canvas.set_window_title('%s Prediction' % currency)
        plt.scatter(twitList, cryptoList, color="red")
        plt.plot(twitList, regressionFunc)
        plt.ylabel("%s value in $" % currency)
        plt.xlabel("Tweets per day")

        plt.title('''Now 1 %s costs $ %s.-
                  We predict it will be worth $ %s .- tomorrow.''' % (currency, actual_data, bitcoinPredict))
        plt.show()

