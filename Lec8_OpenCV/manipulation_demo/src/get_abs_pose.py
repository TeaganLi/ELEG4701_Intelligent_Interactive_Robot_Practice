#!/usr/bin/env python  
import rospy
import message_filters
from std_msgs.msg import Int32, Float32
#from geometry_msgs.msg import Pose

from tf.transformations import euler_from_quaternion, quaternion_from_euler, \
                               quaternion_matrix, quaternion_from_matrix
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Header
import numpy as np

def PoseStamped_2_mat(p):
    q = p.orientation
    pos = p.position
    T = quaternion_matrix([q.x,q.y,q.z,q.w])
    T[:3,3] = np.array([pos.x,pos.y,pos.z])
    return T

def aMat_2_posestamped(m,f_id="test"):
    q = quaternion_from_matrix(m)
    p = PoseStamped(header = Header(frame_id=f_id), #robot.get_planning_frame()
                    pose=Pose(position=Point(*m[:3,3]), 
                    orientation=Quaternion(*q)))
    return p
def Mat_2_posestamped(m):
    q = quaternion_from_matrix(m)
    comb_pose = Pose()
    comb_pose.position = Point(*m[:3,3])
    comb_pose.orientation = Quaternion(*q)
    return comb_pose 
def callback(came_pose, mark_pose):
  # The callback processing the pairs of numbers that arrived at approximately the same time
  print('zt')
  came_mat = PoseStamped_2_mat(came_pose)
  mark_mat = PoseStamped_2_mat(mark_pose)
  comb_mat =  np.matmul(came_mat, mark_mat)
  comb_pose = Mat_2_posestamped(comb_mat) 
  comb_pose_pub.publish(comb_pose)
  print(comb_pose)
rospy.init_node('combined_pub')
print('tony')
came_base_sub = message_filters.Subscriber('/camera_opt_pose', Pose)
mark_came_sub = message_filters.Subscriber('/cube_marker_pose', Pose)
comb_pose_pub = rospy.Publisher('/final_pose/marker', Pose, queue_size=10)

ts = message_filters.ApproximateTimeSynchronizer([came_base_sub, mark_came_sub], 10, 0.1, allow_headerless=True)
ts.registerCallback(callback)
rospy.spin()
