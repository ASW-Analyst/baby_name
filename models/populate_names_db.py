import pandas as pd
from sqlalchemy import text
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

data_list = [tuple(row) for row in df_names[["Name", "Gender"]].values]

# ✅ Fix: Wrap SQL statement in `text()`
sql = text("INSERT INTO names (name, gender) VALUES (:1, :2,)")

# Use `executemany()` for bulk insert
with engine.connect() as connection:
    connection.execute(sql, data_list)

print("Database successfully populated!")
