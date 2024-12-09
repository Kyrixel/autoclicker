import pyautogui
import time
import random
from pynput import keyboard, mouse

click_location = None
running = False
key1 = 'z'
key2 = 'x' 

def on_click(x, y, button, pressed):
    global click_location
    if pressed:
        click_location = (x, y)
        return False

def select_mouse_location():
    print("Click anywhere on the screen to set the mouse click location...")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def simulate_keypress_and_click():
    global running, click_location
    if not click_location:
        print("Mouse click location not set. Please run the script again.")
        return

    print("Autoclicker is active. Press '~' to toggle on/off.")
    while True:
        if running:
            pyautogui.keyDown(key1)
            duration_key1 = random.uniform(0.4, 0.75)
            time.sleep(duration_key1)
            pyautogui.keyUp(key1)

            time.sleep(0.01)

            pyautogui.keyDown(key2)
            duration_key2 = random.uniform(0.4, 0.75)
            time.sleep(duration_key2)
            pyautogui.keyUp(key2)

            time.sleep(0.1)

            pyautogui.click(click_location[0], click_location[1])
        else:
            time.sleep(0.1)

def toggle_running(key):
    global running
    try:
        if key.char == '~':
            running = not running
            status = "running" if running else "paused"
            print(f"Autoclicker is now {status}.")
    except AttributeError:
        pass

if __name__ == "__main__":
    select_mouse_location()

    listener = keyboard.Listener(on_press=toggle_running)
    listener.start()

    try:
        simulate_keypress_and_click()
    except KeyboardInterrupt:
        print("Autoclicker stopped.")
    finally:
        listener.stop()
