## introduction

This package is the defination of message "aruco_tf_id.msg".
aruco_tf_id.msg contains two members. One is "int64 id", the other is "geometry_msgs/TransformStamped tf". "id" is the ID of aruco marker being detected, while "tf" is the transformation of aruco marker being detected with respect to the camera.

## How to use

1. copy this package into your ROS workspace and run catkin_make in terminal.
2. If you use python
	"from aruco_msg.msg import aruco_tf_id"
3. If you use C++
	"#include <aruco_msg/aruco_tf_id.h>" 
