import sys
import time
from toggle import toggle_running

def print_and_replace(message):
    # Prints a message and replaces it on the same line
    sys.stdout.write(f"\r{message}")
    sys.stdout.flush()

def loading():
    options = ["|", "/", "-", "\\"]
    
    while toggle_running.get_toggle_status():
        # Displays a loading animation while the toggle status is True
        for option in options:
            print_and_replace(f"=== {option} ===")
            time.sleep(0.1)
            
    return
