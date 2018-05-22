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
        # Authorize with Twitter API
        consumer = oauth.Consumer(key=config.myKey, secret=config.mySecret)
        access_token = oauth.Token(key=config.myToken, secret=config.myTokenSecret)
        client = oauth.Client(consumer, access_token)

        cryptoDataPosts = ['bitcoin', 'ethereum', 'ripple', 'cardano', 'litecoin']
        # Call twitter api to do a search with each keyword from cryptoDataPosts
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
                # Send the tweetText to the analyseSentiment Method and receive the Sentiment as a result
                t = tweetText
                sentimentResult = tweetCollection().analyseSentiment(t)
                # Send all the variables to the DB via the twitterDataDao
                twitterDataDao().updateTwitterTable(user, tweetID, postDate, tweetText, followers, retweet, val, sentimentResult)

    def analyseSentiment(self, t):
        # environment variable needs to be set: GOOGLE_APPLICATION_CREDENTIALS="Key Location"
        # This way we can leave the argument for the LanguageServiceClient empty.
        language_client = google.cloud.language.LanguageServiceClient()

        # Specify the text you want to analyse
        text = t
        document = google.cloud.language.types.Document(
            content=text,
            language='en',
            type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

        # Use Language to detect the sentiment of the text.
        response = language_client.analyze_sentiment(document=document)
        sentiment = response.document_sentiment
        sentimentResult = sentiment.score
        return sentimentResult


    def getAnalysis(self, cryptoName):
        df = twitterDataDao().selectTweets(cryptoName)
        df['postDate'] = pd.to_datetime(df['postDate'])
        df['postDate'] = df['postDate'].values.astype('datetime64[D]')
        result = df.groupby('postDate').sum()
        # now that we have a sum value of each day for each row,
        # sum the followers, retweets and sentiments, replacing  none values by 0
        sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) #/ result['COUNT(id)']
        lastSum = sum.iloc[-7:]
        tweetValue = lastSum.values.tolist()

        print(tweetValue)
        return  tweetValue


    def get_last_tweets(self,cryptoName):
        df = twitterDataDao().selectTweets(cryptoName)
        df['postDate'] = pd.to_datetime(df['postDate'])
        df['postDate'] = df['postDate'].values.astype('datetime64[D]')
        result = df.groupby('postDate').sum()
        # now that we have a sum value of each day for each row,
        # sum the followers, retweets and sentiments, replacing  none values by 0
        sum = (result['followers'] + result['retweet'] + result.fillna(0)['sentiment']) #/ result['COUNT(id)']
        lastSum = sum.iloc[-1]
        tweetValue = lastSum.tolist()

        print(tweetValue)
        return tweetValue
