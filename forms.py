from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

class CreateUserForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=255)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=255)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=3, max=255)])
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
    pages = IntegerField("Pages", validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    overview = TextAreaField("Overview", validators=[Length(max=255)])
    cover_img = StringField("Cover Image", validators=[DataRequired()])
    submit = SubmitField()

# form on books page that allows user to update all book info
# and also add whether or not they're currently reading
# and their pages read and thoughts
class UpdateBookForm(FlaskForm):
    title = StringField("Title", validators=[Length(min=6, max=255)])
    author = StringField("Author", validators=[Length(min=6, max=255)])
    pages = IntegerField("Pages", validators=[NumberRange(min=0, max=1000000)])
    overview = TextAreaField("Overview", validators=[Length(max=255)])
    pages_read = IntegerField("Pages Read", validators=[NumberRange(min=0, max=1000000)])
    currently_reading = BooleanField("Currently Reading", default=False)
    submit = SubmitField()


