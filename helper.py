from app import db
from app.models import Type, Frequency, UeModel

db.create_all()
Type.insert_types()
Frequency.insert_frequency()
UeModel.insert_models()



