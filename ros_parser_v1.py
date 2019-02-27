#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import sys
from config import *

csvData = pd.read_csv(sys.argv[1])
can_id_list = csvData['ID'].values.tolist()
can_id = list(set(can_id_list))
id_length = len(can_id)
col_length = len(csvData.columns)


i = 1

for i in range(len(can_id)):
    globals()['signal_{}'.format(i+1)] = csvData[csvData['ID'] == can_id[i]]
    globals()['numSig_{}'.format(i+1)] = globals()['signal_{}'.format(i+1)].count()


globals()['numSig_{}'.format(1)]



i = 1
j = 1

conditional_if = ['\t', 'if data.id == ']
conditional_elif = ['\t', 'elif data.id == ']
variable = ['\t','\t','self.cdata.']
colon = [':', '\n']
equal = [' = ']
dot = ['.']
signals_begin = ['signals', '[', '\'']
signals_end = ['\'', ']', '\n']

script = open('test4.py', 'w')

f = open(sys.argv[2], 'r')
lines = f.readlines()
for line in lines:
    script.writelines(line)
f.close()

signal_id = ('%d' % signal_1.iloc[1].ID)

script.writelines(conditional_if)
script.write(signal_id)
script.writelines(colon)

for i in range(1, len(can_id)+1):
    for j in range(1, globals()['numSig_{}'.format(i)].ID+1):
        rosmsg_1 = globals()['signal_{}'.format(i)].iloc[j-1].ROSMSG1
        sig = globals()['signal_{}'.format(i)].iloc[j-1].SIG
        if col_length > 3 :
            rosmsg_2 = globals()['signal_{}'.format(i)].iloc[j-1].ROSMSG2
        script.writelines(variable)
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
        script.writelines(conditional_elif)
        script.write(tmp_id)
        script.writelines(colon)
script.write('\n')

f = open(sys.argv[3], 'r')
lines = f.readlines()
for line in lines:
    script.writelines(line)
f.close()

script.close()






