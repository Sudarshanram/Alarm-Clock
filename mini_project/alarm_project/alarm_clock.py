from playsound import playsound
import time

CLEAR= "\033[2"        # Clearing terminal
CLEAR_AND_RETURN = "\033[H"     # Clearing terminal

def alarm(second): 
    time_slip=0

    
    print(CLEAR)
    while time_slip < second:
        time.sleep(1)
        time_slip += 1

        time_left= second - time_slip
        minutes_left= time_left // 60  # gives aprox value  
        seconds_left =time_left % 60    

        print(f"{CLEAR_AND_RETURN} Alarm will sounds in {minutes_left:2d}:{seconds_left:2d}")

print("alarm_sound.mp3") # printing Sound file

minutes =int(input("Enter minute to wait:"))
seconds  =int(input("Enter seconds to wait:"))
total_seconds = minutes*60 +seconds

alarm(total_seconds)
