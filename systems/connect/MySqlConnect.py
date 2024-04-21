import mysql.connector as mydb
import logging
import sys
import os
sys.path.append(os.path.join( "/app"))

def mysql_connect():
    logging.debug('- -[Connect]DB接続開始')
    conn = mydb.connect(
        host = 'my-mysql',
        user = 'root',    
        password = '********',
        database = 'mmg'
        # database = 'test_mmg'
    )
    conn.ping(reconnect = True)
    logging.debug('- -[Connect]DB接続完了')
    return(conn)