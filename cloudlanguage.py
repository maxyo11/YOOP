import config
import mysql.connector
import google.cloud.language



# Authentication Google Cloud API:
def analyseSentiment(t):
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
    print(u'Text: {}'.format(text))
    print(u'Sentiment: Score: {}, Magnitude: {}'.format(
        sentiment.score, sentiment.magnitude))
    sentimentresult = sentiment.score
    return sentimentresult



# Create a Language client.
# language_client = google.cloud.language.LanguageServiceClient()



