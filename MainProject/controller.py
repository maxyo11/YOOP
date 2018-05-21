from MainProject.tweetCollection import tweetCollection
from MainProject.priceCollection import priceCollection
from MainProject.autoCollect import autoCollectThreading
from MainProject.priceDao import priceDao

class Controller:
    def __init__(self):
        running = 1

    def chooseFunction(self):
        print("Welcome to Plutus. This program might make you rich!")
        print("What would you like to do?")
        print("Your choices: \n 1. Collect tweets and crypto prices right now.\n"
              "2. Collect tweets and crypto prices automatically.\n"
              "3. Analyse a currency of your choice.\n "
              "4. Convert the price of a cryptocurrency to the price of a FIAT currency.")
        while True:
            choice = input("Please choose what you want to do. (1 / 2 / 3 / 4 ) ")
            if choice == "1":
                #tweetCollection().callapi()
                priceCollection().collectPrice()
                break
            if choice == "2":
                print("Tweets will now be collected twice a day while this is running.")
                autoCollectThreading().run()
                break
            if choice == "3":
                while True:
                    cryptoName = input("Please choose a currency. (bitcoin, ethereum, ripple, cardano, litecoin) ")
                    NameList = ['bitcoin', 'ethereum', 'ripple', 'cardano', 'litecoin']
                    if cryptoName in NameList:
                        print(f"You have chosen {cryptoName}.")
                        resultPrices = priceCollection().getPrice(cryptoName)
                        resultAnalysis = tweetCollection().getAnalysis(cryptoName)
                        break
                    print("You have made an invalid choice, please try again!")
                break
            if choice == "4":
                #converterFunction
                break

            print("This was not a valid input! Please try again.")







Controller().chooseFunction()