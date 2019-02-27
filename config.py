
#Default Variables
Libraries = ['rospy','os','cantools']
className = ['can_parser']

#User-Input
parserName = 'mobileye_can_parser.py'

csvFileName = ['mobileye.csv']

Message = [
        ['can_msgs.msg', 'Frame'],
        ['mobileye_msgs.msg', 'Mobileye'],
        ['mobileye_msgs.msg','ObstacleInfo'],
    ]

dbcPath = ['../DBC/CAN2_TRW.dbc']

subscribedTopic = ['/can/mobileye/rx']


