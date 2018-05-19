from MainProject.DBops import DBops
import mysql.connector
import config

class twitterDataDao:

    def __init__(self):
        self.DBops = DBops


    def updateTwitterTable(self, user, tweetID, postDate, tweetText, followers, retweet, val, sentimentresult):

        DBops().getDB()

        try:
            DBops.cnx.cursor().execute(
                "INSERT INTO twitterTable (user, tweet_ID, postDate, tweetText, followers, retweet, Currency, sentiment)"
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (user, tweetID, postDate, tweetText, followers, retweet, val, sentimentresult))
        finally:
            DBops.cnx.commit()









'''        try:
            with DBops.cnx.cursor as cursor:
                cursor.execute(
                    "INSERT INTO twitterTable (user, tweet_ID, postDate, tweetText, followers, retweet, Currency,)"
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (user, tweetID, postDate, tweetText, followers, retweet, val,))
        except BaseException as ex:
            x = 1
        finally:
            DBops.cnx.commit()
            print('test')

'''