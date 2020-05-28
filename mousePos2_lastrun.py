#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on May 28, 2020, at 15:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'mousePos2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\mousePosTest2\\mousePos2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='Use your mouse to move the cursor between the middle start position and the outward targets.\n\nAlways try to move as straight and smooth as possible. Once you settle into your pace, do not slow down: whenever you make an error, just do better on the next trial. Pace is key.\n\nPress SPACE to start!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr1Resp = keyboard.Keyboard()

# Initialize components for Routine "fixation1"
fixation1Clock = core.Clock()
fix1 = visual.TextStim(win=win, name='fix1',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
trial1Mouse = event.Mouse(win=win)
x, y = [None, None]
trial1Mouse.mouseClock = core.Clock()
win.mouseVisible = False

# psychoJS.window

targetAngles = [30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60]
#targetAngles = [(t/180)*pi for t in targetAngles]

#mouse = event.Mouse(visible = False)
#mouse = new psychoJS.event.Mouse({"visible": false});


# document.getElementById('hide_id').style.cursor = 'none';
# document.documentElement.style.cursor = 'none';

trial1Target = visual.Polygon(
    win=win, name='trial1Target',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trial1Home = visual.Polygon(
    win=win, name='trial1Home',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trial1Cursor = visual.Polygon(
    win=win, name='trial1Cursor',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trial1Step
trial1Step = 0
trial1StepContainer = []
trial1Num = visual.TextStim(win=win, name='trial1Num',
    text='45',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trial1Skip = keyboard.Keyboard()

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
instr2 = visual.TextStim(win=win, name='instr2',
    text='Next trials coming.\n\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr2Resp = keyboard.Keyboard()

# Initialize components for Routine "fixation2"
fixation2Clock = core.Clock()
fix2 = visual.TextStim(win=win, name='fix2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
trial2Mouse = event.Mouse(win=win)
x, y = [None, None]
trial2Mouse.mouseClock = core.Clock()
win.mouseVisible = False

# psychoJS.window

targetAngles = [30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60]
#targetAngles = [(t/180)*pi for t in targetAngles]

#mouse = event.Mouse(visible = False)
#mouse = new psychoJS.event.Mouse({"visible": false});


# document.getElementById('hide_id').style.cursor = 'none';
# document.documentElement.style.cursor = 'none';

trial2Target = visual.Polygon(
    win=win, name='trial2Target',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trial2Home = visual.Polygon(
    win=win, name='trial2Home',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trial2Cursor = visual.Polygon(
    win=win, name='trial2Cursor',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trial2Step
trial2Step = 0
trial2StepContainer = []
trial2Num = visual.TextStim(win=win, name='trial2Num',
    text='45',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "end"
endClock = core.Clock()
thanks = visual.TextStim(win=win, name='thanks',
    text='Thanks',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
instr1Resp.keys = []
instr1Resp.rt = []
_instr1Resp_allKeys = []
# keep track of which components have finished
instructions1Components = [instr1, instr1Resp]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1.frameNStart = frameN  # exact frame index
        instr1.tStart = t  # local t and not account for scr refresh
        instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
        instr1.setAutoDraw(True)
    
    # *instr1Resp* updates
    waitOnFlip = False
    if instr1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr1Resp.frameNStart = frameN  # exact frame index
        instr1Resp.tStart = t  # local t and not account for scr refresh
        instr1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr1Resp, 'tStartRefresh')  # time at next scr refresh
        instr1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr1Resp.status == STARTED and not waitOnFlip:
        theseKeys = instr1Resp.getKeys(keyList=['space'], waitRelease=False)
        _instr1Resp_allKeys.extend(theseKeys)
        if len(_instr1Resp_allKeys):
            instr1Resp.keys = _instr1Resp_allKeys[-1].name  # just the last key pressed
            instr1Resp.rt = _instr1Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr1.started', instr1.tStartRefresh)
thisExp.addData('instr1.stopped', instr1.tStopRefresh)
# check responses
if instr1Resp.keys in ['', [], None]:  # No response was made
    instr1Resp.keys = None
thisExp.addData('instr1Resp.keys',instr1Resp.keys)
if instr1Resp.keys != None:  # we had a response
    thisExp.addData('instr1Resp.rt', instr1Resp.rt)
thisExp.addData('instr1Resp.started', instr1Resp.tStartRefresh)
thisExp.addData('instr1Resp.stopped', instr1Resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation1"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation1Components = [fix1]
for thisComponent in fixation1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix1* updates
    if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix1.frameNStart = frameN  # exact frame index
        fix1.tStart = t  # local t and not account for scr refresh
        fix1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
        fix1.setAutoDraw(True)
    if fix1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix1.tStop = t  # not accounting for scr refresh
            fix1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix1, 'tStopRefresh')  # time at next scr refresh
            fix1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation1"-------
for thisComponent in fixation1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix1.started', fix1.tStartRefresh)
thisExp.addData('fix1.stopped', fix1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials1 = data.TrialHandler(nReps=45, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials1')
thisExp.addLoop(trials1)  # add the loop to the experiment
thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
if thisTrials1 != None:
    for paramName in thisTrials1:
        exec('{} = thisTrials1[paramName]'.format(paramName))

for thisTrials1 in trials1:
    currentLoop = trials1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the trial1Mouse
    trial1Mouse.x = []
    trial1Mouse.y = []
    trial1Mouse.leftButton = []
    trial1Mouse.midButton = []
    trial1Mouse.rightButton = []
    trial1Mouse.time = []
    gotValidClick = False  # until a click is received
    trial1Mouse.mouseClock.reset()
    targetangle = targetAngles[trials1.thisN]
    targetangle_rad = pi*(targetangle/180)
    targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
    
    # Math.PI
    # Math.cos()
    # Math.sin()
    
    targetOpacity = 0
    homeOpacity = 0
    
    homeStart = False
    reachOut = False
    
    trial1Step = 1
    steps = []
    
    #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
    trial1Num.text = str(trials1.thisN+1)
    
    trial1Cursor.pos = (.5,.5)
    trial1Mouse.pos = (.5,.5)
    trial1Skip.keys = []
    trial1Skip.rt = []
    _trial1Skip_allKeys = []
    # keep track of which components have finished
    trial1Components = [trial1Mouse, trial1Target, trial1Home, trial1Cursor, trial1Num, trial1Skip]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *trial1Mouse* updates
        if trial1Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Mouse.frameNStart = frameN  # exact frame index
            trial1Mouse.tStart = t  # local t and not account for scr refresh
            trial1Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Mouse, 'tStartRefresh')  # time at next scr refresh
            trial1Mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if trial1Mouse.status == STARTED:  # only update if started and not finished!
            x, y = trial1Mouse.getPos()
            trial1Mouse.x.append(x)
            trial1Mouse.y.append(y)
            buttons = trial1Mouse.getPressed()
            trial1Mouse.leftButton.append(buttons[0])
            trial1Mouse.midButton.append(buttons[1])
            trial1Mouse.rightButton.append(buttons[2])
            trial1Mouse.time.append(trial1Mouse.mouseClock.getTime())
        CursorTargetDistance = sqrt((trial1Cursor.pos[0]-trial1Target.pos[0])**2 + (trial1Cursor.pos[1]-trial1Target.pos[1])**2)
        CursorHomeDistance = sqrt(trial1Cursor.pos[0]**2 + trial1Cursor.pos[1]**2)
        
        steps.append(trial1Step)
        # steps.push(step)
        
        if not(homeStart):
            homeOpacity = 1
            targetOpacity = 0
            trial1Step = 1
            if (CursorHomeDistance < .025):
                homeStart = True
                print('end step 1'+' ('+str(globalClock.getTime())+')')
        
        if (not(reachOut) and homeStart):
            homeOpacity = 0
            targetOpacity = 1
            trial1Step = 2
            if (CursorTargetDistance < .025):
                reachOut = True
                print('end step 2'+' ('+str(globalClock.getTime())+')')
        
        if (reachOut):
            homeOpacity = 1
            targetOpacity = 0
            trial1Step = 3
            if (CursorHomeDistance < .025):
                # maybe this ends the loop prematurely?
                print('end step 3'+' ('+str(globalClock.getTime())+')')
                continueRoutine = False
                
        #steps = steps.append(step)
        
        # *trial1Target* updates
        if trial1Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Target.frameNStart = frameN  # exact frame index
            trial1Target.tStart = t  # local t and not account for scr refresh
            trial1Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Target, 'tStartRefresh')  # time at next scr refresh
            trial1Target.setAutoDraw(True)
        if trial1Target.status == STARTED:  # only update if drawing
            trial1Target.setOpacity(targetOpacity, log=False)
            trial1Target.setPos(targetPos, log=False)
        
        # *trial1Home* updates
        if trial1Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Home.frameNStart = frameN  # exact frame index
            trial1Home.tStart = t  # local t and not account for scr refresh
            trial1Home.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Home, 'tStartRefresh')  # time at next scr refresh
            trial1Home.setAutoDraw(True)
        if trial1Home.status == STARTED:  # only update if drawing
            trial1Home.setOpacity(homeOpacity, log=False)
        
        # *trial1Cursor* updates
        if trial1Cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Cursor.frameNStart = frameN  # exact frame index
            trial1Cursor.tStart = t  # local t and not account for scr refresh
            trial1Cursor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Cursor, 'tStartRefresh')  # time at next scr refresh
            trial1Cursor.setAutoDraw(True)
        if trial1Cursor.status == STARTED:  # only update if drawing
            trial1Cursor.setPos((trial1Mouse.getPos()[0], trial1Mouse.getPos()[1]), log=False)
        
        # *trial1Num* updates
        if trial1Num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Num.frameNStart = frameN  # exact frame index
            trial1Num.tStart = t  # local t and not account for scr refresh
            trial1Num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Num, 'tStartRefresh')  # time at next scr refresh
            trial1Num.setAutoDraw(True)
        
        # *trial1Skip* updates
        waitOnFlip = False
        if trial1Skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial1Skip.frameNStart = frameN  # exact frame index
            trial1Skip.tStart = t  # local t and not account for scr refresh
            trial1Skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial1Skip, 'tStartRefresh')  # time at next scr refresh
            trial1Skip.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trial1Skip.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trial1Skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trial1Skip.status == STARTED and not waitOnFlip:
            theseKeys = trial1Skip.getKeys(keyList=['space'], waitRelease=False)
            _trial1Skip_allKeys.extend(theseKeys)
            if len(_trial1Skip_allKeys):
                trial1Skip.keys = _trial1Skip_allKeys[-1].name  # just the last key pressed
                trial1Skip.rt = _trial1Skip_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials1 (TrialHandler)
    trials1.addData('trial1Mouse.x', trial1Mouse.x)
    trials1.addData('trial1Mouse.y', trial1Mouse.y)
    trials1.addData('trial1Mouse.leftButton', trial1Mouse.leftButton)
    trials1.addData('trial1Mouse.midButton', trial1Mouse.midButton)
    trials1.addData('trial1Mouse.rightButton', trial1Mouse.rightButton)
    trials1.addData('trial1Mouse.time', trial1Mouse.time)
    trials1.addData('trial1Mouse.started', trial1Mouse.tStartRefresh)
    trials1.addData('trial1Mouse.stopped', trial1Mouse.tStopRefresh)
    # thisExp.addData('step', stepvector)
    thisExp.addData('step', steps)
    thisExp.addData('targetangle_deg', targetangle)
    
    # psychoJS.experiment.addData('columnName', variable)
    #psychoJS.experiment.addData('step', steps)
    #psychoJS.experiment.addData('targetangle_deg', targetangle)
    trials1.addData('trial1Target.started', trial1Target.tStartRefresh)
    trials1.addData('trial1Target.stopped', trial1Target.tStopRefresh)
    trials1.addData('trial1Home.started', trial1Home.tStartRefresh)
    trials1.addData('trial1Home.stopped', trial1Home.tStopRefresh)
    trials1.addData('trial1Cursor.started', trial1Cursor.tStartRefresh)
    trials1.addData('trial1Cursor.stopped', trial1Cursor.tStopRefresh)
    trials1.addData('trial1Num.started', trial1Num.tStartRefresh)
    trials1.addData('trial1Num.stopped', trial1Num.tStopRefresh)
    # check responses
    if trial1Skip.keys in ['', [], None]:  # No response was made
        trial1Skip.keys = None
    trials1.addData('trial1Skip.keys',trial1Skip.keys)
    if trial1Skip.keys != None:  # we had a response
        trials1.addData('trial1Skip.rt', trial1Skip.rt)
    trials1.addData('trial1Skip.started', trial1Skip.tStartRefresh)
    trials1.addData('trial1Skip.stopped', trial1Skip.tStopRefresh)
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 45 repeats of 'trials1'


# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
instr2Resp.keys = []
instr2Resp.rt = []
_instr2Resp_allKeys = []
# keep track of which components have finished
instructions2Components = [instr2, instr2Resp]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2* updates
    if instr2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2.frameNStart = frameN  # exact frame index
        instr2.tStart = t  # local t and not account for scr refresh
        instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2, 'tStartRefresh')  # time at next scr refresh
        instr2.setAutoDraw(True)
    
    # *instr2Resp* updates
    waitOnFlip = False
    if instr2Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2Resp.frameNStart = frameN  # exact frame index
        instr2Resp.tStart = t  # local t and not account for scr refresh
        instr2Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2Resp, 'tStartRefresh')  # time at next scr refresh
        instr2Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr2Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr2Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr2Resp.status == STARTED and not waitOnFlip:
        theseKeys = instr2Resp.getKeys(keyList=['space'], waitRelease=False)
        _instr2Resp_allKeys.extend(theseKeys)
        if len(_instr2Resp_allKeys):
            instr2Resp.keys = _instr2Resp_allKeys[-1].name  # just the last key pressed
            instr2Resp.rt = _instr2Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr2.started', instr2.tStartRefresh)
thisExp.addData('instr2.stopped', instr2.tStopRefresh)
# check responses
if instr2Resp.keys in ['', [], None]:  # No response was made
    instr2Resp.keys = None
thisExp.addData('instr2Resp.keys',instr2Resp.keys)
if instr2Resp.keys != None:  # we had a response
    thisExp.addData('instr2Resp.rt', instr2Resp.rt)
thisExp.addData('instr2Resp.started', instr2Resp.tStartRefresh)
thisExp.addData('instr2Resp.stopped', instr2Resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation2Components = [fix2]
for thisComponent in fixation2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix2* updates
    if fix2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fix2.frameNStart = frameN  # exact frame index
        fix2.tStart = t  # local t and not account for scr refresh
        fix2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fix2, 'tStartRefresh')  # time at next scr refresh
        fix2.setAutoDraw(True)
    if fix2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fix2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            fix2.tStop = t  # not accounting for scr refresh
            fix2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix2, 'tStopRefresh')  # time at next scr refresh
            fix2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation2"-------
for thisComponent in fixation2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix2.started', fix2.tStartRefresh)
thisExp.addData('fix2.stopped', fix2.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials2 = data.TrialHandler(nReps=45, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials2')
thisExp.addLoop(trials2)  # add the loop to the experiment
thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
if thisTrials2 != None:
    for paramName in thisTrials2:
        exec('{} = thisTrials2[paramName]'.format(paramName))

for thisTrials2 in trials2:
    currentLoop = trials2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the trial2Mouse
    trial2Mouse.x = []
    trial2Mouse.y = []
    trial2Mouse.leftButton = []
    trial2Mouse.midButton = []
    trial2Mouse.rightButton = []
    trial2Mouse.time = []
    gotValidClick = False  # until a click is received
    trial2Mouse.mouseClock.reset()
    targetangle = targetAngles[trials2.thisN]
    targetangle_rad = pi*(targetangle/180)
    targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
    
    # Math.PI
    # Math.cos()
    # Math.sin()
    
    targetOpacity = 0
    homeOpacity = 0
    
    homeStart = False
    reachOut = False
    
    trial2Step = 1
    steps = []
    
    #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
    trial2Num.text = str(trials2.thisN+1)
    
    trial2Cursor.pos = (.5,.5)
    trial2Mouse.pos = (.5,.5)
    # keep track of which components have finished
    trial2Components = [trial2Mouse, trial2Target, trial2Home, trial2Cursor, trial2Num]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial2"-------
    while continueRoutine:
        # get current time
        t = trial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *trial2Mouse* updates
        if trial2Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Mouse.frameNStart = frameN  # exact frame index
            trial2Mouse.tStart = t  # local t and not account for scr refresh
            trial2Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Mouse, 'tStartRefresh')  # time at next scr refresh
            trial2Mouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if trial2Mouse.status == STARTED:  # only update if started and not finished!
            x, y = trial2Mouse.getPos()
            trial2Mouse.x.append(x)
            trial2Mouse.y.append(y)
            buttons = trial2Mouse.getPressed()
            trial2Mouse.leftButton.append(buttons[0])
            trial2Mouse.midButton.append(buttons[1])
            trial2Mouse.rightButton.append(buttons[2])
            trial2Mouse.time.append(trial2Mouse.mouseClock.getTime())
        CursorTargetDistance = sqrt((trial2Cursor.pos[0]-trial2Target.pos[0])**2 + (trial2Cursor.pos[1]-trial2Target.pos[1])**2)
        CursorHomeDistance = sqrt(trial2Cursor.pos[0]**2 + trial2Cursor.pos[1]**2)
        
        steps.append(trial2Step)
        # steps.push(step)
        
        if not(homeStart):
            homeOpacity = 1
            targetOpacity = 0
            trial2Step = 1
            if (CursorHomeDistance < .025):
                homeStart = True
                print('end step 1'+' ('+str(globalClock.getTime())+')')
        
        if (not(reachOut) and homeStart):
            homeOpacity = 0
            targetOpacity = 1
            trial2Step = 2
            if (CursorTargetDistance < .025):
                reachOut = True
                print('end step 2'+' ('+str(globalClock.getTime())+')')
        
        if (reachOut):
            homeOpacity = 1
            targetOpacity = 0
            trial2Step = 3
            if (CursorHomeDistance < .025):
                # maybe this ends the loop prematurely?
                print('end step 3'+' ('+str(globalClock.getTime())+')')
                continueRoutine = False
                
        #steps = steps.append(step)
        
        # *trial2Target* updates
        if trial2Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Target.frameNStart = frameN  # exact frame index
            trial2Target.tStart = t  # local t and not account for scr refresh
            trial2Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Target, 'tStartRefresh')  # time at next scr refresh
            trial2Target.setAutoDraw(True)
        if trial2Target.status == STARTED:  # only update if drawing
            trial2Target.setOpacity(targetOpacity, log=False)
            trial2Target.setPos(targetPos, log=False)
        
        # *trial2Home* updates
        if trial2Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Home.frameNStart = frameN  # exact frame index
            trial2Home.tStart = t  # local t and not account for scr refresh
            trial2Home.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Home, 'tStartRefresh')  # time at next scr refresh
            trial2Home.setAutoDraw(True)
        if trial2Home.status == STARTED:  # only update if drawing
            trial2Home.setOpacity(homeOpacity, log=False)
        
        # *trial2Cursor* updates
        if trial2Cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Cursor.frameNStart = frameN  # exact frame index
            trial2Cursor.tStart = t  # local t and not account for scr refresh
            trial2Cursor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Cursor, 'tStartRefresh')  # time at next scr refresh
            trial2Cursor.setAutoDraw(True)
        if trial2Cursor.status == STARTED:  # only update if drawing
            trial2Cursor.setPos((-(trial2Mouse.getPos()[0]), trial2Mouse.getPos()[1]), log=False)
        
        # *trial2Num* updates
        if trial2Num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial2Num.frameNStart = frameN  # exact frame index
            trial2Num.tStart = t  # local t and not account for scr refresh
            trial2Num.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial2Num, 'tStartRefresh')  # time at next scr refresh
            trial2Num.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials2 (TrialHandler)
    trials2.addData('trial2Mouse.x', trial2Mouse.x)
    trials2.addData('trial2Mouse.y', trial2Mouse.y)
    trials2.addData('trial2Mouse.leftButton', trial2Mouse.leftButton)
    trials2.addData('trial2Mouse.midButton', trial2Mouse.midButton)
    trials2.addData('trial2Mouse.rightButton', trial2Mouse.rightButton)
    trials2.addData('trial2Mouse.time', trial2Mouse.time)
    trials2.addData('trial2Mouse.started', trial2Mouse.tStartRefresh)
    trials2.addData('trial2Mouse.stopped', trial2Mouse.tStopRefresh)
    # thisExp.addData('step', stepvector)
    thisExp.addData('step', steps)
    thisExp.addData('targetangle_deg', targetangle)
    
    # psychoJS.experiment.addData('columnName', variable)
    #psychoJS.experiment.addData('step', steps)
    #psychoJS.experiment.addData('targetangle_deg', targetangle)
    trials2.addData('trial2Target.started', trial2Target.tStartRefresh)
    trials2.addData('trial2Target.stopped', trial2Target.tStopRefresh)
    trials2.addData('trial2Home.started', trial2Home.tStartRefresh)
    trials2.addData('trial2Home.stopped', trial2Home.tStopRefresh)
    trials2.addData('trial2Cursor.started', trial2Cursor.tStartRefresh)
    trials2.addData('trial2Cursor.stopped', trial2Cursor.tStopRefresh)
    trials2.addData('trial2Num.started', trial2Num.tStartRefresh)
    trials2.addData('trial2Num.stopped', trial2Num.tStopRefresh)
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 45 repeats of 'trials2'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [thanks]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks.frameNStart = frameN  # exact frame index
        thanks.tStart = t  # local t and not account for scr refresh
        thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
        thanks.setAutoDraw(True)
    if thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            thanks.tStop = t  # not accounting for scr refresh
            thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks, 'tStopRefresh')  # time at next scr refresh
            thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks.started', thanks.tStartRefresh)
thisExp.addData('thanks.stopped', thanks.tStopRefresh)
win.mouseVisible = True

# psychoJS.window.mouseVisible = true;
win.mouseVisible = True

# psychoJS.window.mouseVisible = true;

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
