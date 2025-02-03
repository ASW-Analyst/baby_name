import pandas as pd
from models.database import SessionLocal
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

df_names = pd.concat([df_boys, df_girls], ignore_index=True)

# Open a database session
db = SessionLocal()

# Insert data
for _, row in df_names.iterrows():
    db.add(BabyName(name=row["Name"], gender=row["Gender"]))

db.commit()
db.close()

print("Database populated with baby names!")
