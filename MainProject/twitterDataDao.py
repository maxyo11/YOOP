from MainProject.DBops import DBops
import sys
import pandas as pd


'''
This Database Access Object establishes a connection with our DB using the DBops class. It then uses this connection
to update the TwitterTable. The values (user, tweetID, postDate, ...) are passed by the callapi method of the
tweetCollection class. 
'''

class twitterDataDao:

    def __init__(self):
        self.DBops = DBops


    def updateTwitterTable(self, user, tweetID, postDate, tweetText, followers, retweet, val, sentimentResult):

        DBops().getDB()

        try:
            DBops.cnx.cursor().execute(
                "INSERT INTO twitterTable (user, tweet_ID, postDate, tweetText, followers, retweet, Currency, sentiment)"
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (user, tweetID, postDate, tweetText, followers, retweet, val, sentimentResult))
        finally:
            DBops.cnx.commit()
            DBops().disconnectDB()

    def selectTweets(self, cryptoName):
        DBops().getDB()
        cursor = DBops.cnx.cursor()
        try:
            df = pd.read_sql("select COUNT(id), postDate, followers, retweet, Currency, sentiment "
                             "from twitterTable "
                             f"WHERE Currency= '{cryptoName}' "
                             "GROUP BY id "
                             "ORDER BY postDate", con=DBops.cnx)
        finally:
            DBops().disconnectDB()

        return df





