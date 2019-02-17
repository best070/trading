from pywinauto import application
from pywinauto import timings
from pywinauto import findwindows

import time
import os

from trading_config import config

password = config["securities"]["kiwoom"]["password"]
certificate = config["securities"]["kiwoom"]["certificate"]

app = application.Application()
app.start("C:/KiwoomFlash3/bin/nkministarter.exe")
title = "번개3 Login"
dig = timings.wait_until_passes(20, 0.5, lambda: app.window(title=title))
pass_ctrl = dig.Edit2
pass_ctrl.set_focus()
pass_ctrl.type_keys(password)

cert_ctrl = dig.Edit3
cert_ctrl.set_focus()
cert_ctrl.type_keys(certificate)

btn_ctrl = dig.button0
btn_ctrl.click()
# w_open_handle = findwindows.find_window(title=title, class_name=u'Edit2')[0]

time.sleep(50)
os.system("taskkill /im nkmini.exe")

# pass_ctrl = findwindows.find_element(class_name="Edit", control_id=1002).SetFocus()
# print(pass_ctrl)
# pass_ctrl = dig.Edit2
# pass_ctrl.SetFocus()
# pass_ctrl.TypeKeys(password)
#
# cert_ctrl = dig.Edit3
# cert_ctrl.SetFocus()
# cert_ctrl.TypeKeys(certificate)
#
# btn_ctrl = dig.Button0
# btn_ctrl.Click()
