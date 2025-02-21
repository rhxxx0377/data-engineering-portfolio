from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from models import User


class UserForm(FlaskForm):
    name = StringField("名前", validators=[DataRequired(message="名前は必須です")])
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスは必須です"),
            Email(message="有効なメールアドレスを入力してください"),
        ],
    )
    submit = SubmitField("登録")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("このメールアドレスは既に登録されています")
