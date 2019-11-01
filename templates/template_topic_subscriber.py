#!/usr/bin/env python
'''
This template includes a topic subscriber.
    Topic name: chatter
    Topic type: String
You can replace listener() and callback to subscribe any thing you want, remember to also modify main()
'''

import rospy                        # the essential module if you want to use python in ROS
from std_msgs.msg import String     # import a standard message type 'String', search online to find more message types

def callback(data):
    '''The function to process the received message'''
    print("I heard %s"%data.data)   # here data type is String with data member,
                                    # for other data type, you may need to search for their defination

def listener():
    '''The function to declare subscriber String typed messages via chatter topic'''
    rospy.Subscriber('chatter', String, callback)     # create a subscriber by providing topic name and its type,
                                                      # and the function to process the received messages
    rospy.spin()                                      # keeps listening to the message

def main():
    rospy.init_node("listener_node", anonymous=True)    # the first thing to do: init a ROS node by providing the node name
    listener()                                            # call the function 'talker' to publish messages

if __name__ == '__main__':
    main()