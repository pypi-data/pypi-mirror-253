from zk import ZK, const, database
import time
from settings import SYNC_RUNNER

def sync_floor2_job():
    max_retries = 3 # Retry 3 times if have error
    retry_count = 0
    lconn = None
    lzk = ZK('192.168.1.73', port=4370)
        
    if SYNC_RUNNER:
        while retry_count < max_retries:
            try:
                print("fetch attendance floor 2 start")
                lconn = lzk.connect()
                lconn.disable_device()
                attendances = lconn.get_attendance()
                lconn.enable_device()
                for attendance in attendances:
                    attendance.device = const.TIME_KEEPER_DEVICE_FLOOR2
                    database.sync_timekeeper_data(attendance)
                print("fetch attendance floor 2 end")
                break  # Break out of the loop if successful
            except Exception as e:
                retry_count += 1
                print("Process terminate for floor 2, error in attempt {}: {}".format(retry_count, e))
                time.sleep(5) # Delay 5 seconds
            finally:
                if lconn:
                    lconn.enable_device()
                    lconn.disconnect()