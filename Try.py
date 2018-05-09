
import requests
from requests_oauthlib import OAuth1
import json
from datetime import date



def main_func(q):  # main function
    limit = int(raw_input('Enter the number of tweets you want :\t'))
    current_time = date.today()  # get the local date
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {'q': q, 'result': 'mixed', 'until': current_time, 'count': limit}
    auth = OAuth1('XXX', 'XXXX', 'XXX',
                  'XXX')  # add your auth details here
    r = requests.get(url, auth=auth, params=params)
    status = r.status_code
    print status
    if status == 200:
        display_tweets(r)


def display_tweets(r):  # diaplay the tweets
    r = r.json()  # parse the json
    tweets = r['statuses']
    l = len(tweets)
    print 'The Tweets for your entered query are:'
    for tweet in tweets:
        print 'Tweet %d :' % (l)+tweet['text']
        l -= 1


'''

#Authentication Google Cloud API:



def analyseSentiment():
    #Import Google Cloud package
    import google.cloud.language
    # environment variable needs to be set: GOOGLE_APPLICATION_CREDENTIALS="Key Location"
    # This way we can leave the argument for the LanguageServiceClient empty.
    language_client = google.cloud.language.LanguageServiceClient()

    # Make an authenticated API request
    #Specify the text you want to analyse
    text = 'Bitcoin is the best thing ever!'
    document = google.cloud.language.types.Document(
        content=text,
        type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

    # Use Language to detect the sentiment of the text.
    response = language_client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment
    print(u'Text: {}'.format(text))
    print(u'Sentiment: Score: {}, Magnitude: {}'.format(
        sentiment.score, sentiment.magnitude))

analyseSentiment()


# Create a Language client.
#language_client = google.cloud.language.LanguageServiceClient()
'''



q = raw_input('Enter the query you want tweets for :\t')
if q:
    main_func(q)