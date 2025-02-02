import os
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
from models.database import SessionLocal
from models.models import User  # Ensure User is imported
from app.auth import auth  # Import authentication blueprint
from app.main import main  # Import main blueprint

# Load environment variables
load_dotenv()


def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")

    if not app.secret_key:
        raise ValueError("❌ SECRET_KEY is missing. Set it in the .env file.")

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        """Loads a user from the database given the user ID."""
        db = SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        db.close()
        return user  # This must return a User object

    # Register Blueprints (routes)
    app.register_blueprint(auth, url_prefix="/auth")  # Authentication routes
    app.register_blueprint(main)  # Main app routes

    return app


app = create_app()
