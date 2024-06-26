import sys
import os
home_dir = os.path.expanduser("~")
sys.path.append(os.path.join(home_dir, "Desktop", "MMG","systems"))
sys.path.append(os.path.join( "/app"))
from flask import Flask, render_template, session
from controller.Users import *
from controller.Goals import *
from controller.Links import *
from controller.Sessions import *
import logging
import datetime

logging.basicConfig(filename='/app/app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__, static_folder='./templates/static')

# セッション暗号化キー設定
# randlst = [random.choice(string.ascii_letters + string.digits) for i in range(50)]
# app.secret_key = ''.join(randlst)
app.secret_key = 'aaa'

app.register_blueprint(users_bp)
app.register_blueprint(goals_bp)
app.register_blueprint(links_bp)

@app.route('/display_user_registration')
def display_user_registration():
    logging.debug('[Display]会員登録画面表示開始')
    email_input = session.get('email_input',"")
    return(render_template('user_registration.html',email_input=email_input))

@app.route('/display_login')
def display_login():
    logging.debug('[Display]ログイン画面表示開始')
    email_input = session.get('email_input',"")
    password_input = session.get('password_input',"")
    return(render_template('login.html',email_input=email_input,password_input=password_input))
    
@app.route('/')
def index():
    logging.debug('[Display]トップページ表示開始')
    if check_session_status():
        return redirect(url_for('display_login'))
    else:
        user_id = session.get('login_user_id')
        goal_list = get_goal_list(user_id)
        linked_goals = get_links(user_id)
        print(linked_goals)
        return(render_template('index.html', goal_list = goal_list,linked_goals=linked_goals,today = datetime.date.today()))

@app.route('/display_new_goal_registration')
def display_new_goal_registration():
    logging.debug('[Display]新規目標登録画面表示開始')
    if check_session_status():
        return redirect(url_for('display_login'))
    else:
        return(render_template('new_goal_registration.html'))

@app.route('/display_link_goals')
def display_link_goals():
    logging.debug('[Display]目標紐付け画面表示開始')
    if check_session_status():
        return redirect(url_for('display_login'))
    else:
        user_id = session.get('login_user_id')
        goal_list = get_goal_list(user_id)
    return(render_template('link_goals.html',goal_list = goal_list))

@app.route('/display_evaluation_goal/goal_id=<goal_id>')
def display_evaluation_goal(goal_id):
    logging.debug('[Display]目標評価画面表示開始')
    if check_session_status():
        return redirect(url_for('display_login'))
    else:
        goal_details = get_goal_details(goal_id)
        goal_detail = goal_details[0]
        return(render_template('evaluation_goal.html',goal_detail=goal_detail))

@app.route('/display_subsequent_goal_registration/goal_id=<goal_id>')
def display_subsequent_goal_registration(goal_id):
    logging.debug('[Display]後続目標登録画面表示開始')
    if check_session_status():
        return redirect(url_for('display_login'))
    else:
        goal_details = get_goal_details(goal_id)
        goal_detail = goal_details[0]
        return(render_template('subsequent_goal_registration.html',goal_detail=goal_detail))

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')