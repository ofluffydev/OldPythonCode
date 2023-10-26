import time as t
import pyautogui

#Initialize variables
clicks = 0
start_time = t.time()

#Loop until stopped
while True:
    if pyautogui.mouseDown():
        clicks+=1

    if t.time() - start_time >= 1:
        # Display the CPS and reset the variables
        cps = clicks / (t.time() - start_time)
        print(f"Clicks per second: {cps:.2f}")
        clicks = 0
        start_time = t.time()