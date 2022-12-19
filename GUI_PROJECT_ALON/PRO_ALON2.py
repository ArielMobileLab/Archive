from concurrent.futures import thread
import tkinter
import sys
import os
import keyboard
import threading 
import time

#-----------------Class---------------------------------

def click_roscore():
    print("here\n")
    os.system("roscore")



def click_start():
    print("here\n")
    os.system("ffset /dev/input/by-id/usb-Logitech_G920_Driving_Force_Racing_Wheel_for_Xbox_One_0000b2eff7d6c59f-event-joystick -a 50 & terminator --geometry=340x130-2700+1000 -T speed -p speed")

def fun(str_a):
    if (str_a=='latency0'):
      os.system('wmctrl -r speed -b add,above ; roslaunch cognata_sdk latency0.launch')
    if (str_a=='latency1'):
      os.system('wmctrl -r speed -b add,above ; roslaunch cognata_sdk latency1.launch')
    if (str_a=='latency2'):
      os.system('wmctrl -r speed -b add,above ; roslaunch cognata_sdk latency2.launch')
    

def secnario(*args):
    str = clicked.get()
    y= threading.Thread(target=fun, args=[str])
    y.start()
#-----------------GENERAL---------------------------------
window = tkinter.Tk()
window.title("TELE")
window.geometry('400x400')
label = tkinter.Label(window, text = "Hello").pack()
x = threading.Thread(target=click_roscore)


#-----------------BUTTONS---------------------------------
button =  tkinter.Button(
    text="Roscore",
    command= x.start,
    width=25,
    height=5,
    bg="black",
    fg="yellow",
)

button2 =  tkinter.Button(
    text="Start",
    command= click_start,
    width=25,
    height=5,
    bg="black",
    fg="yellow",
)

button.pack()
button2.pack()

#-----------------kill---------------------------------
def click_kill():
    x.st
    quit()

button3 =  tkinter.Button(
    text="Kill",
    command= click_kill,
    width=25,
    height=5,
    bg="red",
    fg="white",
)

button3.pack()

#-----------------option_menu---------------------------------

options = ['latency0','latency1', 'latency2']

def change(*args):
    print("changing condition...")
    print(options)


clicked = tkinter.StringVar(window)
clicked.set(options[0])
clicked.trace("w",secnario)



drop= tkinter.OptionMenu(window, clicked, *options)
drop.pack()



#-----------------Camera---------------------------------
def start_camera_1():
    os.system("cd /opt/driveu/node")
    os.system("./run_node")
    os.system("omer")

button2 =  tkinter.Button(
    text="TELE Camera",
    command= start_camera_1,
    width=25,
    height=5,
    bg="black",
    fg="white",
)

button2.pack()

#-----------------run---------------------------------
window.mainloop()
