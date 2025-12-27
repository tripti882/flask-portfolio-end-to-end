from flask import Blueprint, render_template, request, redirect, url_for, flash
import json, os

contact_bp = Blueprint("contact", __name__)

# Get absolute path to data file
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_FILE = os.path.join(base_dir, "data", "messages.json")

# --- Helpers ---
def load_messages():
    """Safely load messages.json, return [] if empty or broken."""
    if not os.path.exists(DATA_FILE):
        # Ensure data directory exists
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []   # empty file → return empty list

def save_messages(messages):
    """Save messages back to messages.json."""
    # Ensure data directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)


# --- Routes ---
@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Collect form data with validation
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Validate form data
        if not name or not email or not message:
            flash("Please fill in all fields.", "error")
            return render_template("contact.html", title="Contact")

        new_entry = {"name": name, "email": email, "message": message}

        # Save
        try:
            messages = load_messages()
            messages.append(new_entry)
            save_messages(messages)
            flash("Thank you for your message! I'll get back to you soon.", "success")
            return redirect(url_for("contact.thankyou"))
        except Exception as e:
            flash("Sorry, there was an error sending your message. Please try again.", "error")
            return render_template("contact.html", title="Contact")

    return render_template("contact.html", title="Contact")


@contact_bp.route("/thankyou")
def thankyou():
    return render_template("thankyou.html", title="Thank You")
