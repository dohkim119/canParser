# Environment & Libraries

envHeader = ['#!/usr/bin/env python']
msgHeaderFrom = ['from']
msgHeaderImport = ['import']

# Class
classHeader = ['class']

# Function
initFunction = ['def __init__(self):']
scriptDIR = ['script_dir = os.path.dirname(__file__)']
canDBPath = ['can_db_path = os.path.join']
script_dir = ['script_dir']

selfDB = ['self.db = cantools.database.load_file(can_db_path)']
subscriber = ['rospy.Subscriber']
publisher = ['self.rx_pub = rospy.Publisher']

callBackFunc = ['self.rx_callback']

queueSize = ['queue_size=1']

cdata = ['self.cdata']

rx_callback = ['def rx_callback(self, data):']

tryVariable = ['try:']
exceptKeyError = ['except KeyError:']
decode_message = ['signals = self.db.decode_message(data.id, data.data)']
returnVariable = ['return']

#Body
conditional_if = ['if data.id == ']
conditional_elif = ['elif data.id == ']
variable = ['self.data.']
signals_begin = ['signals', '[', '\'']
signals_end = ['\'', ']', '\n']

#Main
mainFunction = ['def main():']
classVariable = ['cp = can_parser()']
initNode = ['rospy.init_node']
anonymousVariable = ['anonymous']
rateVariable = ['rate = rospy.Rate']

shutdownCondition = ['while not rospy.is_shutdown():']
headerStamp = ['cp.cdata.header.stamp = rospy.Time.now()']

logInfoVariable = ['rospy.loginfo']
cpCdata = ['cp.cdata']

publishVariable = ['cp.rx_pub.publish(cp.cdata)']
sleepVariable = ['rate.sleep()']

#Main Conditional
mainIF = ['if __name__ == ', '\'', '__main__', '\'', ':']
mainVariable = ['main()']


# basicVariable
space = [' ']
comma = [', ']
dot = ['.']
equal = [' = ']
nospaceEqual = ['=']
singleQuote = ['\'']
doubleQuote = ['\"']

colon = [':']
indentation = ['    ']
doubleIndentation = ['        ']
tripleIndentation = ['            ']
parenthesisOpen = ['(']
parenthesisClose = [')']