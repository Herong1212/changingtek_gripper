#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import rospy
import minimalmodbus
# import serial
import threading
import time
from sensor_msgs.msg import JointState

# 读取保持寄存器的值
def read_register(instrument, register_address):
    value = instrument.read_register(register_address, functioncode=3)
    return value

# 写入保持寄存器的值
def write_register(instrument, register_address, value):
    instrument.write_register(register_address, value, functioncode=6)

# 读取输出参数
def read_output_param_finger1(instrument):
  with lock:
    return read_register(instrument, FINGER_1_OUTPUT_PARAM_REGISTER)

def read_output_param_finger2(instrument):
  with lock:
    return read_register(instrument, FINGER_2_OUTPUT_PARAM_REGISTER)

# 写入目标速度  
def write_target_speed_finger1(instrument, speed):
  with lock:
    write_register(instrument, FINGER_1_SPEED_REGISTER, speed)

def write_target_speed_finger2(instrument, speed):
  with lock:
    write_register(instrument, FINGER_2_SPEED_REGISTER, speed)

# 读取目标位置  
def read_target_position_finger1(instrument):
  with lock:
    return read_register(instrument, FINGER_1_POSITION_REGISTER)

def read_target_position_finger2(instrument):
  with lock:
    return read_register(instrument, FINGER_2_POSITION_REGISTER)
# 读取当前位置
# def read_current_position(instrument):
#   with lock:
#     return read_register(instrument, CURRENT_POSITION_REGISTER)
  
# 读写寄存器的具体函数
  
# 寄存器地址常量
FINGER_1_POSITION_REGISTER = 10  
FINGER_1_OUTPUT_PARAM_REGISTER = 11
FINGER_1_SPEED_REGISTER = 12
FINGER_1_ACCELERATED_SPEED_REGISTER = 13
FINGER_2_POSITION_REGISTER = 20  
FINGER_2_OUTPUT_PARAM_REGISTER = 21
FINGER_2_SPEED_REGISTER = 22
FINGER_2_ACCELERATED_SPEED_REGISTER = 23
FINGER_3_POSITION_REGISTER = 30  
FINGER_3_OUTPUT_PARAM_REGISTER = 31
FINGER_3_SPEED_REGISTER = 32
FINGER_3_ACCELERATED_SPEED_REGISTER = 33
CLOSE_REGISTER = 40
OPEN_REGISTER = 41
SYNCHRONIZATION_REGISTER = 42

# 串口设置
PORT = '/dev/ttyUSB0'
instrument = minimalmodbus.Instrument(PORT, 1)
instrument.serial.baudrate = 115200
instrument.serial.timeout = 0.5
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.mode = minimalmodbus.MODE_RTU
# 线程锁
lock = threading.Lock()


l1 = [0 for i in range(3)]
l2 = [0 for i in range(3)]
l3 = [0 for i in range(3)]

def callback(data,args):
  # print(data)
  rate = rospy.Rate(50)
  p1 = int(( - data.position[0])  * 100)
  p2 = int(( - data.position[3])  * 100)
  p3 = int(( - data.position[6])  * 100)
  
  l1.pop(0)
  l1.append(p1)
  l2.pop(0)
  l2.append(p2)
  l3.pop(0)
  l3.append(p3)
  
  if l1.count(p1) >=3:
    write_register(args,FINGER_3_POSITION_REGISTER,p1)   #传入位置信息
  if l2.count(p2) >=3:
    write_register(args,FINGER_2_POSITION_REGISTER,p2)   #传入位置信息
  if l3.count(p3) >=3:
    write_register(args,FINGER_1_POSITION_REGISTER,p3)   #传入位置信息

  rate.sleep()


if __name__ == '__main__':
    print("程序开始")
    write_register(instrument,SYNCHRONIZATION_REGISTER,0)   #设置异步
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback, (instrument))
    time.sleep(1)
    rospy.spin()
