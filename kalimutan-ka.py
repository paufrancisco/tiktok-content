import time
import sys
from colorama import Fore

# ANSI escape codes for color and blink effect
BLINK = '\033[5m'
RESET = '\033[0m'

# New Colors from your specified hex codes
COLOR_1 = '\033[38;5;18m'    # Nearest to #211C84 (Dark Blue/Purple)
COLOR_2 = '\033[38;5;63m'    # Nearest to #4D55CC (Mid Blue)
COLOR_3 = '\033[38;5;99m'    # Nearest to #7A73D1 (Lavender Blue)
COLOR_4 = '\033[38;5;189m'   # Nearest to #B5A8D5 (Pale Purple)
COLOR_5 = '\033[38;5;124m'   # Nearest to #B82132 (Dark Red)
COLOR_6 = '\033[38;5;174m'   # Nearest to #D2665A (Soft Red)
COLOR_7 = '\033[38;5;216m'   # Nearest to #F2B28C (Peach)
COLOR_8 = '\033[38;5;107m'   # #89AC46 (Greenish tone)
COLOR_9 = '\033[38;5;191m'   # #D3E671 (Pale greenish yellow)
COLOR_10 = '\033[38;5;229m'   # #F8ED8C (Very light yellow)

# Updated palette with descriptive names
DARK_PURPLE = COLOR_1
MID_BLUE = COLOR_2
LAVENDER_BLUE = COLOR_3
PALE_PURPLE = COLOR_4
DARK_RED = COLOR_5
SOFT_RED = COLOR_6
PEACH = COLOR_7
OLIVE_GREEN = COLOR_8
LIGHT_GREEN = COLOR_9
PALE_YELLOW = COLOR_10
 

# Text to blink
fireworks_text = [
    """
                      q o o p
                      q o!o p
                      d o!o b
                       \!!!/
                       |===|
                       |!!!|
                       |!!!|
                       |!!!|
                       |!!!|
                       |!!!|
                       |!!!|
                      _|!!!|__
                    .+=|!!!|--.`.
                  .'   |!!!|   `.\.
                 /     !===!     \\.
                 |    /|!!!|\    ||
                  \   \!!!!!/   //
                   )   `==='   ((
                 .'    !!!!!    `..
                /      !!!!!      \\.
               |       !!!!!       ||
               |       !!!!!       ||
               |       !!!!!       ||
                \     =======     //
doc pau          `.    ooooo    .;'
                   `-._______.-'
"""
]

# Function to cycle through colors
def cycle_colors():
    return [COLOR_8, COLOR_9, COLOR_10]

# Simulate slow typing effect
def slow_type(message, color, speed=0.05):
    sys.stdout.write(color)  # Apply color
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    print()

# Updated lyrics
message1 = ("Hirap tanggaping 'di mo na 'ko kailangan           ", COLOR_1)
message2 = ("Sana nama'y nilabanan mo                  ", COLOR_2)
message2b = ("Anong nangyari sa tayo?         ", COLOR_3)
message3 = ("Hanggang sa huli       ", COLOR_4)
message3b = ("Tuluyan bang kakalimutan na?        ", COLOR_5)
message4 = ("Ayoko pang mawalan ng pag-asa        ", COLOR_6)
message4b = ("Mga mata mo'y masilayan ko       ", COLOR_7)
message5 = ("At kahit ano pang gawin kong pagkukunwari        ", COLOR_8)
message6 = ("Ay tila ba nakalimutan na'ng             ", COLOR_9)
message6b = ("KALIMUTAN ka                             ", COLOR_10)


# Print updated lyrics with slow typing effect
slow_type(*message1, speed=0.07)
slow_type(*message2, speed=0.09)
slow_type(*message2b, speed=0.07)
slow_type(*message3, speed=0.07)
slow_type(*message3b, speed=0.09)
slow_type(*message4, speed=0.11)
slow_type(*message4b, speed=0.11)
slow_type(*message5, speed=0.09)
slow_type(*message6, speed=0.07)
slow_type(*message6b, speed=0.07)


# Trigger blink effect with yellow, red, and orange after the lyrics
while True:
    for color in cycle_colors():
        sys.stdout.write(BLINK)  # Start blink effect
        for line in fireworks_text:
            sys.stdout.write(color)  # Apply color
            print(line)
        sys.stdout.write(RESET)  # Reset the terminal effect
        time.sleep(0.5)  # Wait for half a second to make the blink effect noticeable
        sys.stdout.write('\033[2J\033[H')  # Clear screen to create a blinking effect
