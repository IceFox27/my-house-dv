from datetime import datetime
from ..extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    avatar = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)