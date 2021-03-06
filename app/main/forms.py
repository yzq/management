# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import Required, Length, ValidationError
from app.models import Type, Element, Eapp, Ecns, Frequency, UeModel, Board


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


class EditeCNSForm(Form):
    ip = StringField(u'维护IP', validators=[Required(), Length(1, 32)])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = StringField(u'密码', validators=[Required(), Length(1, 64)])
    usage = SelectField(u'环境')
    pc_ip = StringField(u'对接PC')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditeCNSForm, self).__init__(*args, **kwargs)
        self.usage.choices = [('simulation', u'模拟线'), ('real', u'真实线')]


class EditeCNS280Form(Form):
    tsn_ip = StringField(u'TSN IP', validators=[Required(), Length(1, 32)])
    tsn_username = StringField(u'TSN 用户名', validators=[Required(), Length(1, 64)])
    tsn_password = StringField(u'TSN 密码', validators=[Required(), Length(1, 64)])
    usn_ip = StringField(u'USN IP', validators=[Required(), Length(1, 32)])
    usn_username = StringField(u'USN 用户名', validators=[Required(), Length(1, 64)])
    usn_password = StringField(u'USN 密码', validators=[Required(), Length(1, 64)])
    ugw_ip = StringField(u'UGW IP', validators=[Required(), Length(1, 32)])
    ugw_username = StringField(u'UGW 用户名', validators=[Required(), Length(1, 64)])
    ugw_password = StringField(u'UGW 密码', validators=[Required(), Length(1, 64)])
    usage = SelectField(u'环境')
    pc_ip = StringField(u'对接 PC')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditeCNS280Form, self).__init__(*args, **kwargs)
        self.usage.choices = [('simulation', u'模拟线'), ('real', u'真实线')]


class EditeAPPForm(Form):
    mdc_ip = StringField('MDC IP', validators=[Required(), Length(1, 32)])
    mdc_username = StringField(u'MDC 用户名', validators=[Required(), Length(1, 64)])
    mdc_password = StringField(u'MDC 密码', validators=[Required(), Length(1, 64)])
    udc_ip = StringField('UDC IP', validators=[Required(), Length(1, 32)])
    udc_username = StringField(u'UDC 用户名', validators=[Required(), Length(1, 64)])
    udc_password = StringField(u'UDC 密码', validators=[Required(), Length(1, 64)])
    # root_username = StringField(u'Linux 用户名', validators=[Required(), Length(1, 64)])
    root_password = StringField(u'root 密码', validators=[Required(), Length(1, 64)])
    # ubp_username = StringField(u'ubp 用户名', validators=[Required(), Length(1, 64)])
    ubp_password = StringField(u'ubp 密码', validators=[Required(), Length(1, 64)])
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditeAPPForm, self).__init__(*args, **kwargs)


        # def validate_mdc_ip(self, field):
        #     if self.eapp.mdc_ip != field.data and \
        #             Eapp.query.filter_by(mdc_ip=field.data).first():
        #         raise ValidationError("MDC IP already in use")
        #
        # def validate_udc_ip(self, field):
        #     if self.eapp.udc_ip != field.data and \
        #             Eapp.query.filter_by(udc_ip=field.data).first():
        #         raise ValidationError("UDC IP already in use")


class EditeNBForm(Form):
    ip = StringField(u'维护 IP', validators=[Required(), Length(1, 32)])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = StringField(u'密码', validators=[Required(), Length(1, 64)])
    board = SelectField(u'模式', coerce=int)
    frequency = SelectField(u'频率', coerce=int)
    enb_id = StringField(u'基站 ID')
    cell_id1 = StringField(u'小区 ID1')
    cell_id2 = StringField(u'小区 ID2')
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditeNBForm, self).__init__(*args, **kwargs)
        self.frequency.choices = [(frequency.id, frequency.number)
                                  for frequency in Frequency.query.order_by(Frequency.number).all()]

        self.board.choices = [(board.id, board.board_model)
                              for board in Board.query.order_by(Board.board_model).all()]


class EditUEForm(Form):
    model = SelectField(u'型号', coerce=int)
    imsi = StringField(u'IMSI', validators=[Required(), Length(1, 32)])
    imei = StringField(u'IMEI', validators=[Required(), Length(1, 64)])
    ki = StringField(u'Ki', validators=[Required(), Length(1, 64)])
    frequency = SelectField(u'频率', coerce=int)
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditUEForm, self).__init__(*args, **kwargs)
        self.frequency.choices = [(frequency.id, frequency.number)
                                  for frequency in Frequency.query.order_by(Frequency.number).all()]
        self.model.choices = [(model.id, model.name)
                              for model in UeModel.query.order_by(UeModel.name).all()
                              if model.name != 'CPE' and model.name != 'TAU']


class EditPsUeForm(EditUEForm):
    ip = StringField(u'维护 IP', validators=[Required(), Length(1, 32)])
    username = StringField(u'用户名', validators=[Required(), Length(1, 64)])
    password = StringField(u'密码', validators=[Required(), Length(1, 64)])
    submit = SubmitField(u'提交')

    def __init__(self, *args, **kwargs):
        super(EditPsUeForm, self).__init__(*args, **kwargs)
        self.frequency.choices = [(frequency.id, frequency.number)
                                  for frequency in Frequency.query.order_by(Frequency.number).all()]
        self.model.choices = [(model.id, model.name)
                              for model in UeModel.query.order_by(UeModel.name).all()
                              if model.name == 'CPE' or model.name == 'TAU']
