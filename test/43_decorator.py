#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 08:50:02
# @Author  : anxi.xue (xueanxi@163.com)
# @Version : $Id$

import os
from time import sleep
from functools import wraps

import logging

logging.basicConfig()
log = logging.getLogger('retrysss')


def retry(f):
    @wraps(f)
    def wrapsf(*args, **kwargs):
        MAX_TIEM = 5
        for attempt in range(1, MAX_TIEM + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed: %s",
                              attempt,
                              MAX_TIEM,
                              (args, kwargs))
                sleep(1 * attempt)
        log.critical("All %s attempts failed : %s", MAX_TIEM, (args, kwargs))
    return wrapsf

counter = 0


@retry
def savetodatabase(args):
    print("\ntry to save savetodatabase")
    global counter
    counter += 1
    print('counter = ', counter)
    # 前面几次counter < 4的时候，会失败，失败之后触发retry
    if counter < 4:
        print("save to savetodatabase failed!!!\n")
        raise ValueError(args)
    else:
        print("Save to database Successful !!!")

if __name__ == '__main__':
    savetodatabase('Some bad values')
