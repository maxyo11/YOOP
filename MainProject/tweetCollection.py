import oauth2 as oauth
import json
import datetime
import config
from datetime import datetime, timezone
import pytz
from MainProject.twitterDataDao import twitterDataDao
import google.cloud.language
import pandas as pd

"""
This class allows us to collect Tweets from the Twitter API. We loop through the list of currencies which we want to
analyse. For each currency an API call is made. We get the response in .json format. To get the individual Tweets
out of the response we have to loop through a list of around 100 Tweets. For each api call we can collect up to 100
Tweets. The text of each Tweet is then passed through the analyseSentiment method. This method responds with the
sentiment of the text. At that point we have collected all the values of the tweet we need. Those values are then sent
to the TwitterDataDao.
"""

class tweetCollection:
    def __init__(self):
        self.placeholder = None

    def callapi(self):

        consumer = oauth.Consumer(key=config.myKey, secret=config.mySecret)
        access_token = oauth.Token(key=config.myToken, secret=config.myTokenSecret)
        client = oauth.Client(consumer, access_token)

        cryptoDataPosts = ['bitcoin', 'ethereum', 'ripple', 'cardano', 'litecoin']
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
            for a in range(0, 105):
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
                sentimentResult = tweetCollection().analyseSentiment(t)
                twitterDataDao().updateTwitterTable(user, tweetID, postDate, tweetText, followers, retweet, val, sentimentResult)

    def analyseSentiment(self, t):
        # environment variable needs to be set: GOOGLE_APPLICATION_CREDENTIALS="Key Location"
        # This way we can leave the argument for the LanguageServiceClient empty.
        language_client = google.cloud.language.LanguageServiceClient()

        # Make an authenticated API request
        # Specify the text you want to analyse
        text = t
        document = google.cloud.language.types.Document(
            content=text,
            language='en',
            type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

        # Use Language to detect the sentiment of the text.
        response = language_client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment
        #print(u'Text: {}'.format(text))
        #print(u'Sentiment: Score: {}, Magnitude: {}'.format(
         #   sentiment.score, sentiment.magnitude))
        sentimentResult = sentiment.score
        return sentimentResult

    def getAnalysis(self,cryptoName):
        data = twitterDataDao().selectTweets(cryptoName)
        df = pd.DataFrame(data)
        df.column[1].map(lambda x: x.strftime('%Y-%m-%d'))
        print(df)
        print(data)
        # for row in data:
        # print row[0], row[1], row[2], row[3], row[5]

        nbPosts = sum(row[0] for row in data)
        sumFollowers = sum(row[2] for row in data)
        sumRetweet = sum(row[3] for row in data) / nbPosts
        countSentiment = len(filter(None, (row[5] for row in data)))
        sumSentiment = (sum(filter(None, (row[5] for row in data))) / countSentiment) * nbPosts
        print(f"{cryptoName}:")
        print(sumFollowers)
        print(nbPosts)
        print(sumRetweet)
        print(sumSentiment)

        tweetsValue = sumRetweet + sumFollowers + sumSentiment

        print(tweetsValue_bitcoin)
        print(countSentiment)



def main():
    #tweetText = callapi2()
    #sentimentresult = cloudlanguage.analyseSentiment()
    while True:
        tweetCollection.callapi(self)
    #if input("x to stop") == 'x':
     #   break


#if __name__ == '__main__':
   # tweetCollection().callapi()


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