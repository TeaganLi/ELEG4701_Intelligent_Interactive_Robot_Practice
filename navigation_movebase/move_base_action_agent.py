# ********************************* #
# Created by Chenming Li, 2019-11-2 #
# ********************************* #

# You can use this program as a black box. 
# It is NOT recommended to make modifications to this .py file, unless necessary.

#!/usr/bin/env python
import roslib
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
# from std_msgs.srv import Float64MultiArray

class move_base_action_agent:
    x = None
    y = None
    z = None
    w = None

    state_msg = {
        0: "PENDING",
        1: "ACTIVE",
        2: "PREEMPTED",
        3: "SUCCEEDED",
        4: "ABORTED",
        5: "REJECTED",
        6: "PREEMPTING",
        7: "RECALLING",
        8: "RECALLED",
        9: "LOST" 
    }

    def __init__(self):
        rospy.init_node('move_base_action_template')
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()
        while not self.client.wait_for_server(rospy.Duration.from_sec(2.0)):
            print("Waiting for the client to connect to the action server")

        self.goal = MoveBaseGoal()

    def prepare_goal(self):
        if self.x == None or self.y == None or self.z == None or self.w == None:
            print("invalid goal received, please give robot position x, y, and the orientation in quarternion with z and w ")
            return false
        else:
            self.goal.target_pose.header.frame_id = "map"
            self.goal.target_pose.pose.position.x = self.x
            self.goal.target_pose.pose.position.y = self.y

            self.goal.target_pose.pose.orientation.z = self.z
            self.goal.target_pose.pose.orientation.w = self.w

            # clear the goal
            self.x = None
            self.y = None
            self.z = None
            self.w = None
    
    def send_goal(self):
        self.client.send_goal(self.goal)

        state = self.client.get_state()
        while not self.client.wait_for_result(rospy.Duration.from_sec(1.0)):
            state = self.client.get_state()
        state = self.client.get_state()
        print("The current goal state is " + str(state) + ": " + self.state_msg.get(state))
        return True

    def cancel_goal(self):
        self.client.cancel_all_goals()
        print("Cancel all goals")
        pass

    def disconnect_move_base_server(self):
        self.__del__()

    def __del__(self):
        self.cancel_goal()

def move_base_cmd_goal():
    pass


