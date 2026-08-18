<img src="https://gw.alipayobjects.com/zos/antfincdn/R8sN%24GNdh6/language.svg" width="18"> English | [简体中文](./README.zh-CN.md)

# Instructions

## Tips
> 1. **Joint-state-publisher-gui** publishing **'/joint_states'** in rviz, We subscribe to this topic through the node to realize the synchronization between the physical device and the model.
> 2. When not using rviz, start the node separately and send the topic **'/joint_states'** to the user through Python code or the terminal command to release messages to realize the control of real device.
> 3.  you can install ros-melodic-state-publisher-gui in the terminal in case of error: can not find **'joint-state-publisher-gui'**
```bash
sudo apt-get install ros-melodic-joint-state-publisher-gui
```

## Environment configuration
1. ubuntu18.04

2. ros-melodic

3. Copy the package **crt-ctm2f110-gripper-visualization** to the src folder of your own Ubuntu system ROS workspace and execute the following statement
```bash
cd ~/catkin_ws/
```
```bash
catkin_make
```
After compiling, execute the following statement：
```bash
source ~/catkin_ws/devel/setup.bash
```

## Run

* Determine the device serial port number and add permissions.
```bash
sudo chmod 777 <your serialport name>
```
such as
```bash
sudo chmod 777 /dev/ttyUSB0
```

* Modify the serial port number in the file 'scripts/gripper_listener.cpp' line 29.
```C++
gs.openSerial(115200, "<your serialport name>")
```

* Using rviz to control the real two-finger-gripper (synchronization mode), drag the gui slider to make the model and the real device move synchronously.
```bash
roslaunch crt_ctm2f110_gripper_visualization crt_ctm2f110_gripper_control_sync.launch
```

* Using rviz to control the real two-finger-gripper (asynchronous mode), drag the gui slider to make the model and the real device move asynchronously.
```bash
roslaunch crt_ctm2f110_gripper_visualization crt_ctm2f110_gripper_control_async.launch
```

* Only using rviz to display the URDF model of the two-finger-gripper (synchronization mode), drag the gui slider to make the model move synchronously.
```bash
roslaunch crt_ctm2f110_gripper_visualization crt_ctm2f110_display_sync.launch
```
![sync_mode](./asserts/sync_mode.png)
<center>Figure1 The two-finger-gripper URDF model showed in Rviz(synchronous mode)</center>

* Only using rviz to display the URDF model of the two-finger-gripper (asynchronous mode), drag the gui slider to make one finger of the model move separately.
```bash
roslaunch crt_ctm2f110_gripper_visualization crt_ctm2f110_display_async.launch
```
![async_mode](./asserts/async_mode.png)
<center>Figure2 The two-finger-gripper URDF model showed in Rviz(asynchronous mode)</center>

* Without using rviz, just enable the node, and use Python sample code to control the physical two-finger-gripper
```bash
roslaunch crt_ctm2f110_gripper_visualization crt_ctm2f110_gripper_node.launch
```
At this time, open another terminal and run:
```bash
rosrun crt_ctm2f110_gripper_visualization gripper_move.py
```
As the Python code will always be sent, you can use the key of Ctrl + Z to stop the program.

* Without using rviz, just enable the node, input commands in the terminal to control the two fingered hand:
```bash
roslaunch crt_ctm2f110_gripper_visualization crt_ctm2f110_gripper_node.launch
```
At this time, open another terminal and run:
example 1:
```bash
rostopic pub --once /joint_states sensor_msgs/JointState '{header: auto, name: ['leftout_joint','left_kckle_joint','leftinn_joint','rightout_joint','right_kckle_joint','rightinn_joint'], position:[0,0,0,0,0,0]}'
```
example 2:
```bash
rostopic pub --once /joint_states sensor_msgs/JointState '{header: auto, name: ['leftout_joint','left_kckle_joint','leftinn_joint','rightout_joint','right_kckle_joint','rightinn_joint'], position:[0.5,0.5,-0.5,0.5,0.5,-0.5]}'
```
example 3:
```bash
rostopic pub --once /joint_states sensor_msgs/JointState '{header: auto, name: ['leftout_joint','left_kckle_joint','leftinn_joint','rightout_joint','right_kckle_joint','rightinn_joint'], position:[1,1,-1,1,1,-1]}'
```
