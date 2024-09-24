from picozero import LED, DistanceSensor
from time import sleep
import sys

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
        

# running = True

# try:
#     while running:
#         go()
        
#         sleep(5)

#         stop()

#         sleep(5)
# except KeyboardInterrupt:
#     print("SHUTTING DOWN")
#     red.off()
#     yellow.off()
#     green.off()


ds = DistanceSensor(echo=17, trigger=16)

def check_distance(threshold_cm: int = 10):
    distance_meters = ds.distance  # Get distance in cm
    distance_cm = distance_meters * 100
    # print(f"Distance: {distance_cm} cm")

    if distance_cm <= threshold_cm:
        return True
    return False

hit_count = 0

stop()

stopped = True

while stopped:
    distance_check= check_distance()
    print(hit_count)

    if not distance_check:
        hit_count = 0
    else:
        hit_count += 1
        if hit_count > 5:
            print("condition met exiting")
            go()
            sleep(5)
            stop()

    sleep(1)
    
