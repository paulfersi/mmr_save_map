from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node 

import os

def generate_launch_description():

   
    config = os.path.join(
        get_package_share_directory("save_map"),
        "config",
        "save_map.yaml"
    )

    return LaunchDescription(
        [
            Node(
                package='save_map',
                executable='save_map',
                name='save_map',
		        output='screen',
                parameters=[config]
            )
        ]
    )