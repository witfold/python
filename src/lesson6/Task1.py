import time
import enum
from itertools import cycle
import sys


class Colors(enum.Enum):
    red = ('\033[1;31;48m', 7)
    yellow = ('\033[1;33;48m', 2)
    green = ('\033[1;36;48m', 4)

    def __init__(self, color, seconds):
        self.color = color
        self.seconds = seconds


class TrafficLight:

    def __init__(self):
        self.__stream = sys.stdout

    def running(self):
        for item in cycle(Colors):
            self.__draw(item)
            if item is Colors.green:
                self.__draw(Colors.yellow)

    def __draw(self, current_color):
        displayed_text = f"{current_color.color} █"
        self.__stream.write('\b' * (len(displayed_text) + 10))
        self.__stream.write(displayed_text)
        self.__stream.flush()
        time.sleep(current_color.seconds)


trafficLight = TrafficLight()
trafficLight.running()
