import unittest
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from tests.test_setting import *
from systems.dao.GoalManagement import *
from systems.controller.Users import *

class TestGoalMethods(unittest.TestCase):
    def test_get_goal_list(self):
        result = get_goal_list(TEST_USER_ID_GET)
        self.assertListEqual(result, TEST_GOAL_LIST)
    def test_insert_goal(self):
        result = insert_goal(TEST_USER_ID_INSERT,TEST_GOAL_TITLE,TEST_ACTION,TEST_DEADLINE)
        self.assertEqual(result, True)
    def test_update_set_goal(self):
        result = update_set_goal(TEST_GOAL_TITLE_UPDATE,TEST_ACTION_UPDATE,TEST_DEADLINE,TEST_GOAL_ID_UPDATE)
        self.assertEqual(result, True)
    def test_delete_set_goal(self):
        result = delete_set_goal(TEST_GOAL_ID_DELETE)
        self.assertEqual(result, True)
    def test_get_goal_details(self):
        result = get_goal_details(TEST_GOAL_ID_DETAILS)
        self.assertListEqual(result,TEST_GOAL_DETAILS)
    def test_evaluation_set_goal(self):
        result = evaluation_set_goal(TEST_GOAL_ID_UPDATE,TEST_STATUS,TEST_EVALUATION)
        self.assertEqual(result, True)
    def test_get_latest_goal_id(self):
        insert_goal(TEST_USER_ID_INSERT,TEST_GOAL_TITLE,TEST_ACTION,TEST_DEADLINE)
        result = get_latest_goal_id(TEST_GOAL_TITLE,TEST_ACTION,TEST_DEADLINE)
        self.assertIsInstance(result,(int))

if __name__ == '__main__':
    unittest.main()
