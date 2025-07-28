from plyer import notification
import time
import pygame
def water():
    notification.notify(
        title="DRINK WATER!!!!",
        message="This is a desktop notification to remind you to drink water",
        app_name="My App",
        timeout=1  # Notification duration in seconds
       
    )

def sound():
    pygame.mixer.init()
    sound_file = pygame.mixer.Sound('mixkit-liquid-bubble-3000.wav')
    sound_file.play()
    


while True:
    time.sleep(600)# sleeps for 10 mintutes after a notification
    water()
    time.sleep(1)# to stop the overlapping of notification sound with windows
    sound()
    
    # this program will generate drink water notification after every 10 minutes