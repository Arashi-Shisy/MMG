import unittest
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from tests.test_setting import *
from systems.dao.UserManagement import *
from systems.controller.Users import *

class TestUserMethods(unittest.TestCase):
    def test_check_user_exist_true(self):
        result = check_user_exist(TEST_USER_EMAIL)
        self.assertEqual(result, True)
    def test_validation_user_registration(self):
        result = validation_user_registration(BLANK,BLANK,BLANK)
        self.assertListEqual(result, [False,'メールアドレスは必須項目です','email_flash'])
        result = validation_user_registration(TEST_PASSWORD,BLANK,BLANK)
        self.assertListEqual(result, [False,'メールアドレスの形式が不正です','email_flash'])
        result = validation_user_registration(TEST_USER_EMAIL,BLANK,BLANK)
        self.assertListEqual(result, [False,'パスワードは必須項目です','password_flash'])
        result = validation_user_registration(TEST_USER_EMAIL,TEST_PASSWORD_ENGLISH,BLANK)
        self.assertListEqual(result, [False,'パスワードは半角英数混合の8~12文字で入力してください','password_flash'])
        result = validation_user_registration(TEST_USER_EMAIL,TEST_PASSWORD_ONLYNUM,BLANK)
        self.assertListEqual(result, [False,'パスワードは半角英数混合の8~12文字で入力してください','password_flash'])
        result = validation_user_registration(TEST_USER_EMAIL,TEST_PASSWORD_13,BLANK)
        self.assertListEqual(result, [False,'パスワードは半角英数混合の8~12文字で入力してください','password_flash'])
        result = validation_user_registration(TEST_USER_EMAIL,TEST_PASSWORD_7,BLANK)
        self.assertListEqual(result, [False,'パスワードは半角英数混合の8~12文字で入力してください','password_flash'])
        result = validation_user_registration(TEST_USER_EMAIL,TEST_PASSWORD,BLANK)
        self.assertListEqual(result, [False,'パスワードが一致しません','password_check_flash'])
        result = validation_user_registration(TEST_USER_EMAIL_EXIST,TEST_PASSWORD,TEST_PASSWORD)
        self.assertListEqual(result, [False,'このメールアドレスは既に使われています','email_flash'])
        result = validation_user_registration(TEST_USER_EMAIL_NOTEXIST,TEST_PASSWORD,TEST_PASSWORD)
        self.assertListEqual(result, [True,'',''])
    def test_validation_login(self):
        result = validation_login(BLANK,BLANK)
        self.assertListEqual(result, [False,'メールアドレスは必須項目です','email_flash'])
        result = validation_login(TEST_USER_EMAIL,BLANK)
        self.assertListEqual(result, [False,'パスワードは必須項目です','password_flash'])
        result = validation_login(TEST_USER_EMAIL_NOTEXIST,TEST_PASSWORD)
        self.assertListEqual(result, [False,'メールアドレスが登録されていません','email_flash'])
        result = validation_login(TEST_USER_EMAIL_EXIST,TEST_PASSWORD)
        self.assertListEqual(result, [True,'',''])
    def test_check_user_exist_false(self):
        result = check_user_exist(TEST_USER_EMAIL_EXIST)
        self.assertEqual(result, False)
    def test_insert_user(self):
        result = insert_user(TEST_USER_EMAIL,TEST_PASSWORD)
        self.assertEqual(result, True)
    def test_login_check(self):
        result = login_check(TEST_USER_EMAIL_EXIST,TEST_PASSWORD)
        self.assertEqual(result[0], True)
        self.assertIsInstance(result[1],(int))
        result = login_check(TEST_USER_EMAIL_EXIST,TEST_PASSWORD_WRONG)
        self.assertEqual(result[0], False)
        self.assertEqual(result[1],0)

if __name__ == '__main__':
    unittest.main()