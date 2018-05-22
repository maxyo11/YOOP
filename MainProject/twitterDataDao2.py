from MainProject.DBops import DBops
import pandas as pd



'''
Here we tried to Inert into the db2. Sadly we did not manage to do so. 
'''

class twitterDataDao:

    def __init__(self):
        self.DBops = DBops


    def updateTwitterTable(self, user, tweetID, postDate, tweetText, followers, retweet, val, sentimentResult):

        DBops().getDB()

        try:
            DBops.cnx.cursor().execute(
                "INSERT INTO user (user, followers)"
                "VALUES (%s,%s)",
                (user, followers))
            x = "LAST_INSERT_ID()"
            DBops.cnx.cursor().execute(
                "INSERT INTO twitterTable (tweetID, user_iduser postDate, tweetText, retweet, Currency, sentiment)"
                "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (tweetID, x, postDate, tweetText, retweet, val, sentimentResult))

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
