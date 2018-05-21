# -*- coding: utf-8 -*-

import mysql.connector
import config
import sys
import pandas as pd
import datetime
import calendar
import time
from bs4 import BeautifulSoup




def retrieve_bitcoin_tweets():
    cnx = mysql.connector.connect(user=config.User, password=config.password,
                                  host=config.host,
                                  database=config.database,
                                  charset=config.charset)
    cursor = cnx.cursor()
    #select the data from MySQL and create a panda table
    df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                   "from twitterTable "
                   "WHERE Currency= 'bitcoin' "
                   "GROUP BY id "
                   "ORDER BY postDate", con=cnx)

    df['postDate'] = pd.to_datetime(df['postDate'])
    df['postDate'] = df['postDate'].values.astype('datetime64[D]')
    result = df.groupby('postDate').sum()
    #now that we have a sum value of each day for each row,
    #sum the followers, retweets and sentiments, replacing  none values by 0
    sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment'])/result['COUNT(id)']
    lastSum = sum.iloc[-6:]
    print(lastSum)
    tweetsValue_bitcoin = lastSum.values.tolist()

    print(tweetsValue_bitcoin)



    # close the cursor object
    cursor.close()
    # close the connection
    cnx.close()
    # exit the program
    sys.exit()



if __name__ == '__main__':
    retrieve_bitcoin_tweets()


    #six_months = date.today() - relativedelta( months = +6 )
