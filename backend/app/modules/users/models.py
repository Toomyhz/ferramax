from datetime import datetime, timezone
from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255),unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    email_verified = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    roles = db.relationship('UserRole', back_populates='user', cascade='all, delete-orphan')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.BigInteger, db.ForeignKey('roles.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.UniqueConstraint('user_id', 'role_id'),
    )

    user = db.relationship('User', back_populates='roles')
    role = db.relationship('Role')

class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

class RolePermission(db.Model):
    __tablename__ = 'role_permissions'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    role_id = db.Column(db.BigInteger, db.ForeignKey('roles.id'), nullable=False)
    permission_id = db.Column(db.BigInteger, db.ForeignKey('permissions.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default= lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.UniqueConstraint('role_id', 'permission_id'),
    )