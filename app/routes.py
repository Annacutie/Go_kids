from app import app, db
from flask import render_template, request, session, url_for, redirect, send_from_directory
from random import randint, choice
from add_and_substact import *
from app.forms import DeleteForm, LoginForm, RegistrationForm, ChangePassword
from flask_login import current_user, login_user
from app.models import User, Progress, ResetPassword
from flask_login  import logout_user, login_required
from sqlite3 import *

operations=["+", "-"]

@app.route("/")
@app.route("/index")
def index():
    title={"main_title":"Go_Adrorible"}
    return render_template("index.html", title=title)

@app.route("/add_and_substact")
def add_and_substact():
    title={"main_title":"add and substact"}
    maths_test={}
    maths_test["add"]=gen_questions(2, "+")
    maths_test["add"]=gen_questions(2, "-")
    return render_template("add_and_substact.html", title=title, maths_test=maths_test)

@app.route("/check",  methods=["POST", ])
def result():
    user_answers=request.form
    answer_list=[]
    print(user_answers)
    '''
    for i in user_answers:
        try:
            answer=int(i)
            answer_list.append(answer)
        except:
            answer_list.append(i)
            '''
    if session["test_type"]=="add_and_substact":
        score=check(session["correct_answers"], user_answers, "english")
        #print(f"this is user's answers {answer_list}")
    else:
        score=check(session["correct_answers"], user_answers)
    m=''
    if current_user.is_authenticated:
        c_user=Progress.query.filter_by(user_id=current_user.id).first()
        c_user.total_score=c_user.total_score + score
        if session["test_type"] == "maths":
            c_user.maths_score=c_user.maths_score + score
            db.session.commit()


        elif session["test_type"] == "science":
            c_user.science_score=c_user.science_score + score
            db.session.commit()
        elif session["test_type"] == "english":
            c_user.english_score=c_user.english_score + score
            db.session.commit()
    else:
        m="You need to login in order to save your score"
    return render_template("check.html", result=score, comment=comment, pestege=pestege, m=m)
