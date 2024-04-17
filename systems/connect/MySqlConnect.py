import mysql.connector as mydb

def mysql_connect():
    conn = mydb.connect(
        host = 'localhost',
        user = 'root',    
        password = '*******',
        database = 'mmg'
        # database = 'test_mmg'
    )
    conn.ping(reconnect = True)
    return(conn)