from pynput import keyboard
from pynput.mouse import Controller as MouseController

mouse = MouseController()
pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)

    # Scroll up: Shift + '=' (which is + when Shift is held)
    if keyboard.Key.shift in pressed_keys and key == keyboard.KeyCode.from_char('='):
        print("Scroll up")
        mouse.scroll(0, 2)

    # Scroll down: Shift + '-' (which is _)
    if keyboard.Key.shift in pressed_keys and key == keyboard.KeyCode.from_char('-'):
        print("Scroll down")
        mouse.scroll(0, -2)

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

print("Press Shift + = (for +) or Shift + - to simulate scroll.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
