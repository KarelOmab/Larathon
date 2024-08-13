from bootstrap.app import db
from database.factories import generate_user

def seed_users(num_users=3):
    db.create_all()
    for _ in range(num_users):
        user = generate_user()
        db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    seed_users(10)
