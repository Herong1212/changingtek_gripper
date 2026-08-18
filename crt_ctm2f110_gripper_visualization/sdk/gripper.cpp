#include "gripper.h"
#include <iostream>

GripperSDK::GripperSDK()
{

}

GripperSDK::~GripperSDK()
{
   closeSerial();
}

//open serial
int GripperSDK::openSerial(int baudRate, const char* serialPort)
{
    if(!ctmINF.begin(baudRate, serialPort))
    {
       std::cout<< "Failed to init serial device!"<<std::endl;
    return 0;
    }
    return 1;
}

//close serial
void GripperSDK::closeSerial()
{
    ctmINF.end();
}

//set gripper position
void GripperSDK::setpos(float p1,float p2)
{
    convert_pos[0] = OFFSET - p1 * SCALER;
    convert_pos[1] = OFFSET - p2 * SCALER;
    ctmINF.RegWritePosEx(1,convert_pos[0],60,100);
    ctmINF.RegWritePosEx(2,convert_pos[1],60,100);
    ctmINF.RegWriteAction();
}
