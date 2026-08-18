cmake_minimum_required(VERSION 2.8.3)

project(crt_ctpm2f50_gripper_visualization)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

#python
catkin_install_python(PROGRAMS
   scripts/GUI2Robot_listener.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
