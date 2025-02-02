from sqlalchemy import Column, Integer, String, UniqueConstraint
from models.database import Base, engine

# Define the Baby Names table


class BabyName(Base):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    gender = Column(String)

    # Enforce uniqueness for (name, gender) pairs
    __table_args__ = (UniqueConstraint(
        "name", "gender", name="unique_name_gender"),)


# Create the tables
Base.metadata.create_all(bind=engine)
