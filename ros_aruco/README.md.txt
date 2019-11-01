ros_aruco package can detect multiple aruco markers and publish the transform of the markers with respect to the camera.

This node can detect aruco marker from "cv::aruco::DICT_4X4_250"
If you want to change the dictionary of aruco marker, change "cv::Ptr<cv::aruco::Dictionary> dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_4X4_250);"

* Topic name: /camera/pose3d
* message type: geometry_msgs::TransformStamped

##How to run:
1. Add this package to your ros workspace and run "catkin_make "
2. "rosrun ros_aruco aruco_sub"
