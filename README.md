🚀 Flask Portfolio – End-to-End Backend & Cloud Project

A full-stack Flask portfolio web application designed, developed, and deployed on AWS EC2 using production-grade backend practices.

This project goes beyond a static portfolio and demonstrates real-world backend development, including authentication, data persistence, structured routing, and Linux server deployment.

🌐 Live Deployment

Hosted on: AWS EC2 (Ubuntu)

Web Server: Nginx

WSGI Server: Gunicorn

Backend Framework: Flask

🎯 Project Objective

To build and deploy a job-ready Flask application that demonstrates:

Backend fundamentals

Server-side rendering

Data handling

Authentication flow

Cloud deployment experience

📌 Core Features
🏠 Home Page

Professional landing page

Clean UI with Tailwind CSS

Template inheritance using base.html

👤 About Page

Dynamic profile and skills rendering

Data-driven design using JSON

💻 Projects Page

Projects loaded dynamically from projects.json

Easy to scale or migrate to a database

📬 Contact Form

User contact form with validation

Messages stored persistently (messages.json)

Thank-you confirmation page after submission

🔐 Authentication System

User Signup & Login

Credentials stored in SQLite database

Foundation for admin/dashboard features

🗄️ Database Integration

SQLite database (users.db)

SQLAlchemy models defined in models.py

Database initialization using create_db.py

🏗️ Application Architecture
User
 ↓
Browser
 ↓
Flask Routes
 ↓
Templates (Jinja2)
 ↓
Data Layer (SQLite / JSON)

🛠️ Tech Stack
Backend

Python

Flask

SQLAlchemy

SQLite

Frontend

HTML5

Tailwind CSS

Jinja2 Templates

Data Storage

JSON (projects, skills, messages)

SQLite (users & authentication)

Cloud & DevOps

AWS EC2 (Ubuntu Linux)

Linux server configuration

Git & GitHub

📂 Project Structure
flask-portfolio-end-to-end/
│
├── app/
│   ├── routes/
│   ├── models.py
│   ├── create_db.py
│   └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── projects.html
│   ├── contact.html
│   ├── login.html
│   ├── signup.html
│   └── thankyou.html
│
├── static/
│   └── images/
│
├── data/
│   ├── projects.json
│   ├── skills.json
│   └── messages.json
│
├── users.db
├── app.py
├── requirements.txt
└── README.md

🚀 Deployment Highlights

Flask application deployed on AWS EC2

Linux-based server environment

Application tested after deployment

Real production experience (not local-only)

🔐 Security & Best Practices

Modular route structure

Separation of concerns (routes, models, templates)

Database-backed authentication

Scalable project structure

Ready for migration to PostgreSQL / RDS

📈 Future Enhancements

Replace JSON storage with PostgreSQL (RDS)

Admin dashboard for managing messages

HTTPS using SSL certificates

CI/CD pipeline with GitHub Actions

Docker containerization

👩‍💻 Author

Tripti
B.Sc Computer Science Student
Aspiring Backend / Cloud Engineer

⭐ Why This Project Stands Out

✔ Backend-focused Flask application
✔ Authentication + database integration
✔ Cloud deployment on AWS EC2
✔ Clean, scalable structure
✔ Built with job readiness, not just academics, in mind
