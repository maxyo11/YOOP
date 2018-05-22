# -*- coding: utf-8 -*-
from __future__ import division
#We import everything from tkInter for the user interface
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from MainProject.Calculation import Calculation



def window(main):
    main.title('Crypto Prediction')

    #500x500 pixels
    #and centered for all sizes of user's screen
    main.update_idletasks()
    width = 500
    height = 500
    x = (main.winfo_screenwidth() // 2 ) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)

    main.geometry('{}x{}+{}+{}'.format(width,height, x, y))


    firstText = Label(main, text="Hi! please select a currency:", font = ("Helvetica", 30, "bold"))
    firstText.place(relx=0.5, rely=0.15, anchor=CENTER)

    #Create buttons and commands
    bitcoinButton = Button(main, text="Bitcoin", font = ("Helvetica", 15, "bold"),
                           command = lambda: Calculation().regressionCrypto(currency="Bitcoin",
                                                              cryptoVal="bitcoin",
                                                              cryptoNum= "1"))
    bitcoinButton.place(relx=0.5, rely=0.3, anchor=CENTER)

    rippleButton = Button(main, text="Ripple", font = ("Helvetica", 15, "bold"),
                          command = lambda: Calculation().regressionCrypto(currency="Ripple",
                                                             cryptoVal="ripple",
                                                             cryptoNum= "52"))
    rippleButton.place(relx=0.5, rely=0.4, anchor=CENTER)

    ethereumButton = Button(main, text="Ethereum", font=("Helvetica", 15, "bold"),
                            command = lambda: Calculation().regressionCrypto(currency="Ethereum",
                                                               cryptoVal="ethereum",
                                                               cryptoNum= "1027"))
    ethereumButton.place(relx=0.5, rely=0.5, anchor=CENTER)

    cardanoButton = Button(main, text="Cardano", font=("Helvetica", 15, "bold"),
                           command = lambda: Calculation().regressionCrypto(currency="Cardano",
                                                              cryptoVal="cardano",
                                                              cryptoNum= "2010"))
    cardanoButton.place(relx=0.5, rely=0.6, anchor=CENTER)

    litecoinButton = Button(main, text="Litecoin", font=("Helvetica", 15, "bold"),
                            command = lambda: Calculation().regressionCrypto(currency="Litecoin",
                                                               cryptoVal="litecoin",
                                                               cryptoNum= "2"))
    litecoinButton.place(relx=0.5, rely=0.7, anchor=CENTER)

def view():
    root = Tk()
    window(root)
    mainloop()




