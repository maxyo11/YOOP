# -*- coding: utf-8 -*-

import mysql.connector
import config
import sys
import pandas as pd
import datetime
import calendar
import time


def retriveCrypto():
    cnx = mysql.connector.connect(user=config.User, password=config.password,
                                  host=config.host,
                                  database=config.database,
                                  charset=config.charset)
    cursor = cnx.cursor()

    #retrieve bitcoin values
    df = pd.read_sql("select bitcoin_data,readable_bitcoin_time from bitcoinData ORDER BY readable_bitcoin_time", con=cnx)
    df['readable_bitcoin_time'] = pd.to_datetime(df['readable_bitcoin_time'])
    df['readable_bitcoin_time'] = df['readable_bitcoin_time'].values.astype('datetime64[D]')
    result = df.groupby('readable_bitcoin_time').describe()
    my_list = result["bitcoin_data"].values
    list_of_list = my_list.tolist()
    cryptoValueBitcoin = [row[2] for row in list_of_list]


    print (cryptoValueBitcoin)

    #retrieve ripple values
    df = pd.read_sql("select ripple_data,readable_ripple_time from rippleData ORDER BY readable_ripple_time", con=cnx)
    df['readable_ripple_time'] = pd.to_datetime(df['readable_ripple_time'])
    df['readable_ripple_time'] = df['readable_ripple_time'].values.astype('datetime64[D]')
    result = df.groupby('readable_ripple_time').describe()
    my_list = result["ripple_data"].values
    list_of_list = my_list.tolist()
    cryptoValueRipple = [row[2] for row in list_of_list]

    print (cryptoValueRipple)

    #retrieve ethereum values
    df = pd.read_sql("select ethereum_data,readable_ethereum_time from ethereumData ORDER BY readable_ethereum_time", con=cnx)
    df['readable_ethereum_time'] = pd.to_datetime(df['readable_ethereum_time'])
    df['readable_ethereum_time'] = df['readable_ethereum_time'].values.astype('datetime64[D]')
    result = df.groupby('readable_ethereum_time').describe()
    my_list = result["ethereum_data"].values
    list_of_list = my_list.tolist()
    cryptoValueEthereum = [row[2] for row in list_of_list]

    print (cryptoValueEthereum)

    #retrieve cardano values
    df = pd.read_sql("select cardano_data,readable_cardano_time from cardanoData ORDER BY readable_cardano_time", con=cnx)
    df['readable_cardano_time'] = pd.to_datetime(df['readable_cardano_time'])
    df['readable_cardano_time'] = df['readable_cardano_time'].values.astype('datetime64[D]')
    result = df.groupby('readable_cardano_time').describe()
    my_list = result["cardano_data"].values
    list_of_list = my_list.tolist()
    cryptoValueCardano = [row[2] for row in list_of_list]

    print (cryptoValueCardano)

    #retrieve litecoin values
    df = pd.read_sql("select litecoin_data,readable_litecoin_time from litecoinData ORDER BY readable_litecoin_time", con=cnx)
    df['readable_litecoin_time'] = pd.to_datetime(df['readable_litecoin_time'])
    df['readable_litecoin_time'] = df['readable_litecoin_time'].values.astype('datetime64[D]')
    result = df.groupby('readable_litecoin_time').describe()
    my_list = result["litecoin_data"].values
    list_of_list = my_list.tolist()
    cryptoValueLitecoin = [row[2] for row in list_of_list]

    print (cryptoValueLitecoin)

    # close the cursor object
    cursor.close()
    # close the connection
    cnx.close()
    # exit the program
    sys.exit()

