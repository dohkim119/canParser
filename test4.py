#!/usr/bin/env python
import rospy
import os
import cantools
from can_msgs.msg import Frame
from mobileye_msgs.msg import Mobileye
from mobileye_msgs.msg import ObstacleInfo

class can_parser:

    def __init__(self):

        script_dir = os.path.dirname(__file__)
        can_db_path = os.path.join(script_dir, '../DBC/CAN2_TRW.dbc')
        self.db = cantools.database.load_file(can_db_path)

        rospy.Subscriber("/can/mobileye/rx", Frame, self.rx_callback)
        self.rx_pub = rospy.Publisher("/mobileye", Mobileye, queue_size=1)

        self.cdata = Mobileye()
        self.cdata.max_obstacles = 10
        self.cdata.obstacle = [ObstacleInfo()]*10

    def rx_callback(self, data):
        try:
            signals = self.db.decode_message(data.id, data.data)
            # rospy.loginfo(data.id)
        except KeyError:
            return

	if data.id == 1793:
		self.cdata.obstacle[0].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[0].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[0].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[0].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[0].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[0].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[0].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1794:
		self.cdata.obstacle[0].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[0].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[0].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[0].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[0].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[0].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[0].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[0].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1795:
		self.cdata.obstacle[0].angle_std = signals['AngleSTD']
		self.cdata.obstacle[0].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[0].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[0].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[0].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1796:
		self.cdata.obstacle[1].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[1].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[1].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[1].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[1].obstacle_pos_y = signals['ObstaclePosY']
	elif data.id == 1797:
		self.cdata.obstacle[1].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[1].obstacle_vel_x = signals['ObstacleVelX']
		self.cdata.obstacle[1].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[1].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[1].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[1].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[1].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[1].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[1].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[1].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1798:
		self.cdata.obstacle[1].angle_std = signals['AngleSTD']
		self.cdata.obstacle[1].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[1].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[1].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[1].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1799:
		self.cdata.obstacle[2].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[2].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[2].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[2].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[2].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[2].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[2].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1800:
		self.cdata.obstacle[2].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[2].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[2].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[2].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[2].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[2].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[2].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[2].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1801:
		self.cdata.obstacle[2].angle_std = signals['AngleSTD']
		self.cdata.obstacle[2].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[2].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[2].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[2].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1802:
		self.cdata.obstacle[3].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[3].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[3].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[3].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[3].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[3].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[3].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1803:
		self.cdata.obstacle[3].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[3].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[3].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[3].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[3].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[3].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[3].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[3].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1804:
		self.cdata.obstacle[3].angle_std = signals['AngleSTD']
		self.cdata.obstacle[3].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[3].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[3].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[3].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1805:
		self.cdata.obstacle[4].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[4].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[4].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[4].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[4].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[4].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[4].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1806:
		self.cdata.obstacle[4].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[4].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[4].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[4].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[4].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[4].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[4].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[4].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1807:
		self.cdata.obstacle[4].angle_std = signals['AngleSTD']
		self.cdata.obstacle[4].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[4].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[4].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[4].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1808:
		self.cdata.obstacle[5].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[5].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[5].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[5].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[5].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[5].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[5].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1809:
		self.cdata.obstacle[5].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[5].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[5].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[5].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[5].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[5].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[5].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[5].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1810:
		self.cdata.obstacle[5].angle_std = signals['AngleSTD']
		self.cdata.obstacle[5].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[5].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[5].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[5].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1811:
		self.cdata.obstacle[6].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[6].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[6].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[6].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[6].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[6].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[6].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1812:
		self.cdata.obstacle[6].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[6].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[6].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[6].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[6].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[6].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[6].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[6].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1813:
		self.cdata.obstacle[6].angle_std = signals['AngleSTD']
		self.cdata.obstacle[6].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[6].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[6].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[6].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1814:
		self.cdata.obstacle[7].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[7].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[7].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[7].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[7].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[7].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[7].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1815:
		self.cdata.obstacle[7].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[7].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[7].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[7].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[7].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[7].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[7].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[7].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1816:
		self.cdata.obstacle[7].angle_std = signals['AngleSTD']
		self.cdata.obstacle[7].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[7].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[7].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[7].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1817:
		self.cdata.obstacle[8].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[8].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[8].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[8].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[8].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[8].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[8].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1818:
		self.cdata.obstacle[8].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[8].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[8].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[8].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[8].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[8].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[8].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[8].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1819:
		self.cdata.obstacle[8].angle_std = signals['AngleSTD']
		self.cdata.obstacle[8].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[8].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[8].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[8].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1820:
		self.cdata.obstacle[9].longitudinal_distance_std = signals['LongitudinalDistanceSTD']
		self.cdata.obstacle[9].obstacle_id = signals['ObstacleID']
		self.cdata.obstacle[9].obstacle_measured = signals['ObstacleMeasured']
		self.cdata.obstacle[9].obstacle_pos_x = signals['ObstaclePosX']
		self.cdata.obstacle[9].obstacle_pos_y = signals['ObstaclePosY']
		self.cdata.obstacle[9].obstacle_valid = signals['ObstacleValid']
		self.cdata.obstacle[9].obstacle_vel_x = signals['ObstacleVelX']
	elif data.id == 1821:
		self.cdata.obstacle[9].blinker_info = signals['BlinkerInfo']
		self.cdata.obstacle[9].inverse_ttc = signals['Inverse_TTC']
		self.cdata.obstacle[9].obstacle_age = signals['ObstacleAge']
		self.cdata.obstacle[9].obstacle_brake_lights = signals['ObstacleBrakeLights']
		self.cdata.obstacle[9].obstacle_lane = signals['ObstacleLane']
		self.cdata.obstacle[9].obstacle_status = signals['ObstacleStatus']
		self.cdata.obstacle[9].obstacle_type = signals['ObstacleType']
		self.cdata.obstacle[9].obstacle_width = signals['ObstacleWidth']
	elif data.id == 1822:
		self.cdata.obstacle[9].angle_std = signals['AngleSTD']
		self.cdata.obstacle[9].obstacle_angle_left = signals['ObstacleAngleLeft']
		self.cdata.obstacle[9].obstacle_angle_rate = signals['ObstacleAngleRate']
		self.cdata.obstacle[9].obstacle_angle_right = signals['ObstacleAngleRight']
		self.cdata.obstacle[9].obstacle_accel_x = signals['Obstacle_Accel_X']
	elif data.id == 1838:
		self.cdata.left_lane.curvature = signals['Curvature']
		self.cdata.left_lane.curvature_derivative = signals['Curvature_Derivative']
		self.cdata.left_lane.lane_location_type = signals['Lane_Location_Type']
		self.cdata.left_lane.lane_type = signals['Lane_Type']
		self.cdata.left_lane.position = signals['Position']
		self.cdata.left_lane.quaility = signals['Quaility']
	elif data.id == 1839:
		self.cdata.left_lane.heading_angle = signals['Heading_Angle']
		self.cdata.left_lane.lane_crossing = signals['Lane_Crossing']
		self.cdata.left_lane.lane_view_range_end = signals['Lane_View_Range_End']
		self.cdata.left_lane.lane_view_range_start = signals['Lane_View_Range_Start']
		self.cdata.left_lane.lane_mark_color = signals['Lane_mark_color']
		self.cdata.left_lane.position_std = signals['Position_STD']
		self.cdata.left_lane.tlc = signals['TLC']
		self.cdata.left_lane.width_marking = signals['Width_marking']
	elif data.id == 1840:
		self.cdata.right_lane.curvature = signals['Curvature']
		self.cdata.right_lane.curvature_derivative = signals['Curvature_Derivative']
		self.cdata.right_lane.lane_location_type = signals['Lane_Location_Type']
		self.cdata.right_lane.lane_type = signals['Lane_Type']
		self.cdata.right_lane.position = signals['Position']
		self.cdata.right_lane.quaility = signals['Quaility']
	elif data.id == 1841:
		self.cdata.right_lane.heading_angle = signals['Heading_Angle']
		self.cdata.right_lane.lane_crossing = signals['Lane_Crossing']
		self.cdata.right_lane.lane_view_range_end = signals['Lane_View_Range_End']
		self.cdata.right_lane.lane_view_range_start = signals['Lane_View_Range_Start']
		self.cdata.right_lane.lane_mark_color = signals['Lane_mark_color']
		self.cdata.right_lane.position_std = signals['Position_STD']
		self.cdata.right_lane.tlc = signals['TLC']
		self.cdata.right_lane.width_marking = signals['Width_marking']
	elif data.id == 1844:
		self.cdata.next_left_lane.curvature = signals['Curvature']
		self.cdata.next_left_lane.curvature_derivative = signals['Curvature_Derivative']
		self.cdata.next_left_lane.lane_location_type = signals['Lane_Location_Type']
		self.cdata.next_left_lane.lane_type = signals['Lane_Type']
		self.cdata.next_left_lane.position = signals['Position']
		self.cdata.next_left_lane.quaility = signals['Quaility']
	elif data.id == 1845:
		self.cdata.next_left_lane.heading_angle = signals['Heading_Angle']
		self.cdata.next_left_lane.lane_crossing = signals['Lane_Crossing']
		self.cdata.next_left_lane.lane_view_range_end = signals['Lane_View_Range_End']
		self.cdata.next_left_lane.lane_view_range_start = signals['Lane_View_Range_Start']
		self.cdata.next_left_lane.lane_mark_color = signals['Lane_mark_color']
		self.cdata.next_left_lane.position_std = signals['Position_STD']
		self.cdata.next_left_lane.tlc = signals['TLC']
		self.cdata.next_left_lane.width_marking = signals['Width_marking']
	elif data.id == 1846:
		self.cdata.next_right_lane.curvature = signals['Curvature']
		self.cdata.next_right_lane.curvature_derivative = signals['Curvature_Derivative']
		self.cdata.next_right_lane.lane_location_type = signals['Lane_Location_Type']
		self.cdata.next_right_lane.lane_type = signals['Lane_Type']
		self.cdata.next_right_lane.position = signals['Position']
		self.cdata.next_right_lane.quaility = signals['Quaility']
	elif data.id == 1847:
		self.cdata.next_right_lane.heading_angle = signals['Heading_Angle']
		self.cdata.next_right_lane.lane_crossing = signals['Lane_Crossing']
		self.cdata.next_right_lane.lane_view_range_end = signals['Lane_View_Range_End']
		self.cdata.next_right_lane.lane_view_range_start = signals['Lane_View_Range_Start']
		self.cdata.next_right_lane.lane_mark_color = signals['Lane_mark_color']
		self.cdata.next_right_lane.position_std = signals['Position_STD']
		self.cdata.next_right_lane.tlc = signals['TLC']
		self.cdata.next_right_lane.width_marking = signals['Width_marking']


    # def tx_callback(self, data):
    #     try:
    #         message = self.db.encode_mssage()
    #     except KeyError:
    #             return

def main():

    cp = can_parser()
    rospy.init_node('mobileye_can_parser', anonymous=False)

    rate = rospy.Rate(30) # 30hz
    while not rospy.is_shutdown():
	cp.cdata.header.stamp = rospy.Time.now()
        rospy.loginfo(cp.cdata.left_lane)
        # rospy.loginfo(cp.cdata.obstacle[5])
        rospy.loginfo(cp.cdata.right_lane)
        cp.rx_pub.publish(cp.cdata)
        rate.sleep()

if __name__ == '__main__':
	main()
