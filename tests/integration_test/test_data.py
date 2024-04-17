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
    }
}
