import unittest
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from tests.test_setting import *
from systems.dao.LinkManagement import *
from systems.controller.Links import *

class TestLinkMethods(unittest.TestCase):
    def test_validation_link_goals_same(self):
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_01)
        self.assertListEqual(result, [False,'同じ目標同士は紐付けできません','top_flash'])
    def test_validation_link_goals_exist01(self):
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_EXIST_02)
        self.assertListEqual(result, [False,'既に紐付けられています','top_flash'])
    def test_validation_link_goals_exist02(self):
        result = validation_link_goals(TEST_LINK_EXIST_02,TEST_LINK_01)
        self.assertListEqual(result, [False,'既に紐付けられています','top_flash'])
    def test_validation_link_goals_True01(self):
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_EXIST_DELETED_04)
        self.assertListEqual(result, [True,'',''])
    def test_validation_link_goals_True02(self):
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_NOTEXIST_09)
        self.assertListEqual(result, [True,'',''])
    def test_insert_goal_links(self):
        result = insert_goal_links(TEST_LINK_NOTEXIST_09,NOW_INT)
        self.assertEqual(result, True)
    def test_check_link_exist01(self):
        result = check_link_exist(TEST_LINK_01,TEST_LINK_EXIST_02)
        self.assertEqual(result,True)
    def test_check_link_exist02(self):
        result = check_link_exist(TEST_LINK_01,TEST_LINK_EXIST_03)
        self.assertEqual(result,True)
    def test_get_linked_goals01(self):
        result = get_linked_goals_01(TEST_LINK_EXIST_05)
        self.assertListEqual(result,TEST_LINK_RESULT_06)
    def test_get_linked_goals02(self):
        result = get_linked_goals_02(TEST_LINK_EXIST_07)
        self.assertListEqual(result,TEST_LINK_RESULT_08)
    def test_get_links(self):
        result = get_links(TEST_LINK_USER_ID)
        self.assertListEqual(result,TEST_GET_LINKS)
if __name__ == '__main__':
    unittest.main()
