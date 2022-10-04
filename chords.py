import keyboard
from datetime import datetime, timedelta

currently_pressed = set()
keystroke = set()
key_press_times = list()
key_release_times = list()
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
    first_keypress = min(key_press_times)
    last_keypress = max(key_press_times)
    keystroke_length = (last_keypress - first_keypress) / timedelta(milliseconds=1)

    if len(keystroke) >= 3 and keystroke_length < 50:
        print("🎹 Chord registered", keystroke, keystroke_length)
        handle_chord(keystroke)


def handle_press(event):
    global key_press_times

    key = event.name
    currently_pressed.add(key)
    keystroke.add(key)
    key_press_times.append(datetime.now())

def handle_release(event):
    global keystroke, key_press_times, key_release_times, currently_pressed

    key = event.name
    if key in currently_pressed:
        currently_pressed.remove(key)

    key_release_times.append(datetime.now())
    
    if keystroke:
        handle_keystroke()

    keystroke = set()
    currently_pressed = set()
    key_press_times = list()
    key_release_times = list()

def handle_hook(event):
    if not register_keypresses:
        return

    if event.event_type == keyboard.KEY_DOWN:
        handle_press(event)

    if event.event_type == keyboard.KEY_UP:
        handle_release(event)

    print(event.event_type, event.name, event.time)
    debug()


def debug():
    print("keystroke", currently_pressed)
    print("currently pressed", currently_pressed)
    print("press times", key_press_times)
    print("release times", key_release_times)
    print("-----")

keyboard.hook(handle_hook)
keyboard.wait()
