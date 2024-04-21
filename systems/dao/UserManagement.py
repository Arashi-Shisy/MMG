import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG","systems"))
sys.path.append(os.path.join( "/app"))
from connect.MySqlConnect import *
from connect.DbConnection import *
import logging

def check_user_exist(email):
    logging.debug('email存在チェック開始')
    if db_search(f"SELECT COUNT(*) FROM users WHERE email = '{email}' and del_flg = 0;")[0][0] == 0:
        logging.debug('email登録なし')
        return(True)
    else:
        logging.debug('email登録あり')
        return(False)
    
def insert_user(email,password):
    logging.debug('新規ユーザー登録開始')
    try:
        db_insert(f"INSERT INTO users (email, password, created_at, updated_at) VALUES ('{email}',SHA2('{password}', 256),NOW(), NOW());")
        logging.debug('新規ユーザー登録成功')
        return(True)
    except Exception as e:
        logging.debug(f"{e.__class__.__name__}: {e}")
        logging.debug('新規ユーザー登録失敗')
        return(False)

def login_check(email,password):
    logging.debug('ログインチェック開始')
    if db_search(f"SELECT COUNT(*) FROM users WHERE email = '{email}' and password = SHA2('{password}', 256) and del_flg = 0;")[0][0] == 1:
        login_user_id = db_search(f"SELECT user_id FROM users WHERE email = '{email}';")[0][0]
        logging.debug('チェックOK')
        return[True,login_user_id]
    else:
        logging.debug('チェックNG')
        return(False,0)