#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import actionlib
import math
import moveit_commander
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import Pose, PoseStamped
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from moveit_msgs.msg import RobotTrajectory
from denso_cobotta_gripper.msg import GripperMoveAction, GripperMoveGoal
from denso_cobotta_driver.srv import GetMotorState
from moveit_python import *

# NOTE: Before start this program, please launch denso_cobotta_bring.launch

class MoveItIkDemo(object):
    def __init__(self):
        # Initialize the moveit_commander module
        moveit_commander.roscpp_initialize(sys.argv)
        #self.target_pose = target_pose               
        # Initialize the arm group in the robot arm that needs to be controlled by the move group
        self.arm = moveit_commander.MoveGroupCommander('arm')
        self.move_group = MoveGroupInterface("arm", "base_link")
        #self.gripper = RobotCommander()
        self.gripper = moveit_commander.MoveGroupCommander('gripper')
        #self.end_gripper_link = self.gripper.get_end_effector_link()
        #self.grip_ref = 'gripper_base'
                
        # Get the name of the terminal link
        self.end_effector_link = self.arm.get_end_effector_link()
        #print(end_effector_link)
                        
        # Set the reference coordinate system used by the target position
        self.reference_frame = 'cobotta_base_link'
        self.gripper_client = actionlib.SimpleActionClient('/cobotta/gripper_move', GripperMoveAction)
    def move_the_arm(self,target_pose):
        self.arm.set_pose_reference_frame(self.reference_frame)
        self.target_pose = target_pose
                
        # Allow re-planning when motion planning fails
        self.arm.allow_replanning(True)
        
        # Set the allowable error of position (unit: meter) and attitude (unit: radians)
        self.arm.set_goal_position_tolerance(0.01)
        self.arm.set_goal_orientation_tolerance(0.05)
        
        # Control the robot arm to return to the initial position
        self.arm.set_named_target('home')
        self.arm.go()
        rospy.sleep(2)
               
        # Set the target pose in the arm working space, the position is described by x, y, z coordinates.
        # The pose is described using quaternions, based on the base_link coordinate system
        target_pose = PoseStamped()
        target_pose.header.frame_id = self.reference_frame
        target_pose.header.stamp = rospy.Time.now()     
        target_pose.pose.position.x =  self.target_pose.position.x - 0.04  #self.target_pose.position.x + 0.035  #-0.004343
        target_pose.pose.position.y =  self.target_pose.position.y   #self.target_pose.position.y + 0.035  #0.035
        target_pose.pose.position.z =   self.target_pose.position.z+0.10 #self.target_pose.position.z + 0.071   #0.07
        target_pose.pose.orientation.x = 3.752417345990631e-05
        target_pose.pose.orientation.y = 0.9999999971462301
        target_pose.pose.orientation.z = 3.1810091785781024e-05
        target_pose.pose.orientation.w = 5.733754301165406e-05

        
        # Set the current state of the robot arm as the initial state of motion        arm.set_start_state_to_current_state()
        
        # Set the target pose of the arm end motion
        self.arm.set_pose_target(target_pose, self.end_effector_link)

        # Planning the path of motion
        self.traj = self.arm.plan()
        print('arm.plan over')
        # Control arm movement according to planned motion path
        self.arm.execute(self.traj)
        rospy.sleep(2)
        print('arm.execute over') 

    def move_to_home(self):
        self.arm.set_named_target('home')
        self.arm.go()


    def translate(self, aix, distance):
        self.arm.get_end_effector_link()
        self.arm.shift_pose_target(aix,distance,self.end_effector_link)
        self.arm.go()
        print('translate okay')

    def ripper_move(self, width, speed, force, timeout=10):
        #rospy.wait_for_service('/cobotta/get_motor_state', 5.0)
        #get_motor_state = rospy.ServiceProxy('/cobotta/get_motor_state', GetMotorState)
        #res = get_motor_state()
        #if res.state is not True:
            #print >> sys.stderr, "  Please motor on."
        goal = GripperMoveGoal()
        goal.target_position = width
        goal.speed = speed
        goal.effort = force
        self.gripper_client.send_goal(goal)

    def gripper_move(self,width,speed=10,force = 10,timeout=10):
        self.ripper_move(width,speed,force,timeout)

    def gripper_change(self,tong):
        #return self.move_group.moveToJointPosition(['link_2'], [-1.046], 0.02)
        #return self.end_effector_link
        self.gripper.set_joint_value_target([0.01])
        #self.gripper.allow_replanning(True)
        ##self.gripper.set_goal_position_tolerance(0.01)
        #self.arm.set_goal_orientation_tolerance(0.05)
        #if (tong):
            #label = 'gripper_open'
        #else:
            #label = 'gripper_closed'
        #self.gripper.set_named_target('gripper_open')
        #self.gripper.go()
        #print('zt')




        #moveit_commander.roscpp_shutdown()
        #moveit_commander.os._exit(0)
    
if __name__ == "__main__":
    rospy.init_node('moveit_ik_demo')
    MoveItIkDemo()

