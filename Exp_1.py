

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
IDname = "Participant's_name"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Import necessary libraries. 
from psychopy import visual, event, core, data
import random
import copy
from numpy import (sin, cos)
import numpy as np

# Create a window.
win = visual.Window(size = (1024, 768), units='pix', colorSpace='rgb', fullscr = False)

# Calculate the pixels per one visual degree angle for this experiment; 21.5 deg - is a value from the paper.
one_deg_in_pix = round(1024/21.5) 

# Present the instruction and waite for 'space'. 
instruction = visual.TextStim(win, text=u"Welcome to the experiment! \n \n You will see 10 crosses and white square in the center of the display after initiating the trial by pressing 'space' on the keyboard. You have to keep your eyes fixated on that square throughout the trial. Several crosses will be blinking. Blinking crosses are target stimuli. You need to track them without eye movements. The trial will be terminated and feedback will be given if an eye movement is detected.Some time while you will be tracking the target objects a square will flash on the screen and your task will be to press a response key ('T') as quickly and as accurately as possible if, and only if, the flash was occurred at the location of a target object. \n \n The experiment consists of 11 blocks. The first one is a practice block.", height = 20)
instruction.draw() 
win.flip()
event.waitKeys(keyList=['space'])

######################### Create necessary functions #########################

# WhatCoorIs() function returns coordinates corresponding to the input data (input is a target index)
def WhatCoorIs(t_indexes):
    if t_indexes == 0:
        t_squar_X1 = t_X1
        t_squar_Y1 = t_Y1
    elif t_indexes == 1:
        t_squar_X1 = t_X2
        t_squar_Y1 = t_Y2
    elif t_indexes == 2:
        t_squar_X1 = t_X3
        t_squar_Y1 = t_Y3
    elif t_indexes == 3:
        t_squar_X1 = t_X4
        t_squar_Y1 = t_Y4
    elif t_indexes == 4:
        t_squar_X1 = t_X5
        t_squar_Y1 = t_Y5
    elif t_indexes == 5:
        t_squar_X1 = t_X6
        t_squar_Y1 = t_Y6
    elif t_indexes == 6:
        t_squar_X1 = t_X7
        t_squar_Y1 = t_Y7
    elif t_indexes == 7:
        t_squar_X1 = t_X8
        t_squar_Y1 = t_Y8
    elif t_indexes == 8:
        t_squar_X1 = t_X9
        t_squar_Y1 = t_Y9
    elif t_indexes == 9:
        t_squar_X1 = t_X10
        t_squar_Y1 = t_Y10
    target_square = [t_squar_X1, t_squar_Y1]
    return target_square

# GetSquareCoord() function returns 10 trials for one target set size condition. 
# It returns: 10 TARG-distr sequences (blink_rand), 10 target-flash coordinates, 10 target-distr flash sequence coordinates.
# non_random_list is non randomized 4 TARG-distr sequence lists (since there are 4 flash type conditions)
def GetSquareCoord(non_random_list):
    
    # Since there are ten objects, 10 coordinates name pairs are needed.
    cordi = [[t_X1, t_Y1], [t_X2, t_Y2], [t_X3, t_Y3], [t_X4, t_Y4], [t_X5, t_Y5], [t_X6, t_Y6], [t_X7, t_Y7], [t_X8, t_Y8], [t_X9, t_Y9], [t_X10, t_Y10]]
    
    # There are 50 trials in one block. There are 5 different target set sizes. Thus, we need 10 trials for each target set size.
    # Also, there are four types of flash conditions "occurring equally often" within each 10 trials. 
    seq = [2,2,3,3] 
    
    # Randomize the sequence of 
    random.shuffle(seq)
    
    # Create lists which will contain several blocks of four coordinates pairs for flashes (total 10 trials for each target set size, not flash type)
    # first_pos means that the flash-target condition will be the first flash in a trial; second_pos - the second flash is the target-flash condition etc.
    first_pos = []
    second_pos = []
    third_pos = []
    fourth_pos = []
    
    # Create lists which will contain the target coordinates.
    first_target_posss = []
    second_target_posss = []
    third_target_posss = []
    fourth_target_posss = []
    
    # Create lists which will contain (in total) 10 elements in each 10 blocks (TARG and distr sequences). TARG is a variable with two colors - black and white.
    # This means that it will be blinking in the beginning of the trial. distr is a variable with two colors - black and black. This means that it will stay black
    # in the begining of the trial.
    if seq[0] == 2:
        first_random_list = [[],[]]
    else:
        first_random_list = [[],[],[]]
    if seq[1] == 2:
        second_random_list = [[],[]]
    else:
        second_random_list = [[],[],[]]
    if seq[2] == 2:
        third_random_list = [[],[]]
    else:
        third_random_list = [[],[],[]]
    if seq[3] == 2:
        fourth_random_list = [[],[]]
    else:
        fourth_random_list = [[],[],[]]
    
    # This one is for target-flash condition that will be the first flash in a trial
    for i in range(seq[0]):
        random.shuffle(non_random_list[0])                                          # Take the first ten TARG-distr sequence and randomize it
        already_random_list = non_random_list[0]                                    # Just rename it
        first_random_list[i].extend(already_random_list)                            # Put this randomized TARG-distr sequence to the first_random_list
        t_indexes_all = [i for i,p in enumerate(already_random_list) if p == TARG]   # Find all TARG element indexes
        t_indexes = random.choice(t_indexes_all)                                    # Choose just one TARG element index
        target_square = WhatCoorIs(t_indexes)                                       # Give the coordinate names which are correspond to chosen index
        d_indexes = [i for i,p in enumerate(already_random_list) if p == distr]      # Find all distr elemnt indexes
        random.shuffle(d_indexes)                                                   # Randomize them
        distr_square_1 = cordi[d_indexes[0]]                                        # Choose the first three distr element indexes 
        distr_square_2 = cordi[d_indexes[1]]                                        # (because we have only three distractor flashes
        distr_square_3 = cordi[d_indexes[2]]                                        # and find the corresponding coordinate names 
        first= [target_square,distr_square_1, distr_square_2, distr_square_3]       # Connect four coordinate name pairs and put the target coordinates to the first place
        first_target_posss.extend([target_square])                                  # Put one target-falsh coordinate to the first_target_posss
        first_pos.extend([first])                                                   # Put connected four coordinate name pairs to the first_pos
    
    # This one is for target-flash condition that will be the second flash in a trial
    for i in range(seq[1]):
        random.shuffle(non_random_list[1])
        already_random_list = non_random_list[1]
        second_random_list[i].extend(already_random_list)
        t_indexes_all = [i for i,p in enumerate(already_random_list) if p == TARG]
        t_indexes = random.choice(t_indexes_all)
        target_square = WhatCoorIs(t_indexes)
        d_indexes = [i for i,p in enumerate(already_random_list) if p == distr]
        random.shuffle(d_indexes)
        distr_square_1 = cordi[d_indexes[0]]
        distr_square_2 = cordi[d_indexes[1]]
        distr_square_3 = cordi[d_indexes[2]]
        second = [distr_square_1,target_square, distr_square_2, distr_square_3]
        second_target_posss.extend([target_square])
        second_pos.extend([second])
    
    # This one is for target-flash condition that will be the third flash in a trial
    for i in range(seq[2]):
        random.shuffle(non_random_list[2])
        already_random_list = non_random_list[2]
        third_random_list[i].extend(already_random_list)
        t_indexes_all = [i for i,p in enumerate(already_random_list) if p == TARG]
        t_indexes = random.choice(t_indexes_all)
        target_square = WhatCoorIs(t_indexes)
        d_indexes = [i for i,p in enumerate(already_random_list) if p == distr]
        random.shuffle(d_indexes)
        distr_square_1 = cordi[d_indexes[0]]
        distr_square_2 = cordi[d_indexes[1]]
        distr_square_3 = cordi[d_indexes[2]]
        third = [distr_square_1,distr_square_2, target_square, distr_square_3]
        third_target_posss.extend([target_square])
        third_pos.extend([third])
    
    # This one is for target-flash condition that will be the fourth flash in a trial
    for i in range(seq[3]):
        random.shuffle(non_random_list[3])
        already_random_list = non_random_list[3]
        fourth_random_list[i].extend(already_random_list)
        t_indexes_all = [i for i,p in enumerate(already_random_list) if p == TARG]
        t_indexes = random.choice(t_indexes_all)
        target_square = WhatCoorIs(t_indexes)
        d_indexes = [i for i,p in enumerate(already_random_list) if p == distr]
        random.shuffle(d_indexes)
        distr_square_1 = cordi[d_indexes[0]]
        distr_square_2 = cordi[d_indexes[1]]
        distr_square_3 = cordi[d_indexes[2]]
        fourth= [distr_square_1,distr_square_2, distr_square_3, target_square]
        fourth_target_posss.extend([target_square])
        fourth_pos.extend([fourth])
    
    # Connect everything. Now there are 10 generated and not randomized between flash type condition trials.
    square_rand_poss= first_pos + second_pos + third_pos + fourth_pos
    blink_rand = first_random_list + second_random_list + third_random_list + fourth_random_list
    target_coordinates = first_target_posss + second_target_posss + third_target_posss + fourth_target_posss
    
    return square_rand_poss, blink_rand, target_coordinates

