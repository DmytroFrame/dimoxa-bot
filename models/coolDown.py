import time
from models.cashTool import CashTool


def coolDown(user, timePause: int=5) -> bool:
    userStatus = CashTool.getStatus(str(user))
    if userStatus is None:
        print(1)
        CashTool.setStatus(str(user), int(time.time()))
        return False

    else:
        if (int(time.time()) - userStatus) < timePause: #300 this 5 minutes in sec
            return True

        else:
            CashTool.setStatus(str(user), int(time.time()))
            return False

        