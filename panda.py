import time
import sys
import threading
from colorama import Fore

# Colors
RED = '\033[31m'
ORANGE = '\033[38;5;214m'   
YELLOW = '\033[33m'
CYAN = '\033[36m'
VIOLET = '\033[35m'
PINK = '\033[38;5;206m'   

# Function to cycle through colors
def cycle_colors():
    return [YELLOW, RED, ORANGE]

# Guitar ASCII Art
guitar = r"""
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
doc java         `.    ooooo    .;'
                   `-._______.-'
"""

# Function to handle guitar blinking continuously in the same position
def blink_guitar():
    sys.stdout.write('\033[2J\033[H')  # Clear the screen and move cursor to the top
    while True:
        for color in cycle_colors():
            sys.stdout.write('\033[H')  # Move the cursor to the top left of the screen
            sys.stdout.write(color)  # Apply color
            sys.stdout.write(guitar)
            sys.stdout.write('\033[0m')  # Reset color
            sys.stdout.flush()  # Ensure the guitar is printed immediately
            time.sleep(0.5)  # Wait for half a second

# Simulate slow typing effect for lyrics
def slow_type(message, color, speed=0.05):
    sys.stdout.write(color)  # Apply color to lyrics
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Lyrics/messages to display
message1 = ("Hirap tanggaping 'di mo na 'ko kailangan", RED)
message2 = ("Sana nama'y nilabanan mo, anong nangyari sa tayo?", ORANGE)
message3 = ("Hanggang sa huli, tuluyan bang kakalimutan na?", YELLOW)
message4 = ("Ayoko pang mawalan ng pag-asa, mga mata mo'y masilayan ko", CYAN)
message5 = ("At kahit ano pang gawin kong pagkukunwari", PINK)
message6 = ("Ay tila ba nakalimutan na'ng kalimutan ka", VIOLET)

# Start the guitar blinking in a separate thread
guitar_thread = threading.Thread(target=blink_guitar)
guitar_thread.daemon = True  # This will exit when the main program ends
guitar_thread.start()

# Print lyrics with slow typing effect (this will run alongside the guitar blinking)
# slow_type(*message1, speed=0.04)
# slow_type(*message2, speed=0.05)
# slow_type(*message3, speed=0.06)
# slow_type(*message4, speed=0.04)
# slow_type(*message5, speed=0.04)
# slow_type(*message6, speed=0.03)

# Keep the program running
while True:
    time.sleep(1)
