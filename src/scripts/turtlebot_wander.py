#!/usr/bin/env python
# This script allows the turtlebot to wander around the map.
# Currently only works for a single turtlebot.
# Needs to be added to launch file so it can automatically execute for each turtlebot


import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan




class TurtlebotWander():
# Thresholds subject to change, we can play around with these numbers
	thr1 = 4
	thr2 = 2
	thr3 = 2
	def __init__(self):
		#initialize node
		rospy.init_node('turtlebot_wander')
	
		rospy.loginfo("CTRL + C to stop Turtlebot")
		rospy.on_shutdown(self.shutdown)
		
		# Publishes velocity to turtlebot
		self.cmd_vel = rospy.Publisher('robot1/cmd_vel', Twist, queue_size=10)
		self.cmd_vel2 = rospy.Publisher('robot2/cmd_vel', Twist, queue_size=10)
		self.cmd_vel3 = rospy.Publisher('robot3/cmd_vel', Twist, queue_size=10)
		self.cmd_vel4 = rospy.Publisher('robot4/cmd_vel', Twist, queue_size=10)
		# Retrieves scanner data
		self.sub = rospy.Subscriber('robot1/scan', LaserScan, self.laserNavigation)
		self.sub2 = rospy.Subscriber('robot2/scan', LaserScan, self.laserNavigation)
		self.sub3 = rospy.Subscriber('robot3/scan', LaserScan, self.laserNavigation)
		self.sub4 = rospy.Subscriber('robot4/scan', LaserScan, self.laserNavigation)
		# Infinite loop
		rospy.spin()
		
	def laserNavigation(self, data):
		print ('range data at 0 deg:  {}'.format(data.ranges[0]))
		print ('range data at 15 deg:  {}'.format(data.ranges[15]))
		print ('range data at 345 deg:  {}'.format(data.ranges[345]))
		
		
		move = Twist()
		
		# No object is scanned within range threshold, turtlebot moves forward
		if data.ranges[0]>self.thr1 and data.ranges[15]>self.thr2 and data.ranges[345]>self.thr3:
			move.linear.x = 0.5
			move.angular.z = 0.0
			print("Going forward")
		# Object is scanned within range threshold, turtlebot rotates and trys to move forward
		else:
			print("Turning")
			move.linear.x = 0.0
			move.angular.z = 1
			# After rotating, checks again if there is obstacle
			if data.ranges[0]>self.thr1 and data.ranges[15]>self.thr2 and data.ranges[345]>self.thr3:
				move.linear.x = 0.5
				move.angular.z = 0.0
				
		self.cmd_vel.publish(move)
		self.cmd_vel2.publish(move)
		self.cmd_vel3.publish(move)
		self.cmd_vel4.publish(move)
		
		
	def shutdown(self):
		rospy.loginfo("Turtlebot shutting down")
		self.cmd_vel.publish(Twist())
		self.cmd_vel2.publish(Twist())
		self.cmd_vel3.publish(Twist())
		self.cmd_vel4.publish(Twist())
		rospy.sleep(1)
	
if __name__ == '__main__':
	try:
		TurtlebotWander()
	except:
		rospy.loginfo("TurtlebotWander node terminated")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


