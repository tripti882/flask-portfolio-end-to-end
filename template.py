import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name
project_name = "portfolio"

# All required files in your portfolio project
list_of_files = [
    "requirements.txt",
    "run.py",

    # app package
    "app/__init__.py",
    "app/routes/home.py",
    "app/routes/about.py",
    "app/routes/projects.py",
    "app/routes/contact.py",

    # templates
    "app/templates/base.html",
    "app/templates/index.html",
    "app/templates/about.html",
    "app/templates/projects.html",
    "app/templates/contact.html",

    # data files
    "data/projects.json",
    "data/skills.json",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
