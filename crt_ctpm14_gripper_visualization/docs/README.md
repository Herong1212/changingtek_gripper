 English | [简体中文](./README.zh-CN.md)

# Instructions

## Tips

> 1. **Joint-state-publisher-gui** publishing **'/joint_states'** in rviz, We subscribe to this topic through the node to realize the synchronization between the physical device and the model.
> 2. you can install ros-melodic-state-publisher-gui in the terminal in case of error: can not find **'joint-state-publisher-gui'**
```bash
sudo apt-get install ros-melodic-joint-state-publisher-gui
```

## Environment configuration
1. ubuntu18.04

2. ros-melodic

3. Copy the package **crt-ctpm14-gripper-visualization** to the src folder in the ROS workspace of  the Ubuntu System and execute the following statement
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

* Using rviz to display the URDF model of the parallel-move gripper. The commands to be executed and the result figure are as follows。
```bash
roslaunch crt_ctpm14_gripper_visualization display.launch
```

![Rviz显示平动手URDF模型](./asserts/ctpm14_display.png)

<center>Figure1  The parallel-move gripper URDF model showed in RViz</center>

* Using rviz to display the URDF model of the parallel-move gripper and draging the gui slider to make the model move synchronously.
```bash
roslaunch crt_ctpm14_gripper_visualization crt_ctpm14_display.launch
```

![Rviz中控制平动手模型运动](./asserts/ctpm14_control.png)

<center>Figure2 Controlling the movement of the parallel-move gripper model in Rviz</center>

