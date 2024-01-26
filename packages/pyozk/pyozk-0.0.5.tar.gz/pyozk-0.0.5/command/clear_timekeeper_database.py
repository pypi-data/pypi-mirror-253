from zk import database

cur = database.con.cursor()
try:
    delete_query = "DELETE FROM timekeepers"
    # Execute the DELETE query to drop the table
    cur.execute(delete_query)
    # Commit the transaction to save the changes
    database.con.commit()
    print("Table deleted successfully!")
except Exception as e:
        # Rollback the changes if an error occurs
        database.con.rollback()
        print("Error:", e)
finally:
    if cur:
        cur.close();
    if database.con:
        database.con.close()