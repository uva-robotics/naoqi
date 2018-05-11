#! /usr/bin/python
"""
Transform AudioBuffer Naoqi messages to AudioData audio_common messages.
"""
import rospy
import numpy
from naoqi_bridge_msgs.msg import AudioBuffer
from audio_common_msgs.msg import AudioData

AUDIO_COMMON_TOPIC = '/audio'
NAOQI_AUDIO_TOPIC = '/pepper_robot/naoqi_driver/audio'

class Converter():
    def __init__(self):
        rospy.loginfo("Setting up pub and sub")
        self.pub = rospy.Publisher(AUDIO_COMMON_TOPIC, AudioData)
        self.sub = rospy.Subscriber(NAOQI_AUDIO_TOPIC, AudioBuffer, self.callback)

    def callback(self, data):
        rospy.loginfo("Callback received!")
        ad = AudioData()
        data_uint8 = numpy.array(data.data, dtype=numpy.uint8)
        ad.data = data_uint8.tolist()
        self.pub.publish(ad)

if __name__=="__main__":

    rospy.init_node('convert_nao_audio_msg')

    converter = Converter()
    rospy.spin()
