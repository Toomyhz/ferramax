from app.modules.users.models import User, Role, UserRole
from extensions import db
def get_user_by_email(email):
    return db.session.query(User).filter(User.email == email).first()

def get_user_by_id(user_id):
    return db.session.query(User).filter(User.id == user_id).first()

def create_user(data):
    user = User(**data)
    db.session.add(user)
    return user

def get_role_by_id(role_id):
    return db.session.query(Role).filter(Role.id == role_id).first()

def get_role_by_name(role_name):
    return db.session.query(Role).filter(Role.name == role_name).first()

def assign_role(user, role):
    user.roles.append(UserRole(user_id=user.id, role_id=role.id))
    return user
