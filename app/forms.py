from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
from app.models import User
class LoginForm(FlaskForm):
    """docstring for ."""

    username=StringField("Username", validators=[DataRequired()])
    password=PasswordField("Password", validators=[DataRequired()])
    remember_me=BooleanField("Remember me")
    submit=SubmitField("Login in")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    password2 = PasswordField("Reapeat Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()

        if user is not None:
            raise ValidationError("Please use a different username")

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError("Please use a email address")

class DeleteForm(FlaskForm):
    """docstring for ."""
    password=PasswordField("Password", validators=[DataRequired()])
    submit_delete=SubmitField("Delete")

class ChangePassword(FlaskForm):
    old_password=PasswordField("old password")
    new_password=PasswordField("new password", validators=[DataRequired()])
    submit_change_password=SubmitField("Change")
