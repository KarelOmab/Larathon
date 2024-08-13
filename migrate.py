"""
python migrate.py
python migrate.py --down
python migrate.py --fresh
"""
import os
import sys
import importlib.util
from bootstrap.app import app, db

def apply_migrations(direction='up', extend_existing=False):
    migrations_dir = os.path.join(os.getcwd(), 'database', 'migrations')
    migration_files = [f for f in sorted(os.listdir(migrations_dir)) if f.endswith('.py')]

    for migration_file in migration_files:
        module_name = migration_file[:-3]  # Remove '.py'
        file_path = os.path.join(migrations_dir, migration_file)

        if module_name in sys.modules:
            del sys.modules[module_name]

        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        
        try:
            spec.loader.exec_module(module)

            if hasattr(module, direction):
                print(f"Applying migration: {migration_file} ({direction})")
                if direction == 'up':
                    getattr(module, direction)(extend_existing=extend_existing)
                else:
                    getattr(module, direction)()
            else:
                print(f"Skipping migration: {migration_file} ({direction} method not found)")
        except Exception as e:
            print(f"Error during migration {migration_file} ({direction}): {e}")

def drop_all_tables():
    print("Dropping all tables...")
    db.reflect()
    db.drop_all()
    db.metadata.clear()  # Clear the MetaData registry
    print("All tables dropped.")

if __name__ == '__main__':
    fresh = '--fresh' in sys.argv
    extend_existing = '--extend-existing' in sys.argv
    direction = 'down' if '--down' in sys.argv else 'up'

    with app.app_context():  # Ensure the app context is active
        if fresh:
            drop_all_tables()

        apply_migrations(direction, extend_existing=extend_existing)
        print(f"Migrations applied successfully in {direction} direction.")

