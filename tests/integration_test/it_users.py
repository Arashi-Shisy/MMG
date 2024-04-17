import unittest
from flask import Flask, session
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from systems.app import app
from systems.controller.Users import users_bp
from test_data import FORM_DATA
from test_setting import *

app.testing = True
app.register_blueprint(users_bp, name='test_users')

class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_registration(self):
        with app.test_client() as client:
            response = client.post('/user_registration', data=FORM_DATA['user_registration'])
            self.assertEqual(response.status_code, 302)
    def test_user_registration_valid(self):
        with app.test_client() as client:
            response = client.post('/user_registration', data=FORM_DATA['user_registration_valid'])
            self.assertEqual(response.status_code, 302)

    def test_login(self):
        with app.test_client() as client:
            response = client.post('/login', data=FORM_DATA['login'])
            self.assertEqual(response.status_code, 302)
    def test_login_valid(self):
        with app.test_client() as client:
            response = client.post('/login', data=FORM_DATA['login_valid'])
            self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()
