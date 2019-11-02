This package comprise three nodes "aruco_sub" "aruco_sub_arm1" "aruco_sub_arm2".
"aruco_sub" is used for the detection of the biggest marker. The transformation of the marker with respect to camera is published on topic "/camera/pose3d".
"aruco_sub_arm1" is used for the detection of the marker on the cover of the box. The transformation of the marker with respect to camera is published on topic "/camera/target1_pose3d".
"aruco_sub_arm2" is used for the detection of the marker on the target object. The transformation of the marker with respect to camera is published on topic "/camera/target2_pose3d".
