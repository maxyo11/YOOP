import oauth2 as oauth
import json
import datetime
import mysql.connector
import config
from datetime import datetime, timezone
import pytz
import cloudlanguage
from MainProject.twitterDataDao import twitterDataDao
from MainProject.DBops import DBops


class tweetCollection:
    def __init__(self):
        self.placeholder = None

    def callapi(self):

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
            # This takes all Tweets out of the json list in twitterData
            # The first try checks if the tweet was a retweet. If it is it gets the main tweet and the retweet is ignored.
            for a in range(0, 100):
                try:
                    user = twitterData[a]['retweeted_status']['user']['screen_name']
                    tweetID = twitterData[a]['retweeted_status']['id_str']
                    postDate = datetime.strptime(twitterData[a]['retweeted_status']["created_at"],
                                                   '%a %b %d %H:%M:%S %z %Y'). \
                        replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                        strftime('%Y-%m-%d %H:%M:%S')
                    tweetText = twitterData[a]['retweeted_status']['text']
                    followers = twitterData[a]['retweeted_status']['user']['followers_count']
                    retweet = twitterData[a]['retweeted_status']['retweet_count']

                except KeyError:
                    try:
                        user = twitterData[a]['user']['screen_name']
                        tweetID = twitterData[a]['id_str']
                        postDate = datetime.strptime(twitterData[a]["created_at"], '%a %b %d %H:%M:%S %z %Y'). \
                        replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                        strftime('%Y-%m-%d %H:%M:%S')
                        tweetText = twitterData[a]['text']
                        followers = twitterData[a]['user']['followers_count']
                        retweet = twitterData[a]['retweet_count']
                        # insert the data to our db
                        # Change and coincide with db!
                    except (IndexError) as er:
                        print(er)
                except IndexError:
                    print("%s Tweets about %s have been collected." % (a, val))
                    break
                t = tweetText
                sentimentresult = cloudlanguage.analyseSentiment(t)
                twitterDataDao().updateTwitterTable(user, tweetID, postDate, tweetText, followers, retweet, val, sentimentresult)


def main():
    #tweetText = callapi2()
    #sentimentresult = cloudlanguage.analyseSentiment()
    while True:
        tweetCollection.callapi(self)
    #if input("x to stop") == 'x':
     #   break


if __name__ == '__main__':
    tweetCollection().callapi()


'''
Copy of Callapi:

def callapi():
    consumer = oauth.Consumer(key=config.myKey, secret=config.mySecret)
    access_token = oauth.Token(key=config.myToken, secret=config.myTokenSecret)
    client = oauth.Client(consumer, access_token)

    cnx = mysql.connector.connect(user=config.User, password=config.password,
                                  host=config.host,
                                  database=config.database,
                                  charset=config.charset)
    cursor = cnx.cursor()
    cryptoDataPosts = ['bitcoin', 'ethereum', 'ripple', 'iota', 'cardano', 'litecoin']
    # call twitter api to do a search with keyword from cryptoDataPosts
    for i, val in enumerate(cryptoDataPosts):
        bitcoinPosts = "https://api.twitter.com/1.1/search/tweets.json?l=en&count=100&q=/%s" % val
        response, data = client.request(bitcoinPosts)
        # Create a json object
        tweets = json.loads(data)
        # print(tweets)
        twitterData = tweets["statuses"]
        # This takes all Tweets out of the json list in twitterData
        # The first try checks if the tweet was a retweet. If it is it gets the main tweet and the retweet is ignored.
        for a in range(0, 100):
            try:
                user = twitterData[a]['retweeted_status']['user']['screen_name']
                tweetID = twitterData[a]['retweeted_status']['id_str']
                postDate = datetime.strptime(twitterData[a]['retweeted_status']["created_at"],
                                               '%a %b %d %H:%M:%S %z %Y'). \
                    replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                    strftime('%Y-%m-%d %H:%M:%S')
                tweetText = twitterData[a]['retweeted_status']['text']
                followers = twitterData[a]['retweeted_status']['user']['followers_count']
                retweet = twitterData[a]['retweeted_status']['retweet_count']

            except KeyError as ex:
                try:
                    user = twitterData[a]['user']['screen_name']
                    tweetID = twitterData[a]['id_str']
                    postDate = datetime.strptime(twitterData[a]["created_at"], '%a %b %d %H:%M:%S %z %Y'). \
                    replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                    strftime('%Y-%m-%d %H:%M:%S')
                    tweetText = twitterData[a]['text']
                    followers = twitterData[a]['user']['followers_count']
                    retweet = twitterData[a]['retweet_count']
                    # insert the data to our db
                    # Change and coincide with db!
                except (IndexError) as er:
                    print(er)
            except IndexError:
                print("%s Tweets about %s have been collected." % (a, val))
                break
            t = tweetText

            sentimentresult = cloudlanguage.analyseSentiment(t)

            cursor.execute(
                 "INSERT INTO twitterTable (user, tweet_ID, postDate, tweetText, followers, retweet, Currency, sentiment) "
                 "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (user, tweetID, postDate, tweetText, followers, retweet, val, sentimentresult))
            cnx.commit()



'''