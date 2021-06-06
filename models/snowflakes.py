import time


def checkBotTime(id):
    idBinary = bin(id)
    twoBinary = str(idBinary)[2:-22]
    decimal = 0 
    for digit in twoBinary: 
        decimal = decimal*2 + int(digit) 

    unixTimeMs = decimal + 1420070400000
    timestamp = (unixTimeMs/1000) 

    if time.time() - timestamp > 7200:
        return True

    elif time.time() - timestamp < 7200:
        return False
