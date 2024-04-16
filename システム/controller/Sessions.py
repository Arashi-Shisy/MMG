from flask import session

def check_session_status():
    if session.get('login') == None: 
        return True
    elif session.get('login_user_id') == None: 
        return True
    else:
        return False