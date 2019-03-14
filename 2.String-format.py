#!/usr/bin/python3.7
# _*_ coding=utf-8 _*_
# 每天一段代码到2020.DDW.
department1 = 'Security'
department2 = 'Pythone'
depart1_m = 'cq_bomb'
depart2_m = 'ddw'
COURSE_FEES_SEC = 456789.12345
COURSE_FEES_Python = 1234.3456
line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.0f The End!' % (department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.0f The End!' % (department2,depart2_m,COURSE_FEES_Python)
length = len(line1)
print('=' *length)
print(line1)
print(line2)
print('=' *length)