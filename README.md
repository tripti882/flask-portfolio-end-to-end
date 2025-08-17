# flask-portfolio-end-to-end
🚀 Flask Portfolio End-to-End

A personal portfolio website built with Flask, Tailwind CSS, and JSON data storage.
It showcases About Me, Projects, and Contact form — with submissions saved locally.

📌 Features

🏠 Home Page – clean landing page with intro.

👤 About Page – quick profile summary.

💻 Projects Page – dynamically loads project data from projects.json.

📬 Contact Page – form where users can send messages.

✅ Thank You Page – confirmation after form submission.

🎨 Responsive UI – styled with Tailwind CSS.

📂 JSON as Database – stores projects, skills, and contact messages.

🛠️ Tech Stack

Backend: Flask (Python)

Frontend: Jinja2 Templates + Tailwind CSS

Data Storage: JSON files (projects.json, messages.json, skills.json)

Deployment Ready: works on local server & can be deployed to Heroku, Render, or Vercel (with Python).

📂 Project Structure
flask-portfolio-end-to-end/
│── run.py                # Entry point
│── requirements.txt       # Dependencies
│── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes/            # Modular route files
│   │   ├── home.py
│   │   ├── about.py
│   │   ├── projects.py
│   │   └── contact.py
│   └── templates/         # HTML templates
│       ├── base.html
│       ├── index.html
│       ├── about.html
│       ├── projects.html
│       ├── contact.html
│       └── thankyou.html
│── data/
│   ├── projects.json
│   ├── skills.json
│   └── messages.json
│── venv/                  # Virtual environment (ignored in git)

⚡ Getting Started
1️⃣ Clone the repo
git clone https://github.com/yourusername/flask-portfolio-end-to-end.git
cd flask-portfolio-end-to-end

2️⃣ Create virtual environment
python -m venv venv
source venv/Scripts/activate   # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
python run.py


Visit 👉 http://127.0.0.1:5000 in your browser.

📬 Contact Form Data

Submissions are stored in data/messages.json.

Example:

[
  {"name": "Alice", "email": "alice@mail.com", "message": "Hi!"},
  {"name": "Bob", "email": "bob@mail.com", "message": "Love your portfolio!"}
]

🚀 Future Improvements

Add authentication (admin login).

Use SQLite/PostgreSQL instead of JSON.

Deploy to Heroku / Render / Vercel.