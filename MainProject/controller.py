from MainProject.tweetCollection import tweetCollection
from MainProject.priceCollection import priceCollection
from MainProject.autoCollect import autoCollectThreading
from MainProject.viewInterface import view


class Controller:
    def __init__(self):
        self.running = 1

    def chooseFunction(self):
        print("Welcome to Plutus. This program might make you rich!")
        print("What would you like to do?")
        print("Your choices: \n 1. Collect tweets and crypto prices right now.\n"
              "2. Collect tweets and crypto prices automatically.\n"
              "3. Analyse a currency of your choice.\n "
              "4. Convert the price of a cryptocurrency to the price of a FIAT currency.")
        while self.running:
            choice = input("Please choose what you want to do. (1 / 2 / 3 / 4 ) ")
            if choice == "1":
                priceCollection().collectPrice()
                tweetCollection().callapi()
                break
            if choice == "2":
                print("Tweets will now be collected twice a day while this is running.\n"
                      "Cryptocurrency prices will be collected once every hour.")
                autoCollectThreading().run()
                break
            if choice == "3":
                view()
                break
            if choice == "4":
                #converterFunction
                break

            print("This was not a valid input! Please try again.")


