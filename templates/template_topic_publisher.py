#!/usr/bin/env python
'''
This template includes a topic publisher.
    Publisher name: pub
    Topic name: chatter
    Topic type: String
You can replace talker() to publish any thing you want, remember to also modify main()
'''

import rospy                        # the essential module if you want to use python in ROS
from std_msgs.msg import String     # import a standard message type 'String', search online to find more message types

def talker():
    '''The function to publish String typed messages via chatter topic'''
    pub = rospy.Publisher('chatter', String, queue_size=10) # create a publisher by providing topic name and its type
    rate = rospy.Rate(10)                                   # the publishing frequency
    while not rospy.is_shutdown():                          # publish in 10hz
        hello_str = "hello world %s" % rospy.get_time()
        print(hello_str)
        pub.publish(hello_str)                              # publish the message
        rate.sleep()                                        # control the publishing frequency


def main():
    rospy.init_node("talker_node", anonymous=True)  # the first thing to do: init a ROS node by providing the node name
    talker()                                        # call the function 'talker' to publish messages

if __name__ == '__main__':
    main()