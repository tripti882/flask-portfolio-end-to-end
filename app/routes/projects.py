from flask import Blueprint, render_template
import json

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/projects")
def projects():
    # Load data from JSON
    with open("data/projects.json") as f:
        projects_data = json.load(f)
    return render_template("projects.html", title="Projects", projects=projects_data)
