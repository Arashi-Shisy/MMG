from connect.MySqlConnect import *
from connect.DbConnection import *

def insert_goal_links(goal_id_01,goal_id_02):
    try:
        db_insert(f"INSERT INTO goal_links (goal_id_01,goal_id_02,created_at, updated_at) VALUES ('{goal_id_01}','{goal_id_02}', NOW(), NOW());")
        return(True)
    except:
        return(False)

def check_link_exist(goal_id_01,goal_id_02):
    if db_search(f"SELECT COUNT(*) FROM goal_links WHERE goal_id_01 = '{goal_id_01}' and goal_id_02 = '{goal_id_02}' and del_flg = 0;")[0][0] != 0:
        return(True)
    elif db_search(f"SELECT COUNT(*) FROM goal_links WHERE goal_id_01 = '{goal_id_02}' and goal_id_02 = '{goal_id_01}' and del_flg = 0;")[0][0] != 0:
        return(True)
    else:
        return(False)

def get_linked_goals_01(goal_id):
    return db_search(f"SELECT links.goal_id_01,links.goal_id_02,goals.goal_title FROM goal_links as links INNER JOIN goals as goals ON links.goal_id_02 = goals.goal_id WHERE links.goal_id_01 = '{goal_id}' and links.del_flg = 0;")

def get_linked_goals_02(goal_id):
    return db_search(f"SELECT links.goal_id_02,links.goal_id_01,goals.goal_title FROM goal_links as links INNER JOIN goals as goals ON links.goal_id_01 = goals.goal_id WHERE links.goal_id_02 = '{goal_id}' and links.del_flg = 0;")


def get_links(user_id):
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
    return (linked_goals)
