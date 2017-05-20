# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required, Length
from app.models import Type


class EditForm(Form):
    ip = StringField(u'维护 IP', validators=[Required(), Length(1, 32)])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = StringField(u'密码', validators=[Required(), Length(1, 64)])
    type = SelectField(u'网元类型', coerce=int)
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.type.choices = [(type.id, type.name)
                             for type in Type.query.order_by(Type.name).all()]
