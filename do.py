# Python example for controlling rotational speed after a delay

import time

def initial_action():
    print("Initial action started.")
    time.sleep(2)  # Delay for 2 seconds
    print("Action after 2 seconds.")
    increase_speed()

def increase_speed():
    print("Increasing rotational speed.")
    # Code to increase rotational speed goes here

initial_action()
