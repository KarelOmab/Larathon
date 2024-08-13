from faker import Faker
from app.Models.User import User

fake = Faker()

def generate_user():
    user = User(
        name=fake.name(),
        email=fake.unique.email(),
    )
    user.set_password('password')  # Default password for all generated users
    return user
