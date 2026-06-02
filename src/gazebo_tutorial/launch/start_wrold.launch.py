from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    pkg_path = get_package_share_directory('gazebo_tutorial')

    world_path = os.path.join(pkg_path, 'worlds', 'warehouse.world')
    models_path = os.path.join(pkg_path, 'models')

    gazebo_model_path = SetEnvironmentVariable(
        name='GAZEBO_MODEL_PATH',
        value=models_path + ':' + os.environ.get('GAZEBO_MODEL_PATH', '')
    )

    gazebo = ExecuteProcess(
        cmd=['gazebo', world_path],
        output='screen'
    )

    return LaunchDescription([
        gazebo_model_path,
        gazebo
    ])
