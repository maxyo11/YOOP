import config
import mysql.connector
# connect to db:
cnx = mysql.connector.connect(user=config.User, password=config.password,
                            host=config.host,
                            database=config.database,
                            charset =config.charset)
cursor = cnx.cursor()

def getTweetText():
    cursor.execute("SELECT tweetText FROM twitterTable")
    row = cursor.fetchone()
    while row is not None:
        print(row[0])
        row = cursor.fetchone()
#getTweetText()

def get_average_sentiment():
    cursor.execute("SELECT AVG(followers) FROM twitterTable")
    average = cursor.fetchone()
    for a in average:
        print(a)




# Authentication Google Cloud API:
def analyseSentiment(t):
    # Import Google Cloud package
    import google.cloud.language
    # environment variable needs to be set: GOOGLE_APPLICATION_CREDENTIALS="Key Location"
    # This way we can leave the argument for the LanguageServiceClient empty.
    language_client = google.cloud.language.LanguageServiceClient()

    # Make an authenticated API request
    # Specify the text you want to analyse
    text = t
    document = google.cloud.language.types.Document(
        content=text,
        type=google.cloud.language.enums.Document.Type.PLAIN_TEXT)

    # Use Language to detect the sentiment of the text.
    response = language_client.analyze_sentiment(document=document)
    sentiment = response.document_sentiment
    print(u'Text: {}'.format(text))
    print(u'Sentiment: Score: {}, Magnitude: {}'.format(
        sentiment.score, sentiment.magnitude))
    sentimentresult = sentiment.score
    return sentimentresult



# Create a Language client.
# language_client = google.cloud.language.LanguageServiceClient()
