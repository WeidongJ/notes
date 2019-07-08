#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from testlogger import Logger

log = Logger(logger='test').get_log()

print(time.time())
log.info('ctime')
print(time.localtime())
print(time.strftime('%Y-%m-%d %H-%M-%S', time.localtime()))
print(time.strptime('7 Jul 2019', '%d %b %Y'))