import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    global_parameters = os.path.join(
        get_package_share_directory('my_robot_bringup'),
        'config',
        'global_params.yaml'
    )

    global_param_node = Node(
        package='my_robot_bringup',
	#node exe -> executable
        node_executable='global_parameter_server',
        name='global_parameter_server',
        parameters=[global_parameters]
    )

    ld.add_action(global_param_node)

    return ld
