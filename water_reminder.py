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
    sound_file = pygame.mixer.Sound('drink_water1.mp3')
    sound_file.play()
    


while True:
   
    water()
    time.sleep(1)# to stop the overlapping of notification sound with windows
    sound()
    time.sleep(600)# sleeps for 10 mintutes after a notification
    
    # this program will generate drink water notification after every 10 minutes