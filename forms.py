from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, SubmitField, validators

class CreateUserForm(FlaskForm):
    email = StringField("Email", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    first_name = StringField("First Name", [validators.InputRequired()])
    last_name = StringField("Last Name")
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", [validators.InputRequired()])
    password = PasswordField("Password", [validators.InputRequired()])
    submit = SubmitField()

class AddBookForm(FlaskForm):
    title = StringField("Title", [validators.InputRequired()])
    author = StringField("Author", [validators.InputRequired()])
    length = IntegerField("Length", [validators.InputRequired()])
    overview = StringField("Overview")
    submit = SubmitField()