#!/usr/bin/env python

# from tony_file.srv import Translate,TranslateResponse
from tony_file.srv import Translate, TranslateResponse
import rospy
import actionlib
from geometry_msgs.msg import Pose
from manipulation_base import MoveItIkDemo
from std_srvs.srv import Trigger,TriggerResponse
from denso_cobotta_gripper.msg import GripperMoveAction, GripperMoveGoal
from std_srvs.srv import SetBool, SetBoolResponse

#tony_info = 0
#target_pose1 = Pose()

def grasp_something(request):
	if (request.data == True):
		length = 0.03
	elif (request.data == False):
		length = 0.021
	gripper_client = actionlib.SimpleActionClient('/gripper_move', GripperMoveAction)
	gripper_move(gripper_client, length, 10, 10, 10)
	response = SetBoolResponse()
	response.success = True
	return response


def callback(target_pose):
	global target_pose1
	target_pose1 = target_pose
	print (target_pose1)


def gripper_move(gripper_client, width, speed, force, timeout=10):
    goal = GripperMoveGoal()
    goal.target_position = width
    goal.speed = speed
    goal.effort = force
    gripper_client.wait_for_server()
    gripper_client.send_goal(goal)
    gripper_client.wait_for_result(rospy.Duration.from_sec(5.))
    #print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    #return AddTwoIntsResponse(req.a + req.b)
# def callback(target_pose):
# 	global tony_info
# 	global target_pose1
# 	if (tony_info == 0):
# 		target_pose1 = target_pose
# 		tony_info = 1


def add_two_ints_server():
    rospy.init_node('preparing_the_translate',log_level=rospy.ERROR)
    #global target_pose1
    #rospy.Subscriber("/tony/marker_pose", Pose, callback)
    #rospy.Subscriber("/final_pose/marker", Pose, callback)
    s = rospy.Service('/set_gripper_move', SetBool, grasp_something)


    print "Ready to add two ints."
    #print(target_pose1)
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

