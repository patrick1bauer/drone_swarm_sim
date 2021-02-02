import rospy
from gazebo_msgs.srv import DeleteModel

# Removes a model from the Gazebo world
def remove_model(model):

	# model must be passed to service as string
	model_str = str(model) 
	
	# Delete model service
	re_model = rospy.ServiceProxy('gazebo/delete_model', DeleteModel)
	
	# Waits on model loader
	rospy.wait_for_service('gazebo/delete_model')
	
	# Removes model from Gazebo world
	re_model(model_str)
	
	
	
	
