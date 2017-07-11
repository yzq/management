# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required, Length, ValidationError
from app.models import Type, Element, Eapp


class EditForm(Form):
    ip = StringField(u'维护 IP', validators=[Required(), Length(1, 32)])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = StringField(u'密码', validators=[Required(), Length(1, 64)])
    type = SelectField(u'网元类型', coerce=int)
    usage = SelectField(u'环境')
    pc_ip = StringField(u'对接PC')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.type.choices = [(type.id, type.name)
                             for type in Type.query.order_by(Type.name).all()]
        self.usage.choices = [('simulation', u'模拟线'), ('real', u'真实线')]

    def validate_ip(self, field):
        if Element.query.filter_by(ip=field.data).first():
            raise ValidationError("Ip already in use")


class EditeCNSForm(Form):
    ip = StringField(u'维护 IP', validators=[Required(), Length(1, 32)])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = StringField(u'密码', validators=[Required(), Length(1, 64)])
    usage = SelectField(u'环境')
    pc_ip = StringField(u'对接PC')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditeCNSForm, self).__init__(*args, **kwargs)
        self.usage.choices = [('simulation', u'模拟线'), ('real', u'真实线')]

    def validate_ip(self, field):
        if Element.query.filter_by(ip=field.data).first():
            raise ValidationError("Ip already in use")


class EditeAPPForm(Form):
    mdc_ip = StringField('MDC IP', validators=[Required(), Length(1, 32)])
    mdc_username = StringField(u'MDC 用户名', validators=[Required(), Length(1, 64)])
    mdc_password = StringField(u'MDC 密码', validators=[Required(), Length(1, 64)])
    udc_ip = StringField('UDC IP', validators=[Required(), Length(1, 32)])
    udc_username = StringField(u'UDC 用户名', validators=[Required(), Length(1, 64)])
    udc_password = StringField(u'UDC 密码', validators=[Required(), Length(1, 64)])
    root_username = StringField(u'Linux 用户名', validators=[Required(), Length(1, 64)])
    root_password = StringField(u'Linux 密码', validators=[Required(), Length(1, 64)])
    # ubp_username = StringField(u'ubp 用户名', validators=[Required(), Length(1, 64)])
    ubp_password = StringField(u'ubp 密码', validators=[Required(), Length(1, 64)])
    submit = SubmitField(u'提交')


    def validate_mdc_ip(self, field):
        if Eapp.query.filter_by(mdc_ip=field.data).first():
            raise ValidationError("MDC IP already in use")

    # def validate_udc_ip(self, field):
    #     if Eapp.query.filter_by(udc_ip=field.data).first():
    #         raise ValidationError("UDC IP already in use")
