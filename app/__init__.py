from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # 🔑 Needed for sessions & flash messages
    app.secret_key = "supersecretkey123"  
    # ⚠️ In real apps: use os.environ or secrets.token_hex(16) instead

    # Import & register blueprints
    from app.routes.home import home_bp
    from app.routes.about import about_bp
    from app.routes.projects import projects_bp
    from app.routes.contact import contact_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)

    return app
