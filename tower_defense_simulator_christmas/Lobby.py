import pyautogui
import cv2
import numpy as np

from Config import *

from Opened import run_background_opened_roblox_check, crash_script

run_background_opened_roblox_check()

print("Starting lobby script")

wait(2)

def IsInCage():
    # Specify the path to your app icon or an image representing the app window
    app_icon_path_image = 'Tower Defense Simulator Cross.png'

    current_dir = os.path.dirname(__file__)

    app_icon_path = os.path.join(current_dir, 'images', check_screen_resolution() + " " + app_icon_path_image)

    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Capture the screen
    screen = np.array(pyautogui.screenshot())
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    app_icon = cv2.imread(app_icon_path, 0)  # Load the app icon as a gray-scale image
    result = cv2.matchTemplate(screen_gray, app_icon, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Set a threshold to determine if the app window is found

    if np.max(result) >= threshold:
        return True
    else:
        return False
    


#Turn_left(0.8)
#Turn_right(0.2)
#Move_forward(False, 0.2)

Reset_character()

wait(7)

def GetInCage():
    Turn_right(0.74)
    wait(0.2)

    Move_forward(True, 3.95)
    Turn_left(0.78)
    Move_forward(True, 0.8)
    Turn_right(1.56)
    Move_forward(True, 0.8)
    wait(1.2)
    print(IsInCage())

while IsInCage() == False:
    GetInCage()
    if IsInCage() == False:
        Reset_character()
        wait(6)
    is_in_cage = IsInCage()
    print("Is In Cage: " + str(is_in_cage))
print("The player is in cage")
while IsInCage() == True:
    print("Waiting for the timer to go off")
    wait(4)
print("The timer has gone off")

crash_script()