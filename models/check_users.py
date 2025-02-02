import pandas as pd
from models.database import SessionLocal

# Open database session
db = SessionLocal()

# Query names table
df = pd.read_sql("SELECT * FROM users LIMIT 5;", con=db.bind)
db.close()

# Print sample data
print(df)
