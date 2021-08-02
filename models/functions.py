import json
import random
from pymongo import MongoClient


def passwordGen(amount=8):
    charsPass = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    password = ""
    while amount > 0:
        password += random.choice(charsPass)
        amount -= 1

    return password


def getSettings(name):
    with open("settings.json", "r") as file:
        array = json.load(file)
        file.close()
    return array[name]
    

def readJsonFile(fileName):
    with open(fileName, "r") as file:
        data = json.load(file)
        file.close()
        return data


def writeJsonFile(fileName, data):
    with open(fileName, "w") as file:
        json.dump(data, file)
        file.close()


def cursor_database(collection=None):
    clientDB = MongoClient(getSettings("mongoData")["url"])
    if collection == None:
        return clientDB[getSettings("mongoData")["database"]]
    else:
        db = clientDB[getSettings("mongoData")["database"]]
        return db[collection]


def check_validation(userString):
    if len(userString) < 3 or len(userString) > 22:
        return False

    validChars = "_-qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
    customString = ""
    for user in userString:
        for valid in validChars:
            if user == valid:
                customString += valid
                break

    return userString == customString


def check_validation_password(password):
    if len(password) < 8 or len(password) > 32:
        return False

    validChars = "_-qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM@#$%!"
    customString = ""
    for user in password:
        for valid in validChars:
            if user == valid:
                customString += valid
                break

    return password == customString
