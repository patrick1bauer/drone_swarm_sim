# Drone Swarm Sim

# Environment Setup

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
6. Make sure ROS_PACKAGE_PATH environment variable includes the directory you're in.
```bash
echo $ROS_PACKAGE_PATH
```
7. Get the latest TurtleBot3 models into the src folder
```bash
cd src
git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
cd ..
```
8. Get the latest sjtu-drone models into the src folder
```bash
cd src
git clone https://github.com/tahsinkose/sjtu-drone.git
cd ..
```
9. Change the path of the sjtu-drone mesh files:
    In catkin_ws/src/sjtu-drone/urdf/sjtu_drone.urdf file, change the filepath on line 12 to:
    /home/noah/catkin_ws/src/sjtu-drone/meshes/quadrotor_4.stl
    and the filepath on line 18 to:
    /home/noah/catkin_ws/src/sjtu-drone/meshes/quadrotor_4.dae
10. Set the TURTLEBOT3_MODEL environment variable to burger
```bash
export TURTLEBOT3_MODEL=burger
```
11. set the GAZEBO_MODEL_PATH environment variable
```bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/noah/catkin_ws/src/drone_swarm_sim/world/models
```
12. Source ROS files
```bash
source /opt/ros/<distro>/setup.bash
```
13. Make the catkin workspace
```bash
catkin_make
```
14. Source the build
```bash
source devel/setup.bash
```
14. Run the simulation
```bash
roslaunch drone-swarm-sim small_city.launch
```

# Check ROS-Topics are published

1. Open new terminal while the simulation is running
2. List out the published rostopics:
```bash
rostopic list
```
