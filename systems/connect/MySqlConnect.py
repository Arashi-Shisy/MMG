import mysql.connector as mydb
import logging
import sys
import os
sys.path.append(os.path.join( "/app"))

def mysql_connect():
    logging.debug('DB接続開始')
    conn = mydb.connect(
        host = 'my-mysql',
        user = 'root',    
        password = 'Bco92855814',
        database = 'mmg'
        # database = 'test_mmg'
    )
    conn.ping(reconnect = True)
    logging.debug('DB接続完了')
    return(conn)