######################### Create the stimuli and generate trial lists ##############################

# Create 10 crosses. 
    # It is worth noting that there are problem with letter size:
    # shape.size(0.42 * one_deg_in_pix) != letter.size(0.42 * one_deg_in_pix) but shape.size(0.42 * one_deg_in_pix) ~ letter.size(40)
one = visual.TextStim(win, text=u"+", height = 40, ori= 45) 
two = visual.TextStim(win, text=u"+", height = 40, ori= 45)
three = visual.TextStim(win, text=u"+", height = 40, ori= 45)
four = visual.TextStim(win, text=u"+", height = 40, ori= 45)
five = visual.TextStim(win, text=u"+", height = 40, ori= 45)
six = visual.TextStim(win, text=u"+", height = 40, ori= 45)
seven = visual.TextStim(win, text=u"+", height = 40, ori= 45)
eight = visual.TextStim(win, text=u"+", height = 40, ori= 45)
nine = visual.TextStim(win, text=u"+", height = 40, ori= 45)
ten = visual.TextStim(win, text=u"+", height = 40, ori= 45)

# Create 10 gray circles to inscribe crosses; 0.42 is a value from the paper
one_sq = visual.Circle(win, fillColor=[0,0,0], lineColor= [0,0,0], radius = ((0.42 * one_deg_in_pix))/2)
two_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius = ((0.42 * one_deg_in_pix))/2)
three_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius= ((0.42 * one_deg_in_pix))/2)
four_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius= ((0.42 * one_deg_in_pix))/2)
five_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius = ((0.42 * one_deg_in_pix))/2)
six_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius = ((0.42 * one_deg_in_pix))/2)
seven_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius= ((0.42 * one_deg_in_pix))/2)
eight_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius= ((0.42 * one_deg_in_pix))/2)
nine_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius= ((0.42 * one_deg_in_pix))/2)
ten_sq = visual.Circle(win, fillColor=[0,0,0],lineColor= [0,0,0], radius= ((0.42 * one_deg_in_pix))/2)

# Create 4 flash-squares
sq1 = visual.Rect(win, name='sq1', fillColor=[1,1,1])
sq2 = visual.Rect(win, name='sq2', fillColor=[1,1,1])
sq3 = visual.Rect(win, name='sq3', fillColor=[1,1,1])
sq4 = visual.Rect(win, name='sq4', fillColor=[1,1,1])

# Create point of fixation; 0.42 is a value from the paper
fix = visual.Rect(win, name='fix', fillColor=[1,1,1])
fix.size = (((0.42 * one_deg_in_pix)*2) , ((0.42 * one_deg_in_pix)*2))

# Create coordinates. It is important to use list type variables (because changeable variables will be needed for motion)
t_X1 = [-100]
t_Y1 = [100]
t_X2 = [0]
t_Y2 = [100]
t_X3 = [100]
t_Y3 = [100]
t_X4 = [-100]
t_Y4 = [0]
t_X5 = [-50]
t_Y5 = [0]
t_X6 = [50]
t_Y6 = [0]
t_X7 = [100]
t_Y7 = [0]
t_X8 = [-100]
t_Y8 = [-100]
t_X9 = [0]
t_Y9 = [-100]
t_X10 =[100]
t_Y10 = [-100]

# These variables are needed for target blinking in the beginning of the trials
distr = ['white', 'white']
TARG = ['white', 'black']

# Prepare input data for GetSquareCoord() function
non_random_list_OneTarg = [[TARG, distr, distr, distr, distr, distr, distr, distr, distr, distr]]*4
non_random_list_TwoTarg = [[TARG, TARG, distr, distr, distr, distr, distr, distr, distr, distr]]*4
non_random_list_ThreeTarg = [[TARG, TARG, TARG, distr, distr, distr, distr, distr, distr, distr]]*4
non_random_list_FourTarg = [[TARG, TARG, TARG, TARG, distr, distr, distr, distr, distr, distr]]*4
non_random_list_FiveTarg = [[TARG, TARG, TARG, TARG, TARG, distr, distr, distr, distr, distr]]*4

# Use the created and explained above function for each target set size condition
square_rand_poss_1, blink_rand_1, target_coordinates_1 = GetSquareCoord(non_random_list_OneTarg)
square_rand_poss_2, blink_rand_2, target_coordinates_2 = GetSquareCoord(non_random_list_TwoTarg)
square_rand_poss_3, blink_rand_3, target_coordinates_3 = GetSquareCoord(non_random_list_ThreeTarg)
square_rand_poss_4, blink_rand_4, target_coordinates_4 = GetSquareCoord(non_random_list_FourTarg)
square_rand_poss_5, blink_rand_5, target_coordinates_5 = GetSquareCoord(non_random_list_FiveTarg)

# Split everything. Now there are 50 generated and not randomized between flash type and target set size condition trials.
square_rand_poss = square_rand_poss_1 + square_rand_poss_2 + square_rand_poss_3 + square_rand_poss_4 + square_rand_poss_5
blink_rand = blink_rand_1 +blink_rand_2 + blink_rand_3 + blink_rand_4 + blink_rand_5
target_coordinates = target_coordinates_1 + target_coordinates_2 + target_coordinates_3 + target_coordinates_4

connect = list(zip(square_rand_poss, blink_rand, target_coordinates))  # Connect everything (like data table)
random.shuffle(connect)                                                # Randomize it
square_rand_poss, blink_rand, target_coordinates = zip(*connect)       # Disconnect it
square_rand_poss = list(square_rand_poss)                              # TConvert all variables to list type
blink_rand = list(blink_rand)                                          #
target_coordinates = list(target_coordinates)                          #

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Now there are 50 randomized trials (finnaly).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# There will be nested loops. 
# One (trial_blocks) deals with blocks (there are 10 blocks and 1 practice block, as written in the paper). 
# It will reinitilize 50 trials if the nested one (inner loop - trials) is completed.

blocks_numb = 11
trial_numb = 50 
trial_blocks = data.TrialHandler(trialList=[None], nReps = blocks_numb, method ='sequential')

# These three lines are additional. If you want to test nested loops, just take several trials by changing trial_numb and blocks_numb values.
square_rand_poss = square_rand_poss[0:trial_numb]
blink_rand = blink_rand[0:trial_numb]
target_coordinates = target_coordinates[0:trial_numb]

# This is imitation of gaze position. Please, keep mouse cursor in the center of visual field.
eye_movement = event.Mouse()

# This variable counts how many times the participant did the saccades.
num_eye_moves = 0

# The last trial in the block is ommitted after breaking the trial (because of eye_movement). 
# Thus, add one meaningless value to the trial lists. There are 51 trials now. 
blink_rand.append([['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white'], ['white', 'white']])
target_coordinates.append([[0], [0]])
square_rand_poss.append([[[0], [0]], [[0], [0]], [[0], [0]], [[0], [0]]])

# Now these lines are meaningless. I will explain them later in the code.
heldfixation = range(trial_numb) + [1]
time_sequence_for_sq = range(trial_numb) + [1] 
time_duration = range(trial_numb) + [1]

# It is needed to add an additional trial if eye movement occures. There is a problem with TrialHandler. 
# It seems that it is impossible to extend trials which are organized with this function. However, it is possible to terminate loops
# and skip meaningless trials. Thus, there is a need to use a value which is bigger than 50 (for example, 300)
trials_50 = range(300) 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Start ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
for block in trial_blocks:
    
    # Create the nested loop with repN = 1
    trials = data.TrialHandler(trials_50, 1, method='sequential')
    
    for thisTrial in trials:
        
        # Show and get mouse curse coordinates
        event.Mouse(visible = True,win=win)
        
        # Reinitilize coordinates after each trial. It is important to update values by replacing the first value in already created lists (see 219 line).
        t_X1[0] = -100
        t_Y1[0] = 100
        t_X2[0] = 0
        t_Y2[0] = 100
        t_X3[0] = 100
        t_Y3[0] = 100
        t_X4[0] = -100
        t_Y4[0] = 0
        t_X5[0] = -50
        t_Y5[0] = 0
        t_X6[0] = 50
        t_Y6[0] = 0
        t_X7[0] = 100
        t_Y7[0] = 0
        t_X8[0] = -100
        t_Y8[0] = -100
        t_X9[0] = 0
        t_Y9[0] = -100
        t_X10[0] = 100
        t_Y10[0] = -100
        
        # Get only one trial from 50 trials in this iteration
        col_1, col_2, col_3, col_4, col_5, col_6, col_7, col_8, col_9, col_10 = blink_rand[thisTrial]    # 10 color pairs (because 10 objects)
        pos_1, pos_2, pos_3, pos_4  = square_rand_poss[thisTrial]                                       # 4 pairs of flash coordinates
        thisTrial_target_coor = target_coordinates[thisTrial]                                           # 1 target-flash coordinate
        
