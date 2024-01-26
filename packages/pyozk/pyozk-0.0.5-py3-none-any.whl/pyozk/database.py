# -*- coding: utf-8 -*-
import psycopg2
from settings import DB_DATABASE, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT
from .const import TIME_KEEPER_STATE, TIME_KEEPER_TYPE

con = psycopg2.connect(database=DB_DATABASE, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)

def sync_timekeeper_data(attendance):
    try:
        cur = con.cursor()
        select_query = "SELECT id FROM users WHERE timekeeper_user_id = %s"
        cur.execute(select_query, (attendance.user_id,))
        user = cur.fetchone()
        if user is None:
            print("User not found with timekeeperUserId", (attendance.user_id))
        else:
            userId = user[0]
            select_query = "SELECT * FROM timekeepers WHERE user_id = %s and time = %s and device_name = %s"
            cur.execute(select_query, (userId, attendance.timestamp, attendance.device))
            punch_time = cur.fetchone()
            if punch_time is None:
                # SQL statement for the INSERT query
                insert_query = """
                    INSERT INTO timekeepers (user_id, timekeeper_user_id, time, state, type, device_name)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                data_to_insert = (userId, attendance.user_id, attendance.timestamp, TIME_KEEPER_STATE[attendance.punch], TIME_KEEPER_TYPE[attendance.status], attendance.device)
                # Execute the INSERT query with the data
                cur.execute(insert_query, data_to_insert)
                
                # Commit the transaction to save the changes
                con.commit()
                print("Data inserted successfully!")
            else:
                print("Punch record existed. Do nothing")
    except Exception as e:
        # Rollback the changes if an error occurs
        con.rollback()
        print("Error:", e)