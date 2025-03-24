import time
import sys
from colorama import Fore

# ANSI escape codes for color and blink effect
BLINK = '\033[5m'
RESET = '\033[0m'

# Colors
RED = '\033[31m'
ORANGE = '\033[38;5;214m'  # Orange (Using extended color codes)
YELLOW = '\033[33m'

# Text to blink
fireworks_text = [
    "++=============-                                                                           ",
    "++=============:                                                                           ",
    "++============-                                           :=-:.                            ",
    "++===========+=:                                         =#####*+-:                        ",
    "+=========+*++=:                                        :=+=++*####+-.                    ",
    "==========++-..                             .-...      :===--=*#######+:                   ",
    "==========+-                            .:-=+=++=:..:.:-=--:--*########*-                  ",
    "===========-.                         .:=+**+++***--=-::-----+**########*-                ",
    "============-.                       :----==++=. :=--------=====++++#####+                ",
    "====+==+===.                       .-===+++=:    -=----=======++==+######-                ",
    "+=========-                     .:--===+=:       =********+++=+++*#######-                ",
    "+========+=.                  .:-===++=.          :+**+++++=====*#######+                  ",
    "++++=====+=:                .--==+++=.               ==========+*######=                   ",
    "+++========:              :--==+++-.                 :+========+*###*=.                    ",
    "++=========.            .-====+++.                   :+==--=====+#+.                       ",
    "+=========-           .-===+++**:                    =+======++****+=-:.                ..",
    "++++++=====.        .-==++++*+*#####*+---=++======--=********************+=:       ..:::::",
    "+**+++++===:        -++++++===##################**********************####**+:  ...:::::::",
    "+++++======-         -++++++++#################*********************#########*-:::::::::::",
    "+++++=======.          .:-=**#################********+++++++*****############*-::::::----",
    "+**+++======-              .=*#############=+==:-:-=:-:-=+.-=:-::--=###########+----------",
    "**+++++======:                 :=*########*-=-+:+:*##-:=#=:-*#*:-###%%#######=------===-",
    "*+++++++++====.                   .:=*####=-=*-=--+-=:=-+:-+-+=:*+:*###%%%######*=-----===",
    "*++*+*+++++===:                       :*##=++*+**=++==---=---=--=-=###%%%%%%%%###*=---====",
    "*++**+++++++++:                         +#+-*###=-**-=+::+-:-=--=#####%%%%%%%%%####=--===="
]

# Function to cycle through colors
def cycle_colors():
    return [YELLOW, RED, ORANGE]

# Simulate slow typing effect
def slow_type(message, color, speed=0.05):
    sys.stdout.write(color)  # Apply color
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)   
    print()   

message1 = ("Kung tama ang hinala, ito'y mabisa na gamot            ", Fore.MAGENTA)
message2 = ("At nang aking inumin, saka ko lang naunawaan              ", Fore.YELLOW)
message3 = ("Gayuma nga, 'lang-hiya, ako'y naloko lamang", Fore.RED)
message4 = ("Nilinlang", Fore.CYAN)
message5 = ("dinaya",Fore.CYAN)
message6 = ("at inuto nang matindi", Fore.CYAN)
message7 = ("Ngayon ay pili ko na kung sino'ng kupal sa hindi", Fore.GREEN)
message8 = ("Ito ay pelikula na binuo patabingi", Fore.MAGENTA)
message9 = ("Isa kang malaking libag na tinubuan ng pisngi", Fore.BLUE)
message10 = ("Alam mo? Mukha kang tuhod", Fore.YELLOW)
message11 = ("na may bukol", Fore.YELLOW)
message12 = ("na may sugat", Fore.YELLOW)
message13 = ("na may nana                        ", Fore.YELLOW)
message14 = ("Ikaw ang dahilan kung ba't nasulat 'tong harana", Fore.RED)
message15 = ("Para sa dalaga na kung 'di dahil sa gayuma ay pinaliguan ko ng bala", Fore.CYAN)

# Print lyrics with slow typing effect
slow_type(*message1, speed=0.04)
slow_type(*message2, speed=0.05)
slow_type(*message3, speed=0.05)
slow_type(*message4, speed=0.07)
slow_type(*message5, speed=0.05)
slow_type(*message6, speed=0.07)
slow_type(*message7, speed=0.05)
slow_type(*message8, speed=0.08)
slow_type(*message9, speed=0.07)
slow_type(*message10, speed=0.04)
slow_type(*message11, speed=0.04)
slow_type(*message12, speed=0.04)
slow_type(*message13, speed=0.04)
slow_type(*message14, speed=0.05)
slow_type(*message15, speed=0.07)

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
