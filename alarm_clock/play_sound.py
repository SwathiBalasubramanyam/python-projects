from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        seconds_left = time_left % 60
        minutes_left = time_left // 60
        hours_left = minutes_left // 60

        print(f"{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm_sound.mp3")


seconds = int(input("Please enter the number of seconds to count"))
alarm(seconds)