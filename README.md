
Command to launch:
```bash
ros2 launch robot_localization ekf.launch.py
# headless (no RViz)
ros2 launch robot_localization ekf.launch.py launch_rviz:=false
```

How the EKF works (brief):
- `ekf_node` fuses odometry (from `diff_odom` — differential drive estimator), IMU, and optionally LiDAR data to produce a single, smoothed pose and velocity estimate (published as `/odometry/filtered`).
- It maintains a state vector (pose, orientation, linear/angular velocities), predicts state with a process model, then corrects using sensor measurements and configured covariances.
- Inputs (odom, IMU, LiDAR) and which state elements are used are controlled by `params/grasshopper_ekf.yaml` (`odom0`, `imu0`, optional `pose0` for LiDAR, their `_config` masks, covariances, and frame names).
