from bootstrap.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    email_verified_at = db.Column(db.DateTime, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    remember_token = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def set_password(self, password):
        """Generate a hashed password and store it."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check a hashed password against a plain-text password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.name}>'
