import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Path to the tuned EKF parameters
    ekf_yaml = os.path.join(
        get_package_share_directory('robot_localization'), 'params', 'grasshopper_ekf.yaml')

    # Path to the RViz config (placed inside this repo's package)
    rviz_config = os.path.join(
        get_package_share_directory('robot_localization'), 'rviz', 'ekf_odometry.rviz')

    return LaunchDescription([
        # ── Launch argument: disable RViz on headless systems ────────────────
        DeclareLaunchArgument(
            'launch_rviz',
            default_value='true',
            description='Set to false to skip RViz (e.g. on headless robot)'
        ),

        # ── EKF: fuses /odom + /bno055/imu → /odometry/filtered ─────────────
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_yaml],
        ),

        # ── Static TF: base_link → base_footprint ────────────────────────────
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_base_footprint',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'base_link', 'base_footprint']
        ),

        # ── Static TF: base_link → laser ─────────────────────────────────────
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_laser',
            arguments=['0.13', '0.0', '0.175', '0.0', '0.0', '0.0', 'base_link', 'laser']
        ),

        # ── Static TF: base_link → cloud ─────────────────────────────────────
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_cloud',
            arguments=['0.13', '0.0', '0.175', '0.0', '0.0', '0.0', 'base_link', 'cloud']
        ),

        # ── RViz2: visualise /odometry/filtered and /odom ────────────────────
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
            condition=IfCondition(LaunchConfiguration('launch_rviz')),
        ),
    ])
