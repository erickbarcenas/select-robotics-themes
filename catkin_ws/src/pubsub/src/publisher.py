#!/user/bin/env python
import rospy
from pubsub.msg import Status
from std_msgs import msg

def publisher():
    pub = rospy.Publisher('pubtopic', Status, queue_size=10)
    rospy.init_node('pubnode', anonymous=False)
    r = rospy.Rate(10)
    msg = Status()
    msg.estado = 'ok'
    msg.codigo = 0

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == "__main__":
    publisher()