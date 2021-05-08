from microbit import *
#from light import *
#from mb import command,slot,gc

#while True:
#    display.show(Image.HAPPY)
#    sleep(1000)
#    display.show(Image.DUCK)
#    sleep(1000)
#    display.show(Image.GHOST)
#    sleep(1000)

uart.init(9600,tx=pin1, rx=pin2)

while True:
    if button_a.is_pressed():
        uart.write(b'R 5')
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        uart.write(b'R 6')
        display.show(Image.DUCK)
    sleep(200)
    
    
    
