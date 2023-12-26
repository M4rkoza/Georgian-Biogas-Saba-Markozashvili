from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from wtforms.fields import StringField, SubmitField, PasswordField, RadioField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, length, equal_to
class AddInformationForm(FlaskForm):
    name = StringField ("სათაური", validators= [DataRequired()])
    subtext = StringField ("ტექსტი", validators= [DataRequired()])
    text = TextAreaField ("ქვეტექსტი", validators= [DataRequired()])
    img = FileField ("სურათი", validators= [FileRequired(), FileAllowed(["jpg", "png", "jpeg"]), FileSize(max_size=1024*1024 * 50)])
    submit = SubmitField("დამატება", validators= [DataRequired()])

class EditInformationForm(FlaskForm):
    editname = StringField ("რედაქტირებული სათაური", validators= [DataRequired()])
    editsubtext = StringField ("რედაქტირებული ტექსტი", validators= [DataRequired()])
    edittext = StringField ("რედაქტირებული ქვეტექსტი", validators= [DataRequired()])
    editimg = FileField("რედაქტირებული სურათი", validators=[FileAllowed(["jpg", "png", "jpeg"]), FileSize(max_size=1024 * 1024 * 50)])
    editsubmit = SubmitField("განახლება", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField("შეიყვანეთ სახელი")
    password = PasswordField("შეიყვანეთ პაროლი", validators=[length(min=6, max=16)])
    repeated_password = PasswordField("გაიმეორეთ პაროლი", validators=[equal_to("password", message= "შეყვანილი პაროლები არ ემთხვევა")])
    gender = RadioField("მონიშნეთ სქესი", choices= ["ქალი", "კაცი"])
    birthday = DateField("შეიყვანეთ დაბადების თარიღი")
    country = SelectField("მონიშნეთ ქვეყანა", choices=["მონიშნეთ ქვეყანა", "საქართველო", "საფრანგეთი", "ამერიკის შეერთებული შტატები", "დანია"])
    submit = SubmitField("რეგისტრაცია", validators= [DataRequired()])
class LoginForm(FlaskForm):
    username = StringField("შეიყვანეთ სახელი", validators=[DataRequired()])
    password = PasswordField("შეიყვანეთ პაროლი", validators=[DataRequired(), length(min=6, max=16)])
    submit = SubmitField("ავტორიზაცია", validators=[DataRequired()])