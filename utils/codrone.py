import time
import CoDrone_mini

drone = CoDrone_mini.CoDrone()
drone.pair()

time.sleep(1)

notes = [440, 493.88, 523.25, 440, 523.25, 493.88, 440, 392, 349.23, 392, 440, 493.88, 440, 349.23]
durations = [0.5, 0.25, 0.25, 0.5, 0.25, 0.25, 1, 0.5, 0.5, 1, 0.5, 0.25, 0.25, 1]

for i in range(len(notes)):
    drone.play_note(notes[i], durations[i])
