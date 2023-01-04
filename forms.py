from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, SubmitField, validators

class CreateUserForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    first_name = StringField("First Name", [validators.InputRequired()])
    last_name = StringField("Last Name")
    submit = SubmitField()

class AddBookForm(FlaskForm):
    title = StringField("Title", [validators.InputRequired()])
    author = StringField("Author", [validators.InputRequired()])
    length = IntegerField("Length", [validators.InputRequired()])
    overview = StringField("Overview")