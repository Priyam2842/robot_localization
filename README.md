robot_localization — EKF integration (minimal)

Architecture
------------
- `launch/ekf.launch.py` — Starts `ekf_node`, three static TF publishers, and (optionally) RViz.
- `params/grasshopper_ekf.yaml` — EKF parameter file (loads odom and IMU inputs).
- `rviz/ekf_odometry.rviz` — Minimal RViz configuration (fixed frame: `odom`).

Instructions
------------
1. Build the workspace and source:

```bash
colcon build --packages-select robot_localization
source install/local_setup.bash
```

2. Launch the EKF (RViz opens by default):

```bash
ros2 launch robot_localization ekf.launch.py
```

3. Verify `/odometry/filtered` is published and review RViz.

Notes
-----
- Adjust topic/frame names in `params/grasshopper_ekf.yaml` if your robot uses different topics.
- To disable RViz (headless), set the launch argument `launch_rviz:=false`.
