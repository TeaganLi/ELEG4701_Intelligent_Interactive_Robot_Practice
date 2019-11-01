#!/usr/bin/env python
'''
This template includes a service server.
    service name: add_two_ints
    service type: AddTwoInts
    service function: handle_add_two_ints
You can replace server() and handle_add_two_ints(), remember to also modify main()
'''

import rospy                        # the essential module if you want to use python in ROS
from YOUR_PACKAGE.srv import AddTwoInts, AddTwoIntsResponse  # user defined service type, refer to ROS tutorial for defining service

def handle_add_two_ints(req):
    '''The function to response to the calling to the service'''
    print("The service is called")
    return AddTwoIntsResponse(req.a + req.b)           # return the result to the client

def server():
    '''The function to declare service add_two_ints with AddTwoInts type'''
    rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)  # create a service with name, type, and function
    rospy.spin()

def main():
    rospy.init_node("server_node", anonymous=True)    # the first thing to do: init a ROS node by providing the node name
    server()

if __name__ == '__main__':
    main()