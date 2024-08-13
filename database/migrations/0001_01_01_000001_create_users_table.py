from bootstrap.app import db
from app.Models.user import User

def up(extend_existing=False):
    if extend_existing:
        User.__table__.extend_existing = True
    User.__table__.create(bind=db.engine)
    print(f"Table '{User.__tablename__}' created.")

def down():
    User.__table__.drop(bind=db.engine)
    print(f"Table '{User.__tablename__}' dropped.")
