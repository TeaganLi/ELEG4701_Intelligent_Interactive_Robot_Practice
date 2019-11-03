# README: MoveBase Related Document
As the `actionlib` may be a little bit complex, we wrote a python class for you to make it easy to use.

## Introduction to `actionlib`
The move_base package has already provided the `actionlib` API, you can use the `actionlib` API instead of the .py files we provided. And the related document can be found at:

### Reference websites
You can refer to the following websites if you want to use `actionlib` directly.
> http://wiki.ros.org/move_base
> 
> http://wiki.ros.org/actionlib
> 
> https://docs.ros.org/diamondback/api/actionlib/html/index.html

## Introduction to the .py file
As using the actionlib API to control the robot may be a little bit complex, we have written two .py files for you. `move_base_action_agent.py` is a class writen in python, and `send_goal_to_move_base_template.py` shows how to use it.

### `move_base_action_agent.py`
It is not recommended to make modification to the code in `move_base_action_agent.py`.

### `send_goal_to_move_base_template.py`
To use the class we provided, you need to:

1. `import move_base_action_agent` at the very first of your code.
2. Declare objects: 
   
    It will connect to the move_base `actionlib server` automaticlly.
   
        agent_obj = move_base_action_agent.move_base_action_agent()

3. Assign to the goal (x, y is the positon of robot, z, w is the orientation in quaternion):
   
        agent_obj.x = X
        agent_obj.y = Y
        agent_obj.z = Z
        agent_obj.w = W
4. Use the `agent_obj.prepare_goal()` and `state = agent_obj.send_goal()` in sequential.
`state` is the returned value of the function `send_goal()`
and the meanings of `state` value is:

        PENDING = 0
        ACTIVE = 1
        PREEMPTED = 2
        SUCCEEDED = 3
        ABORTED = 4
        REJECTED = 5
        PREEMPTING = 6
        RECALLING = 7
        RECALLED = 8
        LOST = 9

5. If you want to cancel the current goal:

        agent_obj.cancel_goal()

6. If you want to terminate the connection to move_base:

        agent_obj.disconnect_move_base_server()
        # May be failed in some situations
