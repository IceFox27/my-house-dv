from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(), Length(min=2, max=100)])
    surname = StringField('Фамилия', validators=[DataRequired(), Length(min=2, max=50)])
    patronymic = StringField('Отчество', validators=[Length(max=50)])
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите фото сотрудника', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрировать сотрудника')