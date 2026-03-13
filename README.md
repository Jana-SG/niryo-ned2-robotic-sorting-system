# Niryo Ned2 Automated Sorting System

This project presents an automated robotic production-line sorting system using the Niryo Ned2 robotic arm. The system simulates a real-world industrial workflow where objects move along a conveyor belt, are detected using sensors and vision, and are then picked, classified, and sorted by the robot arm.

## Project Components
- Niryo Ned2 robotic arm
- Adaptive gripper
- Conveyor belt
- Niryo vision camera
- IR sensor
- Workspace marker
- Blockly control logic
- Python control script using Niryo ROS wrapper

## Repository Structure
- `code/` → Python script for robot execution
- `blockly/` → Blockly screenshots of the logic flow
- `docs/` → project report and presentation
- `images/` → additional visuals

## Main Features
- Conveyor-based object handling
- Vision-guided color detection
- Pick-and-place automation
- Color-based sorting
- Stack placement logic for red and blue objects

## Technologies Used
- Python
- ROS / Niryo ROS Wrapper
- Blockly
- Niryo Studio / Niryo ecosystem

## How It Works
1. Robot calibrates automatically
2. Conveyor is initialized
3. Objects are moved into observation area
4. Vision system detects object color
5. Robot picks and places based on color
6. Stack counters are updated

## Authors
University of Jordan  
Artificial Intelligence Department  
Intelligent Robotics Project
