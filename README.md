# ROS2 Gazebo Study Workspace

## 프로젝트 목적

ROS2와 Gazebo 기반의 로봇 시뮬레이션 및 자율주행 시스템 학습을 위한 Workspace이다.

현재 목표:

* Gazebo 시뮬레이션 환경 이해
* ROS2 Topic / Node 구조 학습
* SLAM 및 Navigation 학습
* Vision AI 및 YOLO 연동
* 실내 자율주행 로봇 시스템 구축

---

## Workspace 구조

```text
robot_ws
├── src
│   └── gazebo_tutorial
├── build
├── install
└── log
```

---

## Package 구조

```text
gazebo_tutorial
├── launch
├── models
├── rviz
├── worlds
├── package.xml
├── setup.py
└── setup.cfg
```

---

## 개발 환경

* Ubuntu 22.04 (WSL2)
* ROS2 Humble
* Gazebo
* Python 3

---

## ROS2 환경 활성화

```bash
source /opt/ros/humble/setup.bash
```

또는 alias 사용:

```bash
humble
```

---

## Workspace Build

```bash
cd ~/robot_ws
colcon build
```

---

## Gazebo 실행

```bash
gazebo
```

또는:

```bash
gazebo ~/robot_ws/src/gazebo_tutorial/worlds/empty.world
```

---

