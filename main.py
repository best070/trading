import sys
import viewController as vc
import dataModel as dm

# pyqt
from PyQt5.QtWidgets import *



class MyAutoTradeApp():
    def __init__(self):
        print("자동매매 프로그램 클래스 입니다.")
        self.myDataModel = dm.DataModel()
        self.myViewController = vc.ViewController(self.myDataModel)

if __name__ == '__main__':
    print("메인이 실행되었습니다.")
    app = QApplication(sys.argv)
    myApp = MyAutoTradeApp()
    myApp.myViewController.show()
    app.exec_()