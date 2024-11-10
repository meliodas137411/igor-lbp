from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import users

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user.password == password:
            session['username'] = username
            return redirect(url_for('main.logado'))  
    return render_template('login.html')
