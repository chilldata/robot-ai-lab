from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    pkg_path = get_package_share_directory('gazebo_tutorial')

    world_path = os.path.join(pkg_path, 'worlds', 'warehouse.world')
    models_path = os.path.join(pkg_path, 'models')

    existing = os.environ.get('GAZEBO_MODEL_PATH', '')
    gazebo_model_path = models_path + (':' + existing if existing else '')

    gazebo = ExecuteProcess(
        cmd=['gazebo', world_path],
        additional_env={'GAZEBO_MODEL_PATH': gazebo_model_path},
        output='screen'
    )

    return LaunchDescription([
        gazebo
    ])
