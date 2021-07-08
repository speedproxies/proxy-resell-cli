import http.client
import mimetypes
import sys
import time
import math
import random
import os
import requests
import simplejson
import keyboard
import colorama
from colorama import Fore, Back, Style

API_KEY = str("KEY")

colorama.init(autoreset=True)
def askUser():
    print(Fore.CYAN + Style.BRIGHT + '''

 .d8888b.                                  888 8888888b.                           d8b
d88P  Y88b                                 888 888   Y88b                          Y8P
Y88b.                                      888 888    888
 "Y888b.   88888b.   .d88b.   .d88b.   .d88888 888   d88P 888d888 .d88b.  888  888 888  .d88b.  .d8888b
    "Y88b. 888 "88b d8P  Y8b d8P  Y8b d88" 888 8888888P"  888P"  d88""88b `Y8bd8P' 888 d8P  Y8b 88K
      "888 888  888 88888888 88888888 888  888 888        888    888  888   X88K   888 88888888 "Y8888b.
Y88b  d88P 888 d88P Y8b.     Y8b.     Y88b 888 888        888    Y88..88P .d8""8b. 888 Y8b.          X88
 "Y8888P"  88888P"   "Y8888   "Y8888   "Y88888 888        888     "Y88P"  888  888 888  "Y8888   88888P'
           888
           888
           888

''')

    url = "http://dash.speedproxies.net/"
    page = requests.get(url)
    pageStatus = page.status_code
    if pageStatus == 200:
            sys.stdout.write(Fore.WHITE + Style.BRIGHT + '\rAPI Status:' + Fore.GREEN + ' Online\n')
    else:
        print(Fore.RED + "API HTTP Error Status: " + str(pageStatus))

    print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "1" + Fore.WHITE + Style.BRIGHT + "] Create new user")
    print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "2" + Fore.WHITE + Style.BRIGHT + "] Add banwidth to user")
    print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "3" + Fore.WHITE + Style.BRIGHT + "] Check user balance")
    print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "4" + Fore.WHITE + Style.BRIGHT + "] Delete banwidth from user")
    print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "5" + Fore.WHITE + Style.BRIGHT + "] Proxy Gen")
    print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "6" + Fore.WHITE + Style.BRIGHT + "] Quit\n")
    taskAsk = input(Fore.WHITE + Style.BRIGHT)


    if taskAsk == "1":
        clear()
        print(Fore.WHITE + Style.BRIGHT + "\n[Create user]")
        userInput = input(Fore.WHITE + Style.BRIGHT + "Username: ").lower()
        if userInput!= "":
            taskCreate(userCreate=userInput)


    elif taskAsk == "2":
        clear()
        print(Fore.WHITE + Style.BRIGHT + "\n[Add bandwidth to user]")
        userInput = (input(Fore.WHITE + Style.BRIGHT + "Username: ")).lower()
        bandInput = float(input(Fore.WHITE + Style.BRIGHT + "Bandwidth (GB): "))
        if userInput!= "" and bandInput!= "":
            taskAddBand(userInput=userInput, bandInput=bandInput)


    elif taskAsk == "3":
        clear()
        print(Fore.WHITE + Style.BRIGHT + "\n[Check bandwidth of user]")
        userInput = input(Fore.WHITE + Style.BRIGHT + "Username: ").lower()
        if userInput!= "":
            taskCheckBal(userInput=userInput)


    elif taskAsk == "4":
        clear()
        print(Fore.WHITE + Style.BRIGHT + "\n[Delete bandwidth from user]")
        userInput = (input(Fore.WHITE + Style.BRIGHT + "Username: ")).lower()
        bandInput = float(input(Fore.WHITE + Style.BRIGHT + "Bandwidth (GB): "))
        if userInput!= "" and bandInput!= "":
            taskDeleteBand(userInput=userInput, bandInput=bandInput)

    elif taskAsk == "5":
        clear()
        userInput = input(Fore.WHITE + Style.BRIGHT + "Username: ").lower()

        ssl = "http"
        hostname = "dns"
        country = (input(Fore.WHITE + Style.BRIGHT + "Country: ")).capitalize()
        sticky = (input(Fore.WHITE + Style.BRIGHT + "Sticky/Randomize: ")).lower()
        quantity = input(Fore.WHITE + Style.BRIGHT + "List Size [10/100/1000]: ")
        print(Fore.WHITE + Style.BRIGHT + "Format:")
        print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "1" + Fore.WHITE + Style.BRIGHT + "] username:password:hostname:port")
        print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "2" + Fore.WHITE + Style.BRIGHT + "] hostname:port:username:password")
        print(Fore.WHITE + Style.BRIGHT + "[" + Fore.CYAN + Style.BRIGHT + "3" + Fore.WHITE + Style.BRIGHT + "] hostname:port@username:password")
        format_input = int(input(Fore.WHITE + Style.BRIGHT))

        if format_input == 1:
            format = "username:password:hostname:port"
        elif format_input == 2:
            format = "hostname:port:username:password"
        elif format_input == 3:
            format = "hostname:port@username:password"
        else:
            format = "username:password:hostname:port"

        taskGen(userInput=userInput, country=country, hostname=hostname, ssl=ssl, sticky=sticky, format=format, quantity=quantity)

    elif taskAsk == "5":
        print(Fore.WHITE + Style.BRIGHT + "Quiting")

    else:
        print(Fore.WHITE + Style.BRIGHT + "Task non existent")

