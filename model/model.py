from database.database import db
from sqlalchemy import func


# model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)

    def getCount():
        return db.session.query(func.count(User.id)).scalar()

    def getUserById(id=1):
        return User.query.filter(User.id == id).first()