############################################ BLOCK  1: set up static and blinking stimuli ############################################
        # To control while loop
        continueRoutine = True 
        
        # Frames for timing; 60 Hz monitor
        frameN = 0
        
        # Start the block of static and blinking stimuli
        while continueRoutine: 
            
            # Update frame after each iteration
            frameN = frameN + 1
            
            # For example, we have 50 trials and 5 saccade detections: 
            # if thisTrial is equal to 55, than inner loop (trials) should be terminated (remember that we have 300 trials in this loop)
            if thisTrial >= (trial_numb + num_eye_moves):
                trials.finished = True
                
                # Then give a feedback that the practice trials are over (the first repetition)
                if trial_blocks.thisRepN == 0:
                    press_space = visual.TextStim(win, text= u" Practice trials are over. \n \n Press space to go to the main " + str(blocks_numb) + " blocks.", height = 20)
                    press_space.draw()
                    win.flip()
                    event.waitKeys(keyList=['space'])
                
                # Or give a feedback that the experiment is over (the last repetition)
                elif trial_blocks.thisRepN == (blocks_numb -1):
                    press_space = visual.TextStim(win, text= u"The experiment is over! Thank you!", height = 20)
                    press_space.draw()
                    win.flip()
                    event.waitKeys(keyList=['space'])
                
                # Or give a feedback that the block is completed
                elif trial_blocks.thisRepN > 0 and trial_blocks.thisRepN != blocks_numb:
                    rep = str(trial_blocks.thisRepN)
                    press_space = visual.TextStim(win, text= u"Block # " + rep + u" is over. Press space to go to the next block", height = 20)
                    press_space.draw()
                    win.flip()
                    event.waitKeys(keyList=['space'])
                
                # And break the loop
                break
            
            # If there is not any saccade detections, than continue the while loop
            
            # This if-elif-elif statement is needed for blinking target stimuli for 10 seconds; 10 sec is a value from the paper
            # 1 second = 60 frames; 10 sec = 600 frames. 600/30 = 20
            if frameN % 2 == 0 and frameN <= 20: 
                for frame in range(30):
                    
                    # Set X and Y coordinates
                    one_sq.setPos([t_X1[0], t_Y1[0]])
                    two_sq.setPos([t_X2[0], t_Y2[0]])
                    three_sq.setPos([t_X3[0], t_Y3[0]])
                    four_sq.setPos([t_X4[0], t_Y4[0]])
                    five_sq.setPos([t_X5[0], t_Y5[0]])
                    six_sq.setPos([t_X6[0], t_Y6[0]])
                    seven_sq.setPos([t_X7[0], t_Y7[0]])
                    eight_sq.setPos([t_X8[0], t_Y8[0]])
                    nine_sq.setPos([t_X9[0], t_Y9[0]])
                    ten_sq.setPos([t_X10[0], t_Y10[0]])
                    
                    one.setPos([t_X1[0], t_Y1[0]])
                    two.setPos([t_X2[0], t_Y2[0]])
                    three.setPos([t_X3[0], t_Y3[0]])
                    four.setPos([t_X4[0], t_Y4[0]])
                    five.setPos([t_X5[0], t_Y5[0]])
                    six.setPos([t_X6[0], t_Y6[0]])
                    seven.setPos([t_X7[0], t_Y7[0]])
                    eight.setPos([t_X8[0], t_Y8[0]])
                    nine.setPos([t_X9[0], t_Y9[0]])
                    ten.setPos([t_X10[0], t_Y10[0]])
                    
                    # Set color 
                    one.color = col_1[0]
                    two.color = col_2[0]
                    three.color = col_3[0]
                    four.color = col_4[0]
                    five.color = col_5[0]
                    six.color = col_6[0]
                    seven.color = col_7[0]
                    eight.color = col_8[0]
                    nine.color = col_9[0]
                    ten.color = col_10[0]
                   
                    # Draw all stimuli and fixation point
                    fix.draw()
                    
                    one_sq.draw()
                    two_sq.draw()
                    three_sq.draw()
                    four_sq.draw()
                    five_sq.draw()
                    six_sq.draw()
                    seven_sq.draw()
                    eight_sq.draw()
                    nine_sq.draw()
                    ten_sq.draw()
                    
                    one.draw()
                    two.draw()
                    three.draw()
                    four.draw()
                    five.draw()
                    six.draw()
                    seven.draw()
                    eight.draw()
                    nine.draw()
                    ten.draw()
                    
                    # Update the window
                    win.flip()
            
            # Some objects will be white color for 30 frames 
            elif frameN % 2 != 0 and frameN <= 20: 
                for frame in range(30):
                    
                    # Set X and Y coordinates
                    one_sq.setPos([t_X1[0], t_Y1[0]])
                    two_sq.setPos([t_X2[0], t_Y2[0]])
                    three_sq.setPos([t_X3[0], t_Y3[0]])
                    four_sq.setPos([t_X4[0], t_Y4[0]])
                    five_sq.setPos([t_X5[0], t_Y5[0]])
                    six_sq.setPos([t_X6[0], t_Y6[0]])
                    seven_sq.setPos([t_X7[0], t_Y7[0]])
                    eight_sq.setPos([t_X8[0], t_Y8[0]])
                    nine_sq.setPos([t_X9[0], t_Y9[0]])
                    ten_sq.setPos([t_X10[0], t_Y10[0]])
                    
                    one.setPos([t_X1[0], t_Y1[0]])
                    two.setPos([t_X2[0], t_Y2[0]])
                    three.setPos([t_X3[0], t_Y3[0]])
                    four.setPos([t_X4[0], t_Y4[0]])
                    five.setPos([t_X5[0], t_Y5[0]])
                    six.setPos([t_X6[0], t_Y6[0]])
                    seven.setPos([t_X7[0], t_Y7[0]])
                    eight.setPos([t_X8[0], t_Y8[0]])
                    nine.setPos([t_X9[0], t_Y9[0]])
                    ten.setPos([t_X10[0], t_Y10[0]])
                    
                    # Set color 
                    one.color = col_1[1]
                    two.color = col_2[1]
                    three.color = col_3[1]
                    four.color = col_4[1]
                    five.color = col_5[1]
                    six.color = col_6[1]
                    seven.color = col_7[1]
                    eight.color = col_8[1]
                    nine.color = col_9[1]
                    ten.color = col_10[1]
                    
                    # Draw all stimuli and fixation point
                    fix.draw()
                    
                    one_sq.draw()
                    two_sq.draw()
                    three_sq.draw()
                    four_sq.draw()
                    five_sq.draw()
                    six_sq.draw()
                    seven_sq.draw()
                    eight_sq.draw()
                    nine_sq.draw()
                    ten_sq.draw()
                    
                    one.draw()
                    two.draw()
                    three.draw()
                    four.draw()
                    five.draw()
                    six.draw()
                    seven.draw()
                    eight.draw()
                    nine.draw()
                    ten.draw()
                    
                    # Update the window
                    win.flip()
            
            # If 10 sec are over
            elif frameN == 21:
                core.wait(1)            # Wait a sec before the motion starts
                continueRoutine = False # Break the while loop and go to the block 2 (motion)

