import oauth2 as oauth
import json
import datetime
import mysql.connector
import config
from datetime import datetime, timezone
import pytz

def dbconnect():
    cnx = mysql.connector.connect(user=config.User, password=config.password,
                                  host=config.host,
                                  database=config.database,
                                  charset=config.charset)



def callapi():
    consumer = oauth.Consumer(key=config.myKey, secret=config.mySecret)
    access_token = oauth.Token(key=config.myToken, secret=config.myTokenSecret)
    client = oauth.Client(consumer, access_token)

    cryptoDataPosts = ['bitcoin', 'ethereum', 'ripple', 'iota', 'cardano', 'litecoin']
    # call twitter api to do a search with keyword from cryptoDataPosts
    for i, val in enumerate(cryptoDataPosts):
        bitcoinPosts = "https://api.twitter.com/1.1/search/tweets.json?l=en&count=100&q=/%s" % val
        response, data = client.request(bitcoinPosts)
        # Create a json object
        tweets = json.loads(data)
        # print(tweets)

        twitterData = tweets["statuses"]
        try:
            for a in range(0, 150):
                user = twitterData[a]['user']['screen_name']
                tweetID = twitterData[a]['id_str']
                postDate = datetime.strptime(twitterData[a]["created_at"], '%a %b %d %H:%M:%S %z %Y'). \
                    replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                    strftime('%Y-%m-%d %H:%M:%S')
                tweetText = twitterData[a]['text']
                followers = twitterData[a]['user']['followers_count']
                retweet = twitterData[a]['retweet_count']
                favorite = twitterData[a]['favorite_count']
                # insert the data to our db
                # Change and coincide with db!
                cnx = mysql.connector.connect(user=config.User, password=config.password,
                                              host=config.host,
                                              database=config.database,
                                              charset=config.charset)
                cursor = cnx.cursor()
                cursor.execute(
                    "INSERT INTO twitterTable (user, tweet_ID, postDate, tweetText, followers, retweet, Currency) "
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (user, tweetID, postDate, tweetText, followers, retweet, val))
                cnx.commit()
                #print(user, val)
        except KeyError as ex:
                print("%s Tweets about %s have been collected.", a, val)
                print(ex)


def sendrttweetstodb():
    try:
        for a in range(0,100):
            userrt = twitterData[a]['retweeted_status']['user']['screen_name']
            tweetIDrt = twitterData[a]['retweeted_status']['id_str']
            postDatert = datetime.strptime(twitterData[a]['retweeted_status']["created_at"], '%a %b %d %H:%M:%S %z %Y').\
                replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                strftime('%Y-%m-%d %H:%M:%S')
            tweetTextrt = twitterData[a]['retweeted_status']['text']
            followersrt = twitterData[a]['retweeted_status']['user']['followers_count']
            retweetrt = twitterData[a]['retweeted_status']['retweet_count']
            favoritert = twitterData[a]['retweeted_status']['favorite_count']

            print(userrt, tweetIDrt, postDatert, tweetTextrt, followersrt, retweetrt, favoritert)

    except KeyError:
        pass
    print("Amount of tweets collected: %s" % a)


def collectstart():
    while True:
        callapi()
        if input("x to stop") == 'x':
            break


if __name__ == '__main__':
    collectstart()


