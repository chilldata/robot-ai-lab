import os

import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    pkg_path = get_package_share_directory('gazebo_tutorial')

    world_path = os.path.join(pkg_path, 'worlds', 'warehouse.world')
    models_path = os.path.join(pkg_path, 'models')
    urdf_path = os.path.join(pkg_path, 'urdf', 'big_robot.urdf')

    existing = os.environ.get('GAZEBO_MODEL_PATH', '')
    ros_share = '/opt/ros/humble/share'
    gazebo_model_path = ':'.join(filter(None, [models_path, ros_share, existing]))

    robot_description = xacro.process_file(urdf_path).toxml()

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
        additional_env={'GAZEBO_MODEL_PATH': gazebo_model_path},
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    spawn_turtlebot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'big_robot',
            '-topic', 'robot_description',
            '-x', '-5.0',
            '-y', '-5.0',
            '-z', '0.20',
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        TimerAction(period=3.0, actions=[spawn_turtlebot]),
    ])
