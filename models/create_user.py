from models.database import SessionLocal
from models.models import User


def create_user(username, password):
    db = SessionLocal()

    # Check if user already exists
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        print("⚠️ User already exists!")
        db.close()
        return

    # Hash password and store user
    user = User(username=username, password_hash=User.hash_password(password))
    db.add(user)
    db.commit()
    db.close()
    print(f"✅ User '{username}' created successfully!")
