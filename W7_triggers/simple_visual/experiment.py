"""
(psychopy39) python experiment.py
"""

from psychopy import visual, monitors, event
from triggers import setParallelData
import os

# path to the file
experimental_pyfile_path = os.path.abspath(__file__)

# path to the directory with the py file containing the experiment
path = os.path.dirname(experimental_pyfile_path)

# now we can define all paths we will be using (e.g. to the stimuli and where we want to save the csv relative to the experimental path!)
stimuli_path = os.path.join(path, "stimuli")
print("path to stimuli: ", stimuli_path)

output_path = os.path.join(path, "output")

# check if the directory exists
if not os.path.exists(output_path):
    os.makedirs(output_path) # create the directory if it doesn't exist

# Create psychopy window
my_monitor = monitors.Monitor('testMonitor')  

win = visual.Window(monitor = my_monitor, fullscr=False, color='black')  # Initiate psychopy Window as the object "win", using the myMon object from last line


# defining visual stimulation
vis_stim = visual.ImageStim(win)
stim_fix = visual.TextStim(win, '+', alignText = 'center')

# defining mouse for response!
mouse = event.Mouse(visible=True, win=win)


pullTriggerDown = False

for stim, trigger in zip(["chili_gul.png", "chili_rod.png"], [1, 2]):
    vis_stim.image = os.path.join(stimuli_path, stim)

    # present the stimuli
    for frame in range(300):
        vis_stim.draw()  # Draw the stimulus

        if frame == 1:  # When the stimulus first appears, trigger the parallel port
            win.callOnFlip(setParallelData, trigger)
            pullTriggerDown = True  # Trigger is active now
        elif pullTriggerDown:  # If the trigger was activated, reset it after one frame
            win.callOnFlip(setParallelData, 0)
            pullTriggerDown = False  # Reset the trigger after it has been pulled

        # Flip the window to show the drawn stimulus
        win.flip()  



    mouse_click = False
    
    # add fixation cross during which the participant can provide a response (e.g. click if stimuli is red), and a trigger for that!
    for frame in range(300):
        stim_fix.draw()  # Draw the stimulus

        if frame == 1:  # When the stimulus first appears, trigger the parallel port
            win.callOnFlip(setParallelData, 100) # trigger 100 for fixation
            pullTriggerDown = True 
        elif pullTriggerDown: 
            win.callOnFlip(setParallelData, 0)
            pullTriggerDown = False  

        if not mouse_click:
            if mouse.getPressed()[0]==1:  # Check if mouse is clicked
                mouse_click = True  # Mouse click detected, exit the loop

                # Send trigger after mouse click
                win.callOnFlip(setParallelData, 3)  # For example, sending trigger 3 when the mouse is clicked

        # Flip the window to show the drawn stimulus
        win.flip()

        # if you want to continue to the next stimuli just after response is given
        #if mouse_click:
        #    win.callOnFlip(setParallelData, 0)
        #    win.flip()
        #    break
        
        
    