#!/usr/bin/env python  
import roslib
#roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
from geometry_msgs.msg import Pose
import turtlesim.srv


if __name__ == '__main__':
    rospy.init_node('turtle_tf_listener', log_level=rospy.ERROR)

    listener = tf.TransformListener()
    pub_cam_opt = rospy.Publisher('/camera_opt_pose', Pose, queue_size=10)
    #now = rospy.Time.now()- rospy.Duration(5.0)
    now = rospy.Time.now()
    past = now - rospy.Duration(5.0)
    #try:
    	#now = rospy.Time.now() - rospy.Duration(5.0)
    	#listener.waitForTransform("cobotta_base_link", "aruco", now, rospy.Duration(1.0))
    	#(trans, rot) = listener.lookupTransform("/turtle2", "/turtle1", now)
    #except (tf.Exception, tf.LookupException, tf.ConnectivityException):
    	#pass
    #listener.waitForTransform("cobotta_base_link", "aruco", rospy.Time(0), rospy.Duration(4.0))
    #listener.waitForTransform("cobotta_base_link", "aruco", now, rospy.Duration(4.0))

    #rospy.wait_for_service('spawn')
    #spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    #spawner(4, 2, 0, 'turtle2')

    #turtle_vel = rospy.Publisher('turtle2/cmd_vel', geometry_msgs.msg.Twist,queue_size=1
    #rospy.sleep(5.0)
    #listener.waitForTransformFull('cobotta_base_link',now, 'camera_depth_optical_frame',now, 'cobotta_base_link', rospy.Duration(4.0))
    #listener.waitForTransform("cobotta_base_link", "camera_depth_optical_frame", now, rospy.Duration(5.0))
    #listener.waitForTransform("camera_depth_optical_frame", "cobotta_base_link", now, rospy.Duration(5.0),polling_sleep_duration = rospy.Duration(0.05))
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # (trans,rot) = listener.lookupTransform('camera_depth_optical_frame', 'cobotta_base_link', rospy.Time(0))
            #(trans,rot) = listener.lookupTransform('aruco', 'cobotta_base_link', rospy.Time(0))
            #print('zt')
            #(trans,rot) = listener.lookupTransform('camera_depth_optical_frame', now,'cobotta_base_link',past, 'cobotta_base_link')
            (trans,rot) = listener.lookupTransform('cobotta_base_link', 'camera_depth_optical_frame', rospy.Time(0))

        # except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        #angular = 4 * math.atan2(trans[1], trans[0])
        #linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        #cmd = geometry_msgs.msg.Twist()
        #cmd.linear.x = linear
        #cmd.angular.z = angular

        #turtle_vel.publish(cmd)
        print('zt_ mark')
        print(len(rot))
        print(trans)
        relative_pos_cam_base = geometry_msgs.msg.Pose()
        relative_pos_cam_base.position = trans
        relative_pos_cam_base.orientation= rot
        tony_cam = Pose()
        tony_cam.position.x = trans[0]
        tony_cam.position.y = trans[1]
        tony_cam.position.z = trans[2]

        tony_cam.orientation.x = rot[0]
        tony_cam.orientation.y = rot[1]
        tony_cam.orientation.z = rot[2]
        tony_cam.orientation.w = rot[3]
        print(relative_pos_cam_base)
        pub_cam_opt.publish(tony_cam)
        print('tony')

        rate.sleep()
