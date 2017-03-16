#!/usr/bin/env python


PACKAGE = 'dynamic_tutorials'
import roslib;roslib.load_manifest(PACKAGE)
import rospy
import dynamic_reconfigure.client


from std_msgs.msg import String , Bool , Int16   	


def callback(config):
	global pub,Zw,aw,bw,cw,dw,global_name,manual_name, parked_name, supervisory_name, autonomous_name, client
	# button_status_
	print config
	global_name = config['Master']
	manual_name = config['Manual']
	parked_name = config['Parked']
	supervisory_name = config['Supervisory']
	autonomous_name = config['Autonomous']

automode_status_pub = rospy.Publisher('/scooter/button_state_automode', Bool)   
emergency_status_pub = rospy.Publisher('/scooter/button_state_emergency', Bool)	#"/scooter/" needed? 
button_status_pub = rospy.Publisher('/scooter/button_status', String)
control_station_pub = rospy.Publisher('/scooter/control_station', Bool) #is the topic correct? how to create the topic
#stm_linear_x_pub = rospy.Publisher('/scooter/stm_linear_x', Int16)
#stm_angle_pub = rospy.Publisher('/scooter/stm_angle', Int16)

automode_status = Bool(False)
emergency_status = Bool(False)
button_status_string = String("nothing")
control_station_status = Bool(False)

#int stm_linear_x_=90  
#int stm_angle_=90
#int joy_linear_x_=90
#int joy_angle_=90
#double pp_angle_=0.0
#double cmd_linear_x_ = 0.0
stm_linear_x_=90  
stm_angle_=90
joy_linear_x_=90
joy_angle_=90
pp_angle_= 0.0
cmd_linear_x_ = 0.0

if __name__ == "__main__":
	rospy.init_node("dynamic_client")
	rospy.wait_for_service("/dynamic_tutorials/set_parameters")
	client = dynamic_reconfigure.client.Client("dynamic_tutorials", timeout=30, config_callback=callback)
	r = rospy.Rate(50)					#Should the rate be 50?

	global_name = False
	manual_name = False
	parked_name = False
	supervisory_name = False
	autonomous_name = False
	
	while not rospy.is_shutdown():	     	
		if global_name == True:
			control_station_status.data = True

			if manual_name == True and parked_name == True and supervisory_name == True and autonomous_name == True:      #do we have to put stm_linear_x and angle here for all the nothing
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing" 
			elif manual_name == True and parked_name == True and supervisory_name == True and autonomous_name == False:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"
			elif manual_name == True and parked_name == True and supervisory_name == False and autonomous_name == True:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"
			elif manual_name == True and parked_name == True and supervisory_name == False and autonomous_name == False:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"
			elif manual_name == True and parked_name == False and supervisory_name == True and autonomous_name == True:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"
			elif manual_name == True and parked_name == False and supervisory_name == True and autonomous_name == False:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"
			elif manual_name == True and parked_name == False and supervisory_name == False and autonomous_name == True:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"

			elif manual_name == True and parked_name == False and supervisory_name == False and autonomous_name == False:		#manual
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "Manual"
				#stm_linear_x_=joy_linear_x_
				#stm_angle_=joy_angle_
			
			elif manual_name == False and parked_name == True and supervisory_name == True and autonomous_name == True:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"
			elif manual_name == False and parked_name == True and supervisory_name == True and autonomous_name == False:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"	
			elif manual_name == False and parked_name == True and supervisory_name == False and autonomous_name == True:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"

			elif manual_name == False and parked_name == True and supervisory_name == False and autonomous_name == False:		#parked
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "stop"
				#stm_linear_x_=90
				#stm_angle_=90

			elif manual_name == False and parked_name == False and supervisory_name == True and autonomous_name == True:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"

			elif manual_name == False and parked_name == False and supervisory_name == True and autonomous_name == False:		#supervisory
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "Supervisory"
				#stm_linear_x_=joy_linear_x_
				#stm_angle_=joy_angle_

			elif manual_name == False and parked_name == False and supervisory_name == False and autonomous_name == True:		#autonomous
				automode_status.data = True																						#need a callback for cmd_linear_x_ and pp_angle_
				emergency_status.data = False
				button_status_string.data = "Auto"
				#stm_linear_x_=Int(180*(cmd_linear_x_+1)/2)
				#stm_angle_=Int(pp_angle_*180/3.14159)+90

			elif manual_name == False and parked_name == False and supervisory_name == False and autonomous_name == False:
				automode_status.data = False
				emergency_status.data = False
				button_status_string.data = "nothing"

			button_status_pub.publish(button_status_string)
			automode_status_pub.publish(automode_status)
			emergency_status_pub.publish(emergency_status)
			control_station_pub.publish(control_station_status)
			#stm_linear_x_pub.publish(stm_linear_x_)
			#stm_angle_pub.publish(stm_angle_)

		else:

			control_station_status.data = False
			control_station_pub.publish(control_station_status)

		r.sleep()
