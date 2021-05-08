from microbit import *

uart.init(9600,tx=pin1, rx=pin2)

def robot_turn_left():
    uart.write(b'R 7')
def robot_turn_right():
    uart.write(b'R 9')
def robot_sleep():
    uart.write(b'R g')
def robot_stand():
    uart.write(b'R 5')
def robot_sit():
    uart.write(b'R a')
def robot_pushup():
    uart.write(b'R f')
def robot_move_forward():
    uart.write(b'R 8')
def robot_move_left():
    uart.write(b'R 4')
def robot_move_right():
    uart.write(b'R 6')
def robot_move_backward():
    uart.write(b'R 2')
def robot_hi():
    uart.write(b'R s')
def robot_fight():
    uart.write(b'R d')
def robot_dance1():
    uart.write(b'R z')
def robot_dance2():
    uart.write(b'R x')
def robot_dance3():
    uart.write(b'R c')