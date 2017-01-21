cmake_minimum_required(VERSION 2.8.3)
project(scooter)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  rospy
  std_msgs
  message_generation
)

generate_dynamic_reconfigure_options(
   cfg/scootercfg.cfg
 )

###################################
## catkin specific configuration ##
###################################

#catkin_package(CATKIN_DEPENDS scooter rospy)

add_executable(scooter_node nodes/scooter.py)

add_dependencies(scooter_node ${PROJECT_NAME}_gencfg)

set_target_properties(scooter_node PROPERTIES LINKER_LANGUAGE CMAKE_py_LINK_EXECUTABLE)


