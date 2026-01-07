# 🚀 Flask Portfolio – End-to-End Production Deployment

A **production-ready personal portfolio web application** built using **Flask**, styled with **Tailwind CSS**, and deployed on **AWS EC2** using **Nginx + Gunicorn**.

This project demonstrates **real-world backend development practices** including cloud deployment, environment configuration, database integration, and scalable architecture — not just a basic Flask demo.

---

## 🌐 Live Deployment

* **Hosted on:** AWS EC2 (Ubuntu)
* **Web Server:** Nginx
* **WSGI Server:** Gunicorn
* **Backend Framework:** Flask

---

## 📌 Key Features

### 🏠 Home Page

* Clean landing page with professional introduction
* Fully responsive UI using Tailwind CSS

### 👤 About Page

* Brief profile summary
* Skills and background displayed dynamically

### 💻 Projects Page

* Dynamically loads project data
* Structured for scalability (migrated from JSON to database-ready design)

### 📬 Contact Page

* User contact form with validation
* Messages stored securely on the backend

### ✅ Thank You Page

* Confirmation page after successful form submission

### 🎨 Responsive Design

* Mobile-first design using Tailwind CSS
* Optimized for desktop, tablet, and mobile devices

---

## 🛠️ Tech Stack

### Backend

* **Python**
* **Flask**
* **Gunicorn** (WSGI server)

### Frontend

* **HTML5**
* **Tailwind CSS**
* **Jinja2 Templates**

### Database & Storage

* JSON-based storage (initial version)
* Structured to migrate to **SQLite / PostgreSQL** using SQLAlchemy

### Cloud & Deployment

* **AWS EC2 (Ubuntu)**
* **Nginx** (Reverse Proxy)
* **Linux Server Configuration**
* **Git & GitHub** for version control

---

## 🏗️ Architecture Overview

```
User
 ↓
Browser
 ↓
Nginx (Reverse Proxy)
 ↓
Gunicorn (WSGI)
 ↓
Flask Application
 ↓
Data Storage (JSON / Database)
```

---

## 🔐 Security & Best Practices

* Environment variables for sensitive data
* Flask production server setup (Gunicorn)
* Reverse proxy with Nginx
* Separation of frontend and backend logic
* Clean project structure for scalability

---

## 📂 Project Structure

```
flask-portfolio/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── projects.html
│   ├── contact.html
│   └── thank_you.html
│
├── static/
│   ├── css/
│   └── assets/
│
├── data/
│   ├── projects.json
│   └── messages.json
│
└── README.md
```

---

## 🚀 Deployment Highlights

* Configured and deployed Flask app on **AWS EC2**
* Integrated **Nginx + Gunicorn** for production readiness
* Enabled persistent background service for the application
* Tested application end-to-end after deployment

---

## 📈 Future Enhancements

* Migrate JSON storage to **PostgreSQL (RDS)**
* Add **Admin Dashboard** to manage contact messages
* Enable **HTTPS (SSL)** using Let’s Encrypt
* CI/CD pipeline using **GitHub Actions**
* Dockerize the application

---

## 👩‍💻 Author

**Tripti**
B.Sc Computer Science Student
Aspiring Backend / Cloud Engineer

---

## ⭐ Why This Project Matters

This project showcases:

* Real-world Flask backend development
* Cloud deployment experience
* Production-grade server configuration
* Clean, scalable project design

👉 Built to demonstrate **job-ready backend and cloud skills**, not just academic concepts.
