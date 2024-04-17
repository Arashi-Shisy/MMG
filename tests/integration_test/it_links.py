import unittest
from flask import Flask, session
import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG"))
from systems.app import app
from systems.controller.Links import links_bp
from test_data import FORM_DATA
from test_setting import *

app.testing = True
app.register_blueprint(links_bp, name='test_links')

class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_link_goals_True(self):
        with app.test_client() as client:
            response = client.post('/link_goals', data=FORM_DATA['link_goals'])
            self.assertEqual(response.status_code, 302)
    def test_link_goals_False(self):
        with app.test_client() as client:
            response = client.post('/link_goals', data=FORM_DATA['link_goals_false'])
            self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
