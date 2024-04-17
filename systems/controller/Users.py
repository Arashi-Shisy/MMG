from flask import render_template, redirect, url_for, request, session, flash, Blueprint
from dao.UserManagement import *
import re

users_bp = Blueprint('users', __name__)

def validation_user_registration(email,password,password_check):
    validation_result = [True,'','']
    if email == "":
        validation_result = [False,'メールアドレスは必須項目です','email_flash']
    elif not "@" in email:
        validation_result = [False,'メールアドレスの形式が不正です','email_flash']
    elif password == "":
        validation_result = [False,'パスワードは必須項目です','password_flash']
    elif not (8 <= len(password) <= 12 and re.match(r"^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]+$", password)):
        validation_result = [False,'パスワードは半角英数混合の8~12文字で入力してください','password_flash']
    elif password != password_check:
        validation_result = [False,'パスワードが一致しません','password_check_flash']
    else:
        user_exist = check_user_exist(email)
        if not user_exist:
            validation_result = [False,'このメールアドレスは既に使われています','email_flash']
    return validation_result

@users_bp.route('/user_registration',methods=["POST"])
def user_registration():
    email = request.form['email']
    password = request.form['password']
    password_check = request.form['password_check']
    session['email_input']=email
    validation_result = validation_user_registration(email,password,password_check)
    validation_result_flg = validation_result[0]
    if validation_result_flg:
        registration_result = insert_user(email,password)
        if registration_result:
            flash('会員登録に成功しました','top_flash')
            return redirect(url_for('display_login'))
        else:
            flash('予期せぬエラーが発生しました','top_flash')
            return redirect(url_for('display_user_registration'))
    else:
        flash_msg = validation_result[1]
        flash_category = validation_result[2]
        flash(flash_msg,flash_category)
        return redirect(url_for('display_user_registration'))

def validation_login(email,password):
    validation_result = [True,'','']
    if email == "":
        validation_result = [False,'メールアドレスは必須項目です','email_flash']
    elif password == "":
        validation_result = [False,'パスワードは必須項目です','password_flash']
    else:
        user_exist = check_user_exist(email)
        if user_exist:
            validation_result = [False,'メールアドレスが登録されていません','email_flash']
    return validation_result

@users_bp.route('/login',methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    session['email_input']=email
    validation_result = validation_login(email,password)
    validation_result_flg = validation_result[0]
    if validation_result_flg:
        login_result = login_check(email,password)[0]
        login_user_id = login_check(email,password)[1]
        if login_result:
            session['login'] = True
            session['login_user_id'] = login_user_id
            return redirect(url_for('index'))
        else:
            flash('パスワードが間違っています','password_flash')
            return redirect(url_for('display_login'))
    else:
        flash_msg = validation_result[1]
        flash_category = validation_result[2]
        flash(flash_msg,flash_category)
        return redirect(url_for('display_login'))
    
