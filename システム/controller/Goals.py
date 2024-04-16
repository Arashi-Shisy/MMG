from flask import render_template, redirect, url_for, request, session, flash, Blueprint
from dao.GoalManagement import *
from dao.LinkManagement import *

goals_bp = Blueprint('goals', __name__)

@goals_bp.route('/update_goal/goal_id=<goal_id>',methods=["POST"])
def update_goal(goal_id):
    goal_title = request.form['goal_title']
    action = request.form['action']
    deadline = request.form['deadline']
    update_result = update_set_goal(goal_title,action,deadline,goal_id)
    if update_result:
        flash('編集に成功しました','top_flash')
        return redirect(url_for('index'))
    else:
        flash('編集に失敗しました','top_flash')
        return redirect(url_for('index'))
    
@goals_bp.route('/delete_goal/goal_id=<goal_id>')
def delete_goal(goal_id):
    delete_result = delete_set_goal(goal_id)
    if delete_result:
        flash('目標を削除しました','top_flash')
        return redirect(url_for('index'))
    else:
        flash('削除に失敗しました','top_flash')
        return redirect(url_for('index'))
    
@goals_bp.route('/add_goal',methods=["POST"])
def add_goal():
    user_id = session.get('login_user_id')
    goal_title = request.form['goal_title']
    action = request.form['action']
    deadline = request.form['deadline']
    insert_result = insert_goal(user_id,goal_title,action,deadline)
    if insert_result:
        flash('登録に成功しました','top_flash')
        return redirect(url_for('index'))
    else:
        flash('登録に失敗しました','top_flash')
        return redirect(url_for('index'))
    

@goals_bp.route('/evaluation_goal/goal_id=<goal_id>',methods=["POST"])
def evaluation_goal(goal_id):
    status = request.form['status']
    evaluation = request.form['evaluation']
    evaluation_result = evaluation_set_goal(goal_id,status,evaluation)
    if evaluation_result:
        return redirect(url_for('display_evaluation_goal', goal_id=goal_id, message='evaluation_success'))
    else:
        flash('評価登録に失敗しました','top_flash')
        return redirect(url_for('index'))

@goals_bp.route('/subsequent_goal_registration/goal_id=<goal_id>',methods=["POST"])
def subsequent_goal_registration(goal_id):
    user_id = session.get('login_user_id')
    goal_title = request.form['goal_title']
    action = request.form['action']
    deadline = request.form['deadline']
    insert_result = insert_goal(user_id,goal_title,action,deadline)
    if insert_result:
        goal_id_01 = goal_id
        goal_id_02 = get_latest_goal_id(goal_title,action,deadline)
        insert_result = insert_goal_links(goal_id_01,goal_id_02)
        if insert_result:
            flash('登録に成功しました','top_flash')
            return redirect(url_for('index'))
        else:
            delete_set_goal(goal_id_02)
            flash('登録に失敗しました','top_flash')
            return redirect(url_for('display_subsequent_goal_registration',goal_id=goal_id))
    else:
        flash('登録に失敗しました','top_flash')
        return redirect(url_for('index'))