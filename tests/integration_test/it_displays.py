import unittest
from flask import Flask, session
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from systems.app import app
from test_data import FORM_DATA
from test_setting import *

app.testing = True

class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_display_user_registration(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['email_input'] = TEST_USER_EMAIL
            response = client.get('/display_user_registration')
            self.assertEqual(response.status_code, 200)

    def test_display_login(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['email_input'] = TEST_USER_EMAIL
                sess['password_input'] = TEST_PASSWORD               
            response = client.get('/display_login')
            self.assertEqual(response.status_code, 200)

    def test_index(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login'] = True
                sess['login_user_id'] = 1
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
    def test_index_notLogin(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 302)

    def test_display_new_goal_registration(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login'] = True
                sess['login_user_id'] = 1
            response = client.get('/display_new_goal_registration')
            self.assertEqual(response.status_code, 200)
    def test_display_new_goal_registration_notLogin(self):
        with app.test_client() as client:
            response = client.get('/display_new_goal_registration')
            self.assertEqual(response.status_code, 302)

    def test_display_link_goals(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login'] = True
                sess['login_user_id'] = 1
            response = client.get('/display_link_goals')
            self.assertEqual(response.status_code, 200)
    def test_display_link_goals_notLogin(self):
        with app.test_client() as client:
            response = client.get('/display_link_goals')
            self.assertEqual(response.status_code, 302)

    def test_display_evaluation_goal(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login'] = True
                sess['login_user_id'] = 1
            response = client.get('/display_evaluation_goal/goal_id=1')
            self.assertEqual(response.status_code, 200)
    def test_display_evaluation_goal_notLogin(self):
        with app.test_client() as client:
            response = client.get('/display_evaluation_goal/goal_id=1')
            self.assertEqual(response.status_code, 302)

    def test_display_subsequent_goal_registration(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login'] = True
                sess['login_user_id'] = 1
            response = client.get('/display_subsequent_goal_registration/goal_id=1')
            self.assertEqual(response.status_code, 200)
    def test_display_subsequent_goal_registration(self):
        with app.test_client() as client:
            response = client.get('/display_subsequent_goal_registration/goal_id=1')
            self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()
