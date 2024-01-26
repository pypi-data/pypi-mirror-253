import json
import sys
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from settings import ENVIRONMENT_DEBUG, ENVIRONMENT_PORT, SYNC_RUNNER
from sync_job.sync_floor1_job import sync_floor1_job
from sync_job.sync_floor2_job import sync_floor2_job
from zk import ZK, base
import time
import atexit

from zk.user import UserEncoder
from zk.attendance import AttendanceEncoder

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Setup Cron Job
scheduler = BackgroundScheduler()
scheduler.add_job(func=sync_floor1_job, trigger="cron", hour=0, minute=0)
scheduler.add_job(func=sync_floor2_job, trigger="cron", hour=0, minute=0)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

# GET method to retrieve a specific book by ID
@app.route('/users/<int:timekeeper_user_id>/attendances', methods=['GET'])
def get_user_attendances(timekeeper_user_id):
    start_date = request.args.get('start')
    end_date = request.args.get('end')
    user_id = request.args.get('userId')

    conn = None
    zk = ZK('192.168.1.130', port=4370)
    conn2 = None
    zk2 = ZK('192.168.1.73', port=4370)
    try:
        conn = zk.connect()
        conn.disable_device()
        attendances = conn.get_limited_attendance(
            users=[timekeeper_user_id],
            start_date=datetime.strptime(start_date, '%Y-%m-%d'),  # from 2023,1,10
            end_date=datetime.strptime(end_date, '%Y-%m-%d')  # to 2022,1,11
        )
        conn.enable_device()

        conn2 = zk2.connect()
        conn2.disable_device()
        attendances2 = conn2.get_limited_attendance(
            users=[timekeeper_user_id],
            start_date=datetime.strptime(start_date, '%Y-%m-%d'),  # from 2023,1,10
            end_date=datetime.strptime(end_date, '%Y-%m-%d')  # to 2022,1,11
        )
        conn2.enable_device()

        return json.dumps(attendances + attendances2, cls=AttendanceEncoder)
    except Exception as e:
        print ("Process terminate : {}".format(e))
        return jsonify(e)
    finally:
        if conn:
            conn.enable_device()
            conn.disconnect()
        if conn2:
            conn2.enable_device()
            conn2.disconnect()

# GET method to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = None
    zk = ZK('192.168.1.130', port=4370)
    try:
        conn = zk.connect()
        conn.disable_device()
        users = conn.get_users()
        conn.enable_device()
        return json.dumps(users, cls=UserEncoder)
    except Exception as e:
        print ("Process terminate : {}".format(e))
        return jsonify(e)
    finally:
        if conn:
            conn.enable_device()
            conn.disconnect()

if __name__ == '__main__':
    base.init()
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
