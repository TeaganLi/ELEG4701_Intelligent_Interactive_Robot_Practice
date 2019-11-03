This package comprise three nodes **aruco_sub**, **aruco_sub_arm1**, **aruco_sub_arm2**.
## Nodes introduction:
1. **aruco_sub** is used for the detection of the biggest marker (attached on tables). The transformation of the marker with respect to camera is published on topic "/camera/pose3d".
2. **aruco_sub_arm1** is used for the detection of the marker on the cover of the box. The transformation of the marker with respect to camera is published on topic "/camera/target1_pose3d".
3. **aruco_sub_arm2** is used for the detection of the marker on the target object. The transformation of the marker with respect to camera is published on topic "/camera/target2_pose3d".

## message type introduction:
All of the three nodes can also publish aruco_tf_id message. Aruco_tf_id message contain the transformation(tf) of aruco marker and the ID of aruco marker. You can check "aruco_tf_id.msg" in package aruco_msg/msg/. You can also get the transformation of aruco marker from tf tree. The frame id is the id of the aruco marker. Considering that you will need to know the ids of different markers, you need to kown where to subscribe aruco_tf_id message.
1. **aruco_sub** publish aruco_tf_id message on topic "/camera/aruco_tf_id".
2. **aruco_sub_arm1** publish aruco_tf_id message on topic "/camera/aruco_tf_id/arm1".
3. **aruco_sub_arm2** publish aruco_tf_id message on topic "/camera/aruco_tf_id/arm2".

## How to use this message:
1. In python
	"from aruco_msg.msg import aruco_tf_id"
2. In C++
	"include <aruco_msg/aruco_tf_id.h>"

## How to run:
1. Add this package (ros_aruco) and aruco_msg to your ros workspace and run "catkin_make "
2. To run aruco_sub:
```
rosrun ros_aruco aruco_sub
```
3. To run aruco_sub_arm1:
```
rosrun ros_aruco aruco_sub_arm1
```
4. To run aruco_sub_arm2:
```
rosrun ros_aruco aruco_sub_arm2
```
5. For convenience, you can run the following to run three nodes all together.
```
roslaunch ros_aruco aruco.launch
```

## marker ID assignment
1. ID 0 is for box cover.
2. ID 1 is for target object.
3. Other IDs are for large markers.



