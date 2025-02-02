from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func
from models.database import SessionLocal
from models.models import BabyName, Rating

main = Blueprint("main", __name__)  # Define Blueprint


@main.route("/")
def home():
    """Homepage: Redirects to /rate if logged in."""
    if current_user.is_authenticated:
        return redirect(url_for("main.rate"))
    return redirect(url_for("auth.login"))


@main.route("/rate", methods=["GET", "POST"])
@login_required
def rate():
    """Show a random baby name and allow the user to rate it."""
    db = SessionLocal()
    name = db.query(BabyName).order_by(func.random()).first()

    if request.method == "POST":
        rating_value = float(request.form["rating"])
        new_rating = Rating(name_id=name.id, user_id=current_user.id, rating=rating_value)
        db.add(new_rating)
        db.commit()
        db.close()
        return redirect(url_for("main.rate"))

    db.close()
    return render_template("rate.html", name=name)
