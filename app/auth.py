from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models.database import SessionLocal
from models.models import User

auth = Blueprint("auth", __name__)

# Flask-Login setup
login_manager = LoginManager()
login_manager.login_view = "auth.login"


# User class for Flask-Login
class UserAuth(UserMixin):
    def __init__(self, user):
        self.id = user.id
        self.username = user.username


@login_manager.user_loader
def load_user(user_id):
    """Loads a user from the database given the user ID."""
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return UserAuth(user) if user else None


# Login Route
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = SessionLocal()
        user = db.query(User).filter(User.username == username).first()
        db.close()

        if user and user.verify_password(password):
            login_user(UserAuth(user))
            return redirect(url_for("main.rate"))  # Redirect to rating page after login

        flash("Invalid username or password", "danger")

    return render_template("login.html")


# Logout Route
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
