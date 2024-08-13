from faker import Faker
from app.Models.user import User

fake = Faker()

class UserFactory:
    @staticmethod
    def __fabricate():
        """Create a single User instance."""
        user = User(
            name=fake.name(),
            email=fake.unique.email(),
            password=fake.password()
        )
        user.set_password(user.password)  # Hash the password
        return user

    @staticmethod
    def create(size=1):
        """Create a batch of User instances."""
        users = []
        for _ in range(size):
            user = UserFactory.__fabricate()
            users.append(user)
        return users
