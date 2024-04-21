import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG","systems"))
sys.path.append(os.path.join( "/app"))
from connect.MySqlConnect import *
from connect.DbConnection import *
import logging

def insert_goal_links(goal_id_01,goal_id_02):
    logging.debug('目標紐付け開始')
    try:
        db_insert(f"INSERT INTO goal_links (goal_id_01,goal_id_02,created_at, updated_at) VALUES ('{goal_id_01}','{goal_id_02}', NOW(), NOW());")
        return(True)
    except Exception as e:
        logging.debug(f"{e.__class__.__name__}: {e}")
        logging.debug('目標紐付け失敗')
        return(False)

def check_link_exist(goal_id_01,goal_id_02):
    logging.debug('目標重複チェック開始')
    if db_search(f"SELECT COUNT(*) FROM goal_links WHERE goal_id_01 = '{goal_id_01}' and goal_id_02 = '{goal_id_02}' and del_flg = 0;")[0][0] != 0:
        logging.debug('目標重複なし')
        return(True)
    elif db_search(f"SELECT COUNT(*) FROM goal_links WHERE goal_id_01 = '{goal_id_02}' and goal_id_02 = '{goal_id_01}' and del_flg = 0;")[0][0] != 0:
        logging.debug('目標重複なし')
        return(True)
    else:
        logging.debug('目標重複あり')
        return(False)

def get_linked_goals_01(goal_id):
    return db_search(f"SELECT links.goal_id_01,links.goal_id_02,goals.goal_title FROM goal_links as links INNER JOIN goals as goals ON links.goal_id_02 = goals.goal_id WHERE links.goal_id_01 = '{goal_id}' and links.del_flg = 0;")

def get_linked_goals_02(goal_id):
    return db_search(f"SELECT links.goal_id_02,links.goal_id_01,goals.goal_title FROM goal_links as links INNER JOIN goals as goals ON links.goal_id_01 = goals.goal_id WHERE links.goal_id_02 = '{goal_id}' and links.del_flg = 0;")


def get_links(user_id):
    logging.debug('紐付け情報取得開始')
    goal_ids = []
    goal_ids = db_search(f"SELECT goal_id FROM goals WHERE user_id = {user_id} and del_flg = 0;")
    linked_goals = []
    for goal_id_raw in goal_ids:
        goal_id = goal_id_raw[0]
        goal_01_exists = get_linked_goals_01(goal_id)
        for goal_01_exist in goal_01_exists:
            linked_goals.append(goal_01_exist)
        goal_02_exists = get_linked_goals_02(goal_id)
        for goal_02_exist in goal_02_exists:
            linked_goals.append(goal_02_exist)
    logging.debug('紐付け情報取得完了')
    return (linked_goals)
