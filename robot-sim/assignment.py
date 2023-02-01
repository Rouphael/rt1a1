from __future__ import print_function

import time
from sr.robot import *

print("Start")

list_of_used_golden_tokens = []
list_of_used_silver_tokens = []

a_th = 2.0 # angle threshold
d_th_silver = 0.4 # distance threshold for silver token
d_th_gold = 0.6 # distance threshold for gold token

dist_gold = 100
dist_silver = 100
rot_y = 0
id_gold = 0
id_silver = 0

silver = True # variable for letting the robot know if it has to look for a silver or for a golden marker

R = Robot() # create the robot object

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
    """
    Function to find the closest silver token
    Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
    id (int): id of the token
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
            rot_y=token.rot_y
            id = token.info.code

    if dist==100:
        return -1, -1, -1
    else:
        return dist, rot_y, id


def find_golden_token():
    """
    Function to find the closest golden token
    Returns:
	dist (float): distance of the closest golden token (-1 if no golden token is detected)
	rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
    id (int): id of the token
    """
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
            rot_y=token.rot_y
            id = token.info.code

    if dist==100:
        return -1, -1 ,-1
    else:
        return dist, rot_y, id

def search_for_token():
    """
    Function to make the robot turn in order to find a token
    """
    turn(-10, 1)

def grab_silver_token():
    """
    Function to make the robot grab a token
    """
    global id_silver
    global silver
    if R.grab(): # we try to grab the token
        print("Grabed!")
        list_of_used_silver_tokens.append(id_silver) # we add the id of the token to the list of used tokens
        silver = False # we change the variable silver to False, so that the robot will look for a golden token
        turn(-10, 7) # we turn a bit to the left
    else:
        print("Grab failed.")

def release_token():
    """
    Function to make the robot release a token
    """
    global id_gold
    global silver
    if R.release():
        print("Released!")
        list_of_used_golden_tokens.append(id_gold) # we add the id of the token to the list of used tokens
        silver = True # we change the variable silver to True, so that the robot will look for a silver token
        drive(-50, 0.5) # we go back a bit
    else:
        print("Release failed.")

def go_to_token():
    """
    Function to make the robot go to a token
    """
    if -a_th<= rot_y <= a_th: # if the robot is well aligned with the token
        print("Drive to silver token")
        drive(50, 0.5) # we go forward
    elif rot_y > a_th: # if the token is on the right of the robot
        print("Turning right") 
        turn(+2, 0.5) # we turn a bit to the right
    else: # if the token is on the left of the robot
        print("Turning left")
        turn(-2, 0.5) # we turn a bit to the left
    

while len(list_of_used_golden_tokens) < 6: # while we have not used all the golden tokens
    if silver == True: 
        print("Focused on silver token")
        dist_silver, rot_y, id_silver = find_silver_token()
        if id_silver not in list_of_used_silver_tokens: # if the token has not been used yet
            if dist_silver == -1: # if the output of the function is -1, it means that no token is detected
                print("Searching for silver token")
                search_for_token() # we search for a token
            elif dist_silver <d_th_silver: # if we are close enouph to the token
                print("Close enough to silver token!")
                grab_silver_token() # we try to grab the token
            else: # if we are not close enough to the token
                print("Drive to silver token")
                go_to_token() # we go to the token
        else: # if the token has already been used
            print("Silver token already used searching for another one")
            search_for_token() # we search for another token

    else:
        print("Focused on gold token")
        dist_gold, rot_y, id_gold = find_golden_token()
        if id_gold not in list_of_used_golden_tokens:
            if dist_gold == -1: # if no token is detected, we make the robot turn 
                print("Searching for gold token")
                search_for_token()  # we search for a token
            elif dist_gold < d_th_gold: # if we are close to the token, we try grab it.
                print("close enough to gold token!")
                release_token() # we try to release the token
            else: # if we are not close enough to the token
                print("Drive to gold token")
                go_to_token() # we go to the token
        else: # if the token has already been used
            print("Gold token already used searching for another one")
            search_for_token() # we search for another token

print("All silver tokens have been placed next to the golden tokens")
print("Task completed")