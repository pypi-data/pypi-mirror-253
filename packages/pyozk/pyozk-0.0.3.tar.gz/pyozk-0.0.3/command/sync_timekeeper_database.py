# -*- coding: utf-8 -*-
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK, database, const

conn = None
zk = ZK('192.168.1.130', port=4370)
conn2 = None
zk2 = ZK('192.168.1.73', port=4370)

try:
    print("fetch attendance floor 1 start")
    conn = zk.connect()
    conn.disable_device()
    attendances = conn.get_attendance()
    conn.enable_device()
    for attendance in attendances:
        attendance.device = const.TIME_KEEPER_DEVICE_FLOOR1
        database.sync_timekeeper_data(attendance)
    print("fetch attendance floor 1 end")

    print("fetch attendance floor 2 start")
    conn2 = zk2.connect()
    conn2.disable_device()
    attendances = conn2.get_attendance()
    conn2.enable_device()
    for attendance in attendances:
        attendance.device = const.TIME_KEEPER_DEVICE_FLOOR2
        database.sync_timekeeper_data(attendance)
    print("fetch attendance floor 2 end")
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.enable_device()
        conn.disconnect()
    if conn2:
        conn2.enable_device()
        conn2.disconnect()
