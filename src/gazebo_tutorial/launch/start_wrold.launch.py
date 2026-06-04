import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node


def generate_launch_description():
    pkg_path = get_package_share_directory('gazebo_tutorial')
    tb3_description_pkg = get_package_share_directory('turtlebot3_description')

    TURTLEBOT3_MODEL = os.environ.get('TURTLEBOT3_MODEL', 'burger')

    world_path = os.path.join(pkg_path, 'worlds', 'warehouse.world')
    models_path = os.path.join(pkg_path, 'models')
    # Use local black-coloured URDF for burger; fall back to upstream for other models
    if TURTLEBOT3_MODEL == 'burger':
        urdf_path = os.path.join(pkg_path, 'urdf', 'turtlebot3_burger_black.urdf')
    else:
        urdf_path = os.path.join(
            tb3_description_pkg, 'urdf', f'turtlebot3_{TURTLEBOT3_MODEL}.urdf'
        )

    existing = os.environ.get('GAZEBO_MODEL_PATH', '')
    ros_share = '/opt/ros/humble/share'
    gazebo_model_path = ':'.join(filter(None, [models_path, ros_share, existing]))

    with open(urdf_path, 'r') as f:
        robot_description = f.read()

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
            '-entity', f'turtlebot3_{TURTLEBOT3_MODEL}',
            '-topic', 'robot_description',
            '-x', '-5.0',
            '-y', '-5.0',
            '-z', '0.01',
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        TimerAction(period=3.0, actions=[spawn_turtlebot]),
    ])
