import base64
import requests
import oauth2 as oauth
import json
#Connect to our MySQL database
#and store the data
import datetime
import mysql.connector
from mysql.connector import errorcode
import time





#Authentificate to our MYSQL db
#utf8mb4 allows to support emoji (4 instead of 3 megabytes)
cnx = mysql.connector.connect(user='sql7234835', password='YF68XHI7r8',
                              host='sql7.freemysqlhosting.net',
                              database='sql7234835',
                              charset = 'utf8mb4')

cursor = cnx.cursor()


#Authentificate to twitter API
#with keys and tokens
myKey = "OoeDEgkX47RFyKcgKGplhg23Q"
mySecret = "4o0jJ8tNmFPlSbkyy8lMDaYazXpIc1f1GF21phvlpy28aPXVgm"
myToken = "989848008694083584-6ZReWbJgEIdqheN8LbO3d9FIlitUNhp"
myTokenSecret = "vLb5aLG4VOoZQBD2A4BCsb2DCZ8QhogR6A8Ly7OjUXxbL"

consumer = oauth.Consumer(key=myKey, secret=mySecret)
access_token = oauth.Token(key=myToken, secret=myTokenSecret)
client = oauth.Client(consumer, access_token)



#list of crypto currencies we want to query
cryptoDataPosts = ['bitcoin', 'ethereum', 'ripple', 'bitcoin cash', 'cardano', 'litecoin']

#call twitter api to do a search with keyword from cryptoDataPosts
for i, val in enumerate(cryptoDataPosts):
    bitcoinPosts = "https://api.twitter.com/1.1/search/tweets.json?l=en&q=/%s" % val
    response, data = client.request(bitcoinPosts)
# Create a json object
tweets = json.loads(data)


twitterData = tweets["statuses"]

for tweetInfo in twitterData:
    print(tweetInfo)

#tweetText = twitterData["text"]

#cursor.execute("INSERT * INTO twitterTable (user, tweet_id, postDate, tweetText, followers, retweet, favorite) VALUES (%s,%s,%s,%s,%s,%s,%s)" % (user, tweet_id, postDate, tweetText, followers, retweet, favorite))
#cnx.commit()



# all the info we want to gather
#if 'text' in tweets:


'''
user = twitterData["user"]["screen_name"]
tweet_id = twitterData["user"]["screen_name"]
postDate = twitterData["created_at"]
tweetText = twitterData["text"]
followers = twitterData["user"]["followers_count"]
retweet = twitterData["retweet_count"]
favorite = twitterData["favorite_count"]

    # insert the data to our db
    # Change and coincide with db!
cursor.execute("INSERT INTO twitterTable (user, tweet_id, postDate, tweetText, followers, retweet, favorite) VALUES (%s,%s,%s,%s,%s,%s,%s)", (user, tweet_id, postDate, tweetText, followers, retweet, favorite))
    cnx.commit()

print(user, tweet_id, postDate, tweetText, followers, retweet, favorite)

'''


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
