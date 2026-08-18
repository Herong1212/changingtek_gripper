cmake_minimum_required(VERSION 2.8.3)

set(project "crt_ctm2f110_gripper_visualization")
project (${project})
set(sdk_dir "sdk")
set(sdk_include_dir "sdk/include")
set(sdklib "CRTServo")

find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   genmsg
)
#added
generate_messages(DEPENDENCIES std_msgs)

#catkin_package()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -O3")
include_directories(${sdk_dir} ${sdk_include_dir})
if(CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
link_directories(${sdk_include_dir}/x86_64)
else()
link_directories(${sdk_include_dir}/arm64)
endif()
link_libraries(${sdklib})

file(GLOB hdrs sdk/*.h)
file(GLOB srs sdk/*.cpp)
add_library(${project} STATIC ${hdrs} ${srs})

#link_directories(sdk)
add_executable(gripper_listener scripts/gripper_listener.cpp)
target_link_libraries(gripper_listener ${catkin_LIBRARIES} ${project})
add_dependencies(gripper_listener crt_ctm2f110_gripper_visualization_generate_messages_cpp)

catkin_package()
include_directories(${catkin_INCLUDE_DIRS})

#added

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
