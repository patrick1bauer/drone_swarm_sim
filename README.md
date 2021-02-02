# Drone Swarm Sim

# Installation

1. Navigate to /home/ directory
2. Create a new directory /home/noah/catkin_ws/
```bash
mkdir noah/catkin_ws/
```
3. Enter the new catkin_ws directory
```bash
cd noah/catkin_ws
```
4. Make a new git repository
```bash
git init
```
5. Pull the drone swarm sim repository
```bash
git pull https://github.com/patrick1bauer/drone_swarm_sim.git 
```
6. Source ROS files
```bash
source /opt/ros/<distro>/setup.bash
```
7. Make the catkin workspace
```bash
catkin_make
```
8. Source the build
```bash
source devel/setup.bash
```
9. Make sure ROS_PACKAGE_PATH environment variable includes the directory you're in.
```bash
echo $ROS_PACKAGE_PATH
```