#!/usr/bin/env python
import logging
logging.basicConfig()
logging.getLogger().setLevel("ERROR")
from std_srvs.srv import Trigger,TriggerResponse
import rospy
from geometry_msgs.msg import Pose
from manipulation_base import MoveItIkDemo



def go_home(request):
	#print('zt')
	moveitDemo = MoveItIkDemo()
	moveitDemo.move_to_home()
	trigger_result = TriggerResponse()
	trigger_result.success = True
	return trigger_result



def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    #rospy.Subscriber("/final_pose/marker", Pose, callback)
    s = rospy.Service('/reset_to_home', Trigger, go_home)


    print "Call this to go home."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
