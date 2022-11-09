import json
import os
import pkgutil
from datetime import datetime, timedelta
import keyboard

currently_pressed = set()
keystroke = set()
key_press_times = list()
key_release_times = list()
register_keypresses = True


dictionary_data = pkgutil.get_data(
    __name__, os.path.join("dictionaries", "english-us.json")
)
WORDS = json.loads(dictionary_data)

print("Ready!")


def type_word(word):
    keyboard.write(word + " ")


def handle_chord(keys):
    global register_keypresses

    register_keypresses = False
    for _ in keys:
        keyboard.send("backspace")

    chord = "".join(sorted(keys))
    if chord in WORDS:
        word = WORDS[chord]
        type_word(word)
    register_keypresses = True


def handle_keystroke():
    first_keypress = min(key_press_times)
    last_keypress = max(key_press_times)
    keystroke_length = (last_keypress - first_keypress) / timedelta(milliseconds=1)

    if len(keystroke) >= 3 and keystroke_length < 50:
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

    if keystroke and not currently_pressed:
        handle_keystroke()
        keystroke = set()
        currently_pressed = set()
        key_press_times = list()
        key_release_times = list()


def handle_hook(event):
    # print("Keyboard event", event)
    if not register_keypresses:
        return

    if event.event_type == keyboard.KEY_DOWN:
        handle_press(event)

    if event.event_type == keyboard.KEY_UP:
        handle_release(event)


def main():
    print("Waiting for keys!")
    keyboard.hook(handle_hook)
    keyboard.wait()


if __name__ == "__main__":
    main()
