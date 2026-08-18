# cthm3f460

## Environment configuration

Ubuntu 18.04.6 LTS  
Python 3.6.9  
ROS melodic 1.14.13  

copy **crt_cthm3f460_gripper_visualization** to the src folder of your own Ubuntu system ROS workspace and execute the following statement

## Run

### 1. After connecting robot, make sure there is a USB port in Ubuntu  
  Input in terminal:
  `ls -l /dev/ttyUSB* `   
  Confirm the device serial port number and add permissions.
  `sudo chmod 777 /dev/ttyUSB0`


### 2. Update ROS envirnment 
Input in terminal:
```sh
cd ~/ws_catkin

catkin_make
```

### 3. Start Rviz node  

```sh
# If you want to use the function, input in terminal:
cd ./src/crt_cthm3f460_gripper_visualization

# use asynchronous fucntion
roslaunch crt_cthm3f460_gripper_visualization display_async.launch

# use synchronous fucntion
roslaunch crt_cthm3f460_gripper_visualization display_sync.launch

```

After inputting,Rviz interface will come out:

![image-1](asserts/001.png#pic_center)
<center>Figure1 cthm3f460 rviz interface</center>  
  
  
![image-2](asserts/004.png#pic_center)

<center>Figure2 joint state publisher asynchronous interface</center>

![image-3](asserts/002.png#pic_center)

<center>Figure3 joint state publisher synchronous  interface</center>

If warning coming out like <font color="red">**Could not find the GUI, install the 'joint_state_publisher_gui' package**</font>,need to install other package,input in terminal:  
`sudo apt-get install ros-melodic-joint-state-publisher-gui `

Click the Fixed Frame under Displays on the left side of RViz to change from map to base_link

Click the add button in the lower left corner to add the RobotModel

The robot model is displayed
![image-4](asserts/003.png#pic_center)
<center>Figure4 Robot Model</center>

