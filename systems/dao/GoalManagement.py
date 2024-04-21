import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG","systems"))
sys.path.append(os.path.join( "/app"))
from connect.MySqlConnect import *
from connect.DbConnection import *
import logging

def get_goal_list(user_id):
    logging.debug('-[Method]ゴール一覧取得開始')
    goal_list = db_search_with_dictionary(f"SELECT goal_id,goal_title,action,deadline,status,evaluation,evaluationed_at,created_at FROM goals WHERE user_id = '{user_id}' and del_flg = 0 ORDER BY created_at DESC;")
    logging.debug('-[Method]ゴール一覧取得終了')
    return(goal_list)

def insert_goal(user_id,goal_title,action,deadline):
    logging.debug('-[Method]新規目標登録開始')
    try:
        db_insert(f"INSERT INTO goals (user_id,goal_title,action,status,deadline,created_at, updated_at) VALUES ('{user_id}','{goal_title}','{action}','進行中','{deadline}',NOW(),NOW());")
        return(True)
    except Exception as e:
        logging.debug('-[Method]新規目標登録失敗')
        logging.debug(f"{e.__class__.__name__}: {e}")
        return(False)

def update_set_goal(goal_title,action,deadline,goal_id):
    try:
        db_insert(f"UPDATE goals SET goal_title = '{goal_title}',action = '{action}',deadline = '{deadline}',updated_at = NOW() WHERE goal_id = {goal_id}")
        logging.debug('-[Method]目標更新成功')
        return(True)
    except Exception as e:
        logging.debug(f"{e.__class__.__name__}: {e}")
        logging.debug('-[Method]目標更新失敗')
        return(False)

def delete_set_goal(goal_id):
    logging.debug('-[Method]目標削除開始')
    try:
        db_insert(f"UPDATE goals SET del_flg = 1 WHERE goal_id = {goal_id}")
        db_insert(f"UPDATE goal_links SET del_flg = 1 WHERE goal_id_01 = {goal_id} or goal_id_02 = {goal_id}")
        return(True)
    except Exception as e:
        logging.debug(f"{e.__class__.__name__}: {e}")
        logging.debug('-[Method]目標削除失敗')
        return(False)

def get_goal_details(goal_id):
    logging.debug('-[Method]目標詳細取得開始')
    goal_details = db_search_with_dictionary(f"SELECT goal_id,goal_title,action,deadline,status,evaluation,evaluationed_at,created_at FROM goals WHERE goal_id = '{goal_id}' ;")
    logging.debug('-[Method]目標詳細取得成功')
    return(goal_details)

def evaluation_set_goal(goal_id,status,evaluation):
    logging.debug('-[Method]評価登録開始')
    try:
        db_insert(f"UPDATE goals SET status = '{status}',evaluation = '{evaluation}',evaluationed_at = NOW(),updated_at = NOW() WHERE goal_id = {goal_id}")       
        return(True)
    except Exception as e:
        logging.debug(f"{e.__class__.__name__}: {e}")
        logging.debug('-[Method]評価登録失敗')  
        return(False)

def get_latest_goal_id(goal_title,action,deadline):
    logging.debug('-[Method]最新目標取得開始')
    goal_id = db_search(f"SELECT goal_id FROM goals WHERE goal_title = '{goal_title}' and action = '{action}' and deadline = '{deadline}' and del_flg = 0 ORDER BY created_at DESC limit 1;")[0][0]
    logging.debug('-[Method]最新目標取得成功')
    return(goal_id)