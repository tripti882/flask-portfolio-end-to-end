from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import get_user_by_username, get_user_by_email, create_user

auth_bp = Blueprint("auth", __name__)

# ------------------------
# LOGIN
# ------------------------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username_or_email = request.form.get("username_or_email")
        password = request.form.get("password")

        if not username_or_email or not password:
            flash("Please provide both username/email and password", "error")
            return render_template("login.html")

        # Try to get user by username or email
        user = get_user_by_username(username_or_email) or get_user_by_email(username_or_email)

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("home.index"))

        flash("Invalid username/email or password", "error")

    return render_template("login.html")


# ------------------------
# SIGNUP
# ------------------------
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            flash("All fields are required", "error")
            return render_template("signup.html")

        # Check if user already exists
        if get_user_by_username(username):
            flash("Username already exists", "error")
            return render_template("signup.html")

        if get_user_by_email(email):
            flash("Email already exists", "error")
            return render_template("signup.html")

        hashed_password = generate_password_hash(password)

        create_user(username, email, hashed_password)

        flash("Account created successfully! Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("signup.html")


# ------------------------
# LOGOUT
# ------------------------
@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("home.index"))
