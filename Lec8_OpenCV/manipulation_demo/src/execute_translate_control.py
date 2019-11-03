#!/usr/bin/env python

# from tony_file.srv import Translate,TranslateResponse
from tony_file.srv import Translate, TranslateResponse
import rospy
from geometry_msgs.msg import Pose
from manipulation_base import MoveItIkDemo


tony_info = 0
target_pose1 = Pose()

def translate_along(request):
	if (request.axis == 'x'):
		first_ele = 0
	elif (request.axis == 'y'):
		first_ele = 1
	elif (request.axis == 'z'):
		first_ele = 2
	distance = request.distance
	moveitDemo = MoveItIkDemo()
	moveitDemo.translate(first_ele, distance)
	#moveitDemo.gripper_move(0.02)
	return TranslateResponse()


    #print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    #return AddTwoIntsResponse(req.a + req.b)
# def callback(target_pose):
# 	global tony_info
# 	global target_pose1
# 	if (tony_info == 0):
# 		target_pose1 = target_pose
# 		tony_info = 1


def add_two_ints_server():
    rospy.init_node('preparing_the_translate')
    #rospy.Subscriber("/final_pose/marker", Pose, callback)
    s = rospy.Service('/set_translate', Translate, translate_along)


    print "Ready to translate along axis."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

