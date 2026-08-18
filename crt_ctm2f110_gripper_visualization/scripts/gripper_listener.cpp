#include "ros/ros.h"
#include "gripper.h"
#include "sensor_msgs/JointState.h"
GripperSDK gs;
void callback(const sensor_msgs::JointStateConstPtr& msg)
{
  float pos[6] = {0.0,0.0,0.0,0.0,0.0,0.0};
  float p1, p2;
  p1 = msg->position[1];
  p2 = msg->position[4];
  pos[0]=msg->position[0];
  pos[1]=msg->position[1];
  pos[2]=msg->position[2];
  pos[3]=msg->position[3];
  pos[4]=msg->position[4];
  pos[5]=msg->position[5];
  ROS_INFO("gripper is reaching: [%f] [%f] [%f] [%f] [%f] [%f]",pos[0],pos[1],pos[2],pos[3],pos[4],pos[5]);
  ROS_INFO_STREAM("Serial Port start write");
  gs.setpos(p1,p2);
  ROS_INFO_STREAM("Serial Port end write");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "gripper_listener");

  ros::NodeHandle nh;
  // open serial
  if(!gs.openSerial(115200, "/dev/ttyUSB0")){
    return 0;
  }
  ros::Subscriber sub = nh.subscribe("/joint_states", 1000, callback); // subscribe node
  ROS_INFO_STREAM("Serial Port opened");
  ros::spin();

  return 0;
}
