from . import db


class Type(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    elements = db.relationship('Element', backref='type', lazy='dynamic')

    @staticmethod
    def insert_types():
        types = ['SWH_L', 'SWH_U', 'ECV_L', 'ECV_U', 'ASU_L', 'ASU_U']
        for t in types:
            type = Type.query.filter_by(name=t).first()
            if type is None:
                type = Type(name=t)
            db.session.add(type)
        db.session.commit()

    def __repr__(self):
        return '<Type %r>' % self.name


class Element(db.Model):
    __tablename__ = 'elements'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(32), unique=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    # status = db.Column(db.Boolean, default=False)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    usage = db.Column(db.String(32))
    pc_ip = db.Column(db.String(32))

    def __repr__(self):
        return '<Element %r>' % self.name


class Ecns(db.Model):
    __tablename__ = 'ecns'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(32), unique=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    usage = db.Column(db.String(32))
    pc_ip = db.Column(db.String(32))

    def __repr__(self):
        return '<Ecns %r>' % self.name


class Eapp(db.Model):
    __tablename__ = 'eapp'
    id = db.Column(db.Integer, primary_key=True)
    mdc_ip = db.Column(db.String(32), unique=True)
    mdc_username = db.Column(db.String(64))
    mdc_password = db.Column(db.String(64))
    udc_ip = db.Column(db.String(32), unique=True)
    udc_username = db.Column(db.String(64))
    udc_password = db.Column(db.String(64))
    root_username = db.Column(db.String(64))
    root_password = db.Column(db.String(64))
    # ubp_username = db.Column(db.String(64))
    ubp_password = db.Column(db.String(64))

    def __repr__(self):
        return '<Eapp %r>' % self.name


class Frequency(db.Model):
    __tablename__ = 'frequency'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64), unique=True)
    enbs = db.relationship('Enb', backref='frequency', lazy='dynamic')
    ues = db.relationship('UE', backref='frequency', lazy='dynamic')

    @staticmethod
    def insert_frequency():
        frequency_list = ['400M', '800M', '1.4G', '1.8G', '2.3G']
        for f in frequency_list:
            number = Frequency.query.filter_by(number=f).first()
            if number is None:
                number = Frequency(number=f)
            db.session.add(number)
        db.session.commit()

    def __repr__(self):
        return '<Frequency %r>' % self.frequency


class Enb(db.Model):
    __tablename__ = 'enbs'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(32), unique=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    # status = db.Column(db.Boolean, default=False)
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequency.id'))
    cell_id1 = db.Column(db.String(32))
    cell_id2 = db.Column(db.String(32))

    def __repr__(self):
        return '<Enb %r>' % self.ip


class UeModel(db.Model):
    __tablename__ = 'ue_models'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    ues = db.relationship('UE', backref='ue_model', lazy='dynamic')

    @staticmethod
    def insert_models():
        models = ['EP650', 'EP680', 'EP820']
        for m in models:
            model = UeModel.query.filter_by(name=m).first()
            if model is None:
                model = UeModel(name=m)
            db.session.add(model)
        db.session.commit()

    def __repr__(self):
        return '<Type %r>' % self.name


class UE(db.Model):
    __tablename__ = 'ues'
    id = db.Column(db.Integer, primary_key=True)
    imsi = db.Column(db.String(32), unique=True)
    ki = db.Column(db.String(32))
    imei = db.Column(db.String(64))
    frequency_id = db.Column(db.Integer, db.ForeignKey('frequency.id'))
    ue_model_id = db.Column(db.Integer, db.ForeignKey('ue_models.id'))




