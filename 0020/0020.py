#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0020.py
   Author:        fynn-PC
   date:          2019/4/19 23:21
   Software:      PyCharm
-------------------------------------------------
"""

"""
 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，
 就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""

import pandas as pd
import os
import functools
import time


def log_time(func):
    @functools.wraps(func)
    def warrap(*args, **kwargs):
        start_time = time.time()
        print("%s is begining. " % (func.__name__))
        res = func(*args, **kwargs)
        end_time = time.time()
        print(
            "%s is end. And it takes %f seconds." %
            (func.__name__, end_time - start_time))
        return res

    return warrap


@log_time
def read_excel():
    data_path = os.path.join(
        os.path.dirname(
            os.path.abspath(
                os.pardir)),
        "2019-03.xls")
    data = pd.read_excel(data_path, index_col='序号')
    list_tmp = []
    for i in range(len(data)):
        tmp = data.iloc[i]['通话时长']
        remove_h = tmp.replace('时', ':')
        remove_m = remove_h.replace('分', ':')
        remove_s = remove_m.replace('秒', '')
        list_tmp.append(remove_s)
    return list_tmp


@log_time
def get_time(list_tmp):
    sum = 0
    for i in list_tmp:
        if i.count(":") == 2:
            h, m, s = i.split(":")
            sum = sum + int(h) + int(m) + int(s)
        elif i.count(":") == 1:
            m, s = i.split(":")
            sum = sum + int(m) + int(s)
        else:
            sum = sum + int(i)
    return sum


@log_time
def print_time(sum):
    s = sum % 60
    m = (sum - s) / 60 % 60
    h = (sum - s) / 60 // 60
    if h != 0:
        print("本月累计通话%d时%d分%d秒。" % (h, m, s))
        print("累计耗时%d秒。" % sum)
    else:
        print("本月累计通话%d分%d秒。" % (m, s))
        print("累计耗时%d秒。" % sum)


if __name__ == '__main__':
    list_tmp = read_excel()
    sum = get_time(list_tmp)
    print_time(sum)
    print('End')
