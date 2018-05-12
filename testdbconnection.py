import mysql.connector
import time
def testconnection():
    try:
        cnx = mysql.connector.connect(user='sql7234835', password='YF68XHI7r8',
                                      host='sql7.freemysqlhosting.net',
                                      database='sql7234835',
                                      charset='utf8mb4')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()



user = "Test3"
tweet_id = "2"
postDate = "1111"
tweetText = "565557"
followers = "2"
retweet = "3"
favorite = "4"

def insertintoDB():
    cnx = mysql.connector.connect(user='sql7234835', password='YF68XHI7r8',
                                  host='sql7.freemysqlhosting.net',
                                  database='sql7234835',
                                  charset='utf8mb4')

    cursor = cnx.cursor()
    cursor.execute("INSERT INTO twitterTable (user, tweet_id, postDate, tweetText, followers, retweet, favorite) VALUES (%s,%s,%s,%s,%s,%s,%s)", (user, tweet_id, postDate, tweetText, followers, retweet, favorite))
    cnx.commit()


insertintoDB()

'''
"INSERT INTO twitterTable"
    "VALUES (user, tweet_id, postDate, tweetText, followers, retweet, favorite) VALUES (%s,%s,%s,%s,%s,%s,%s)" % (
    user, tweet_id, postDate, tweetText, followers, retweet, favorite))

'''