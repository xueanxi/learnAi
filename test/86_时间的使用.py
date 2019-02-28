# -*- coding: utf-8 -*-
# @Time    : 2/28/19 10:23 AM
# @Author  : Anxi.xue
# @Email   : xueanxi@163.com

import datetime
import time

today = datetime.date.today()
print('today',today)
print('today.timetuple',today.timetuple())
yestoday = today - datetime.timedelta(days=1)
print('yestoday',yestoday)
lastmonth = today.month - 1 if today.month - 1 else 12
print('last month',lastmonth)
time_stamp = time.time()
print('time stamp:',time_stamp)
datenow = datetime.datetime.fromtimestamp(time_stamp)
print('时间戳转datetime:',datenow)
print('datetime转时间戳:',int(time.mktime(today.timetuple())))
strnow = datenow.strftime('%Y-%m-%d %H:%M:%S')
print('datetime转字符串:',strnow)
print('字符串转datetime:',datetime.datetime.strptime(strnow,'%Y-%m-%d %H:%M:%S'))
print('补时差', today + datetime.timedelta(hours=8))