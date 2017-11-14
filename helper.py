from app import db
from app.models import Type, Frequency, UeModel, Board

db.create_all()
Type.insert_types()
Frequency.insert_frequency()
UeModel.insert_models()
Board.insert_models()


