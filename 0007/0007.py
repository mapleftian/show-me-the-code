#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0007.py
   Author:        Fynn-mac
   date:          2019-03-23 22:20
   Software:      PyCharm
-------------------------------------------------
"""
'''
第0007题：
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来
'''
'''
思路：
1、打开文件
2、
'''

'''
优化：
1、使用f.tell()函数在file中计数时总是报错，显示当行f.tell()为1062
'''
import os

def analyze_code(pathInput):
    total_lines = 0
    comment_lines = 0
    blank_lines = 0
    is_comments = False
    comment_index = 0 #记录以'''或"""开头的注释位置
    with open(pathInput,"r",encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip()
            if not is_comments:
                if line.startswith("'''") or line.startswith('"""'):
                    comment_index = 1
                    is_comments = True
                elif line.startswith("#"):
                    comment_lines+=1
                elif line == '':
                    blank_lines += 1
                else:
                    total_lines += 1
            else:
                if line.endswith("'''") or line.endswith('"""'):
                    is_comments = False
                    comment_lines = comment_lines+comment_index+1
                else:
                    comment_index += 1
    return total_lines,comment_lines,blank_lines

def dirNotExit(pathInput):
    if os.path.exists(pathInput):
        return False
    else:
        return True

if __name__ == '__main__':
    pathInput = input("请输入文件路径:\n")
    while dirNotExit(pathInput):
        pathInput = input("当前路径不存在，请重新输入:\n")
    total_lines,comment_lines,blank_lines = analyze_code(pathInput)
    print("代码行数为：{}".format(total_lines))
    print("注释行数为：{}".format(comment_lines))
    print("空格行数为：{}".format(blank_lines))