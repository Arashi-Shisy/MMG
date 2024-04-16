from connect.MySqlConnect import *
from connect.DbConnection import *

def get_goal_list(user_id):
    goal_list = db_search_with_dictionary(f"SELECT goal_id,goal_title,action,deadline,status,evaluation,evaluationed_at,created_at FROM goals WHERE user_id = '{user_id}' and del_flg = 0 ORDER BY created_at DESC;")
    return(goal_list)

def insert_goal(user_id,goal_title,action,deadline):
    try:
        db_insert(f"INSERT INTO goals (user_id,goal_title,action,deadline,created_at, updated_at) VALUES ('{user_id}','{goal_title}','{action}','{deadline}',NOW(),NOW());")
        return(True)
    except:
        return(False)

def update_set_goal(goal_title,action,deadline,goal_id):
    try:
        db_insert(f"UPDATE goals SET goal_title = '{goal_title}',action = '{action}',deadline = '{deadline}',updated_at = NOW() WHERE goal_id = {goal_id}")
        return(True)
    except:
        return(False)

def delete_set_goal(goal_id):
    try:
        db_insert(f"UPDATE goals SET del_flg = 1 WHERE goal_id = {goal_id}")
        db_insert(f"UPDATE goal_links SET del_flg = 1 WHERE goal_id_01 = {goal_id} or goal_id_02 = {goal_id}")
        return(True)
    except:
        return(False)

def get_goal_details(goal_id):
    goal_details = db_search_with_dictionary(f"SELECT goal_id,goal_title,action,deadline,status,evaluation,evaluationed_at,created_at FROM goals WHERE goal_id = '{goal_id}' ;")
    return(goal_details)

def evaluation_set_goal(goal_id,status,evaluation):
    try:
        db_insert(f"UPDATE goals SET status = '{status}',evaluation = '{evaluation}',evaluationed_at = NOW(),updated_at = NOW() WHERE goal_id = {goal_id}")       
        return(True)
    except:
        return(False)

def get_latest_goal_id(goal_title,action,deadline):
    goal_id = db_search(f"SELECT goal_id FROM goals WHERE goal_title = '{goal_title}' and action = '{action}' and deadline = '{deadline}' and del_flg = 0 ORDER BY created_at DESC limit 1;")[0][0]
    return(goal_id)