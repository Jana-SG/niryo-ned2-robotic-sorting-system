# Niryo Ned2 Vision-Guided Sorting System

A vision-guided robotic sorting system built using the **Niryo Ned2 robotic arm**, **Blockly programming**, and **Python ROS control**.

This project simulates an automated production-line environment where objects move along a conveyor belt, are detected using sensors and the robot’s vision system, and are picked and sorted based on their color.

---

# System Demonstration

## System Setup

![System Setup](images/system_setup.jpg)

*Niryo Ned2 robotic sorting system with conveyor, IR sensor, and colored cubes.*

---

## System Build Video
[Watch the build process](images/system_build_and_demo.mp4)

## System Overview

The robotic system performs automated **pick-and-place sorting** using the following workflow:

1. Robot performs **automatic calibration**
2. Conveyor moves objects into the workspace
3. **IR sensor detects object arrival**
4. Robot moves to an **observation pose**
5. Vision system identifies **object color**
6. Robot picks the object
7. Object is placed in the correct sorting location
8. Stacks are updated dynamically

---

## Sorting Logic

Objects are sorted based on detected color.

| Color | Action |
|------|------|
| 🔴 Red | Pick and place into **Red stack** |
| 🔵 Blue | Pick and place into **Blue stack** |
| 🟢 Green | Move to **discard area** |

Stack height automatically increases after each placement using counters in the code.

Example logic:

```python
place_from_pose(..., 0.115 + Red_stack * 0.01)
```
## Hardware Components

The system includes the following hardware:

- **Niryo Ned2 robotic arm**
- **Adaptive gripper**
- **Conveyor belt**
- **Niryo vision camera**
- **IR sensor**
- **Workspace calibration marker**
- **Colored cubes (simulated objects)**

---

## Software Stack

The project integrates several software tools for robot control, perception, and automation:

- **Python**
- **ROS (Robot Operating System)**
- **Niryo ROS Python Wrapper**
- **Blockly (Niryo Studio)**

Blockly was used to visually design the robot control logic. The Blockly program was then exported as Python code using the Niryo ROS wrapper.

---

## Code Explanation

The Python script was generated from **Blockly logic** and executed using the **Niryo ROS Python wrapper**.

The code coordinates robot movement, sensor detection, conveyor control, and vision-based object sorting.

---

### Robot Initialization

```python
n = NiryoRosWrapper()
n.calibrate_auto()
```
This connects to the Niryo Ned2 robot and performs **automatic calibration**, ensuring that all joints and reference frames are properly initialized before the robot begins executing tasks.

Calibration is necessary to guarantee accurate robot positioning during pick-and-place operations.

---

### Conveyor Control

```python
n.control_conveyor(ConveyorID.ID_1, True, 100, ConveyorDirection.BACKWARD)
```
**Conveyor Activation**
This command activates the **conveyor belt**, moving objects toward the robot workspace.

Parameters specify:

- **Conveyor ID** – identifies which conveyor is used
- **Speed** – controls the conveyor movement speed
- **Direction** – determines the movement direction of the conveyor

The conveyor continues running until an object is detected by the IR sensor.

---

## Sensor Detection

```python
while n.digital_read('DIS'):
```
The robot continuously reads the digital input sensor (DI5) connected to the system.
When an object arrives at the detection point:

- The IR sensor changes state
- The robot stops the conveyor
- The robot begins the sorting process

This allows the robot to synchronize its actions with the arrival of objects on the conveyor.

## Observation Position
```python
n.move_pose(...)
```
After stopping the conveyor, the robot moves to a predefined observation pose.
This position is optimized for the vision camera to clearly view objects inside the workspace before attempting a pick operation.

## Vision-Based Picking
```python
n.vision_pick('', 9/1000.0, ObjectShape.ANY, ObjectColor.RED)
```
The robot uses the Niryo vision system to detect objects within the workspace.
The vision module performs:

-object detection
-color identification
-coordinate estimation for picking

The robot then attempts to pick the detected object if it matches the specified color.

### Placement Logic

```python
n.place_from_pose(...)
```
Once an object has been successfully picked, the robot moves to a predefined placement position.
Each color corresponds to a different drop-off location in the sorting area.

### Stack Height Adjustment
Stack counters track how many objects have been placed in each stack.

```python
place_from_pose(..., 0.115 + Red_stack * 0.01)
```
Each new object increases the placement height slightly, allowing objects to stack vertically without collision.
This creates organized stacks for each color category.

### LED Feedback

```python
n.led_ring.solid([153,51,0,0], wait=False)
```
The robot's LED ring changes color to indicate which object has been detected and processed.
This provides a visual indication of the sorting process.

### Continuous Sorting Loop

The entire system operates inside a loop that repeatedly:

1. Moves objects using the conveyor
2. Detects objects using the IR sensor
3. Uses the vision system to identify object color
4. Picks the object with the robotic gripper
5. Places it in the correct sorting location
6. Updates stack counters
7. Restarts the conveyor

This allows the robotic system to perform **continuous automated sorting**.

---

## Blockly Program

The system logic was initially designed using **Blockly in Niryo Studio**, which provides a visual programming interface for robot control.

Blockly blocks were used to implement:

- conveyor control  
- sensor detection  
- color detection  
- robot motion  
- stacking logic  

Screenshots of the Blockly logic are included in the repository.

---

## Example Workflow

1️⃣ Conveyor moves objects into workspace  
2️⃣ IR sensor detects object arrival  
3️⃣ Robot stops the conveyor  
4️⃣ Robot moves to observation position  
5️⃣ Vision system detects object color  
6️⃣ Robot picks the object  
7️⃣ Robot places the object in the correct location  
8️⃣ Conveyor restarts and the process repeats

