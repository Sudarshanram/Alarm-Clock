from playsound import playsound
import time

CLEAR= "\033[2"
CLEAR_AND_RETURN = "\033[H"

def alarm(second):
    time_slip=0

    
    print(CLEAR)
    while time_slip < second:
        time.sleep(1)
        time_slip += 1

        time_left= second - time_slip
        minutes_left= time_left // 60  # gives aprox value  
        seconds_left =time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:2d}:{seconds_left:2d}")

print("alarm_sound.mp3")

minutes =int(input("Enter minute to wait:"))
seconds  =int(input("Enter seconds to wait:"))
total_seconds = minutes*60 +seconds

alarm(total_seconds)