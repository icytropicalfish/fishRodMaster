import pyautogui
import time
import win32api
import win32con
import keyboard
import json

def load_config():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {
            "trigger_key": "q",
            "subsequent_key": "mouse4",
            "wait_time": 0.01
        }
        save_config(config)
    return config

def save_config(config):
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=4)

def perform_action(trigger_key, subsequent_key, wait_time):
    pyautogui.press(trigger_key)
    
    pyautogui.click(button='right')
    
    time.sleep(wait_time)
    
    if subsequent_key.startswith('mouse'):
        if subsequent_key == 'mouse4':
            win32api.mouse_event(win32con.MOUSEEVENTF_XDOWN, 0, 0, 1, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_XUP, 0, 0, 1, 0)
        elif subsequent_key == 'mouse5':
            win32api.mouse_event(win32con.MOUSEEVENTF_XDOWN, 0, 0, 2, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_XUP, 0, 0, 2, 0)
    else:
        pyautogui.press(subsequent_key)

if __name__ == "__main__":
    print("Welcome to use my fish rod assister!")
    print("You can change the keys by modifying the config.json file.")
    print("\033[91mWarning: For educational purposes only, not to be used for cheating.\033[0m")
    config = load_config()
    
    trigger_key = config['trigger_key']
    subsequent_key = config['subsequent_key']
    wait_time = config['wait_time']

    print("Press '\\' to exit the program.")

    while True:
        try:
            if keyboard.is_pressed('\\'):
                print("Exiting program.")
                break
            if keyboard.is_pressed(trigger_key):
                perform_action(trigger_key, subsequent_key, wait_time)
                while keyboard.is_pressed(trigger_key):
                    time.sleep(0.1)
        except Exception as e:
            print(f"An error occurred: {e}")
            break
        time.sleep(0.001)
