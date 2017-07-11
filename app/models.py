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




