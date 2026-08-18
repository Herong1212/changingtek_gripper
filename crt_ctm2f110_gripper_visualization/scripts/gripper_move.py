#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import time

def talker():
    print("move start")
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher_gui')
    rate = rospy.Rate(10) # 10hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['finger_joint','left_kckle_joint','leftinn_joint','rightout_joint','right_kckle_joint','rightinn_joint']
    hello_str.position = [0.5,0.5,-0.5,0.5,0.5,-0.5] #position:[(0~1),(0~1),-(0~1),...]
    hello_str.velocity = []
    hello_str.effort = []
    pub.publish(hello_str)
    rate.sleep()

if __name__ == '__main__':
    while True:
       talker()
    time.sleep(1)
