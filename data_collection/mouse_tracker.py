
import threading
from pynput.mouse import Listener
import datetime

class MouseListener:
    def __init__(self, time_interval):
        self.log = "Mouse tracking Started...\n"
        self.interval = time_interval

    def appendlog(self, string):
        self.log = self.log + f'{datetime.datetime.now()} ' + string + '\n'

    def on_move(self, x, y):
        current_move = f"move {x} {y}"
        self.appendlog(current_move)

    def on_click(self, x, y, mouse_button, is_downward_press: bool):
        """
        x is x-coordinate of click
        y is y-coordinate of click
        mouse_button is whether it was the right or left mouse button
        is_downward_press is a boolean
        """
        current_click = f"click {x} {y} {mouse_button} {is_downward_press}"
        self.appendlog(current_click)

    def on_scroll(self, x, y, dx, dy):
        """
        ``(x, y)`` is the new pointer position, and ``(dx, dy)`` is the scroll
        vector.
        """
        current_scroll = f"scroll {x} {y} {dx} {dy}"
        self.appendlog(current_scroll)

    def report(self):
        with open('mouselog.txt', 'a') as fh:
            fh.write(self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def run(self):
        with Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener:
            self.report()
            mouse_listener.join()

keylogger = MouseListener(10)
keylogger.run()
