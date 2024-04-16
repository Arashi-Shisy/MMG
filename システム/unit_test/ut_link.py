import unittest
from unit_test_setting import *
import sys
sys.path.append("システム/")
from dao.LinkManagement import *
from controller.Links import *

class TestLinkMethods(unittest.TestCase):
    def test_validation_link_goals(self):
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_01)
        self.assertListEqual(result, [False,'同じ目標同士は紐付けできません','top_flash'])
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_EXIST_02)
        self.assertListEqual(result, [False,'既に紐付けられています','top_flash'])
        result = validation_link_goals(TEST_LINK_EXIST_02,TEST_LINK_01)
        self.assertListEqual(result, [False,'既に紐付けられています','top_flash'])
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_EXIST_DELETED_04)
        self.assertListEqual(result, [True,'',''])
        result = validation_link_goals(TEST_LINK_01,TEST_LINK_NOTEXIST_09)
        self.assertListEqual(result, [True,'',''])
    def test_insert_goal_links(self):
        result = insert_goal_links(TEST_LINK_NOTEXIST_09,TEST_LINK_NOTEXIST_10)
        self.assertEqual(result, True)
    def test_check_link_exist(self):
        result = check_link_exist(TEST_LINK_01,TEST_LINK_EXIST_02)
        self.assertEqual(result,True)
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
