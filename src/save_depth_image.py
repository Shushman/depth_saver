#!/usr/bin/env python
PACKAGE = 'depth_saver'
import roslib
roslib.load_manifest(PACKAGE)
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import yaml

class image_saver:

	def __init__(self,topic,file_name):

		self.image_sub = rospy.Subscriber(topic,Image,self.callback)
		self.file_name = file_name
		self.bridge = CvBridge()

	def callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv2(data,desired_encoding="passthrough")
		except CvBridgeError, e:
			print e
			sys.exit(2)
                file_name_txt = self.file_name+'.txt'
                file_name_png = self.file_name+'.png'
                #cv2.imwrite(file_name_png,cv_image)
		img_array = np.asarray(cv_image)
                np.savetxt(file_name_txt,img_array)
		print 'File saving done!'
                raw_input('Wait')
                sys.exit(0)

def main(args):

	#print '{0} and {1}'.format(args[0],args[1])
	i_s = image_saver(args[0],args[1])
	rospy.init_node('depth_saver',anonymous=True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "Shutdown"
	cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv[1:])
