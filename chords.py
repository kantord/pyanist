import keyboard
from datetime import datetime, timedelta

currently_pressed = set()
keystroke = set()
first_keypress = None
register_keypresses = True

def handle_chord(keys):
    global register_keypresses

    register_keypresses = False
    for _ in keys:
        keyboard.send("backspace")

    for character in "hello world":
        keyboard.send(character)
    register_keypresses = True

def handle_keystroke():
    global keystroke, first_keypress

    keystroke_end = datetime.now()
    keystroke_length = (keystroke_end - first_keypress) / timedelta(milliseconds=1)

    if len(keystroke) > 1:
        print("🎹 Chord registered", keystroke, keystroke_length)
        handle_chord(keystroke)

    keystroke = set()
    first_keypress = None

def handle_press(event):
    global first_keypress

    if not register_keypresses:
        return

    key = event.name
    currently_pressed.add(key)
    keystroke.add(key)
    if not first_keypress:
        first_keypress = datetime.now()

def handle_release(event):
    key = event.name
    currently_pressed.remove(key)
    
    if not currently_pressed:
        handle_keystroke()

def handle_hook(event):
    if event.event_type == keyboard.KEY_DOWN:
        handle_press(event)

    if event.event_type == keyboard.KEY_UP:
        handle_release(event)

keyboard.hook(handle_hook)
keyboard.wait()
