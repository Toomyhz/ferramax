from app.modules.users.models import User
from extensions import db

def get_by_email(email):
    return db.session.query(User).filter(User.email == email).first()

def create_user(data):
    user = User(**data)

    db.session.add(user)
    db.session.commit()
    return user
