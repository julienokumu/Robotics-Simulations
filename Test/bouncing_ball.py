import mujoco
import numpy as np

# Load the MJCF model
model = mujoco.MjModel.from_xml_path("ball.xml")
data = mujoco.MjData(model)

# Simulate for 1000 steps
for _ in range(1000):
    mujoco.mj_step(model, data)  # Advance simulation by one step
    print(f"Ball height: {data.qpos[2]:.3f}")  # Print z-position of the ball

# Optional: Visualize (requires GLFW or similar; may need additional setup)
import mujoco.viewer
mujoco.viewer.launch(model)  # Opens a window to show the bouncing ball
