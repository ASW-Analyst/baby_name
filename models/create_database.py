from sqlalchemy import inspect
from models.database import engine
from models.models import Base, BabyName  # Import your models

# Create an inspector to check if the table exists
inspector = inspect(engine)
table_names = inspector.get_table_names()

# Drop only the "names" table if it exists
if "names" in table_names:
    print("Dropping existing 'names' table...")
    BabyName.__table__.drop(bind=engine, checkfirst=True)
else:
    print("'names' table does not exist, skipping drop.")

# Recreate the tables
print("Creating tables...")
Base.metadata.create_all(bind=engine)

print("Database updated successfully!")
