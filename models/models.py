from sqlalchemy import Column, Integer, String, UniqueConstraint
from models.database import Base, engine

import bcrypt

# Define the Baby Names table


class BabyName(Base):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    gender = Column(String)

    # Enforce uniqueness for (name, gender) pairs
    __table_args__ = (UniqueConstraint(
        "name", "gender", name="unique_name_gender"),)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())


# Create the tables
Base.metadata.create_all(bind=engine)
