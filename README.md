## rt1a1
Università di Genova/MSc in Robotics Engineering/Research Track 1/1st Assignment

**********************
**********************
**********************
**********************
**********************
# [UNIGE Università di Genova](https://unige.it/it/) , [MSc in Robotics Engineering](https://courses.unige.it/10635) , [Research_Track_1](https://unige.it/en/off.f/2021/ins/51201.html?codcla=10635) , First Assignment
### Professor. [Carmine Recchiuto](https://github.com/CarmineD8)
### Autheor : [Rafael Rabbani](https://github.com/Rouphael)

**********************
**********************
**********************
# 1. Python Robotics Simulator

explenation of this part is written in the [README.md](/robot-sim/README.md) file in the robot-sim folder

**********************
**********************
**********************

# 2. assignment.py
This is a python code for controlling a robot to search for silver tokens, grab, and release them next to golden tokens. The robot uses the sr.robot library, which is a Python library for communicating with a robot.

The code first imports some necessary libraries, including time and sr.robot. The list_of_used_golden_tokens and list_of_used_silver_tokens lists store the IDs of the tokens that the robot has already grabbed.

A set of variables such as dist_gold, dist_silver, rot_y, id_gold, id_silver, and silver are also defined. The angle threshold (a_th) and distance thresholds for silver (d_th_silver) and golden tokens (d_th_gold) are set as well.

The drive and turn functions control the linear and angular velocities of the robot's wheels, respectively. The find_silver_token and find_golden_token functions look for the closest silver and golden tokens, respectively, and return their distances, rotation angles, and IDs. The search_for_token function makes the robot turn to look for tokens. The grab_silver_token function makes the robot grab a silver token, and the release_token function makes the robot release a token. The go_to_token function makes the robot go to a token.
## 2.1 Functions
### 2.1.1 drive
This function sets a linear velocity for the robot's wheels. It takes in two arguments: the speed of the wheels and the time interval for which the speed will be maintained. It sets the power of both motors to the specified speed and then waits for the specified interval, after which it stops the motors.
### 2.1.2 turn
This function sets an angular velocity for the robot's wheels. It takes in two arguments: the speed of the wheels and the time interval for which the speed will be maintained. It sets the power of one motor to the specified speed and the other to the opposite of the speed, and then waits for the specified interval, after which it stops the motors.
### 2.1.3 find_silver_token
This function finds the closest silver token that the robot can see and returns the distance, rotation angle, and id of that token. The function iterates through all the tokens that the robot sees and compares their distances with the current closest token. If a token with a shorter distance is found and its marker type is "silver", the distance, rotation angle, and id of that token are stored. If no silver token is found, the function returns -1, -1, -1.
### 2.1.4 find_golden_token
This function finds the closest golden token that the robot can see and returns the distance, rotation angle, and id of that token. The function iterates through all the tokens that the robot sees and compares their distances with the current closest token. If a token with a shorter distance is found and its marker type is "golden", the distance, rotation angle, and id of that token are stored. If no golden token is found, the function returns -1, -1, -1.
### 2.1.5 search_for_token
This function makes the robot turn to find a token. It sets an angular velocity for the robot's wheels in the opposite direction for 1 second.
### 2.1.6 grab_silver_token
This function makes the robot grab a silver token. If the R.grab method returns True, it means that the token has been successfully grabbed, and the function prints "Grabbed!". The id of the grabbed token is added to the list of used silver tokens, and the silver variable is set to False, indicating that the robot will now look for a golden token. The robot then turns to the left for 7 seconds. If the grab fails, the function prints "Grab failed."
### 2.1.7 release_token
his function makes the robot release a token. If the R.release method returns True, it means that the token has been successfully released, and the function prints "Released!". The id of the released token is added to the list of used golden tokens, and the silver variable is set to True, indicating that the robot will now look for a silver token. The robot then moves backward for 0.5 seconds. If the release fails, the function prints "Release failed."
### 2.1.8 go_to_token
This function makes the robot go to a token. It checks if the rotation angle between the robot and the token is within the specified angle threshold. If the angle is within the threshold, the robot moves forward for 0.5 seconds. If the angle is greater than the threshold, the robot turns in the opposite direction of the angle for an interval proportional to the angle. If the angle is less than the negative of the threshold, the robot turns in the same direction as the angle for an interval proportional to the angle.

## 2.2 Main Code
The code runs a loop until all 6 golden tokens have been used. In each iteration, the code checks if it should focus on silver or golden tokens.
### 2.2.1 Focus on silver token
If it's focused on silver tokens, the code performs the following steps:

1.    It calls the find_silver_token function to get the distance, rotation and ID of the nearest silver token.
2.    If the returned ID of the silver token isn't in the list of used silver tokens, it performs the next steps.
3.    If the distance of the silver token is -1, it means no silver token was detected, so the code calls the search_for_token function.
4.    If the distance of the silver token is less than the defined threshold d_th_silver, the code calls the grab_silver_token function.
5.    If the distance of the silver token is not less than the defined threshold, the code calls the go_to_token function to drive to the silver token.
6.    If the returned ID of the silver token is in the list of used silver tokens, the code skips to step 3 and calls search_for_token.

### 2.2.2 Focus on findig golden token
If it's focused on golden tokens, the code performs the following steps:
1.    It calls the find_golden_token function to get the distance, rotation and ID of the nearest golden token.
2.    If the returned ID of the golden token isn't in the list of used golden tokens, it performs the next steps.
3.    If the distance of the golden token is -1, it means no golden token was detected, so the code calls the search_for_token function.
4.    If the distance of the golden token is less than the defined threshold d_th_gold, the code calls the release_token function.
5.    If the distance of the golden token is not less than the defined threshold, the code calls the go_to_token function to drive to the golden token.
6.    If the returned ID of the golden token is in the list of used golden tokens, the code skips to step 3 and calls search_for_token.

After all golden tokens have been used, the code outputs "All silver tokens have been placed next to the golden tokens" and "Task completed".

# 3. Results
![start](/pic/Screenshot%20from%202023-02-01%2018-25-47.png)

![nearend](/pic/Screenshot%20from%202023-02-01%2018-27-44.png)

![end](/pic/Screenshot%20from%202023-02-01%2018-27-49.png)


