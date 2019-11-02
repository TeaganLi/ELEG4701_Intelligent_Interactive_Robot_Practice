#!/usr/bin/env python

# Course: ELEG 4701 Lc8
# Data:   2019/10/22
# Author: Xuhui Nie
# About:  convert the image between ros img and OpenCV img


from __future__ import print_function

import roslib

roslib.load_manifest('lc8')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class image_converter:

    # define the init function
    def __init__(self):
        rospy.init_node('imageconverter', anonymous=True)
        self.image_pub = rospy.Publisher("opencv_img_msg", Image)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('camera/color/image_raw', Image, self.callback)

    # callback function when received the subscriber msg
    def callback(self, data):
        try:
            # msg img -> OpenCV img
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        # get the  height width and channels of the img
        (rows, cols, channels) = cv_image.shape
        # add a cycle in the img
        if cols > 60 and rows > 60:
            cv2.circle(cv_image, (50, 50), 20, 255)
        cv2.imshow("the received image in OpenCV format", cv_image)
        cv2.waitKey(3)

        # publish the img in ros format
        try:
            msg = self.bridge.cv2_to_imgmsg(cv_image, "bgr8")
            self.image_pub.publish(msg)
        except CvBridgeError as e:
            print(e)


def main():
    image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
