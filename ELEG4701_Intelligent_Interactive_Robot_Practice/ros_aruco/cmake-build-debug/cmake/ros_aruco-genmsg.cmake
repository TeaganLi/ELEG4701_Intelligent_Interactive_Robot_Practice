# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ros_aruco: 1 messages, 0 services")

set(MSG_I_FLAGS "-Iros_aruco:/home/mh/catkin_ws/src/ros_aruco/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ros_aruco_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" NAME_WE)
add_custom_target(_ros_aruco_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_aruco" "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" "geometry_msgs/Vector3:geometry_msgs/Quaternion:geometry_msgs/Transform:geometry_msgs/TransformStamped:std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ros_aruco
  "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/TransformStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_aruco
)

### Generating Services

### Generating Module File
_generate_module_cpp(ros_aruco
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_aruco
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ros_aruco_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ros_aruco_generate_messages ros_aruco_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" NAME_WE)
add_dependencies(ros_aruco_generate_messages_cpp _ros_aruco_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_aruco_gencpp)
add_dependencies(ros_aruco_gencpp ros_aruco_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_aruco_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ros_aruco
  "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/TransformStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_aruco
)

### Generating Services

### Generating Module File
_generate_module_eus(ros_aruco
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_aruco
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ros_aruco_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ros_aruco_generate_messages ros_aruco_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" NAME_WE)
add_dependencies(ros_aruco_generate_messages_eus _ros_aruco_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_aruco_geneus)
add_dependencies(ros_aruco_geneus ros_aruco_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_aruco_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ros_aruco
  "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/TransformStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_aruco
)

### Generating Services

### Generating Module File
_generate_module_lisp(ros_aruco
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_aruco
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ros_aruco_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ros_aruco_generate_messages ros_aruco_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" NAME_WE)
add_dependencies(ros_aruco_generate_messages_lisp _ros_aruco_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_aruco_genlisp)
add_dependencies(ros_aruco_genlisp ros_aruco_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_aruco_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ros_aruco
  "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/TransformStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_aruco
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ros_aruco
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_aruco
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ros_aruco_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ros_aruco_generate_messages ros_aruco_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" NAME_WE)
add_dependencies(ros_aruco_generate_messages_nodejs _ros_aruco_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_aruco_gennodejs)
add_dependencies(ros_aruco_gennodejs ros_aruco_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_aruco_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ros_aruco
  "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/TransformStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_aruco
)

### Generating Services

### Generating Module File
_generate_module_py(ros_aruco
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_aruco
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ros_aruco_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ros_aruco_generate_messages ros_aruco_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/mh/catkin_ws/src/ros_aruco/msg/aruco_tf_id.msg" NAME_WE)
add_dependencies(ros_aruco_generate_messages_py _ros_aruco_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_aruco_genpy)
add_dependencies(ros_aruco_genpy ros_aruco_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_aruco_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_aruco)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_aruco
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(ros_aruco_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_aruco)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_aruco
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(ros_aruco_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_aruco)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_aruco
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(ros_aruco_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_aruco)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_aruco
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(ros_aruco_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_aruco)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_aruco\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_aruco
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(ros_aruco_generate_messages_py geometry_msgs_generate_messages_py)
endif()
