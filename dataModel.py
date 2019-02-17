class DataModel:
    def __init__(self):
        print("데이터 모델 입니다.")
        self.myLoginInfo = None
        self.itemList = []

    class Logininfo:
        def __init__(self, accCnt, accList, userId, userName, keyBSEC, firew, serverGubun):
            self.accCnt = accCnt
            self.accList = accList
            self.userId = userId
            self.userName = userName
            self.keyBSEC = keyBSEC
            self.firew = firew
            self.serverGubun = serverGubun


        def getServerGubun(self):
            if self.serverGubun == '1':
                return "모의투자"
            else:
                return "실서버"

    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName