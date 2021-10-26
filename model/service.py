from database.database import db
from .model import User


def getUser(id=1):
    user = User.getUserById(id=id)
    result = {
        'id': user.id,
        'name': user.name
    }
    return result

