
#Default Variables

Libraries = ['rospy','os','cantools']

className = 'can_parser'

Message = [
        ['can_msgs.msg', 'Frame'],
        ['mobileye_msgs.msg', 'Mobileye'],
        ['mobileye_msgs.msg','ObstacleInfo'],
    ]


#User-Input

# 1. '__init__' Function Variable


nodeName = 'mobileye_can_parser'

csvFileName = 'mobileye.csv'

dbcPath = '../DBC/CAN2_TRW.dbc'

subscribedTopic = '/can/mobileye/rx'

publishMSG = '/mobileye'
publishMSGType = 'Mobileye'

isCdata = True # True / False
CData = [
        ['max_obstacles', '10'],
        ['obstacle', '[ObstacleInfo()]*10']
]

# 2. 'main' Function Variable

anonymous = False # True / False

rate = '30'

isMultipleLogInfo = True # True / False

logInfo = ['left_lane', 'right_lane']

