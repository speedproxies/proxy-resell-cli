import sys
import math
import os
import requests

logo = ('''

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
API_KEY = str('KEY')

def askUser():
    print(logo)
    url = "http://dash.speedproxies.net"
    page = requests.get(url)
    pageStatus = page.status_code
    if pageStatus == 200:
        apiCheck = "SUCCESS"
    else:
        apiCheck = "FAIL"
    print("\rAPI Check: " + apiCheck)
    print("STATUS CODE: " + str(pageStatus) + "\n")

    print("\n1 - Create new user")
    print("2 - Add bandwidth to user")
    print("3 - Remove bandwidth to user")
    print("4 - Check user bandwidth")
    print("5 - Check reseller balance")
    print("0 - Quit\n")
    taskAsk = input()

    if taskAsk == "1":
        os.system("cls")
        print(logo)
        print("\nCREATE NEW USER\n")
        userInput = input("USERNAME: ").lower()
        if userInput!= "":
            taskCreate(userCreate=userInput)

    elif taskAsk == "2":
        os.system("cls")
        print(logo)
        print("\nADD USER BANDWIDTH\n")
        userInput = input("USERNAME: ").lower()
        bandInput = float(input("BANDWIDTH (GB): "))
        if userInput!= "" and bandInput!= "":
            taskAddBand(userInput=userInput, bandInput=bandInput)

    elif taskAsk == "3":
        os.system("cls")
        print(logo)
        print("\nREMOVE USER BANDWIDTH\n")
        userInput = input("USERNAME: ").lower()
        bandInput = float(input("BANDWIDTH (GB): "))
        if userInput!= "" and bandInput!= "":
            taskDeleteBand(userInput=userInput, bandInput=bandInput)

    elif taskAsk == "4":
        os.system("cls")
        print(logo)
        print("\nCHECK USER BANDWIDTH\n")
        userInput = input("USERNAME: ").lower()
        if userInput!= "":
            taskCheckBal(userInput=userInput)

    elif taskAsk == "5":
        os.system('cls')
        print(logo)
        print("\nCHECK RESELL BALANCE\n")
        taskCheckResellBal(apiKey=API_KEY)

    elif taskAsk == "0":
        os.system("cls")
        print(logo)
        print("Quitting")
        sys.exit()

    else:
        os.system("cls")
        print(logo)
        print("Unknown option.")

def taskCreate(userCreate):
    os.system("cls")
    print(logo)
    print("\nCREATE NEW USER\n")
    url = "https://dash.speedproxies.net/api/standard-resi/create-user"
    payload = '{"username":"' + userCreate + '"}'
    headers = {
      'Authorization': API_KEY
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    createdUser = jsonResponse["data"]["username"]
    createdPassword = jsonResponse["data"]["proxy_authkey"]
    print("PROXY USERNAME: " + str(createdUser))
    print("PROXY PASSWORD: " + str(createdPassword))
    main_screen = str(input("Finished? \n")).lower()
    if main_screen == "yes":
        os.system("cls")
        askUser()

def taskAddBand(userInput, bandInput):
    os.system("cls")
    print(logo)
    print("\nADD USER BANDWIDTH\n")
    calcBand = float(bandInput * 100)
    url = "https://dash.speedproxies.net/api/standard-resi/give-balance"
    payload = '{"username":"' + str(userInput) + '","bandwidth":"' + str(calcBand) + '"}'
    headers = {
      'Authorization': API_KEY
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    bandBalance = jsonResponse["data"]["balance"]
    calcBand = float(bandBalance / 100)
    userDB = jsonResponse["data"]["username"]
    print("PROXY USERNAME: " + str(userDB))
    print("BANDWIDTH ADDED: " + str(bandInput) + "GB")
    print("BANDWIDTH REMAINING: " + str(calcBand) + "GB \n")
    main_screen = str(input("Finished? \n")).lower()
    if main_screen == "yes":
        os.system("cls")
        askUser()

def taskDeleteBand(userInput, bandInput):
    os.system("cls")
    print(logo)
    print("\nREMOVE USER BANDWIDTH\n")
    calcBand = float(bandInput * 100)
    url = "https://dash.speedproxies.net/api/standard-resi/remove-balance"
    payload = '{"username":"' + str(userInput) + '","bandwidth":"' + str(calcBand) + '"}'
    headers = {
      'Authorization': API_KEY
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    bandBalance = jsonResponse["data"]["balance"]
    calcBand = float(bandBalance / 100)
    userDB = jsonResponse["data"]["username"]
    print("PROXY USERNAME: " + str(userDB))
    print("BANDWIDTH REMOVED: " + str(bandInput) + "GB")
    print("BANDWIDTH REMAINING: " + str(calcBand) + "GB \n")
    main_screen = str(input("Finished? \n")).lower()
    if main_screen == "yes":
        os.system("cls")
        askUser()

def taskCheckResellBal(apiKey):
    os.system("cls")
    print(logo)
    print("\nCHECK RESELLER BALANCE\n")
    url = "https://dash.speedproxies.net/api/standard-resi/reseller-info"
    headers = {
      'Authorization': API_KEY
    }
    response = requests.request("GET", url, headers=headers)
    jsonResponse = response.json()

    print("$" + jsonResponse)
    main_screen = str(input("Finished? \n")).lower()
    if main_screen == "yes":
        os.system("cls")
        askUser()

def taskCheckBal(userInput):
    os.system('cls')
    print(logo)
    print("\nCHECK RESELL BALANCE\n")
    url = "https://dash.speedproxies.net/api/standard-resi/user-info"
    payload = '{"username":"' + str(userInput) + '"}'
    headers = {
      'Authorization': API_KEY
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    jsonResponse = response.json()

    bandBalance = jsonResponse["data"]["balance"]
    calcBand = float(bandBalance / 100)
    userDB = jsonResponse["data"]["username"]
    print("PROXY USERNAME: " + str(userDB))
    print("BANDWIDTH REMAINING: " + str(calcBand) + "GB \n")
    main_screen = str(input("Finished? \n")).lower()
    if main_screen == "yes":
        os.system("cls")
        askUser()

askUser()
