#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from chassis_config import *
from parsingVariable import *


def createHeader(script):

    # parsing envHeader
    script.writelines(envHeader)
    script.writelines('\n')

    # parsing Libraries
    for num in range(len(Libraries)):
        script.writelines(msgHeaderImport)
        script.writelines(space)
        script.write(Libraries[num])
        script.writelines('\n')

    # parsing Message package and type
    msg = pd.DataFrame(Message, columns=['msgPackage', 'msgType'])

    for msgNum in range(len(msg)):
        script.writelines(msgHeaderFrom)
        script.writelines(space)
        script.writelines(msg.loc[msgNum].msgPackage)
        script.writelines(space)
        script.writelines(msgHeaderImport)
        script.writelines(space)
        script.writelines(msg.loc[msgNum].msgType)
        script.writelines('\n')
    script.writelines('\n')

    createClass(script, msg)

def createClass(script, msg):

    script.writelines(classHeader)
    script.writelines(space)
    script.writelines(className)
    script.writelines(colon)
    script.writelines('\n\n')

    script.writelines(indentation)
    script.writelines(initFunction)
    script.writelines('\n\n')

    script.writelines(indentation)
    script.writelines(indentation)
    script.writelines(scriptDIR)
    script.writelines('\n')

    script.writelines(indentation)
    script.writelines(indentation)
    script.writelines(canDBPath)
    script.writelines(parenthesisOpen)
    script.writelines(script_dir)
    script.writelines(comma)
    script.writelines(singleQuote)
    script.writelines(dbcPath)
    script.writelines(singleQuote)
    script.writelines(parenthesisClose)
    script.writelines('\n')

    script.writelines(indentation)
    script.writelines(indentation)
    script.writelines(selfDB)
    script.writelines('\n\n')

    #Subscriber

    script.writelines(indentation)
    script.writelines(indentation)
    script.writelines(subscriber)
    script.writelines(parenthesisOpen)
    script.writelines(doubleQuote)
    script.writelines(subscribedTopic)
    script.writelines(doubleQuote)
    script.writelines(comma)
    script.writelines(msg.loc[0].msgType)
    script.writelines(comma)
    script.writelines(callBackFunc)
    script.writelines(parenthesisClose)
    script.writelines('\n')

    #Publisher

    script.writelines(indentation)
    script.writelines(indentation)
    script.writelines(publisher)
    script.writelines(parenthesisOpen)
    script.writelines(doubleQuote)
    script.writelines(publishMSG)
    script.writelines(doubleQuote)
    script.writelines(comma)
    script.writelines(publishMSGType)
    script.writelines(comma)
    script.writelines(queueSize)
    script.writelines(parenthesisClose)
    script.writelines('\n\n')

    #Can Data
    script.writelines(doubleIndentation)
    script.writelines(cdata)
    script.writelines(equal)
    script.writelines(msg.loc[1].msgType)
    script.writelines(parenthesisOpen)
    script.writelines(parenthesisClose)
    script.writelines('\n')

    if isCdata:
        cdataMSG = pd.DataFrame(CData, columns=['msgName', 'msgValue'])
        for i in range(len(cdataMSG)):
            script.writelines(doubleIndentation)
            script.writelines(cdata)
            script.writelines(dot)
            script.writelines(cdataMSG.loc[i].msgName)
            script.writelines(equal)
            script.writelines(cdataMSG.loc[i].msgValue)
            script.writelines('\n')
    script.writelines('\n')

    #rx_callback Function
    script.writelines(indentation)
    script.writelines(rx_callback)
    script.writelines('\n')
    script.writelines(doubleIndentation)
    script.writelines(tryVariable)
    script.writelines('\n')
    script.writelines(doubleIndentation)
    script.writelines(indentation)
    script.writelines(decode_message)
    script.writelines('\n\n')
    script.writelines(doubleIndentation)
    script.writelines(exceptKeyError)
    script.writelines('\n')
    script.writelines(tripleIndentation)
    script.writelines(returnVariable)
    script.writelines('\n\n')

