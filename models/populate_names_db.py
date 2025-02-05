import pandas as pd
from models.database import SessionLocal, engine
from models.models import BabyName

df_boys = pd.read_excel("data/boysnames2023.xlsx",
                        sheet_name="Table_6",
                        skiprows=4)

df_boys = df_boys.drop(columns=["Rank", "Count"])
df_boys["Gender"] = "Boy"

df_girls = pd.read_excel("data/girlsnames2023.xlsx",
                         sheet_name="Table_6",
                         skiprows=4)
df_girls = df_girls.drop(columns=["Rank", "Count"])
df_girls["Gender"] = "Girl"

df_names = pd.concat([df_boys, df_girls])
df_names_val = df_names.values
# Open a database session
db = SessionLocal()

# Insert data
with engine.connect() as connection:
    sql = "INSERT INTO names (name, gender) VALUES (%s, %s)"
    connection.execute(sql, df_names_val.tolist())

db.commit()
db.close()

print("Database populated with baby names!")
