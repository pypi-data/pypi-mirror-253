# -*- coding: utf-8 -*-
import json
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK, database, const, pubsub
from zk.attendance import AttendanceEncoder

print('running!')

conn = None
zk = ZK('192.168.1.73', port=4370)

try:
    conn = zk.connect()
    for attendance in conn.live_capture():
        if attendance is None:
            pass
        else:
            attendance.device = const.TIME_KEEPER_DEVICE_FLOOR2
            database.sync_timekeeper_data(attendance)
            pubsub.publish(const.TIMEKEEPING_CHANNEL, json.dumps(attendance, cls=AttendanceEncoder))
except Exception as e:
    print ("Process terminate : {}".format(e))
    sys.exit()
finally:
    if conn:
        conn.disconnect()
    
