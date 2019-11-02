#!/usr/bin/env python
# !coding=utf-8

# Course: ELEG 4701 Lc8
# Data:   2019/10/22
# Author: Xuhui Nie
# About:  process the img based on OpenCV API and send out the target position


from __future__ import print_function

import roslib

roslib.load_manifest('lc8')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

# set Yellow_Green thresh
lower_blue = np.array([0, 70, 70])
upper_blue = np.array([100, 255, 255])


# convert the img between ros and OpenCV and
class image_converter:

    # subcribe the color img and depth img
    def __init__(self):
        rospy.init_node('imageconverter', anonymous=True)
        self.image_pub = rospy.Publisher("opencv_img_msg", Image)
        global position_pub
        position_pub = rospy.Publisher("position_from_opencv", String, queue_size=10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('camera/color/image_raw', Image, self.callback)
        self.image_depth = rospy.Subscriber('/camera/aligned_depth_to_color/image_raw', Image,
                                            callback=self.convert_depth_image, queue_size=1)
        rospy.spin()

    # convert the depth image to matrix format
    def convert_depth_image(self, ros_image):
        depth_image = ros_image
        try:
            # Convert the depth image using the default passthrough encoding
            depth_image = self.bridge.imgmsg_to_cv2(ros_image, "passthrough")
        except CvBridgeError, e:
            print(e)
        # Convert the depth image to a Numpy array
        global depth_array
        depth_array = np.array(depth_image, dtype=np.float32)

    # convert the ROS color img to OpenCV format and RGB->HSV
    def callback(self, data):
        try:
            cv2_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            cv2.imshow('img in BRG8 format', cv2_image)
            hsv_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2HSV)  # RGB->HSV
            cv2.imshow('img in HSV format', hsv_image)
        except CvBridgeError as e:
            print(e)
        cv2.waitKey(3)

        try:
            msg = self.bridge.cv2_to_imgmsg(cv2_image, "bgr8")
            self.image_pub.publish(msg)
            # process the img in 6Hz to reduce the usage of computing resource
            global count_frame
            count_frame = count_frame + 1
            if count_frame == 5:
                ana = ImageAnalysis()
                lf = ana.colorfilter(cv2_image)
                ana.analysis(lf)
                count_frame = 0

        except CvBridgeError as e:
            print(e)


# process the img and send put the position
class ImageAnalysis:
    def __init__(self):
        self.shapes = {'triangle': 0, 'rectangle': 0, 'polygons': 0, 'circles': 0}

    # return the img after color filter
    def colorfilter(self, image):
        h, w, ch = image.shape
        result = np.zeros((h, w, ch), dtype=np.uint8)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # RGB->HSV
        mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        res = cv2.bitwise_or(result, image, mask=mask)
        temp = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
        # cv2.imshow('org', image)
        # cv2.imshow('Mask', mask)
        cv2.imshow('img after color filter', res)
        return res

    # analysis the img after color filter
    def analysis(self, frame):
        h, w, ch = frame.shape
        # cv2.imshow("input image 001", frame)
        result = np.zeros((h, w, ch), dtype=np.uint8)
        # binary the img
        # print("start to detect lines...\n")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        # print("thresh is：%s" % ret)
        cv2.imshow("img after binary", binary)
        # find all the contours in the img
        binary, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        print("all the len contours: %d", range(len(contours)))
        for cnt in range(len(contours)):
            # draw the contour
            # print(cnt)
            cv2.drawContours(result, contours, cnt, (0, 255, 0), 2)
            # approximate the contour
            epsilon = 0.01 * cv2.arcLength(contours[cnt], True)
            approx = cv2.approxPolyDP(contours[cnt], epsilon, True)
            # find out the target
            corners = len(approx)
            if 4 < corners < 10:  # the corners is limited
                mm = cv2.moments(contours[cnt])  # get the center of the target
                area = cv2.contourArea(contours[cnt])
                if 200 < area < 20000:                # limit the area
                    cx = int(mm['m10'] / mm['m00'])   # get x in pixel
                    cy = int(mm['m01'] / mm['m00'])   # get y in pixel
                    cv2.circle(result, (cx, cy), 3, (0, 0, 255), -1)  # point out the cycle in red
                    # color analysis
                    color = frame[cy][cx]
                    # get the depth info in mm
                    global depth_array
                    depth = depth_array[cy][cx]
                    # print("depth--------------->: %d", depth)
                    # publish the position msg
                    global position_pub
                    position_pub.publish(str(cx) + ' , ' + str(cy) + " , " + str(depth))
                    color_str = "(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"
                    print("area: %.2f color: %s, position: %d pixel , %d pixel , %.2f mm" % (area, color_str, cx, cy, depth))
                    cv2.imshow("Analysis Result", result)


def main(args):
    global count_frame
    count_frame = 0
    ic = image_converter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)
