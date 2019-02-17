import sys
from PyQt5.QtWidgets import *

# PyQt 소개
# app = QApplication(sys.argv)
# label = QLabel("Hello QyQt")
# # label = QPushButton("Quit")
# label.show()
# app.exec_()\

# 위젯과 윈도우
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Pystock")
#         self.setGeometry(300, 300, 300, 400)
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mywindow = MyWindow()
#     mywindow.show()
#     app.exec_()
#
# class Parent:
#     house = "yong-san"
#     def __init__(self):
#         self.money = 10000
#
# class Child1(Parent):
#     def __init__(self):
#         super().__init__()
#         pass
#
# class Child2(Parent):
#     def __init__(self):
#         pass
#
# child1 = Child1()
# child2 = Child2()
#
# print('Child1', dir(child1))
# print('Child2', dir(child2))

# self.setWindowTitle("PyStock")
# self.setGeometry(300, 300, 300, 400)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mywindow = MyWindow()
#     mywindow.show()
#     app.exec_()

# # 이벤트 처리
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")
#         self.setGeometry(300, 300, 300, 400)
#
#         btn1 = QPushButton("Click me", self)
#         #move(창에서 버튼까지의 가로 간격, 세로 간격)
#         btn1.move(40, 20)
#         btn1.clicked.connect(self.btn1_clicked)
#
#     def btn1_clicked(self):
#         QMessageBox.about(self, "message", "clicked")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

# # Open API+ 로그인하기
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QAxContainer import *
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyStock")
#         self.setGeometry(300, 300, 300, 150)
#
#         self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
#
#         btn1 = QPushButton("Login", self)
#         btn1.move(20, 20)
#         btn1.clicked.connect(self.btn1_clicked)
#
#         btn2 = QPushButton("Check state", self)
#         btn2.move(20, 70)
#         btn2.clicked.connect(self.btn2_clicked)
#
#     def btn1_clicked(self):
#         ret = self.kiwoom.dynamicCall("CommConnect()")
#
#     def btn2_clicked(self):
#         if self.kiwoom.dynamicCall("GetConnectState()") == 0:
#             self.statusBar().showMessage("Not connected")
#         else:
#             self.statusBar().showMessage("Connected")
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300,300,300,400)

        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10,60,280,80)
        self.text_edit.setEnabled(False)

        self.kiwoom.OnEventConnect.connect(self.event_connect)

    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공")


if __name__=="__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
