import models.functions as func


def setStatus(id, status):
    array = func.readJsonFile("cash.json")
    array.update({str(id): status})
    func.writeJsonFile("cash.json", array)


def getStatus(id):
    try:
        array = func.readJsonFile("cash.json")
        return array[str(id)]
    except:
        return None


def delStatus(id):
    array = func.readJsonFile("cash.json")
    del array[str(id)]
    func.writeJsonFile("cash.json", array)