def taskCreate(userCreate):
    clear()
    print(Fore.WHITE + Style.BRIGHT + "\n[Create user]")
    print(Fore.WHITE + Style.BRIGHT + "Username: " +userCreate)

    url = "https://dash.speedproxies.net/api/standard-resi/create-user"

    payload = '{"username":"' + str(userCreate) + '"}'
    headers = {
      'Authorization': API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    createdUser = jsonResponse["data"]["username"]
    createdPassword = jsonResponse["data"]["proxy_authkey"]

    print(Fore.WHITE + Style.BRIGHT + "Proxy Username: " + str(createdUser))
    print(Fore.WHITE + Style.BRIGHT + "Proxy Username: " + str(createdPassword))

    main_screen = str(input(Fore.WHITE + Style.BRIGHT + "\nFinished (yes)? \n")).lower()

    if main_screen == "yes":
        os.system('cls')
        askUser()

def taskAddBand(userInput, bandInput):
    clear()
    print(Fore.WHITE + Style.BRIGHT + "\n[Add bandwidth to user]")
    print(Fore.WHITE + Style.BRIGHT + "Username: " + userInput)
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth (GB): " + str(bandInput))

    addBand = float(bandInput * 100)

    url = "https://dash.speedproxies.net/api/standard-resi/give-balance"

    payload = '{"username":"' + str(userInput) + '","bandwidth":"' + str(addBand) + '"}'
    headers = {
      'Authorization': API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    bandBalance = jsonResponse["data"]["balance"]
    calcBand = float(bandBalance / 100)
    userDB = jsonResponse["data"]["username"]

    print(Fore.WHITE + Style.BRIGHT + "Proxy Username: " + str(userDB))
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth Added: " + str(bandInput) + "GB")
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth Remaining: " + str(calcBand) + "GB \n")

    main_screen = str(input(Fore.WHITE + Style.BRIGHT + "\nFinished (yes)? \n")).lower()

    if main_screen == "yes":
        os.system('cls')
        askUser()

def taskDeleteBand(userInput, bandInput):
    clear()
    print(Fore.WHITE + Style.BRIGHT + "\n[Delete bandwidth from user]")
    print(Fore.WHITE + Style.BRIGHT + "Username: " +userInput)
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth (GB): " + str(bandInput))

    addBand = (bandInput * 100)

    url = "https://dash.speedproxies.net/api/standard-resi/remove-balance"

    payload = '{"username":"' + str(userInput) + '","bandwidth":"' + str(addBand) + '"}'
    headers = {
      'Authorization': API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    bandBalance = jsonResponse["data"]["balance"]
    calcBand = float(bandBalance / 100)
    userDB = jsonResponse["data"]["username"]

    print(Fore.WHITE + Style.BRIGHT + "Proxy Username: " + str(userDB))
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth Removed: " + str(bandInput) + "GB")
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth Remaining: " + str(calcBand) + "GB \n")

    main_screen = str(input(Fore.WHITE + Style.BRIGHT + "\nFinished (yes)? \n")).lower()

    if main_screen == "yes":
        os.system('cls')
        askUser()

def taskCheckBal(userInput):
    clear()
    print(Fore.WHITE + Style.BRIGHT + "\n[Check bandwidth of user]")
    print(Fore.WHITE + Style.BRIGHT + "Username: " +userInput)

    url = "https://dash.speedproxies.net/api/standard-resi/user-info"
    payload = '{"username":"' + str(userInput) + '"}'
    headers = {
      'Authorization': API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    bandBalance = jsonResponse["data"]["balance"]
    calcBand = float(bandBalance / 100)
    userDB = jsonResponse["data"]["username"]

    print(Fore.WHITE + Style.BRIGHT + "Proxy Username: " + str(userDB))
    print(Fore.WHITE + Style.BRIGHT + "Bandwidth Remaining: " + str(calcBand) + "GB \n")

    main_screen = str(input(Fore.WHITE + Style.BRIGHT + "\nFinished (yes)? \n")).lower()

    if main_screen == "yes":
        os.system('cls')
        askUser()

def taskGen(userInput, country, hostname, ssl, sticky, format, quantity):
    clear()
    print(Fore.WHITE + Style.BRIGHT + "\n[Generate Proxy List]")
    print(Fore.WHITE + Style.BRIGHT + "Username: " +userInput)
    print(Fore.WHITE + Style.BRIGHT + "Country: " +country)
    print(Fore.WHITE + Style.BRIGHT + "Mode: " +sticky)
    print(Fore.WHITE + Style.BRIGHT + "Format: " +format)
    print(Fore.WHITE + Style.BRIGHT + "Quantity: " +quantity)

    url = "https://dash.speedproxies.net/api/standard-resi/view-proxylist"

    payload = '{"username":"' + str(userInput) + '","country":"' + str(country) + '","hostname":"' + str(hostname) + '","ssl":"' + str(ssl) + '","sticky":"' + str(sticky) + '","format":"' + str(format) + '","quantity":"' + str(quantity) + '"}'
    headers = {
      'Authorization': API_KEY,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    proxylist = jsonResponse["data"]["formatted_proxy_list"]

    print("\n")
    for x in proxylist:
        print(Fore.WHITE + Style.BRIGHT + x)

    main_screen = str(input(Fore.WHITE + Style.BRIGHT + "\nFinished (yes)? \n")).lower()

    if main_screen == "yes":
        os.system('cls')
        askUser()

def clear():
    os.system( 'cls' )

askUser()
