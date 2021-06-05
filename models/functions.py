import random, json


def passwordGen(amount=8):
    charsPass = "qwertyuiopasdfghjklzxcvbnm"
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



def setStatus(id, status):
    array = readJsonFile("progresUsers.json")
    array.update({str(id): status})
    writeJsonFile("progresUsers.json", array)


def getStatus(id):
    try:
        array = readJsonFile("progresUsers.json")
        return array[str(id)]
    except:
        return None

def delStatus(id):
    array = readJsonFile("progresUsers.json")
    del array[str(id)]
    writeJsonFile("progresUsers.json", array)


def readJsonFile(fileName):
    with open(fileName, "r") as file:
        data = json.load(file)
        file.close()
        return data


def writeJsonFile(fileName, data):
    with open(fileName, "w") as file:
        json.dump(data, file)
        file.close()


# print(getSettings("rconData"))