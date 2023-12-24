import time
from pynput.keyboard import Key, Controller
import win32api
import win32con
import pyautogui
import random
import cv2
import numpy as np
import os

def wait(value):
    time.sleep(value)

from screeninfo import get_monitors

def check_screen_resolution():
    # Get all available monitors
    monitors = get_monitors()
    
    if len(monitors) > 0:
        # Get the first monitor's width and height
        width, height = monitors[0].width, monitors[0].height
        
        # Check if it matches the desired resolution
        return str(width) + "x" + str(height)
    else:
        return "No monitors found"

def Left_arrow_unpress():

    keyboard = Controller()

    keyboard.release(Key.left)

def Left_arrow_press():

    keyboard = Controller()

    keyboard.press(Key.left)

def Right_arrow_unpress():

    keyboard = Controller()

    keyboard.release(Key.right)

def Right_arrow_press():

    keyboard = Controller()

    keyboard.press(Key.right)

def Forward_arrow_unpress():

    keyboard = Controller()

    keyboard.release(Key.up)

def Forward_arrow_press():

    keyboard = Controller()

    keyboard.press(Key.up)

def Shift_unpress():

    keyboard = Controller()

    keyboard.release(Key.shift)

def Shift_press():

    keyboard = Controller()

    keyboard.press(Key.shift)

def r_unpress():

    keyboard = Controller()

    keyboard.release('r')

def r_press():

    keyboard = Controller()

    keyboard.press('r')

def Escape_unpress():

    keyboard = Controller()

    keyboard.release(Key.esc)

def Escape_press():

    keyboard = Controller()

    keyboard.press(Key.esc)

def Enter_unpress():

    keyboard = Controller()

    keyboard.release(Key.enter)

def Enter_press():

    keyboard = Controller()

    keyboard.press(Key.enter)

def Tab_unpress():

    keyboard = Controller()

    keyboard.release(Key.tab)

def Tab_press():
    
    keyboard = Controller()

    keyboard.press(Key.tab)

def number_1_unpress():

    keyboard = Controller()

    keyboard.release('1')

def number_1_press():
    
    keyboard = Controller()

    keyboard.press('1')

def number_2_unpress():

    keyboard = Controller()

    keyboard.release('2')

def number_2_press():
    
    keyboard = Controller()

    keyboard.press('2')

def q_unpress():

    keyboard = Controller()

    keyboard.release("q")

def q_press():
    
    keyboard = Controller()

    keyboard.press("q")

def e_unpress():

    keyboard = Controller()

    keyboard.release("e")

def e_press():
    
    keyboard = Controller()

    keyboard.press("e")

def Reset_character():

    Escape_press()
    wait(0.4)
    r_press()
    wait(0.4)
    Enter_press()
    wait(0.4)
    Escape_unpress()
    r_unpress()
    Enter_unpress()

def Turn_left(seconds):
    Left_arrow_press()
    wait(seconds)
    Left_arrow_unpress()

def Turn_right(seconds):
    Right_arrow_press()
    wait(seconds)
    Right_arrow_unpress()

def Move_forward(holdshift, seconds):
    if holdshift:
        Shift_press()
    Forward_arrow_press()
    wait(seconds)
    Forward_arrow_unpress()
    if holdshift:
        Shift_unpress()

####################################################################################
#MOVE MOUSE UP

screen_width, screen_height = pyautogui.size()

# Get the current position of the mouse
x, y = screen_width / 2, screen_height / 2

# Specify the coordinates of the desired position to drag and click
def move_mouse_to_the_position(aa, bb):

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

def move_screen_up():
    move_mouse_to_the_position(x, y)
    pyautogui.mouseDown(button='right')
    move_mouse_to_the_position(x - 2, y + 20)
    move_mouse_to_the_position(x - 2, y + 20)
    pyautogui.mouseUp(button='right')

####################################################################################

def Zoom_out():
    from pynput.mouse import Controller

    mouse = Controller()
    for i in range(20):
        mouse.scroll(0, -1)

def Click_at_random_thing_on_the_screen():
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Define the size of the square area (percentage of the screen size)
    square_area_percentage = 0.5  # Adjust this value as per your requirement

    # Calculate the square area dimensions
    square_area_width = int(screen_width * 0.8)
    square_area_height = int(screen_height * 0.3)
    square_area_left = int((screen_width - square_area_width) / 2)
    square_area_top = int((screen_height - square_area_height) / 2)

    # Generate a random position within the square area
    random_x = random.randint(square_area_left, square_area_left + square_area_width)
    random_y = random.randint(square_area_top, square_area_top + square_area_height)

    # Move the mouse to the random position
    move_mouse_to_the_position(random_x, random_y)

    wait(0.2)

    move_mouse_to_the_position(random_x + 2, random_y + 4)

    wait(0.4)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def Click_on_an_image(image):
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
    current_dir = os.path.dirname(__file__)

    saved_image = cv2.imread(os.path.join(current_dir, 'images', check_screen_resolution() + " " + image))
    
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

        if image == "Tower Defense Simulator Return To Lobby.png" or image == "Tower Defense Simulator Return To Lobby 2.png":
            move_mouse_to_the_position(match_location[0] + 12, match_location[1] - 38)
        move_mouse_to_the_position(match_location[0], match_location[1])
        moving_mouse_and_clicking(match_location[0] - 4, match_location[1] + 6)
        return True
    else:
        print("Image not found.")
        return False

def Click_on_an_image_specialized_for_upgrading(image):
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
    current_dir = os.path.dirname(__file__)

    saved_image = cv2.imread(os.path.join(current_dir, 'images', check_screen_resolution() + " " + image))

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
        wait(0.2)

        for i in range(5):
            e_press()
            wait(0.2)
            e_unpress()
            wait(0.2)
        
        if image == 'Tower Defense Simulator Stats Icon.png':
            wait(0.02)
            q_press()
            wait(0.02)
            q_unpress()
            wait(0.02)
        move_mouse_to_the_position(match_location[0], match_location[1])
        moving_mouse_and_clicking(match_location[0] - 4, match_location[1] + 6)
        return True
    else:
        print("Image not found.")
        return False

def Click_on_an_image_specialized_for_upgrading_custom_militant(image):
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
    current_dir = os.path.dirname(__file__)

    saved_image = cv2.imread(os.path.join(current_dir, 'images', check_screen_resolution() + " " + image))

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
        wait(20)

        for i in range(5):
            e_press()
            wait(1)
            e_unpress()
            wait(1.2)
        
        if image == 'Tower Defense Simulator Stats Icon.png':
            wait(0.12)
            q_press()
            wait(0.12)
            q_unpress()
            wait(0.12)
        move_mouse_to_the_position(match_location[0], match_location[1])
        moving_mouse_and_clicking(match_location[0] - 4, match_location[1] + 6)
        return True
    else:
        print("Image not found.")
        return False