def createBody(script):

    csvData = pd.read_csv(csvFileName)
    can_id_list = csvData['ID'].values.tolist()
    can_id = list(set(can_id_list))
    id_length = len(can_id)
    col_length = len(csvData.columns)


    for i in range(len(can_id)):
        globals()['signal_{}'.format(i+1)] = csvData[csvData['ID'] == can_id[i]]
        globals()['numSig_{}'.format(i+1)] = globals()['signal_{}'.format(i+1)].count()


    globals()['numSig_{}'.format(1)]

    signal_id = ('%d' % signal_1.iloc[1].ID)

    script.writelines(doubleIndentation)
    script.writelines(conditional_if)
    script.write(signal_id)
    script.writelines(colon)
    script.writelines('\n')

    for i in range(1, len(can_id)+1):
        for j in range(1, globals()['numSig_{}'.format(i)].ID+1):
            rosmsg_1 = globals()['signal_{}'.format(i)].iloc[j-1].ROSMSG1
            sig = globals()['signal_{}'.format(i)].iloc[j-1].SIG
            if col_length > 3 :
                rosmsg_2 = globals()['signal_{}'.format(i)].iloc[j-1].ROSMSG2
            script.writelines(tripleIndentation)
            script.writelines(cdata)
            script.writelines(dot)
            script.write(rosmsg_1)
            if col_length > 3 :
                script.writelines(dot)
                script.write(rosmsg_2)
            script.writelines(equal)
            script.writelines(signals_begin)
            script.write(sig)
            script.writelines(signals_end)
        if i < len(can_id):
            tmp_id = ('%d' % globals()['signal_{}'.format(i+1)].iloc[0].ID)
            script.writelines(doubleIndentation)
            script.writelines(conditional_elif)
            script.write(tmp_id)
            script.writelines(colon)
            script.writelines('\n')
    script.write('\n')

def createMain(script):

    script.writelines(mainFunction)
    script.writelines('\n\n')
    script.writelines(indentation)
    script.writelines(classVariable)
    script.writelines('\n')

    script.writelines(indentation)
    script.writelines(initNode)
    script.writelines(parenthesisOpen)
    script.writelines(singleQuote)
    script.writelines(nodeName)
    script.writelines(singleQuote)
    script.writelines(comma)
    script.writelines(anonymousVariable)
    script.writelines(nospaceEqual)

    if anonymous:
        script.writelines('True')
    else:
        script.writelines('False')

    script.writelines(parenthesisClose)
    script.writelines('\n\n')

    #Rate
    script.writelines(indentation)
    script.writelines(rateVariable)
    script.writelines(parenthesisOpen)
    script.writelines(rate)
    script.writelines(parenthesisClose)
    script.writelines('\n')

    #Shutdown Condition
    script.writelines(indentation)
    script.writelines(shutdownCondition)
    script.writelines('\n')

    #Header Stamp
    script.writelines('\t')
    script.writelines(headerStamp)
    script.writelines('\n')

    #Log Info

    if isMultipleLogInfo:
        for num in range(len(logInfo)):
            script.writelines(doubleIndentation)
            script.writelines(logInfoVariable)
            script.writelines(parenthesisOpen)
            script.writelines(cpCdata)
            script.writelines(dot)
            script.writelines(logInfo[num])
            script.writelines(parenthesisClose)
            script.writelines('\n')

    else:
        script.writelines(doubleIndentation)
        script.writelines(logInfoVariable)
        script.writelines(parenthesisOpen)
        script.writelines(cpCdata)
        script.writelines(parenthesisClose)
        script.writelines('\n')

    #Publish
    script.writelines(doubleIndentation)
    script.writelines(publishVariable)
    script.writelines('\n')

    #Sleep
    script.writelines(doubleIndentation)
    script.writelines(sleepVariable)
    script.writelines('\n\n')

def createMainConditional(script):

    #Main Conditional
    script.writelines(mainIF)
    script.writelines('\n')
    script.writelines('\t')
    script.writelines(mainVariable)
    script.writelines('\n')


def main ():

    script = open(nodeName + '.py', 'w')
    createHeader(script)
    createBody(script)
    createMain(script)
    createMainConditional(script)
    script.close()

if __name__ == '__main__':
	main()






