import schedule
from MainProject.priceCollection import priceCollection
from MainProject.tweetCollection import tweetCollection
import threading

"""
This script automatically collects Cryptoprices and Tweets in a separated thread, while it is running.
The Tweet collection is limited to 2 times a day due to the Google Cloud Sentiment Analysis which costs money after
5000 Api calls. 
"""


def price():
    priceCollection().collectPrice()

def tweet():
    tweetCollection().callapi()

def test():
    print("Test")


""" 
Threading class:
    The run() method will be started and it will run in the background
    until the application is closed.
"""
class autoCollectThreading(object):


    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

        schedule.clear()                                # gets rid of old schedules
        schedule.every().hour.do(price)
        schedule.every().day.at("08:00").do(tweet)      # Tweet collection happens twice a day.
        schedule.every().day.at("20:00").do(tweet)
        schedule.every().day.at("08:00").do(price)
        schedule.every().day.at("20:00").do(price)

    def run(self):
        """ Method that runs forever """
        while True:
            schedule.run_pending()










