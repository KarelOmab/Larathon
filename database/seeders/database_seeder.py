from bootstrap.app import db
from database.seeders.user_seeder import UserSeeder

def run_seeders():
    """Run all seeders."""
    UserSeeder.run()

if __name__ == '__main__':
    with db.app.app_context():
        run_seeders()
        print("Database seeding completed.")
