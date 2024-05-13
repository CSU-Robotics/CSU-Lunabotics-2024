#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def video_publisher():
    rospy.init_node('video_publisher', anonymous=True)
    video_pub = rospy.Publisher('video_topic', Image, queue_size=10)
    rate = rospy.Rate(10)  # adjust the publishing rate if needed

    cap = cv2.VideoCapture(0)  # adjust the camera index if needed
    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret:
            ros_image = bridge.cv2_to_imgmsg(frame, "bgr8")
            video_pub.publish(ros_image)
        rate.sleep()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        video_publisher()
    except rospy.ROSInterruptException:
        pass

