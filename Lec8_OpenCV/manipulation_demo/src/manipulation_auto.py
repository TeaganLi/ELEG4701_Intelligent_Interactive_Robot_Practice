#!/usr/bin/env python

# from tony_file.srv import Translate,TranslateResponse
from tony_file.srv import Translate, TranslateResponse
import rospy
import actionlib
from geometry_msgs.msg import Pose
from manipulation_base import MoveItIkDemo
from std_srvs.srv import Trigger,TriggerResponse
from denso_cobotta_gripper.msg import GripperMoveAction, GripperMoveGoal

tony_info = 0
target_pose1 = Pose()

def handle_add_two_ints(request):
	#global target_pose1
	to_move_x = -1 * target_pose1.position.y
	to_move_y = -1 * target_pose1.position.x
	to_move_z = -1 * target_pose1.position.z + 0.09
	print(to_move_x)
	print(to_move_y)
	print(to_move_z)

	moveitDemo = MoveItIkDemo()
	gripper_client = actionlib.SimpleActionClient('/gripper_move', GripperMoveAction)
	gripper_move(gripper_client, 0.03, 10, 10, 10)
	moveitDemo.translate(1,to_move_y)
	moveitDemo.translate(0,to_move_x)
	#moveitDemo.translate(1,to_move_y)
	moveitDemo.translate(2,to_move_z)
	rospy.sleep(5)
	moveitDemo.translate(1,0.038)
	moveitDemo.translate(0,0.06)
	moveitDemo.translate(2,-0.04)
#	gripper_client = actionlib.SimpleActionClient('/gripper_move', GripperMoveAction)
	gripper_move(gripper_client, 0.0115, 10, 10, 10)
	moveitDemo.arm.set_named_target('home')
	moveitDemo.arm.go()

	trigger_result = TriggerResponse()
	trigger_result.success = True
	return trigger_result

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
    rospy.Subscriber("/cube_marker_pose", Pose, callback)
    #rospy.Subscriber("/final_pose/marker", Pose, callback)
    s = rospy.Service('/fine_tune', Trigger, handle_add_two_ints)


    print "Ready to add two ints."
    #print(target_pose1)
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

