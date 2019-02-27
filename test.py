#!/usr/bin/env python
import rospy
import os
import cantools
from can_msgs.msg import Frame
from chassis_msgs.msg import Chassis

class can_parser:

    def __init__(self):

        script_dir = os.path.dirname(__file__)
        can_db_path = os.path.join(script_dir, '../DBC/CAN1_Chassis_Simple.dbc')
        self.db = cantools.database.load_file(can_db_path)

        rospy.Subscriber("/can/chassis/rx", Frame, self.rx_callback)
        self.rx_pub = rospy.Publisher("/chassis", Chassis, queue_size=1)
        # rospy.Subscriber("/command", Command, self.tx_callback)
        # self.tx_pub = rospy.Publisher("/can/chassis/tx", Frame, queue_size=1)

	self.cdata = Chassis()

    def rx_callback(self, data):
        try:
            signals = self.db.decode_message(data.id, data.data)
        except KeyError:
            return

	if data.id == 544:
		self.cdata.cyl_pres = signals['CYL_PRES']
		self.cdata.lat_accel = signals['LAT_ACCEL']
		self.cdata.long_accel = signals['LONG_ACCEL']
		self.cdata.yaw_rate = signals['YAW_RATE']
	elif data.id == 897:
		self.cdata.cf_mdps_currmode = signals['CF_Mdps_CurrMode']
		self.cdata.cf_mdps_wlmp = signals['CF_Mdps_WLmp']
		self.cdata.cr_mdps_drvtq = signals['CR_Mdps_DrvTq']
		self.cdata.cr_mdps_strang = signals['CR_Mdps_StrAng']
	elif data.id == 320:
		self.cdata.cf_yrs_ax = signals['CF_Yrs_Ax']
	elif data.id == 356:
		self.cdata.cf_esc_act = signals['CF_Esc_Act']
		self.cdata.cf_esc_ctrmode = signals['CF_Esc_CtrMode']
		self.cdata.cf_esc_def = signals['CF_Esc_Def']
		self.cdata.cr_esc_strtqreq = signals['CR_Esc_StrTqReq']
	elif data.id == 902:
		self.cdata.whl_spd_fl = signals['WHL_SPD_FL']
		self.cdata.whl_spd_fr = signals['WHL_SPD_FR']
		self.cdata.whl_spd_rl = signals['WHL_SPD_RL']
		self.cdata.whl_spd_rr = signals['WHL_SPD_RR']
	elif data.id == 1287:
		self.cdata.esc_off_step = signals['ESC_Off_Step']
	elif data.id == 688:
		self.cdata.sas_angle = signals['SAS_Angle']
		self.cdata.sas_speed = signals['SAS_Speed']
	elif data.id == 593:
		self.cdata.cf_mdps_def = signals['CF_Mdps_Def']
		self.cdata.cr_mdps_outtq = signals['CR_Mdps_OutTq']
		self.cdata.cr_mdps_strcoltq = signals['CR_Mdps_StrColTq']
		self.cdata.cr_mdps_strtq = signals['CR_Mdps_StrTq']
	elif data.id == 304:
		self.cdata.cr_yrs_latac = signals['CR_Yrs_LatAc']
		self.cdata.cr_yrs_yr = signals['CR_Yrs_Yr']

    # def tx_callback(self, data):
    #     try:
    #         message = self.db.encode_mssage()
    #     except KeyError:
    #             return

def main():

    cp = can_parser()
    rospy.init_node('chassis_can_parser', anonymous=False)

    rate = rospy.Rate(50) # 50hz
    while not rospy.is_shutdown():
	cp.cdata.header.stamp = rospy.Time.now()
        rospy.loginfo(cp.cdata)
        cp.rx_pub.publish(cp.cdata)
        rate.sleep()

if __name__ == '__main__':
	main()
