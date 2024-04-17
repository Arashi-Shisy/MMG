import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG","tests"))
from test_setting import *

FORM_DATA = {
    'update_goal': {
        'goal_title': TEST_GOAL_TITLE_UPDATE,
        'action': TEST_ACTION_UPDATE,
        'deadline': TEST_DEADLINE
    },
    'add_goal': {
        'goal_title': TEST_GOAL_TITLE,
        'action': TEST_ACTION,
        'deadline': TEST_DEADLINE
    },
    'evaluation_goal': {
        'status': TEST_STATUS,
        'evaluation': TEST_EVALUATION
    },
    'subsequent_goal_registration': {
        'goal_title': TEST_GOAL_TITLE,
        'action': TEST_ACTION,
        'deadline': TEST_DEADLINE
    },
    'user_registration':{
        'email': TEST_USER_EMAIL,
        'password': TEST_PASSWORD,
        'password_check': TEST_PASSWORD
    },
    'user_registration_valid':{
        'email': TEST_USER_EMAIL_EXIST,
        'password': TEST_PASSWORD,
        'password_check': TEST_PASSWORD
    },
    'login':{
        'email':TEST_USER_EMAIL_EXIST,
        'password':TEST_PASSWORD
    },
    'login_valid':{
        'email':TEST_USER_EMAIL_EXIST,
        'password':TEST_PASSWORD_WRONG
    },
    'link_goals':{
        'goal_id_01':TEST_LINK_NOTEXIST_09,
        'goal_id_02':NOW_INT
    },
    'link_goals_false':{
        'goal_id_01':TEST_LINK_01,
        'goal_id_02':TEST_LINK_EXIST_02
    }
}
