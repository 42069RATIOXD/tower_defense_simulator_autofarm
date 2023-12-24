import subprocess

def check_library_installed(library_name):
    try:
        # Try importing the library
        __import__(library_name)
    except ImportError:
        return False
    return True

def install_library(library_name):
    print(f"Installing {library_name}...")
    try:
        subprocess.check_call(['pip', 'install', library_name])
        print(f"{library_name} installed successfully!")
    except Exception as e:
        print(f"Failed to install {library_name}: {e}")

required_libraries = ['time', 'pyautogui', 'opencv-python', 'numpy', 'os', 'screeninfo', 'pynput.mouse', 'inspect', 'threading', 'pygetwindow', 'pywin32', 'pynput']

for library in required_libraries:
    if not check_library_installed(library):
        install_library(library)
import time
from Opened import run_background_opened_roblox_check

# import pygetwindow as gw

# window = gw.getWindowsWithTitle('Roblox')[0]


# window.activate()
# window.maximize()

time.sleep(2)

run_background_opened_roblox_check()


print("Tower Defense Simulator.py started")

while True:
    subprocess.call(["python", "Lobby.py"])
    subprocess.call(["python", "Game.py"])