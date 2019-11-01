cmake_minimum_required(VERSION 2.8.3)
project(ros_aruco)
set (CMAKE_CXX_STANDARD 11)
find_package(catkin REQUIRED COMPONENTS cv_bridge image_transport message_generation sensor_msgs tf2 tf2_ros geometry_msgs roscpp)
find_package (Eigen3 REQUIRED NO_MODULE)
## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

catkin_package(CATKIN_DEPENDS cv_bridge image_transport message_runtime sensor_msgs)
find_package(OpenCV)
find_package(Ceres REQUIRED)
include_directories(${CERES_INCLUDE_DIRS})
include_directories(include ${catkin_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS})

add_message_files(
        FILES
        aruco_tf_id.msg
)
add_executable(aruco_sub src/aruco_sub.cpp)
add_dependencies(aruco_sub ${catkin_EXPORTED_TARGETS} ${${PROJECT_NAME}_EXPORTED_TARGETS})
target_link_libraries(aruco_sub ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})
install(TARGETS aruco_sub
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
        )