#!/usr/bin/env python

# Course: ELEG 4701 Lc8
# Data:   2019/10/22
# Author: Xuhui Nie
# About:  check the ros img converted from OpenCV

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


def callback(data):
    bridge = CvBridge()
    cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.imshow("the received img in ros msg format", cv_img)
    cv2.waitKey(3)


def displayrosimg():
    rospy.init_node('check', anonymous=True)
    rospy.Subscriber('/opencv_img_msg', Image, callback)
    rospy.spin()


if __name__ == '__main__':
    displayrosimg()
