import time 
import mouse
import keyboard
import sys

switch_bool = False
main_loop = True

def switch():
    global switch_bool
    if switch_bool:
        switch_bool = False
        print("switched off")
    else:
        switch_bool = True
        print("switched on")

def click_exit():
    global main_loop
    print("successful exit")
    main_loop = False
    sys.exit()
    
keyboard.add_hotkey("alt+s", switch)
keyboard.add_hotkey("alt+d", click_exit)

print("alt+s to start programm")
print("alt+d to close programm")

while main_loop:
    if switch_bool:
        time.sleep(0.001)
        mouse.double_click()