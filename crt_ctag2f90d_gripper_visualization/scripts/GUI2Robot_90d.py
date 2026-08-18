#!/usr/bin/ python3
# -*- coding: UTF-8 -*-

import minimalmodbus
import serial
import threading
import rospy
import time
from sensor_msgs.msg import JointState

# 寄存器地址
ENABLE = 0x0100
POSITION_LOW_8 = 0x0103
TRIGGER = 0x0108
ALARM_RESET = 0x110

PORT = '/dev/ttyUSB0'  # 修改为您的COM口号
BAUD = 115200

instrument = minimalmodbus.Instrument(PORT, 1)
instrument.serial.baudrate = BAUD
instrument.serial.timeout = 1

lock = threading.Lock()

def write_register(instrument, addr, value):
    with lock:
        instrument.write_register(addr, value, functioncode=6)


l1 = [0 for i in range(5)]
l2 = [1001]


def callback(data):
    rate = rospy.Rate(50)
    p = int( (data.position[1] / 0.91) * 9000)

    global l1,l2

    l1.append(p)
    l1.pop(0)

    if l1.count(p) >=3:
        l2.append(p)
        if l2[-1] != l2[-2]:
            print(p)
            write_register(instrument, POSITION_LOW_8, p)
            write_register(instrument, TRIGGER, 1)
        l2.pop(0)

    rate.sleep()

if __name__ == '__main__':
    write_register(instrument, ALARM_RESET, 1)
    write_register(instrument, ENABLE, 1)

    print("程序开始")
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)
    time.sleep(1)
    rospy.spin()
