from flask import Blueprint, render_template
import json
import os

projects_bp = Blueprint("projects", __name__)

@projects_bp.route("/projects")
def projects():
    # Load data from JSON - use absolute path based on app root
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_file = os.path.join(base_dir, "data", "projects.json")
    
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            projects_data = json.load(f)
    except FileNotFoundError:
        projects_data = []
    except json.JSONDecodeError:
        projects_data = []
    
    return render_template("projects.html", title="Projects", projects=projects_data)
