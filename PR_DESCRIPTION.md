Title: Add EKF launch, parameters, and RViz config

Summary
-------
This PR adds a simple EKF integration for the Grasshopper robot:

- `launch/ekf.launch.py` — Launches `ekf_node`, three static transforms, and RViz.
- `params/grasshopper_ekf.yaml` — EKF parameter file tuned conservatively for testing.
- `rviz/ekf_odometry.rviz` — Minimal RViz configuration (Fixed frame = `odom`).

Notes
-----
- The launch expects `robot_localization` to be available in the workspace and will load `params/grasshopper_ekf.yaml` from this package.
- RViz file is placed under `robot_localization/rviz/ekf_odometry.rviz` and is referenced by the launch.
- The EKF subscribes to `/odom` and `/bno055/imu` topics by default. Adjust topic names in the parameters if your robot uses different topic namespaces.

How to test
-----------
1. Build the workspace:

```bash
colcon build --packages-select robot_localization
source install/local_setup.bash
```

2. Launch the EKF locally (RViz will open):

```bash
ros2 launch robot_localization ekf.launch.py
```

3. Verify that `/odometry/filtered` is published and RViz shows `odom`/`odometry/filtered` topics.

Follow-ups
----------
- Parameter tuning for your specific sensors is recommended.
- Optional: make the RViz path configurable via a launch argument.

Reviewer checklist
------------------
- [ ] Confirm `params/grasshopper_ekf.yaml` fits your topic names and frames.
- [ ] Run the launch and verify `ekf_node` starts without errors.
- [ ] Optionally test on a bag or with live sensors.
