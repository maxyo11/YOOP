from MainProject.DBops import DBops


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