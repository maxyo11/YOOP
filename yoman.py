import oauth2 as oauth
import json
import datetime
import mysql.connector
import config
from datetime import datetime, timezone
import pytz


#Authentificate to our MYSQL db
#utf8mb4 allows to support emoji (4 instead of 3 megabytes)

'''
cnx = mysql.connector.connect(user=config.User, password=config.password,
                            host=config.host,
                            database=config.database,
                            charset =config.charset)
cursor = cnx.cursor()

'''


#Authentificate to twitter API
#with keys and tokens

consumer = oauth.Consumer(key=config.myKey, secret=config.mySecret)
access_token = oauth.Token(key=config.myToken, secret=config.myTokenSecret)
client = oauth.Client(consumer, access_token)

'''

#list of crypto currencies we want to query
cryptoDataPosts = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'cardano', 'litecoin']

#call twitter api to do a search with keyword from cryptoDataPosts
for i, val in enumerate(cryptoDataPosts):
    bitcoinPosts = "https://api.twitter.com/1.1/search/tweets.json?l=en&count=100&q=/%s" % val
    response, data = client.request(bitcoinPosts)

# Create a json object
tweets = json.loads(data)
#print(tweets)


twitterData = tweets["statuses"]
#print(twitterData)


#test = twitterData[1]['retweeted_status']['user']['followers_count']
#print(test)


#tweetText = twitterData["text"]

# all the info we want to gather


# NEW: Below you can see how to gather data for each variable.
'''


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

    except (KeyError, IndexError) as er:
        pass
    print("Amount of tweets collected: %s" % a)
    print(er)


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
        # This takes all Tweets out of the json list in twitterData
        try:
            for a in range(0, 101):
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
        except (KeyError, IndexError) as ex:
                print("%s Tweets about %s have been collected." % (a, val))
                print(ex)
        # This takes the tweets which have been retweeted out of the results list.
        try:
            for a in range(0, 100):
                userrt = twitterData[a]['retweeted_status']['user']['screen_name']
                tweetIDrt = twitterData[a]['retweeted_status']['id_str']
                postDatert = datetime.strptime(twitterData[a]['retweeted_status']["created_at"],
                                               '%a %b %d %H:%M:%S %z %Y'). \
                    replace(tzinfo=timezone.utc).astimezone(pytz.timezone('Europe/Berlin')). \
                    strftime('%Y-%m-%d %H:%M:%S')
                tweetTextrt = twitterData[a]['retweeted_status']['text']
                followersrt = twitterData[a]['retweeted_status']['user']['followers_count']
                retweetrt = twitterData[a]['retweeted_status']['retweet_count']
                favoritert = twitterData[a]['retweeted_status']['favorite_count']

                print(userrt, tweetIDrt, postDatert, tweetTextrt, followersrt, retweetrt, favoritert)

        except (KeyError, IndexError) as er:
            pass
            print("Amount of tweets collected: %s" % a)
            print(er)


#callapi()

def callapi2():
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
                print(user)

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
                    print(user)
                except (IndexError) as er:
                    print(er)
                print(ex)
            except IndexError:
                print("Amount of tweets collected: %s" % a)
                break


            cnx = mysql.connector.connect(user=config.User, password=config.password,
                                              host=config.host,
                                              database=config.database,
                                              charset=config.charset)
            cursor = cnx.cursor()
            cursor.execute(
                 "INSERT INTO twitterTable (user, tweet_ID, postDate, tweetText, followers, retweet, Currency) "
                 "VALUES (%s,%s,%s,%s,%s,%s,%s)", (user, tweetID, postDate, tweetText, followers, retweet, val))
            cnx.commit()



callapi2()








'''
    #postViews = tweets ["engagement"]

    insert = "INSERT INTO TwitterData (bitcoinPosts) VALUES (%s)"
    cursor.execute(insert, (json.dumps(bitcoinPosts),))
    cnx.commit()


        cursor.execute(
            "INSERT INTO TwitterData (datetime, postViews, tweet) VALUES (%s,%s,%s)",
            (datetime, postViews, tweet))

        cnx.commit()
      

cnx.close()


#cnx.commit()

'''





























'''

#We import everything from tkInter for the user interface
from tkinter import *

#create the user interface
class appView():

#Create GUI
    root = Tk()
    def window(main):
        main.title('Crypto Prediction')

    # Our app shall be 500x500 pixels
    # and centered for all sizes of user'sscreen
        main.update_idletasks()
        width = 500
        height = 500
        x = (main.winfo_screenwidth() // 2 ) - (width // 2)
        y = (main.winfo_screenheight() // 2) - (height // 2)

        main.geometry('{}x{}+{}+{}'.format(width,height, x, y))

        #Create the frame for our buttons
        lf = Frame(main)
        lf.pack
        rf = Frame (main)
        rf.pack()

        #Create the Buttons
        b1 = Button(lf, text = "Trends", fg = "blue")
        b2 = Button (rf, text= "Predict", fg = "green")
        b1.pack(side=LEFT)
        b2.pack(side=RIGHT)
        lf.pack(side=LEFT)
        rf.pack(side=RIGHT)

    window(root)
    mainloop()


#Create the trends function
def trendsCrypto():
for i, val in enumerate(cryptoDataPosts):


#Create the prediction function
'''