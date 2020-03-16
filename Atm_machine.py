import time
import pyttsx3
import datetime
import os
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak("Good Morning!, Ma'am")
        speak("Welcome to Global Bank Services")
        time.sleep(1)
        speak("swipe your card here")

    if currentH >= 12 and currentH < 18:
        speak("Good Afternoon!, Ma'am")
        speak("Welcome to Global Bank Services")
        speak("swipe your card here")

    if currentH >= 18 and currentH !=0:
        speak("Good Evening Mam")
        speak("Welcome to Global Bank Services")
        time.sleep(2)
        speak("swipe your card here")

greetMe()
    
atm_pin = 9999

transation = ["Balance Enquiry", "Withdraw Money","Deposit Money", "Change your pin", "Transfer Money", "Quit"]

pin = int(input(speak("Enter your 4 digit pin: ")))

if pin==atm_pin:
    
    speak(" Choose your Transaction: ")
    
    print("1. Balance Enquiry")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change your pin")
    print("5. Transfer Money")
    print("6. Quit")
    trans=input("transation: ")
    time.sleep(2)
    
    
    
    if trans == "Balance Enquiry":
        slip = input(speak("Do you want slip? "))
        time.sleep(2)
        speak("please wait, we are processing")
        time.sleep(2)
        if slip == "yes":
            speak("Here is your slip.... ")
            time.sleep(1)
            speak(".....Collect your Card.....")
            speak("Thankyou for using Global Bank Services ")
            speak("Have a nice day, Bye...")
        else:
            speak("Thankyou for using Global Bank Services ")
            speak("Have a nice day, Bye...")
            
            
            
    elif trans == "Withdraw Money":
        amount = int(input(speak("Enter the amount: ")))
        if (amount>=100):
            speak("........please wait, your Transaction is under process.......")
            time.sleep(2)
            speak("Collect your Cash")
            time.sleep(2)
            speak(".....Collect your Card.....")
            time.sleep(2)
            speak("Thankyou for using Global Bank Services ")
            speak("Have a nice day, Bye...")
            
        else:
            speak("Enter valid amount")
              
                
                
    elif trans == "Deposit Money" :
        amount = int(input(speak("Enter a amount to deposite:")))
        time.sleep(2)
        if (amount>0):
            speak("Your deposit have successfully deposited, Thankyou for using Global Bank Services")
            speak("Have a nice day, Bye...")
            
        else:
            speak("Enter valid amount")
        
        
        
    elif trans == "Change your pin" :
        change_pin= int(input(speak(" Enter your new pin: ")))
        if change_pin >=0:
            speak("Your pin is successfully changed...., Thankyou for using Global Bank Services")
            speak("Have a nice day, Bye...")
            
        else:
            speak(" Enter a valid pin to proceed ")
            
            
            
    elif trans == "Transfer Money" :
        amount = int(input(speak("Enter a amount to transfer:")))
        if (amount>0):
            speak("Your amount have successfully transfered, Thankyou for using Global Bank Services")
            speak("Have a Good day, Bye...")
            
        else:
            speak("Enter valid amount")
            
            
    elif trans == "Quit":
        quit_1=input(speak("press 'yes' to quit"))
        if quit_1 == "yes":
            speak("quit")
            speak("Collect your card")
            speak("Thankyou for using Global Bank Services ")
            speak("Have a Good day, Bye...")
            
        else:
            speak(" Choose any Transaction: ")
            
            
            
else:
    speak("Wrong pin entered.... Try Again")