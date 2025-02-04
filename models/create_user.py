from models.database import SessionLocal
from models.models import User
import os


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


admin1_user = os.getenv("ADMIN_USER1")
admin1_pass = os.getenv("ADMIN_PASS1")

admin2_user = os.getenv("ADMIN_USER2")
admin2_pass = os.getenv("ADMIN_PASS2")

create_user(admin1_user, admin1_pass)
create_user(admin2_user, admin2_pass)
