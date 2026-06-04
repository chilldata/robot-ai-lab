from setuptools import find_packages, setup

package_name = 'gazebo_tutorial'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/start_wrold.launch.py']),
        ('share/' + package_name + '/worlds', ['worlds/warehouse.world']),
        ('share/' + package_name + '/models/box_obstacle',
            ['models/box_obstacle/model.sdf', 'models/box_obstacle/model.config']),
        ('share/' + package_name + '/models/cone',
            ['models/cone/model.sdf', 'models/cone/model.config']),
        ('share/' + package_name + '/models/wall',
            ['models/wall/model.sdf', 'models/wall/model.config']),
        ('share/' + package_name + '/urdf',
            ['urdf/turtlebot3_burger_black.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='junghee',
    maintainer_email='wjdgml3834@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
