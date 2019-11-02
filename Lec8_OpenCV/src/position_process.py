#!/usr/bin/env python
# !coding=utf-8

# Course: ELEG 4701 Lc8
# Data:   2019/10/22
# Author: Xuhui Nie
# About:  get the position based on realsense

import rospy
from std_msgs.msg import String
import string
from geometry_msgs.msg import Pose

k = [614.2276611328125, 0.0, 327.88189697265625,
     0.0, 613.449462890625, 239.263671875,
     0.0, 0.0, 1.0]

# camera internal reference
camera_factor = 1
camera_cx = 327.88189697265625
camera_cy = 239.263671875
camera_fx = 614.2276611328125
camera_fy = 613.449462890625

tony_info = 0
target_pose1 = Pose()

def position_transform():
    rospy.init_node('position_process', anonymous=True)

    # get the msg from opencv_img_processing_V6
    rospy.Subscriber('/position_from_opencv', String, callback)
    # publish the msg to manipluation_demo
    global pub_cam_opt
    pub_cam_opt = rospy.Publisher('/cube_marker_pose', Pose, queue_size=10)
    rospy.spin()


def callback(position_msg):
    # define picture to_down' coefficient of ratio
    # print(position_msg.data)
    # print position_msg.data.split(" , ")

    # handle the msg string->float
    [s_x, s_y, s_z] = position_msg.data.split(' , ')
    d_x = float(s_x)
    d_y = float(s_y)
    d_z = float(s_z)
    # get the position in realsense world space
    p_z = float(d_z / camera_factor)
    p_x = (d_x - camera_cx) * p_z / camera_fx
    p_y = (d_y - camera_cy) * p_z / camera_fy
    # print("the world position: "+str(p_x)+" "+str(p_y)+" "+str(p_z))

    # publish the Pose msg
    tony_cam = Pose()
    tony_cam.position.x = p_x/1000
    tony_cam.position.y = p_y/1000
    tony_cam.position.z = p_z/1000

    tony_cam.orientation.x = 0
    tony_cam.orientation.y = 0
    tony_cam.orientation.z = 0
    tony_cam.orientation.w = 0
    # print(relative_pos_cam_base)
    if p_z != 0:
        global pub_cam_opt
        pub_cam_opt.publish(tony_cam)


if __name__ == '__main__':
    position_transform()