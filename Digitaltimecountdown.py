import time

def countdown_timer(seconds):
    print("\n⏳ Timer Started!\n")
    while seconds > 0:
        # Format seconds into MM:SS (Minutes:Seconds)
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # \r overwrites the current line in the terminal
        print(f"Time remaining: {timer_display}", end="\r")
        
        time.sleep(1)  # Wait for 1 second
        seconds -= 1

    print("\n⏰ Time's up!")

# Ask the user for input in seconds
total_seconds = int(input("Enter time in seconds: "))
countdown_timer(total_seconds)