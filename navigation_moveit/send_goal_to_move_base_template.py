#!/usr/bin/env python

# move_base_action_agent is a python file, which is composed for easier usage of Move_Base
import rospy
import move_base_action_agent


if __name__ == '__main__':

    # Suppose you are going to control the robot to move to the Point_I, Point_II and Point_III in sequence.
    # Point_I   : x = 2.0; y = 2.0
    # Point_II  : x = 5.0; y = 5.0
    # Point_III : x = 1.0; y = 1.0
    goal_vector = [[2.0, 2.0, 1.0, 1.0], [5.0, 5.0, 1.0, 1.0], [10.0, 10.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]]

    
    agent_obj = move_base_action_agent.move_base_action_agent()

    test_count = 0  # ignore this


    for goal in goal_vector:
        
        if rospy.is_shutdown():
            break

        agent_obj.x = goal[0]
        agent_obj.y = goal[1]
        agent_obj.z = goal[2]
        agent_obj.w = goal[3]

        # when you want to terminate the whole goal_sending process, please use this part.
        # if test_count == 1:
        #     agent_obj.disconnect_move_base_server()
        #     break

        # when you want to cancel the current goal, and send the next one to move_base, please use this part.
        # if test_count == 2:
        #     agent_obj.cancel_goal()
        
        # Please use prepare_goal and send_goal in sequence
        agent_obj.prepare_goal()
        state = agent_obj.send_goal()   

        # state will illustrate the final state of the robot base
        ''' 
        Document for the state
        uint8 PENDING=0
        uint8 ACTIVE=1
        uint8 PREEMPTED=2
        uint8 SUCCEEDED=3
        uint8 ABORTED=4
        uint8 REJECTED=5
        uint8 PREEMPTING=6
        uint8 RECALLING=7
        uint8 RECALLED=8
        uint8 LOST=9
        '''

        test_count = test_count + 1     # ignore this
        
