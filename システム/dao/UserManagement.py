from connect.MySqlConnect import *
from connect.DbConnection import *

def check_user_exist(email):
    if db_search(f"SELECT COUNT(*) FROM users WHERE email = '{email}' and del_flg = 0;")[0][0] == 0:
        return(True)
    else:
        return(False)
    
def insert_user(email,password):
    try:
        db_insert(f"INSERT INTO users (email, password, created_at, updated_at) VALUES ('{email}',SHA2('{password}', 256),NOW(), NOW());")
        return(True)
    except:
        return(False)

def login_check(email,password):
    if db_search(f"SELECT COUNT(*) FROM users WHERE email = '{email}' and password = SHA2('{password}', 256) and del_flg = 0;")[0][0] == 1:
        login_user_id = db_search(f"SELECT user_id FROM users WHERE email = '{email}';")[0][0]
        return[True,login_user_id]
    else:
        return(False,0)