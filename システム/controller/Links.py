from flask import render_template, redirect, url_for, request, session, flash, Blueprint
from dao.LinkManagement import *

links_bp = Blueprint('links', __name__)

def validation_link_goals(goal_id_01,goal_id_02):
    validation_result = [True,'','']
    if goal_id_01 == goal_id_02:
        validation_result = [False,'同じ目標同士は紐付けできません','top_flash']
    elif check_link_exist(goal_id_01,goal_id_02):
        validation_result = [False,'既に紐付けられています','top_flash']
    return validation_result

@links_bp.route('/link_goals',methods=["POST"])
def add_goal():
    goal_id_01 = request.form['goal_id_01']
    goal_id_02 = request.form['goal_id_02']
    validation_result = validation_link_goals(goal_id_01,goal_id_02)
    validation_result_flg = validation_result[0]
    if validation_result_flg:
        insert_result = insert_goal_links(goal_id_01,goal_id_02)
        if insert_result:
            flash('紐付けに成功しました','top_flash')
            return redirect(url_for('index'))
        else:
            flash('登録に失敗しました','top_flash')
            return redirect(url_for('display_link_goals'))
    else:
        flash_msg = validation_result[1]
        flash_category = validation_result[2]
        flash(flash_msg,flash_category)
        return redirect(url_for('display_link_goals'))
