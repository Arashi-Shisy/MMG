from .MySqlConnect import *

def db_insert(sql):
    # コネクション
    conn = mysql_connect()
    cursor = conn.cursor();
    
    # SQL実行
    cursor.execute(sql)
    conn.commit()
    
    # コネクション閉鎖
    cursor.close();
    conn.close();
    
def db_search(sql):
    # コネクション
    conn = mysql_connect()
    cursor = conn.cursor();
    
    # SQL実行、結果取得
    cursor.execute(sql)
    raw = cursor.fetchall()
    
    # コネクション閉鎖
    cursor.close();
    conn.close();
    
    return raw
    
def db_search_with_dictionary(sql):
    # コネクション
    conn = mysql_connect()
    cursor = conn.cursor(dictionary=True);
    
    cursor.execute(sql)
    raw = cursor.fetchall()
    
    # コネクション閉鎖
    cursor.close();
    conn.close();
    
    return raw

def db_update(sql):
    # コネクション
    conn = mysql_connect()
    cursor = conn.cursor();
    
    # SQL実行
    cursor.execute(sql)
    conn.commit()
    
    # コネクション閉鎖
    cursor.close();
    conn.close();
    
def db_delete(sql):
    # コネクション
    conn = mysql_connect()
    cursor = conn.cursor();
    
    # SQL実行
    cursor.execute(sql)
    conn.commit()
    
    # コネクション閉鎖
    cursor.close();
    conn.close();
