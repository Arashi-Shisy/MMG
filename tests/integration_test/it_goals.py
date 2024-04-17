import unittest
from flask import Flask, session
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from systems.app import app
from systems.controller.Goals import goals_bp
from test_data import FORM_DATA
from test_setting import *

app.testing = True
app.register_blueprint(goals_bp, name='test_goals')

class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update_goal(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login_user_id'] = 123
            response = client.post('/update_goal/goal_id='+ str(TEST_GOAL_ID_UPDATE), data=FORM_DATA['update_goal'])
            self.assertEqual(response.status_code, 302)

    def test_delete_goal(self):
        with app.test_client() as client:
            response = client.get('/delete_goal/goal_id=' + str(TEST_GOAL_ID_DELETE))
            self.assertEqual(response.status_code, 302)
    def test_add_goal(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login_user_id'] = 123
            response = client.post('/add_goal', data=FORM_DATA['add_goal'])
            self.assertEqual(response.status_code, 302)
    def test_evaluation_goal(self):
        with app.test_client() as client:
            response = client.post('/evaluation_goal/goal_id='+ str(TEST_GOAL_ID_UPDATE), data=FORM_DATA['evaluation_goal'])
            self.assertEqual(response.status_code, 302)
    def test_subsequent_goal_registration(self):
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['login_user_id'] = 123
            response = client.post('/subsequent_goal_registration/goal_id='+str(TEST_LINK_NOTEXIST_09), data=FORM_DATA['subsequent_goal_registration'])
            self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
