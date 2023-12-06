#hengu-s
#AAG
#Officially started on December 5, 2023

import pyautogui
#import os
from pynput import *
import time
import random

                                  
'''                                 #the following is used for cursor troubleshooting
                                    #and not needed to run program if all is well
def get_coords(x, y):
     print("Now at: {}".format((x, y)))
     
with mouse.Listener(on_move = get_coords) as listen:
    listen.join()
'''

def main():
    pyautogui.PAUSE = 40 #waits 40 seconds before clicking a button
    
    allFunc() #calls the function to start up program
    
def allFunc(): #plays all the functions in 40 sec intervals
        playButFunc() 
        end1Func()
        end2Func()
        end3Func()
        end4Func()
        end5Func()
        finalFunc()
        collectFunc()
        nextFunc()
        time.sleep(random.randint(15, 30)) #should create a random time where it waits
        allFunc() #creates an infinite loop to have it automated
        
def playButFunc():
    #global x = 0
    #while x != 1:
    playBut = pyautogui.locateCenterOnScreen("play.PNG", confidence=.55) #grabs the png and clicks it
    pyautogui.click(playBut, duration=.5)
        #x += 1
    
def end1Func():
    end1 = pyautogui.locateCenterOnScreen("end1.PNG", confidence=.55)
    pyautogui.click(end1, duration=.5)

def end2Func():
    end2 = pyautogui.locateCenterOnScreen("end2.PNG", confidence=.55)
    pyautogui.click(end2, duration=.5)
    
def end3Func():
    end3 = pyautogui.locateCenterOnScreen("end3.PNG", confidence=.55)
    pyautogui.click(end3, duration=.5)
    
def end4Func():
    end4 = pyautogui.locateCenterOnScreen("end4.PNG", confidence=.55)
    pyautogui.click(end4, duration=.5)
    
def end5Func():
    end5 = pyautogui.locateCenterOnScreen("end5.PNG", confidence=.55)
    pyautogui.click(end5, duration=.5)
    
def finalFunc():
    final = pyautogui.locateCenterOnScreen("finalTurn.PNG", confidence=.55)
    pyautogui.click(final, duration=.5)
    
def collectFunc():
    collect = pyautogui.locateCenterOnScreen("collectRewards.PNG", confidence=.55)
    pyautogui.click(collect, duration=.5)
    
def nextFunc():
    nextBut = pyautogui.locateCenterOnScreen("next.PNG", confidence=.55)
    pyautogui.click(nextBut, duration=.75)

'''
def magikFunc1():
    fourOuttaSeven = pyautogui.locateCenterOnScreen("4_7.PNG", confidence=.5)
    pyautogui.click(fourOuttaSeven, duration=.5)
    
def magikFunc2():
    fiveOuttaSeven = pyautogui.locateCenterOnScreen("5_7.PNG", confidence=.5)
    pyautogui.click(fiveOuttaSeven, duration=.5)
    
def magikFunc3():
    sixOuttaSeven = pyautogui.locateCenterOnScreen("6_7.PNG", confidence=.5)
    pyautogui.click(sixOuttaSeven, duration=.5)
'''
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
