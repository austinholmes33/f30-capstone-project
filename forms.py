from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    first_name = StringField("First Name", [validators.InputRequired()])
    last_name = StringField("Last Name")

class AddBook(FlaskForm):
    title = StringField("Title", [validators.InputRequired()])
    length = IntegerField("Length", [validators.InputRequired()])
    overview = StringField("Overview")