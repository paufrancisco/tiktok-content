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
message1 = ("I saw her in the rightest way", COLOR_1)
message2 = ("Looking like Anne Hathaway", COLOR_2)
message2b = ("Laughing while she hit her pen", COLOR_3)
message3 = ("And coughed, and coughed", COLOR_4)
message3b = ("And then, she came up to my knees", COLOR_5)
message4 = ("Begging, baby, would you please?", COLOR_6)
message4b = ("Do the things you said you'd do to me, to me", COLOR_7)
message5 = ("Oh, won't you kiss me on the mouth and love me like a sailor?", COLOR_8)
message6 = ("And when you get a taste, can you tell me what's my flavor?", COLOR_9)
message6b = ("I don't believe in God, but I believe that you're my savior", COLOR_10)
message7 = ("My mom says that she's worried, but I'm covered in this favor", COLOR_1)
message8 = ("And when we're getting dirty, I forget all that is wrong", COLOR_2)
message9 = ("I sleep so I can see you 'cause I hate to wait so long", COLOR_3)
message10 = ("I sleep so I can see you and I hate to wait so long", COLOR_4)

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
slow_type(*message7, speed=0.07)
slow_type(*message8, speed=0.09)
slow_type(*message9, speed=0.07)
slow_type(*message10, speed=0.07)

# Trigger blink effect with yellow, red, and orange after the lyrics
while True:
    for color in cycle_colors():
        sys.stdout.write(BLINK)  # Start blink effect
        print(color + "* * * * * FIREWORKS * * * * *" + RESET)
        time.sleep(0.5)  # Wait for half a second to make the blink effect noticeable
        sys.stdout.write('\033[2J\033[H')  # Clear screen to create a blinking effect
