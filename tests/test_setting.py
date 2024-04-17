import datetime

TODAY = datetime.date.today()
TODAY_STR = str(TODAY)
NOW = str(datetime.datetime.today())
BLANK = ""

# USERS_TEST
TEST_USER_EMAIL = NOW + '@test.com'
TEST_USER_EMAIL_EXIST = 'exist@test.com'
TEST_USER_EMAIL_NOTEXIST = 'notexist@test.com'
TEST_PASSWORD = 'test0001'
TEST_PASSWORD_WRONG = 'test0002'
TEST_PASSWORD_ONLYNUM = '12345678'
TEST_PASSWORD_ENGLISH = 'abcdefgh'
TEST_PASSWORD_13 = '1234567890123'
TEST_PASSWORD_7 = '1234567'

# GOALS_TEST
TEST_GOAL_TITLE = NOW + '_test_goal_title'
TEST_GOAL_TITLE_UPDATE = NOW + '_test_goal_title_update'
TEST_ACTION = NOW + '_test_action_update'
TEST_ACTION_UPDATE = NOW + '_test_goal_action'
TEST_DEADLINE = TODAY
TEST_STATUS = "達成"
TEST_EVALUATION = NOW + '_test_evaluation'
TEST_USER_ID_GET = 1
TEST_USER_ID_INSERT = 2
TEST_GOAL_ID_UPDATE = 3
TEST_GOAL_ID_DELETE = 4
TEST_GOAL_ID_DETAILS = 1
TEST_GOAL_LIST = [{'goal_id': 1, 'goal_title': 'test_goal_title01', 'action': 'test_action', 'deadline': datetime.date(2024, 4, 1), 'status': '進行中', 'evaluation': 'test_evaluation', 'evaluationed_at': datetime.date(2024, 5, 1), 'created_at': datetime.date(2024, 6, 1)}, {'goal_id': 2, 'goal_title': 'test_goal_title02', 'action': 'test_action', 'deadline': datetime.date(2023, 4, 1), 'status': '達成', 'evaluation': 'test_evaluation', 'evaluationed_at': datetime.date(2023, 5, 1), 'created_at': datetime.date(2023, 6, 1)}]
TEST_GOAL_DETAILS = [{'goal_id': 1, 'goal_title': 'test_goal_title01', 'action': 'test_action', 'deadline': datetime.date(2024, 4, 1), 'status': '進行中', 'evaluation': 'test_evaluation', 'evaluationed_at': datetime.date(2024, 5, 1), 'created_at': datetime.date(2024, 6, 1)}]

#LINKS_TEST
TEST_LINK_01 = 1
TEST_LINK_EXIST_02 = 2
TEST_LINK_EXIST_03 = 3
TEST_LINK_EXIST_DELETED_04 = 4
TEST_LINK_EXIST_05 = 5
TEST_LINK_RESULT_06 = [(5, 6, 'LINKED_GOAL_06')]
TEST_LINK_EXIST_07 = 7
TEST_LINK_RESULT_08 = [(7, 8, 'LINKED_GOAL_08')]
TEST_LINK_NOTEXIST_09 = 9
TEST_LINK_NOTEXIST_10 = 10
TEST_LINK_USER_ID = 3
TEST_GET_LINKS = [(5, 6, 'LINKED_GOAL_06'), (6, 5, 'LINKED_GOAL_05'), (7, 8, 'LINKED_GOAL_08'), (8, 7, 'LINKED_GOAL_07')]