#!/usr/bin/env python
import logging
logging.basicConfig()
logging.getLogger().setLevel("ERROR")
from std_srvs.srv import Trigger,TriggerResponse
import rospy
from geometry_msgs.msg import Pose
from manipulation_base import MoveItIkDemo


tony_info = 0
target_pose1 = Pose()

def relative_position_move(request):
	global tony_info
	global target_pose1
	if (tony_info == 0):
		#print('Cannot find target')
		trigger_result = TriggerResponse()
		trigger_result.success = False
		trigger_result.message = 'cannot receive any target message'
	else:
		print('zt')
		moveitDemo = MoveItIkDemo()
		moveitDemo.move_the_arm(target_pose1)
		trigger_result = TriggerResponse()
		trigger_result.success = True


	return trigger_result

    #print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    #return AddTwoIntsResponse(req.a + req.b)
def callback(target_pose):
	global tony_info
	global target_pose1
	if (tony_info == 0):
		target_pose1 = target_pose
		tony_info = 1


def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    rospy.Subscriber("/final_pose/marker", Pose, callback)
    s = rospy.Service('/set_relative_pose', Trigger, relative_position_move)


    print "Ready to move to relative pose."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
