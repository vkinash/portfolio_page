from db_config import db
from flask import render_template, request, redirect, url_for, flash
from app.models.users import Login
from werkzeug.security import generate_password_hash, check_password_hash
from const import SECRET
from flask_login import login_user, logout_user, login_required


def login():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = db.session.query(Login).filter_by(name=name).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))

        login_user(user, remember=remember)
        return redirect(url_for('edit_profile'))
    else:
        return render_template("login.html")


@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def signup():
    if request.method == "POST":
        scrt = request.form.get('secret')
        name = request.form.get('name')
        password = request.form.get('password')

        if scrt != SECRET:
            flash({"type": "secret", "message": 'Wrong secret'})
            return redirect(url_for('signup'))

        user = db.session.query(Login).filter_by(name=name).first()

        if user:
            flash({"type": "exists", "message": 'User already exists'})
            return redirect(url_for('signup'))

        new_user = Login(name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    else:
        return render_template("signup.html")

