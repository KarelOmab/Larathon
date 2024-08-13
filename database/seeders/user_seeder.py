from bootstrap.app import db
from database.factories.user_factory import UserFactory

class UserSeeder:
    @staticmethod
    def run():
        """Seed the database with users."""
        users = UserFactory.create(size=10)
        for user in users:
            db.session.add(user)
        db.session.commit()
        print(f"Seeded {len(users)} users.")
