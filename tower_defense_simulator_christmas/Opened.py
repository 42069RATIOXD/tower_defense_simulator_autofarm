import os
def run_background_opened_roblox_check():
    import pyautogui
    import cv2
    import numpy as np
    import inspect
    from screeninfo import get_monitors

    import threading
    import time

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

    def IsRobloxOpened():
        # Specify the path to your app icon or an image representing the app window
        app_icon_path_image = 'Tower Defense Simulator Roblox Text.png'

        current_dir = os.path.dirname(__file__)

        app_icon_path = os.path.join(current_dir, 'images', check_screen_resolution() + " " + app_icon_path_image)

        # Get the screen resolution
        screen_width, screen_height = pyautogui.size()

        # Capture the screen
        screen = np.array(pyautogui.screenshot())
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        app_icon = cv2.imread(app_icon_path, 0)  # Load the app icon as a gray-scale image
        result = cv2.matchTemplate(screen_gray, app_icon, cv2.TM_CCOEFF_NORMED)
        threshold = 0.96  # Set a threshold to determine if the app window is found

        caller_script = inspect.stack()[1][1]

        if np.max(result) >= threshold:
            print("Roblox is closed" + str(caller_script))
            return True
        else:
            print("Roblox is opened" + str(caller_script))
            return False

    # Function that will crash the script if condition is true
    def check_condition():
        while True:
            # Check the condition
            if IsRobloxOpened() == False:
                print("Condition is true. Crashing the script...")
                # Terminate the whole script
                import os
                os._exit(1)
            time.sleep(2)  # Wait for 2 seconds before rechecking the condition

    # Main script loop

    # Create a thread for the function that updates every 2 seconds
    condition_thread = threading.Thread(target=check_condition)

    # Start the condition thread
    condition_thread.start()

    time.sleep(2)

def crash_script():
    import threading
    import time
    
    # Function that will crash the script if condition is true
    def check_condition():
        print("Exited")
        import os
        os._exit(1)

    # Create a thread for the function that updates every 2 seconds
    condition_thread = threading.Thread(target=check_condition)

    # Start the condition thread
    condition_thread.start()

    time.sleep(2)