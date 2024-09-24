from picozero import LED
from time import sleep

red = LED(0)
yellow = LED(1)
green = LED(2)

def stop():
    print("starting sequence")
    yellow.on()
    green.off()
    sleep(2)
    red.on()
    yellow.off()
        
        
def go():
    yellow.on()
    sleep(1)
    red.off()
    yellow.off()
    green.on()
        

running = True

try:
    while running:
        go()
        
        sleep(5)

        stop()

        sleep(5)
except KeyboardInterrupt:
    print("SHUTTING DOWN")
    red.off()
    yellow.off()
    green.off()

    
