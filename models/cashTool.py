import models.functions as func

class CashTool():
    def setStatus(id: str, status: str) -> None:
        array = func.readJsonFile("cash.json")
        array.update({str(id): status})
        func.writeJsonFile("cash.json", array)


    def getStatus(id: str) -> str:
        try:
            array = func.readJsonFile("cash.json")
            return array[str(id)]
        except:
            return None


    def delStatus(id: str) -> None:
        array = func.readJsonFile("cash.json")
        del array[str(id)]
        func.writeJsonFile("cash.json", array)