#!/usr/bin/env python
'''
This template includes a service client.
    service name: add_two_ints
    service type: AddTwoInts
You can replace server(), remember to also modify main()
'''

import rospy                        # the essential module if you want to use python in ROS
from YOUR_PACKAGE.srv import AddTwoInts  # user defined service type, refer to ROS tutorial for defining service

def client(x, y):
    '''The function to call the service add_two_ints'''
    add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)   # create a handle for calling the service
    response = add_two_ints(x, y)                                   # call the handle just like a function
    return response.sum

def main():
    rospy.wait_for_service('add_two_ints')              # For clients, you don't need to init_node,
                                                        # instead you need to wait for the servie you want to call
    client(1, 1)

if __name__ == '__main__':
    main()