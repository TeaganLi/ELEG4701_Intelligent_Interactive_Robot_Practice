This package comprise three nodes "aruco_sub" "aruco_sub_arm1" "aruco_sub_arm2".
## Nodes introduction:
1. "aruco_sub" is used for the detection of the biggest marker. The transformation of the marker with respect to camera is published on topic "/camera/pose3d".
2. "aruco_sub_arm1" is used for the detection of the marker on the cover of the box. The transformation of the marker with respect to camera is published on topic "/camera/target1_pose3d".
3. "aruco_sub_arm2" is used for the detection of the marker on the target object. The transformation of the marker with respect to camera is published on topic "/camera/target2_pose3d".

## message type introduction:
All of the three nodes publish aruco_tf_id message. Aruco_tf_id message contain the transformation(tf) of aruco marker and the ID of aruco marker. You can check "aruco_tf_id.msg" in package aruco_msg/msg/.
You can also get the transformation of aruco marker from tf tree. The frame id is the id of the aruco marker.

## How to use this message:
1. In python
	"from aruco_msg.msg import aruco_tf_id"
2. In C++
	"include <aruco_msg/aruco_tf_id.h>"

## How to run:
1. Add this package (ros_aruco) and aruco_msg to your ros workspace and run "catkin_make "
2. "rosrun ros_aruco aruco_sub" to run node1.
3. "rosrun ros_aruco aruco_sub_arm1" to run node2.
4. "rosrun ros_aruco aruco_sub_arm2" to run node3.
5. For convenience, you can use "roslaunch ros_aruco aruco.launch" to run three nodes all together.

## marker ID assignment
1. ID 0 is for box cover.
2. ID 1 is for target object.
3. Other IDs are for large markers.



