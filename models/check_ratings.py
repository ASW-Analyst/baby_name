import pandas as pd
from models.database import SessionLocal

# Open a database session
db = SessionLocal()

# Load all ratings into a DataFrame
df = pd.read_sql("SELECT * FROM ratings;", con=db.bind)

# Close the database session
db.close()

# Print the first few ratings
print(df.head())
