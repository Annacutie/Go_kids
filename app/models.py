##########
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
class User(UserMixin, db.Model):

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), index=True, unique=True)
    email=db.Column(db.String(120), index=True, unique=True)
    password_hash=db.Column(db.String(128))
    results=db.relationship("Progress", backref='student', lazy="dynamic")
    reset=db.relationship("ResetPassword", backref='RestorePassword', lazy="dynamic")

    def __repr__(self):
        return f"User {self.username}"

    def set_password(self, password):
        self.password_hash=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Progress(UserMixin, db.Model):
    total_score=db.Column(db.Integer, index=True)
    id=db.Column(db.Integer, primary_key=True)
    science_score=db.Column(db.Integer)
    maths_score=db.Column(db.Integer)
    english_score=db.Column(db.Integer)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))

class ResetPassword(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    question=db.Column(db.String(100), index=True)
    answer=db.Column(db.String(100), index=True)
    user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
