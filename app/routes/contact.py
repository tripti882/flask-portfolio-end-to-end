from flask import Blueprint, render_template, request, redirect, url_for
import json, os

contact_bp = Blueprint("contact", __name__)
DATA_FILE = "data/messages.json"

# --- Helpers ---
def load_messages():
    """Safely load messages.json, return [] if empty or broken."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []   # empty file → return empty list

def save_messages(messages):
    """Save messages back to messages.json."""
    with open(DATA_FILE, "w") as f:
        json.dump(messages, f, indent=4)


# --- Routes ---
@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Collect form data
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        new_entry = {"name": name, "email": email, "message": message}

        # Save
        messages = load_messages()
        messages.append(new_entry)
        save_messages(messages)

        # Redirect to thank you page
        return redirect(url_for("contact.thankyou"))

    return render_template("contact.html", title="Contact")


@contact_bp.route("/thankyou")
def thankyou():
    return render_template("thankyou.html", title="Thank You")
