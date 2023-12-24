import pyautogui
import time
import cv2
import numpy as np

import os
from Towers import *

from Config import *

from Opened import run_background_opened_roblox_check, crash_script

#subprocess.call(["python", "Lobby.py"])

print("ertgherghergherfg")

#wait(2)

run_background_opened_roblox_check()

wait(2)

file = open('User config.txt', 'r')
# Read the contents of the file as a string
user_config_content = file.read()
# Close the file after reading
file.close()

def IsSeeingDifficultyVote():
    # Specify the path to your app icon or an image representing the app window
    app_icon_path_image = 'Tower Defense Simulator Dificulty Vote.png'

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
    print(np.max(result))

    if np.max(result) >= threshold:
        return True
    else:
        return False

while IsSeeingDifficultyVote() == False:
    print("Not seeing")
    #wait(2)
    print("Checking again")

print("Seeing difficulty Vote")


time.sleep(2)

# Load the image from the folder
#saved_image = cv2.imread(check_screen_resolution() + " " + 'Tower Defense Simulator Difficulty Vote Molten.png')

current_dir = os.path.dirname(__file__)

saved_image = cv2.imread(os.path.join(current_dir, 'images', check_screen_resolution() + " " + 'Tower Defense Simulator Difficulty Vote Molten.png'))

# Capture the screen
screen_image = pyautogui.screenshot()
screen_image = cv2.cvtColor(np.array(screen_image), cv2.COLOR_RGB2BGR)

# Calculate the center coordinates of the saved image
saved_image_height, saved_image_width = saved_image.shape[:2]
saved_image_center = (saved_image_width // 2, saved_image_height // 2)

# Find the template matching results
result = cv2.matchTemplate(screen_image, saved_image, cv2.TM_CCOEFF_NORMED)
y, x = np.unravel_index(result.argmax(), result.shape)
match_location = (x + saved_image_center[0], y + saved_image_center[1])

# Check if the image is found based on a similarity threshold
similarity_threshold = 0.8
if np.max(result) >= similarity_threshold:
    print("Image found at position:", match_location)
else:
    print("Image not found.")

import win32api
import win32con

# Specify the coordinates of the desired position to drag and click
def moving_mouse_and_clicking(aa, bb):
    x_position = aa
    y_position = bb

    # Obtain the current screen resolution
    screen_resolution = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

    # Calculate the absolute coordinates based on the screen resolution
    absolute_x = int(x_position * 65535 / screen_resolution[0])
    absolute_y = int(y_position * 65535 / screen_resolution[1])

    # Drag mouse to the specified position
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, absolute_x, absolute_y, 0, 0)

    # Wait for 1 second
    time.sleep(0.4)

    # Perform a left-click at the current position
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
moving_mouse_and_clicking(match_location[0], match_location[1])
moving_mouse_and_clicking(match_location[0] - 4, match_location[1] + 6)
moving_mouse_and_clicking(match_location[0] - 2, match_location[1] + 8)

print("Chose difficulty")

wait(4)

move_screen_up()

Zoom_out()

Tab_press()
wait(0.4)
Tab_unpress()

print("Starting putting towers")

Towers_set = user_config_content
print(Towers_set)

if Towers_set == "Scout or Soldier":
    print(Towers_set)
    
    for i in range(20):
        thetoweratplaced = Place_tower_1()
    print(thetoweratplaced)

    wait(40)

    for i in range(15):
        thetoweratplaced = Place_tower_1_with_upgrades()
    print(thetoweratplaced)

    wait(80)

    for i in range(15):
        thetoweratplaced = Place_tower_1_with_upgrades()
    print(thetoweratplaced)

    wait(120)

    for i in range(10):
        thetoweratplaced = Place_tower_1_with_upgrades()
    print(thetoweratplaced)

    wait(40)

    while Click_on_an_image("Tower Defense Simulator Return To Lobby.png") == False or Click_on_an_image("Tower Defense Simulator Return To Lobby 2.png") == False:
        thetoweratplaced = Place_tower_1_with_upgrades()
        wait(6)
    for i in range(10):
        Click_on_an_image("Tower Defense Simulator Return To Lobby.png")
        wait(0.2)
        Click_on_an_image("Tower Defense Simulator Return To Lobby 2.png")
        wait(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        wait(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
elif Towers_set == "Militant and Soldier or Militant and Scout or Militant and Military Base":
    print(Towers_set)

    for i in range(20):
        thetoweratplaced = Place_tower_2()
    print(thetoweratplaced)

    wait(40)

    for i in range(20):
        thetoweratplaced = Place_tower_2_with_upgrades()
    print(thetoweratplaced)

    wait(80)
    
    while Click_on_an_image("Tower Defense Simulator Return To Lobby.png") == False or Click_on_an_image("Tower Defense Simulator Return To Lobby 2.png") == False:
        thetoweratplaced = Place_tower_1_with_upgrades_custom_militant()
        wait(0.02)
    for i in range(10):
        Click_on_an_image("Tower Defense Simulator Return To Lobby.png")
        wait(0.2)
        Click_on_an_image("Tower Defense Simulator Return To Lobby 2.png")
        wait(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        wait(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        wait(0.2)

crash_script()