def retrieve_tweets():
    cnx = mysql.connector.connect(user=config.User, password=config.password,
                                  host=config.host,
                                  database=config.database,
                                  charset=config.charset)
    cursor = cnx.cursor()

    # BITCOIN

    # select the data from MySQL and create a panda table
    df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                     "from twitterTable "
                     "WHERE Currency= 'bitcoin' "
                     "GROUP BY id "
                     "ORDER BY postDate", con=cnx)

    df['postDate'] = pd.to_datetime(df['postDate'])
    df['postDate'] = df['postDate'].values.astype('datetime64[D]')
    result = df.groupby('postDate').sum()
    # now that we have a sum value of each day for each row,
    # sum the followers, retweets and sentiments, replacing  none values by 0
    sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) / result['COUNT(id)']
    lastSum = sum.iloc[-6:]
    print(lastSum)
    tweetsValue_bitcoin = lastSum.values.tolist()

    print(tweetsValue_bitcoin)


    # RIPPLE

    # select the data from MySQL and create a panda table
    df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                     "from twitterTable "
                     "WHERE Currency= 'ripple' "
                     "GROUP BY id "
                     "ORDER BY postDate", con=cnx)

    df['postDate'] = pd.to_datetime(df['postDate'])
    df['postDate'] = df['postDate'].values.astype('datetime64[D]')
    result = df.groupby('postDate').sum()
    # now that we have a sum value of each day for each row,
    # sum the followers, retweets and sentiments, replacing  none values by 0
    sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) / result['COUNT(id)']
    lastSum = sum.iloc[-6:]
    print(lastSum)
    tweetsValue_ripple = lastSum.values.tolist()

    print(tweetsValue_ripple)

    # ETHEREUM

    # select the data from MySQL and create a panda table
    df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                     "from twitterTable "
                     "WHERE Currency= 'ethereum' "
                     "GROUP BY id "
                     "ORDER BY postDate", con=cnx)

    df['postDate'] = pd.to_datetime(df['postDate'])
    df['postDate'] = df['postDate'].values.astype('datetime64[D]')
    result = df.groupby('postDate').sum()
    # now that we have a sum value of each day for each row,
    # sum the followers, retweets and sentiments, replacing  none values by 0
    sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) / result['COUNT(id)']
    lastSum = sum.iloc[-6:]
    print(lastSum)
    tweetsValue_ethereum = lastSum.values.tolist()

    print(tweetsValue_ethereum)

    # LITECOIN

    # select the data from MySQL and create a panda table
    df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                     "from twitterTable "
                     "WHERE Currency= 'litecoin' "
                     "GROUP BY id "
                     "ORDER BY postDate", con=cnx)

    df['postDate'] = pd.to_datetime(df['postDate'])
    df['postDate'] = df['postDate'].values.astype('datetime64[D]')
    result = df.groupby('postDate').sum()
    # now that we have a sum value of each day for each row,
    # sum the followers, retweets and sentiments, replacing  none values by 0
    sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) / result['COUNT(id)']
    lastSum = sum.iloc[-6:]
    print(lastSum)
    tweetsValue_litecoin = lastSum.values.tolist()

    print(tweetsValue_litecoin)

    # CARDANO

    # select the data from MySQL and create a panda table
    df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                     "from twitterTable "
                     "WHERE Currency= 'cardano' "
                     "GROUP BY id "
                     "ORDER BY postDate", con=cnx)

    df['postDate'] = pd.to_datetime(df['postDate'])
    df['postDate'] = df['postDate'].values.astype('datetime64[D]')
    result = df.groupby('postDate').sum()
    # now that we have a sum value of each day for each row,
    # sum the followers, retweets and sentiments, replacing  none values by 0
    sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) / result['COUNT(id)']
    lastSum = sum.iloc[-6:]
    print(lastSum)
    tweetsValue_cardano = lastSum.values.tolist()

    print(tweetsValue_cardano)


    # close the cursor object
    cursor.close()
    # close the connection
    cnx.close()
    # exit the program
    sys.exit()



if __name__ == '__main__':
    retrieve_tweets()




'''

1. separate per day and per currency!

finalValue = X + Y*numberOfDailyTweets * 

SUMOF: ( eachFollowers*A + eachRetweets*B + eachSentiment*C)


Nbtweets

(Sumsentiment /1000)*nbTweets

sumRetweets
sumFollowers


Regression:
X1: Number of tweet per day
X2: Sum of value of tweets (%100 

Y= Value of bitcoin


Shall I add the same calculation to the code? 
https://bitinfocharts.com/comparison/tweets-price-btc-eth-ltc-xrp-ada.html


I: Make the regression inversed --> ŷ = b1X1 + b2X2 + a
a) Convert bitinfocharts into json, collect and send to the db the infos
b) take into account the number of tweets per day X1, the sum of value of tweets X2 (followers and retweet for all, sentiment for the 1000 most followers one) and the value of the currency Y 
c) Create the function and the graph with a interactive algorithm dependent of the currency and date
d) thus, the values b1, b2 and a will be created

II: Create the prediction
a) based on the interactive regression function, select the number of tweets in the past 24hours (X1) and the sum of tweet value (X2)
b) compute the predicted value of the currency (Y) 
c) Print a message

III: Create the View
a) 2 buttons: trends and prediction, followed by the choice of currency
b) trends show a graph and the function
c) prediction show the estimated value for currency tomorow, show the reliability of the regression (strong or weak), and tell either to buy or sell

'''

