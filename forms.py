from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class CreateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=255)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=255)])
    confirm_password = PasswordField("Confirm Password", validators=[(DataRequired(), Length(min=3, max=255), EqualTo("password"))])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name")
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=255)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=255)])
    submit = SubmitField()

class AddBookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=6, max=255)])
    author = StringField("Author", validators=[DataRequired(), Length(min=6, max=255)])
    length = IntegerField("Length", validators=[DataRequired(), Length(max=255)])
    overview = TextAreaField("Overview", Length(max=255))
    submit = SubmitField()

# SOME SORT OF UPDATE FORM FOR PAGES READ
# TO BE USED ON BOOK_DETAILS PAGE