import time
import random

def start_stopwatch():
    """
    Starts the stopwatch and returns the start time.

    No arguments are passing . 
    """
    start_time = time.time()
    print("Stopwatch started.")
    return start_time

def stop_stopwatch(start_time):
    """
    Stops the stopwatch and prints the elapsed time.

    Arguments : 
    start_time (float)

    Will calculate and return the elapsed time .
    """
    end_time = time.time()
    if(start_time==0):
        return "Stop watch didn't start"
    else:
        return end_time - start_time
   


start_time = start_stopwatch()


time.sleep(random.randint(1,10))  # waiting for some seconds to calculate the elapsed time betwwen the start time and stop time


print(f"Elapsed time is{stop_stopwatch(start_time)} seconds")