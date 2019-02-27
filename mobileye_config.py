
#Default Variables
Libraries = ['rospy','os','cantools']
className = 'can_parser'

#User-Input
nodeName = 'mobileye_can_parser'

csvFileName = 'mobileye.csv'

Message = [
        ['can_msgs.msg', 'Frame'],
        ['mobileye_msgs.msg', 'Mobileye'],
        ['mobileye_msgs.msg','ObstacleInfo'],
    ]

dbcPath = '../DBC/CAN2_TRW.dbc'

subscribedTopic = '/can/mobileye/rx'

publishMSG = '/mobileye'
publishMSGType = 'Mobileye'

isCdata = True # True / False
CData = [
        ['max_obstacles', '10'],
        ['obstacle', '[ObstacleInfo()]*10']
]

anonymous = False # True / False

rate = '30'

isMultipleLogInfo = True # True / False

logInfo = ['left_lane', 'right_lane']
