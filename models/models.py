from sqlalchemy import Column, Integer, String, UniqueConstraint, Float, ForeignKey
from models.database import Base, engine
from flask_login import UserMixin

import bcrypt

# Define the Baby Names table


class BabyName(Base):
    __tablename__ = "names"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), index=True, nullable=False)
    gender = Column(String(4), nullable=False)

    # Enforce uniqueness for (name, gender) pairs
    __table_args__ = (UniqueConstraint(
        "name", "gender", name="unique_name_gender"),)


class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_id = Column(Integer, ForeignKey("names.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)


# Create the tables
Base.metadata.create_all(bind=engine)
