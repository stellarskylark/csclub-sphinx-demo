"""Functions and classes relating to colors."""
from enum import Enum

class Color(Enum):
    """Enum with values for primary and secondary colors"""
    RED = "red"
    PURPLE = "purple"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    ORANGE = "orange"

PRIMARY = [Color.RED, Color.BLUE, Color.YELLOW]

def print_red():
    """Prints the value of Color.RED"""
    print(Color.RED)
def print_purple():
    """Prints the value of Color.PURPLE"""
    print(Color.PURPLE)
def print_blue():
    """Prints the value of Color.BLUE"""
    print(Color.BLUE)
def print_green():
    """Prints the value of Color.GREEN"""
    print(Color.GREEN)
def print_yellow():
    """Prints the value of Color.YELLOW"""
    print(Color.YELLOW)

def mix_colors(a, b):
    """Mixes two primary colors. Returns ``b`` if one or both colors
    are not primary.
    """
    if a in PRIMARY or b in PRIMARY:
        print("Can't combine non-primary colors")
        return b
    if a == b:
        return a

    if a == Color.RED:
        if b == Color.YELLOW:
            return Color.ORANGE
        else: # b is blue
            return Color.PURPLE
    elif a == Color.BLUE:
        if b == Color.YELLOW:
            return Color.GREEN
        else: # b is red
            return Color.PURPLE
    else: # a is yellow
        if b == Color.RED:
            return Color.ORANGE
        else: # b is blue
            return Color.GREEN
