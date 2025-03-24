import time
import sys
from colorama import Fore, Style

def slow_type(text, color=Fore.WHITE, speed=0.1):
    """Prints text one character at a time with a delay and optional color."""
    sys.stdout.write(color)  # Set the color
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(Style.RESET_ALL)  # Reset to default color
    print()  # Add a newline at the end

message1 = ("Shout sa mga kabataan diyan      ", Fore.YELLOW)
message2 = ("MAAAA !", Fore.RED)
message3 = ("Ano ulam?       ", Fore.CYAN)
message4 = ("Shout sa mga kabataan diyan", Fore.GREEN)
message5 = ("Wag kayo puro cellphone", Fore.MAGENTA)
message6 = ("Galaw galaw din!", Fore.BLUE)

slow_type(*message1, speed=0.05)
slow_type(*message2, speed=0.06)
slow_type(*message3, speed=0.06)
slow_type(*message4, speed=0.04)
slow_type(*message5, speed=0.03)
slow_type(*message6, speed=0.07)
