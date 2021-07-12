#import keyboard, threading
import keyboard 
from pynput.mouse import Controller 
from time import sleep
import threading

def blockinput_start():
        mouse = Controller()
        # global block_input_flag
        for i in range(150):
            keyboard.block_key(i)
        while block_input_flag == 1:
            mouse.position = (0, 0) #lock mouse position 
    
def block_input_stop():
        # global block_input_flag
        block_input_flag = 0 # changed position
        # means mouse cursor sahi ho jayega 
        for i in range(150):
            keyboard.unblock_key(i)

def blockinput():
    global block_input_flag #first  time declaration 
    block_input_flag = 1   
    # init
    t1 = threading.Thread(target=blockinput_start())
    t1.start()
    print("[SUCCESS] Input blocked!")
    # todo : use colorma to print on big screen
    

def unblockinput():
    block_input_stop()
    print("[SUCCESS] Input unblocked!")
    # todo : use colorma to print on big screen

    

    


blockinput()
print("now blocking")
sleep(5)
print("now unblocking")
unblockinput()
