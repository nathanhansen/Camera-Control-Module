#Author Nathan Hansen
#nathanhansen2010@gmail.com
#NathanHansenLAX on Twitter

#Creates a manual brightness and contrast circuit for the PiCamera to take
#time-lapse photos

from picamera import PiCamera
from gpiozero import MCP3008, Button
from time import sleep
from datetime import datetime

pot1 = MCP3008(channel=0) #reads the potentiometer from channel 0 on the MCP
pot2 = MCP3008(channel=1) #reads potentiometer to channel 1 on the MCP
button = Button(17) #lets the program know that the button is connected to GPIO 17
camera = PiCamera() #create a connection to the PiCamera

def capture():
    for i in range(timer):
        timestamp = datetime.now().isoformat()
        camera.capture('/home/pi/%s.jpg' % timestamp)
        sleep(delay)

camera.start_preview(fullscreen=False, window = (0, 0, 1280, 720))

try:
    timer=int(input("How many photos should the time-lapse capture?"))
    delay=int(input("How many seconds between shots?"))

    while True:
        brightness = round(pot1.value * 100)
        print("Brightness",brightness)
        contrast = round(pot2.value * 200)
        print("Contrast",contrast)
        camera.brightness=brightness
        camera.contrast=contrast
        settings="Brightness: "+str(brightness)+"Contrast: "+str(contrast)
        print(settings)
        camera.annotate_text=settings
        sleep(0.1)
        button.when_held=capture

except KeyboardInterrupt:
    camera.stop_preview()

finally:
    print("TIMELAPSE EXITING")
    
