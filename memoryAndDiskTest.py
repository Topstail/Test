#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2018-12-17 17:16
# @Author : opsonly # @Site :
# @File : systemissue.py
# @Software: PyCharm


import psutil


def memissue():
    print('内存信息：')
    mem = psutil.virtual_memory()
    # 单位换算为MB
    memtotal = mem.total/1024/1024
    memused = mem.used/1024/1024
    membaifen = (memused / memtotal) * 100
    print('已用内存:', '%.2fMB' % memused)
    print('总内存:', '%.2fMB' % memtotal)
    print('内存利用率:', '%.2f%%' % membaifen)


def cuplist():
    print('磁盘信息：')
    disk = psutil.disk_partitions()
    diskuse = psutil.disk_usage('/')
    #单位换算为GB
    diskused = diskuse.used / 1024 / 1024 / 1024
    disktotal = diskuse.total / 1024 / 1024 / 1024
    diskbaifen = diskused / disktotal * 100
    print('所在磁盘已使用空间:', '%.2fGB' % diskused)
    print('所在磁盘总空间:', '%.2fGB' % disktotal)
    print('所在磁盘使用率:', '%.2f%%' % diskbaifen)


memissue()
print('*******************')
cuplist()