############################################ BLOCK  2: move stimuli ############################################
        
        # Reinitilize the value
        continueRoutine = True
        frameN = 0 
        
        # Create a clock for motion part
        motionClock = core.Clock()
        motionClock.reset()
        
        # 1 sec is 60 frames
        fr = 30
        
        # V (1-10) are the speed (deg/frame) values. One of them will be randomly chosen; 1.25 deg - 9.4 deg are the values from the paper 
        V1 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V2 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V3 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V4 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V5 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V6 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V7 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V8 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V9 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        V10 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
        
        # Alpha (1-10) are the directions. One of them will be chosen from among 8 equal divisions of the compass. Values are shifted to 22.5 
        Alpha1 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha2 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha3 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha4 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha5 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha6 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha7 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha8 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha9 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        Alpha10 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
        
        Alpha1_X = cos(Alpha1)
        Alpha1_Y = sin(Alpha1)
        Alpha2_X = cos(Alpha2)
        Alpha2_Y = sin(Alpha2)
        Alpha3_X = cos(Alpha3)
        Alpha3_Y = sin(Alpha3)
        Alpha4_X = cos(Alpha4)
        Alpha4_Y = sin(Alpha4)
        Alpha5_X = cos(Alpha5)
        Alpha5_Y = sin(Alpha5)
        Alpha6_X = cos(Alpha6)
        Alpha6_Y = sin(Alpha6)
        Alpha7_X = cos(Alpha7)
        Alpha7_Y = sin(Alpha7)
        Alpha8_X = cos(Alpha8)
        Alpha8_Y = sin(Alpha8)
        Alpha9_X = cos(Alpha9)
        Alpha9_Y = sin(Alpha9)
        Alpha10_X = cos(Alpha10)
        Alpha10_Y = sin(Alpha10)
        
        # Start the block of moving stimuli
        while continueRoutine: 
            
            # If the previous loop was terminated than terminate this loop too and update num_eye_moves
            if thisTrial == (trial_numb + num_eye_moves) :
                num_eye_moves = 0
                break
            
            # Update frame after each iteration
            frameN = frameN + 1
            
            # There is line written below which inserts string 'NO' into the heldfixation list which was created above (see 301 line)
            # Thus, if there is 'NO' then in this trial participant did an eye movement. So, it is needed to
            # use the same motion duration and the same flash time.
            # The same values were inserted to the end of the lists (mot_dur and time_sequence_for_sq were created above see 301-303 lines)
            if heldfixation[thisTrial] == 'NO':
                mot_dur = time_duration[thisTrial]
                rand_time_square1, rand_time_square2, rand_time_square3, rand_time_square4 = time_sequence_for_sq[thisTrial]
            else:
                # If this trial is not the terminated one, then...
                # Motion duration must be randomly selected from 7 to 15 sec as written in the paper
                
                # Test if the target flash is the fourth flash
                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_4[0][0], pos_4[1][0]]:
                    
                    # In the paper there is a rule that the end of the animation occurred at least 4 s after the target-flash.
                    # There are only three values below because it is impossible to use the duration less than 13 sec in this flash type condition.
                    # For example, we have 12 seconds for motion. It means that four flashes (0.83 mc each) should be presented
                    # in the interval from 3 sec (flashes start "at least 3 s after the start of the animation") to 7.17 sec 
                    # (12 - 4 = 8; 8 - 0.83 = 7.17). Flashes will be very close to each other in the time and they will overlap. 
                    # Thus, there are only three possible values for this flash type condition. 
                    # There will be unequal possible variants in each flash type conditions because of this rule 
                    mot_dur = random.choice([13,14,15])
                    if mot_dur == 15: # 2                               # In order to avoid overlapping, predetermine possible same intervals for each flashes
                        rand_time_square1 = random.uniform(3, 4.17)     # Interval step is 2 
                        rand_time_square2 = random.uniform(5, 6.17)
                        rand_time_square3 = random.uniform(7, 8.17)
                        rand_time_square4 = random.uniform(9, 10.17)
                    elif mot_dur == 14: #1.75
                        rand_time_square1 = random.uniform(3, 3.92)
                        rand_time_square2 = random.uniform(4.75, 5.67)
                        rand_time_square3 = random.uniform(6.5, 7.42)
                        rand_time_square4 = random.uniform(8.25, 9.17)
                    elif mot_dur == 13: #1.5
                        rand_time_square1 = random.uniform(3, 3.67)
                        rand_time_square2 = random.uniform(4.5, 5.17)
                        rand_time_square3 = random.uniform(6, 6.67)
                        rand_time_square4 = random.uniform(7.5, 8.17)
                
                # Test if the target flash is the third flash
                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_3[0][0], pos_3[1][0]]:
                    mot_dur = random.choice([11,12,13,14,15])
                    if mot_dur == 15: # 2.7 
                        rand_time_square1 = random.uniform(3, 4.87)
                        rand_time_square2 = random.uniform(5.7, 7.47)
                        rand_time_square3 = random.uniform(8.3, 10.17)
                        rand_time_square4 = random.uniform(11, 14.17)
                    elif mot_dur == 14: #2.4
                        rand_time_square1 = random.uniform(3, 4.57)
                        rand_time_square2 = random.uniform(5.4, 6.87)
                        rand_time_square3 = random.uniform(7.77, 9.17)
                        rand_time_square4 = random.uniform(10, 13.17)
                    elif mot_dur == 13: #2
                        rand_time_square1 = random.uniform(3, 4.17)
                        rand_time_square2 = random.uniform(5, 6.17)
                        rand_time_square3 = random.uniform(7, 8.67)
                        rand_time_square4 = random.uniform(9, 12.17)
                    if mot_dur == 12: #1.7
                        rand_time_square1 = random.uniform(3, 3.87)
                        rand_time_square2 = random.uniform(4.7, 5.47)
                        rand_time_square3 = random.uniform(6.3, 7.17)
                        rand_time_square4 = random.uniform(8, 11.17)
                    if mot_dur == 11: #1.4
                        rand_time_square1 = random.uniform(3, 3.57)
                        rand_time_square2 = random.uniform(4.4, 4.87)
                        rand_time_square3 = random.uniform(5.7, 6.17)
                        rand_time_square4 = random.uniform(7, 10.17)
                
                # Test if the target flash is the second flash
                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_2[0][0], pos_2[1][0]]:
                    mot_dur = random.choice([10,11,12,13,14,15])
                    if mot_dur == 15: # 2
                        rand_time_square1 = random.uniform(3, 5.17)
                        rand_time_square2 = random.uniform(6, 8.17)
                        rand_time_square3 = random.uniform(9, 11.17)
                        rand_time_square4 = random.uniform(12, 14.17)
                    if mot_dur == 14: #2.75
                        rand_time_square1 = random.uniform(3, 4.92)
                        rand_time_square2 = random.uniform(5.75, 7.17)
                        rand_time_square3 = random.uniform(8, 9.67)
                        rand_time_square4 = random.uniform(10.5, 13.17)
                    if mot_dur == 13: #2.5
                        rand_time_square1 = random.uniform(3, 4.67)
                        rand_time_square2 = random.uniform(5.5, 7.17)
                        rand_time_square3 = random.uniform(8, 9.67)
                        rand_time_square4 = random.uniform(10.5, 12.17)
                    if mot_dur == 12:#2.25
                        rand_time_square1 = random.uniform(3, 4.42)
                        rand_time_square2 = random.uniform(5.25, 6.67)
                        rand_time_square3 = random.uniform(7.5, 8.92)
                        rand_time_square4 = random.uniform(9.75, 11.17)
                    if mot_dur == 11: #2
                        rand_time_square1 = random.uniform(3, 4.17)
                        rand_time_square2 = random.uniform(5, 6.17)
                        rand_time_square3 = random.uniform(7, 8.17)
                        rand_time_square4 = random.uniform(9, 10.17)
                    if mot_dur == 10: #1.5
                        rand_time_square1 = random.uniform(3, 3.67)
                        rand_time_square2 = random.uniform(4.5, 5.17)
                        rand_time_square3 = random.uniform(6, 7.17)
                        rand_time_square4 = random.uniform(8, 9.17)
                
                # Test if the target flash is the first flash
                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_1[0][0], pos_1[1][0]]:
                    mot_dur = random.choice([8,9,10,11,12,13,14,15])
                    if mot_dur == 15: # 2
                        rand_time_square1 = random.uniform(3, 5.17)
                        rand_time_square2 = random.uniform(6, 8.17)
                        rand_time_square3 = random.uniform(9, 11.17)
                        rand_time_square4 = random.uniform(12, 14.17)
                    if mot_dur == 14: #2.75
                        rand_time_square1 = random.uniform(3, 4.92)
                        rand_time_square2 = random.uniform(5.75, 7.17)
                        rand_time_square3 = random.uniform(8, 9.67)
                        rand_time_square4 = random.uniform(10.5, 13.17)
                    if mot_dur == 13: #2.5
                        rand_time_square1 = random.uniform(3, 4.67)
                        rand_time_square2 = random.uniform(5.5, 7.17)
                        rand_time_square3 = random.uniform(8, 9.67)
                        rand_time_square4 = random.uniform(10.5, 12.17)
                    if mot_dur == 12:#2.25
                        rand_time_square1 = random.uniform(3, 4.42)
                        rand_time_square2 = random.uniform(5.25, 6.67)
                        rand_time_square3 = random.uniform(7.5, 8.92)
                        rand_time_square4 = random.uniform(9.75, 11.17)
                    if mot_dur == 11: #2
                        rand_time_square1 = random.uniform(3, 4.17)
                        rand_time_square2 = random.uniform(5, 6.17)
                        rand_time_square3 = random.uniform(7, 8.17)
                        rand_time_square4 = random.uniform(9, 10.17)
                    if mot_dur == 10: #1.75
                        rand_time_square1 = random.uniform(3, 3.92)
                        rand_time_square2 = random.uniform(4.75, 5.67)
                        rand_time_square3 = random.uniform(6.5, 7.42)
                        rand_time_square4 = random.uniform(8.25, 9.17)
                    if mot_dur == 9: #1.5
                        rand_time_square1 = random.uniform(3, 3.67)
                        rand_time_square2 = random.uniform(4.5, 5.17)
                        rand_time_square3 = random.uniform(6, 6.67)
                        rand_time_square4 = random.uniform(7.5, 8.17)
                    if mot_dur == 8: 
                        rand_time_square1 = random.uniform(3, 3.17)
                        rand_time_square2 = random.uniform(4, 4.47)
                        rand_time_square3 = random.uniform(5.3, 5.87)
                        rand_time_square4 = random.uniform(6.7, 7.17)
            
            if frameN <= 1: 
                for frame in range(200):
                    
                    # The velocity and/or direction of the moving objects were changing every few hundred milliseconds as written in the paper
                    
                    # 1000 mc is 30 frames; 900 mc is 27 frames ("every few hundred milliseconds")
                    repeate_rand_time = int(round(random.uniform(10,27)))
                    
                    # These values will be changing every repeate_rand_time. 
                    # It will be determined if direction and speed changes simultaneously or not in this repeate_rand_time
                    SimultaniouslyOrNot_1 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_2 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_3 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_4 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_5 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_6 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_7 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_8 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_9 = random.choice(['yes', 'no'])
                    SimultaniouslyOrNot_10 = random.choice(['yes', 'no'])
                    
                    # These values will be changing every repeate_rand_time. 
                    # It will be determined if direction or speed changes in this repeate_rand_time (if SimultaniouslyOrNot == 'no')
                    SpeedOrDegree_1 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_2 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_3 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_4 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_5 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_6 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_7 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_8 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_9 = random.choice(['speed', 'degree'])
                    SpeedOrDegree_10 = random.choice(['speed', 'degree'])
                    
                    # Determine whether direction and/or velocity will be changed
    ######## FIRST OBJECT
                    if SimultaniouslyOrNot_1 == "yes":
                        V1 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr)) 
                        Alpha1 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]) 
                        Alpha1_Y = sin(Alpha1)
                    elif SimultaniouslyOrNot_1 == "no":
                        if SpeedOrDegree_1 == "speed":
                            V1 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_1 == "degree":
                            Alpha1 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha1_X = cos(Alpha1)
                            Alpha1_Y = sin(Alpha1)
    ######## SECOND
                    if SimultaniouslyOrNot_2 == "yes":
                        V2 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha2 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha2_X = cos(Alpha2)
                        Alpha2_Y = sin(Alpha2)
                    elif SimultaniouslyOrNot_2 == "no":
                        if SpeedOrDegree_2 == "speed":
                            V2 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_2 == "degree":
                            Alpha2 =random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]) 
                            Alpha2_X = cos(Alpha2)
                            Alpha2_Y = sin(Alpha2)
    ######## THIRD
                    if SimultaniouslyOrNot_3 == "yes":
                        V3 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr)) 
                        Alpha3 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha3_X = cos(Alpha3)
                        Alpha3_Y = sin(Alpha3)
                    elif SimultaniouslyOrNot_3 == "no":
                        if SpeedOrDegree_3 == "speed":
                            V3 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_3 == "degree":
                            Alpha3 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha3_X = cos(Alpha3)
                            Alpha3_Y = sin(Alpha3)
    ######## FOURTH
                    if SimultaniouslyOrNot_4 == "yes":
                        V4 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha4 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha4_X = cos(Alpha4)
                        Alpha4_Y = sin(Alpha4)
                    elif SimultaniouslyOrNot_4 == "no":
                        if SpeedOrDegree_4 == "speed":
                            V4 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_4 == "degree":
                            Alpha4 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha4_X = cos(Alpha4)
                            Alpha4_Y = sin(Alpha4)
    ######## FIFTH
                    if SimultaniouslyOrNot_5 == "yes":
                        V5 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha5 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha5_X = cos(Alpha5)
                        Alpha5_Y = sin(Alpha5)
                    elif SimultaniouslyOrNot_5 == "no":
                        if SpeedOrDegree_5 == "speed":
                            V5 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_5 == "degree":
                            Alpha5 = random.choice([23, 68, 113, 158, 203, 248, 293, 338])
                            Alpha5_X = cos(Alpha5)
                            Alpha5_Y = sin(Alpha5)
    ######## SIXTH
                    if SimultaniouslyOrNot_6 == "yes":
                        V6 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha6 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha6_X = cos(Alpha6)
                        Alpha6_Y = sin(Alpha6)
                    elif SimultaniouslyOrNot_6 == "no":
                        if SpeedOrDegree_6 == "speed":
                            V6 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_6 == "degree":
                            Alpha6 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha6_X = cos(Alpha6)
                            Alpha6_Y = sin(Alpha6)
    ######## SEVENTH
                    if SimultaniouslyOrNot_7 == "yes":
                        V7 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha7 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5]) 
                        Alpha7_X = cos(Alpha7)
                        Alpha7_Y = sin(Alpha7)
                    elif SimultaniouslyOrNot_7 == "no":
                        if SpeedOrDegree_7 == "speed":
                            V7 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_7 == "degree":
                            Alpha7 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha7_X = cos(Alpha7)
                            Alpha7_Y = sin(Alpha7)
    ######## EIGHTH
                    if SimultaniouslyOrNot_8 == "yes":
                        V8 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha8 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha8_X = cos(Alpha8)
                        Alpha8_Y = sin(Alpha8)
                    elif SimultaniouslyOrNot_8 == "no":
                        if SpeedOrDegree_8 == "speed":
                            V8 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_8 == "degree":
                            Alpha8 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha8_X = cos(Alpha8)
                            Alpha8_Y = sin(Alpha8)
    ######## NINTH
                    if SimultaniouslyOrNot_9 == "yes":
                        V9 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha9 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha9_X = cos(Alpha9)
                        Alpha9_Y = sin(Alpha9)
                    elif SimultaniouslyOrNot_9 == "no":
                        if SpeedOrDegree_9 == "speed":
                            V9 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_9 == "degree":
                            Alpha9 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha9_X = cos(Alpha9)
                            Alpha9_Y = sin(Alpha9)
    ######## TENTH
                    if SimultaniouslyOrNot_10 == "yes":
                        V10 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        Alpha10 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                        Alpha10_X = cos(Alpha10)
                        Alpha10_Y = sin(Alpha10)
                    elif SimultaniouslyOrNot_10 == "no":
                        if SpeedOrDegree_10 == "speed":
                            V10 = random.uniform(((1.25*one_deg_in_pix)/fr), ((9.4*one_deg_in_pix)/fr))
                        elif SpeedOrDegree_10 == "degree":
                            Alpha10 = random.choice([22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5])
                            Alpha10_X = cos(Alpha10)
                            Alpha10_Y = sin(Alpha10)
                            
                    # The motion code starts here
                    for next_random_will_be in range(repeate_rand_time):
                        
                        # Get the current motion time
                        motion_t = motionClock.getTime()
                        
                        # Get mouse curse coordinates
                        x_eye,y_eye = eye_movement.getPos()
                        
                        # Allowed area for eye movements
                        d = np.sqrt(x_eye**2+y_eye**2)
                        
                        # If the gaze position (mouse curse) is out of the allowed area...
                        if d > (2*one_deg_in_pix):
                            
                            # Update num_eye_moves
                            num_eye_moves = num_eye_moves + 1
                            
                            # Save this trial values (it is needed the same motion duration and same flash time for terminated trial)
                            same_mot_dur = mot_dur
                            same_square_time1 = rand_time_square1
                            same_square_time2 = rand_time_square2
                            same_square_time3 = rand_time_square3
                            same_square_time4 = rand_time_square4
                            
                            # Determine where was target in the sequence in the terminated trial?
                            this_square_rand_poss = square_rand_poss[thisTrial]
                            this_target_coordinates = target_coordinates[thisTrial]
                            if [this_target_coordinates[0][0],this_target_coordinates[1][0]] == [this_square_rand_poss[0][0], this_square_rand_poss[0][1]]:
                                target_index_was = 0
                            elif [this_target_coordinates[0][0],this_target_coordinates[1][0]] == [this_square_rand_poss[1][0], this_square_rand_poss[1][1]]:
                                target_index_was = 1
                            elif [this_target_coordinates[0][0],this_target_coordinates[1][0]] == [this_square_rand_poss[2][0], this_square_rand_poss[2][1]]:
                                target_index_was = 2
                            elif [this_target_coordinates[0][0],this_target_coordinates[1][0]] == [this_square_rand_poss[3][0], this_square_rand_poss[3][1]]:
                                target_index_was = 3
                            
                            # Get the new target square coordinates
                            this_blink = copy.deepcopy(blink_rand[thisTrial])
                            random.shuffle(this_blink)
                            new_target_indexes_all = [i for i,p in enumerate(this_blink) if p == ['white', 'black']]
                            new_target_index = random.choice(new_target_indexes_all)
                            new_target_square = WhatCoorIs(new_target_index)
                            
                            # Get the new distractor square coordinates
                            new_d_indexes = [i for i,p in enumerate(this_blink) if p == ['white', 'white']]
                            random.shuffle(new_d_indexes)
                            cordin = [[t_X1, t_Y1], [t_X2, t_Y2], [t_X3, t_Y3], [t_X4, t_Y4], [t_X5, t_Y5], [t_X6, t_Y6], [t_X7, t_Y7], [t_X8, t_Y8], [t_X9, t_Y9], [t_X10, t_Y10]]
                            new_distr_square_1 = cordin[new_d_indexes[0]]
                            new_distr_square_2 = cordin[new_d_indexes[1]]
                            new_distr_square_3 = cordin[new_d_indexes[2]]
                            
                            # Create new targ-distr falsh coordinates sequence of the same flash type
                            if target_index_was == 0:
                                new_square_cor_seq = [new_target_square,new_distr_square_1, new_distr_square_2, new_distr_square_3]
                            elif target_index_was == 1:
                                new_square_cor_seq = [new_distr_square_1,new_target_square, new_distr_square_2, new_distr_square_3]
                            elif target_index_was == 2:
                                new_square_cor_seq = [new_distr_square_1,new_distr_square_2, new_target_square, new_distr_square_3]
                            elif target_index_was == 3:
                                new_square_cor_seq = [new_distr_square_1,new_distr_square_2, new_distr_square_3, new_target_square]
                            
                            # Insert terminated trial paramentrs into the main trail lists
                            
                            # Thus, there are the same flash type, motion duration, flash time, target size, but new coordinates.
                            blink_rand.insert(len(blink_rand) - 1, this_blink)
                            square_rand_poss.insert(len(square_rand_poss) - 1, new_square_cor_seq)
                            target_coordinates.insert(len(target_coordinates) - 1, new_target_square)
                            heldfixation.insert(len(heldfixation)-1, 'NO')
                            time_sequence_for_sq.insert(len(time_sequence_for_sq)-1, [same_square_time1, same_square_time2, same_square_time3, same_square_time4])
                            time_duration.insert(len(time_duration)-1, same_mot_dur)
                            
                            # Give a feedback reminder
                            eye_feedback = visual.TextStim(win, text= u"Please, keep your eyes fixated on the center square throughout the trial", height = 20)
                            eye_feedback.draw()
                            win.flip()
                            event.waitKeys(keyList=['space'])
                            
                            # And break the loop (motion)
                            break
                            
                       # get current motion time in sec
                       # i = visual.TextStim(win, text= next_random_will_be, height = 30, pos= (-300,300))
                       # mowt = visual.TextStim(win, text=motion_t, height = 30, pos=(0,300))
                       # i.draw()
                       # mowt.draw()
                       
                        # Stop the motion if current (motion time) > (randomly chosen mot_dur) and allow to initiate the next trial
                        if motion_t > mot_dur:
                            press_space = visual.TextStim(win, text=u"Press space", height = 20)
                            press_space.draw()
                            win.flip()
                            event.waitKeys(keyList=['space'])
                            
                            # And break the inner 'for' loop (there will be breaks for outer loops below)
                            break 
                            
                        # else continue moving
                        else: 
            ###FIRST        
                            # Y limits
                            plus = 384-12
                            
                            # X limits 
                            plus_X = 384-12
                            
                            t_X1[0] = t_X1[0] + (V1)*(Alpha1_X)   # Replace X coordinate with new value. V1 * Alpha1_X = how many pix will added to the previous value
                            t_Y1[0] = t_Y1[0] + (V1)*(Alpha1_Y)   # Replace X coordinate with new value. V1 * Alpha1_Y = how many pix will added to the previous value
                            
                            # Detect edges. Objects will bounce off if they meet the plus x plus_X square's edges.
                            if t_X1[0] > plus_X:
                                t_X1[0] = plus_X
                                Alpha1_X = -Alpha1_X
                            if t_Y1[0] > plus:
                                t_Y1[0] = plus
                                Alpha1_Y = -Alpha1_Y
                            if t_X1[0] < -plus_X:
                                t_X1[0] = -plus_X
                                Alpha1_X = -Alpha1_X
                            if t_Y1[0] < -plus:
                                t_Y1[0] = -plus
                                Alpha1_Y = -Alpha1_Y
            ###SECOND
                            t_X2[0] = t_X2[0] + (V2)*(Alpha2_X)
                            t_Y2[0] = t_Y2[0] + (V2)*(Alpha2_Y)
                            
                            if t_X2[0] > plus_X:
                                t_X2[0] = plus_X
                                Alpha2_X = -Alpha2_X
                            if t_Y2[0] > plus:
                                t_Y2[0] = plus
                                Alpha2_Y = -Alpha2_Y
                            if t_X2[0] < -plus_X:
                                t_X2[0] = -plus_X
                                Alpha2_X = -Alpha2_X
                            if t_Y2[0] < -plus:
                                t_Y2[0] = -plus
                                Alpha2_Y = -Alpha2_Y
            ###THIRD
                            t_X3[0] = t_X3[0] + (V3)*(Alpha3_X)
                            t_Y3[0] = t_Y3[0] + (V3)*(Alpha3_Y)
                            
                            if t_X3[0] > plus_X:
                                t_X3[0] = plus_X
                                Alpha3_X = -Alpha3_X
                            if t_Y3[0] > plus:
                                t_Y3[0] = plus
                                Alpha3_Y = -Alpha3_Y
                            if t_X3[0] < -plus_X:
                                t_X3[0] = -plus_X
                                Alpha3_X = -Alpha3_X
                            if t_Y3[0] < -plus:
                                t_Y3[0] = -plus
                                Alpha3_Y = -Alpha3_Y
            ###FOURTH
                            t_X4[0] = t_X4[0] + (V4)*(Alpha4_X)
                            t_Y4[0] = t_Y4[0] + (V4)*(Alpha4_Y)
                            
                            if t_X4[0] > plus_X:
                                t_X4[0] = plus_X
                                Alpha4_X = -Alpha4_X
                            if t_Y4[0] > plus:
                                t_Y4[0] = plus
                                Alpha4_Y = -Alpha4_Y
                            if t_X4[0] < -plus_X:
                                t_X4[0] = -plus_X
                                Alpha4_X = -Alpha4_X
                            if t_Y4[0] < -plus:
                                t_Y4[0] = -plus
                                Alpha4_Y = -Alpha4_Y
            ###FIFTH
                            t_X5[0] = t_X5[0] + (V5)*(Alpha5_X)
                            t_Y5[0] = t_Y5[0] + (V5)*(Alpha5_Y)
                            
                            if t_X5[0] > plus_X:
                                t_X5[0] = plus_X
                                Alpha5_X = -Alpha5_X
                            if t_Y5[0] > plus:
                                t_Y5[0] = plus
                                Alpha5_Y = -Alpha5_Y
                            if t_X5[0] < -plus_X:
                                t_X5[0] = -plus_X
                                Alpha5_X = -Alpha5_X
                            if t_Y5[0] < -plus:
                                t_Y5[0] = -plus
                                Alpha5_Y = -Alpha5_Y
            ###SIXTH
                            t_X6[0] = t_X6[0] + (V6)*(Alpha6_X)
                            t_Y6[0] = t_Y6[0] + (V6)*(Alpha6_Y)
                            
                            if t_X6[0] > plus_X:
                                t_X6[0] = plus_X
                                Alpha6_X = -Alpha6_X
                            if t_Y6[0] > plus:
                                t_Y6[0] = plus
                                Alpha6_Y = -Alpha6_Y
                            if t_X6[0] < -plus_X:
                                t_X6[0] = -plus_X
                                Alpha6_X = -Alpha6_X
                            if t_Y6[0] < -plus:
                                t_Y6[0] = -plus
                                Alpha6_Y = -Alpha6_Y
            ###SEVETH
                            t_X7[0] = t_X7[0] + (V7)*(Alpha7_X)
                            t_Y7[0] = t_Y7[0] + (V7)*(Alpha7_Y)
                            
                            if t_X7[0] > plus_X:
                                t_X7[0] = plus_X
                                Alpha7_X = -Alpha7_X
                            if t_Y7[0] > plus:
                                t_Y7[0] = plus
                                Alpha7_Y = -Alpha7_Y
                            if t_X7[0] < -plus_X:
                                t_X7[0] = -plus_X
                                Alpha7_X = -Alpha7_X
                            if t_Y7[0] < -plus:
                                t_Y7[0] = -plus
                                Alpha7_Y = -Alpha7_Y
            ###EIGHTH
                            t_X8[0] = t_X8[0] + (V8)*(Alpha8_X)
                            t_Y8[0] = t_Y8[0] + (V8)*(Alpha8_Y)
                            
                            if t_X8[0] > plus_X:
                                t_X8[0] = plus_X
                                Alpha8_X = -Alpha8_X
                            if t_Y8[0] > plus:
                                t_Y8[0] = plus
                                Alpha8_Y = -Alpha8_Y
                            if t_X8[0] < -plus_X:
                                t_X8[0] = -plus_X
                                Alpha8_X = -Alpha8_X
                            if t_Y8[0] < -plus:
                                t_Y8[0] = -plus
                                Alpha8_Y = -Alpha8_Y
            ###NINTH
                            t_X9[0] = t_X9[0] + (V9)*(Alpha9_X)
                            t_Y9[0] = t_Y9[0] + (V9)*(Alpha9_Y)
                            
                            if t_X9[0] > plus_X:
                                t_X9[0] = plus_X
                                Alpha9_X = -Alpha9_X
                            if t_Y9[0] > plus:
                                t_Y9[0] = plus
                                Alpha9_Y = -Alpha9_Y
                            if t_X9[0] < -plus_X:
                                t_X9[0] = -plus_X
                                Alpha9_X = -Alpha9_X
                            if t_Y9[0] < -plus:
                                t_Y9[0] = -plus
                                Alpha9_Y = -Alpha9_Y
            ###TENTH
                            t_X10[0] = t_X10[0] + (V10)*(Alpha10_X)
                            t_Y10[0] = t_Y10[0] + (V10)*(Alpha10_Y)
                            
                            if t_X10[0] > plus_X:
                                t_X10[0] = plus_X
                                Alpha10_X = -Alpha10_X
                            if t_Y10[0] > plus:
                                t_Y10[0] = plus
                                Alpha10_Y = -Alpha10_Y
                            if t_X10[0] < -plus_X:
                                t_X10[0] = -plus_X
                                Alpha10_X = -Alpha10_X
                            if t_Y10[0] < -plus:
                                t_Y10[0] = -plus
                                Alpha10_Y = -Alpha10_Y
                            
                            # ((0.42 * one_deg_in_pix))/2): first object radius
                            # (((0.42 * one_deg_in_pix))/2): second object radius
                            # round(0.75 * one_deg_in_pix)): "no two objects could be closer than 0.75 deg apart"
                            distance_collision =  (((((0.42 * one_deg_in_pix))/2) + (((0.42 * one_deg_in_pix))/2))**2 + round(0.75 * one_deg_in_pix))
                            
                            # This bunch of if statements are needed to detect collisions between two objects. 
                            # Objects will bounce off each other
                            if (t_X1[0]-t_X2[0])**2 + (t_Y1[0]-t_Y2[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha2_X = - Alpha2_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha2_Y = - Alpha2_Y
                            if (t_X1[0]-t_X3[0])**2 + (t_Y1[0]-t_Y3[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha3_X = - Alpha3_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha3_Y = - Alpha3_Y
                            if (t_X1[0]-t_X4[0])**2 + (t_Y1[0]-t_Y4[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha4_X = - Alpha4_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha4_Y = - Alpha4_Y
                            if (t_X1[0]-t_X5[0])**2 + (t_Y1[0]-t_Y5[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha5_X = - Alpha5_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha5_Y = - Alpha5_Y
                            if (t_X1[0]-t_X6[0])**2 + (t_Y1[0]-t_Y6[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha6_X = - Alpha6_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha6_Y = - Alpha6_Y
                            if (t_X1[0]-t_X7[0])**2 + (t_Y1[0]-t_Y7[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha7_X = - Alpha7_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha7_Y = - Alpha7_Y
                            if (t_X1[0]-t_X8[0])**2 + (t_Y1[0]-t_Y8[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha8_X = - Alpha8_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X1[0]-t_X9[0])**2 + (t_Y1[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha9_X = - Alpha9_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X1[0]-t_X10[0])**2 + (t_Y1[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha1_X = - Alpha1_X
                                Alpha10_X = - Alpha10_X
                                Alpha1_Y = - Alpha1_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X2[0]-t_X3[0])**2 + (t_Y2[0]-t_Y3[0])**2 <=distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha3_X = - Alpha3_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha3_Y = - Alpha3_Y
                            if (t_X2[0]-t_X3[0])**2 + (t_Y2[0]-t_Y3[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha3_X = - Alpha3_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha3_Y = - Alpha3_Y
                            if (t_X2[0]-t_X4[0])**2 + (t_Y2[0]-t_Y4[0])**2 <=distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha4_X = - Alpha4_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha4_Y = - Alpha4_Y
                            if (t_X2[0]-t_X5[0])**2 + (t_Y2[0]-t_Y5[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha5_X = - Alpha5_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha5_Y = - Alpha5_Y
                            if (t_X2[0]-t_X6[0])**2 + (t_Y2[0]-t_Y6[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha6_X = - Alpha6_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha6_Y = - Alpha6_Y
                            if (t_X2[0]-t_X7[0])**2 + (t_Y2[0]-t_Y7[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha7_X = - Alpha7_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha7_Y = - Alpha7_Y
                            if (t_X2[0]-t_X8[0])**2 + (t_Y2[0]-t_Y8[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha8_X = - Alpha8_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X2[0]-t_X9[0])**2 + (t_Y2[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha9_X = - Alpha9_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X2[0]-t_X10[0])**2 + (t_Y2[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha2_X = - Alpha2_X
                                Alpha10_X = - Alpha10_X
                                Alpha2_Y = - Alpha2_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X3[0]-t_X4[0])**2 + (t_Y3[0]-t_Y4[0])**2 <= distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha4_X = - Alpha4_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha4_Y = - Alpha4_Y
                            if (t_X3[0]-t_X5[0])**2 + (t_Y3[0]-t_Y5[0])**2 <= distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha5_X = - Alpha5_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha5_Y = - Alpha5_Y
                            if (t_X3[0]-t_X6[0])**2 + (t_Y3[0]-t_Y6[0])**2 <= distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha6_X = - Alpha6_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha6_Y = - Alpha6_Y
                            if (t_X3[0]-t_X7[0])**2 + (t_Y3[0]-t_Y7[0])**2 <= distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha7_X = - Alpha7_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha7_Y = - Alpha7_Y
                            if (t_X3[0]-t_X8[0])**2 + (t_Y3[0]-t_Y8[0])**2 <= distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha8_X = - Alpha8_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X3[0]-t_X9[0])**2 + (t_Y3[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha9_X = - Alpha9_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X3[0]-t_X10[0])**2 + (t_Y3[0]-t_Y10[0])**2 <=distance_collision:
                                Alpha3_X = - Alpha3_X
                                Alpha10_X = - Alpha10_X
                                Alpha3_Y = - Alpha3_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X4[0]-t_X5[0])**2 + (t_Y4[0]-t_Y5[0])**2 <=distance_collision:
                                Alpha4_X = - Alpha4_X
                                Alpha5_X = - Alpha5_X
                                Alpha4_Y = - Alpha4_Y
                                Alpha5_Y = - Alpha5_Y
                            if (t_X4[0]-t_X6[0])**2 + (t_Y4[0]-t_Y6[0])**2 <= distance_collision:
                                Alpha4_X = - Alpha4_X
                                Alpha6_X = - Alpha6_X
                                Alpha4_Y = - Alpha4_Y
                                Alpha6_Y = - Alpha6_Y
                            if (t_X4[0]-t_X7[0])**2 + (t_Y4[0]-t_Y7[0])**2 <=distance_collision:
                                Alpha4_X = - Alpha4_X
                                Alpha7_X = - Alpha7_X
                                Alpha4_Y = - Alpha4_Y
                                Alpha7_Y = - Alpha7_Y
                            if (t_X4[0]-t_X8[0])**2 + (t_Y4[0]-t_Y8[0])**2 <= distance_collision:
                                Alpha4_X = - Alpha4_X
                                Alpha8_X = - Alpha8_X
                                Alpha4_Y = - Alpha4_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X4[0]-t_X9[0])**2 + (t_Y4[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha4_X = - Alpha4_X
                                Alpha9_X = - Alpha9_X
                                Alpha4_Y = - Alpha4_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X4[0]-t_X10[0])**2 + (t_Y4[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha4_X = - Alpha4_X
                                Alpha10_X = - Alpha10_X
                                Alpha4_Y = - Alpha4_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X5[0]-t_X6[0])**2 + (t_Y5[0]-t_Y6[0])**2 <= distance_collision:
                                Alpha5_X = - Alpha5_X
                                Alpha6_X = - Alpha6_X
                                Alpha5_Y = - Alpha5_Y
                                Alpha6_Y = - Alpha6_Y
                            if (t_X5[0]-t_X7[0])**2 + (t_Y5[0]-t_Y7[0])**2 <=distance_collision:
                                Alpha5_X = - Alpha5_X
                                Alpha7_X = - Alpha7_X
                                Alpha5_Y = - Alpha5_Y
                                Alpha7_Y = - Alpha7_Y
                            if (t_X5[0]-t_X8[0])**2 + (t_Y5[0]-t_Y8[0])**2 <=distance_collision:
                                Alpha5_X = - Alpha5_X
                                Alpha8_X = - Alpha8_X
                                Alpha5_Y = - Alpha5_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X5[0]-t_X9[0])**2 + (t_Y5[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha5_X = - Alpha5_X
                                Alpha9_X = - Alpha9_X
                                Alpha5_Y = - Alpha5_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X5[0]-t_X10[0])**2 + (t_Y5[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha5_X = - Alpha5_X
                                Alpha10_X = - Alpha10_X
                                Alpha5_Y = - Alpha5_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X6[0]-t_X7[0])**2 + (t_Y6[0]-t_Y7[0])**2 <= distance_collision:
                                Alpha6_X = - Alpha6_X
                                Alpha7_X = - Alpha7_X
                                Alpha6_Y = - Alpha6_Y
                                Alpha7_Y = - Alpha7_Y
                            if (t_X6[0]-t_X8[0])**2 + (t_Y6[0]-t_Y8[0])**2 <= distance_collision:
                                Alpha6_X = - Alpha6_X
                                Alpha8_X = - Alpha8_X
                                Alpha6_Y = - Alpha6_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X6[0]-t_X9[0])**2 + (t_Y6[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha6_X = - Alpha6_X
                                Alpha9_X = - Alpha9_X
                                Alpha6_Y = - Alpha6_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X6[0]-t_X10[0])**2 + (t_Y6[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha6_X = - Alpha6_X
                                Alpha10_X = - Alpha10_X
                                Alpha6_Y = - Alpha6_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X7[0]-t_X8[0])**2 + (t_Y7[0]-t_Y8[0])**2 <=distance_collision:
                                Alpha7_X = - Alpha7_X
                                Alpha8_X = - Alpha8_X
                                Alpha7_Y = - Alpha7_Y
                                Alpha8_Y = - Alpha8_Y
                            if (t_X7[0]-t_X9[0])**2 + (t_Y7[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha7_X = - Alpha7_X
                                Alpha9_X = - Alpha9_X
                                Alpha7_Y = - Alpha7_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X7[0]-t_X10[0])**2 + (t_Y7[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha7_X = - Alpha7_X
                                Alpha10_X = - Alpha10_X
                                Alpha7_Y = - Alpha7_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X8[0]-t_X9[0])**2 + (t_Y8[0]-t_Y9[0])**2 <= distance_collision:
                                Alpha8_X = - Alpha8_X
                                Alpha9_X = - Alpha9_X
                                Alpha8_Y = - Alpha8_Y
                                Alpha9_Y = - Alpha9_Y
                            if (t_X8[0]-t_X10[0])**2 + (t_Y8[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha8_X = - Alpha8_X
                                Alpha10_X = - Alpha10_X
                                Alpha8_Y = - Alpha8_Y
                                Alpha10_Y = - Alpha10_Y
                            if (t_X9[0]-t_X10[0])**2 + (t_Y9[0]-t_Y10[0])**2 <= distance_collision:
                                Alpha9_X = - Alpha9_X
                                Alpha10_X = - Alpha10_X
                                Alpha9_Y = - Alpha9_Y
                                Alpha10_Y = - Alpha10_Y
                            
                        # These lines are needed only to test flashes
                        #    if col_1[1] == 'black':
                        #        one.color = 'black'
                        #    else:
                        #        one.color = 'white'
                        #        
                        #    if  col_2[1] == 'black':
                        #        two.color = 'black'
                        #    else:
                        #        two.color = 'white'
                        #        
                        #    if  col_3[1] == 'black':
                        #        three.color = 'black'
                        #    else:
                        #        three.color = 'white'
                        #        
                        #    if  col_4[1] == 'black':
                        #        four.color = 'black'
                        #    else:
                        #        four.color = 'white'
                        #        
                        #    if  col_5[1] == 'black':
                        #        five.color = 'black'
                        #    else:
                        #        five.color = 'white'
                        #        
                        #    if  col_6[1] == 'black':
                        #        six.color = 'black'
                        #    else:
                        #        six.color = 'white'
                        #        
                        #    if  col_7[1] == 'black':
                        #        seven.color = 'black'
                        #    else:
                        #        seven.color = 'white'
                        #        
                        #    if col_8[1] == 'black':
                        #        eight.color = 'black'
                        #    else:
                        #        eight.color = 'white'
                        #        
                        #    if  col_9[1] == 'black':
                        #        nine.color = 'black'
                        #    else:
                        #        nine.color = 'white'
                        #        
                        #    if  col_10[1] == 'black':
                        #        ten.color = 'black'
                        #    else:
                        #        ten.color = 'white'
                        #   
                            
                            # All moving objects will be white
                            one.color = col_1[0]
                            two.color = col_2[0]
                            three.color = col_3[0]
                            four.color = col_4[0]
                            five.color = col_5[0]
                            six.color = col_6[0]
                            seven.color = col_7[0]
                            eight.color = col_8[0]
                            nine.color = col_9[0]
                            ten.color = col_10[0]
                            
                            # Set stimuli coordinates
                            one_sq.setPos([t_X1[0], t_Y1[0]])
                            two_sq.setPos([t_X2[0], t_Y2[0]])
                            three_sq.setPos([t_X3[0], t_Y3[0]])
                            four_sq.setPos([t_X4[0], t_Y4[0]])
                            five_sq.setPos([t_X5[0], t_Y5[0]])
                            six_sq.setPos([t_X6[0], t_Y6[0]])
                            seven_sq.setPos([t_X7[0], t_Y7[0]])
                            eight_sq.setPos([t_X8[0], t_Y8[0]])
                            nine_sq.setPos([t_X9[0], t_Y9[0]])
                            ten_sq.setPos([t_X10[0], t_Y10[0]])
                            
                            one.setPos([t_X1[0], t_Y1[0]])
                            two.setPos([t_X2[0], t_Y2[0]])
                            three.setPos([t_X3[0], t_Y3[0]])
                            four.setPos([t_X4[0], t_Y4[0]])
                            five.setPos([t_X5[0], t_Y5[0]])
                            six.setPos([t_X6[0], t_Y6[0]])
                            seven.setPos([t_X7[0], t_Y7[0]])
                            eight.setPos([t_X8[0], t_Y8[0]])
                            nine.setPos([t_X9[0], t_Y9[0]])
                            ten.setPos([t_X10[0], t_Y10[0]])
                            
                            sq1.setPos([pos_1[0][0], pos_1[1][0]])
                            sq2.setPos([pos_2[0][0], pos_2[1][0]])
                            sq3.setPos([pos_3[0][0], pos_3[1][0]])
                            sq4.setPos([pos_4[0][0], pos_4[1][0]])
                            
                            if motion_t >= rand_time_square1 and motion_t <= (rand_time_square1 + 0.83):                      # If it is the frist flash time
                                sq1.size = ((round(0.6*one_deg_in_pix)*2), (round(0.6*one_deg_in_pix)*2))                     # Increase the size of flash-square (it will overlap the cross); 0.6 is a value from the paper
                                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_1[0][0], pos_1[1][0]]:   # If it is target-flash
                                    # print('target')                                                                        # (This line just for testing)
                                    trials.addData('target_sq_time', rand_time_square1)                                      # Add target-falsh time for this trial
                            else:                                                                                            #
                                sq1.size = (0.1, 0.1)                                                                        # keep small size of the square flash if it is not this flash time
                            
                            if motion_t >= rand_time_square2 and motion_t <= (rand_time_square2+ 0.83):
                                sq2.size = ((round(0.6*one_deg_in_pix)*2), (round(0.6*one_deg_in_pix)*2))
                                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_2[0][0], pos_2[1][0]]:
                                   # print('target')
                                    trials.addData('target_sq_time', rand_time_square2) 
                            else:
                                sq2.size = (0.1, 0.1)
                            
                            if motion_t >= rand_time_square3 and motion_t <= (rand_time_square3 + 0.83):
                                sq3.size = ((round(0.6*one_deg_in_pix)*2), (round(0.6*one_deg_in_pix)*2))
                                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_3[0][0], pos_3[1][0]]:
                                   # print('target')
                                    trials.addData('target_sq_time', rand_time_square3) 
                            else:
                                sq3.size = (0.1, 0.1)
                                
                            if motion_t >= rand_time_square4 and motion_t <= (rand_time_square4 + 0.83):
                                sq4.size = ((round(0.6*one_deg_in_pix)*2), (round(0.6*one_deg_in_pix)*2))
                                if [thisTrial_target_coor[0][0],thisTrial_target_coor[1][0]] == [pos_4[0][0], pos_4[1][0]]:
                                   # print('target')
                                    trials.addData('target_sq_time', rand_time_square4) 
                            else:
                                sq4.size = (0.1, 0.1)
                           
                           # It is needed to press 't' for target-flash
                            keys = event.getKeys(['t'])
                           
                           # If 't' is pressed, break the loop
                            if 't' in keys:
                                trials.addData('keys', keys)
                                trials.addData('key_time_resp', motion_t) 
                                trials.addData('sq_1_start', rand_time_square1)
                                trials.addData('sq_2_start', rand_time_square2)
                                trials.addData('sq_3_start', rand_time_square3)
                                trials.addData('sq_4_start', rand_time_square4)
                                
                                if thisTrial <  (trial_numb + num_eye_moves):
                                    press_space = visual.TextStim(win, text=u"Press space", height = 20)
                                    press_space.draw()
                                    win.flip()
                                    event.waitKeys(keyList=['space'])
                                break
                                
                                # If nothing is pressed or there is eye movement
                            else:
                                trials.addData('keys', '-')
                                trials.addData('key_time_resp','-')
                                trials.addData('sq_1_start', rand_time_square1)
                                trials.addData('sq_2_start', rand_time_square2)
                                trials.addData('sq_3_start', rand_time_square3)
                                trials.addData('sq_4_start', rand_time_square4)
                            
                            # If t is not pressed, motion_t < mot_dur and there is not eye movement, draw stimuli
                            fix.draw()
                            
                            one_sq.draw()
                            two_sq.draw()
                            three_sq.draw()
                            four_sq.draw()
                            five_sq.draw()
                            six_sq.draw()
                            seven_sq.draw()
                            eight_sq.draw()
                            nine_sq.draw()
                            ten_sq.draw()
                            
                            sq1.draw()
                            sq2.draw()
                            sq3.draw()
                            sq4.draw()
                            
                            one.draw()
                            two.draw()
                            three.draw()
                            four.draw()
                            five.draw()
                            six.draw()
                            seven.draw()
                            eight.draw()
                            nine.draw()
                            ten.draw()
                            
                            win.flip()
                            
                    # break everything (several nested loops) and go to the next trial
                    else: 
                        continue
                    break
                else:
                    continue
                break

# save data
    trials.saveAsExcel( IDname + '.xlsx', sheetName='trials')
win.close()


