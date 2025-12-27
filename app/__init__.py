from flask import Flask
from flask_login import LoginManager
import os
from datetime import datetime

def create_app():
    # Get the root directory (parent of app/)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    app = Flask(
        __name__,
        template_folder=os.path.join(root_dir, "templates"),
        static_folder=os.path.join(root_dir, "static")
    )
    
    # 🔑 Needed for sessions & flash messages
    app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey123")  
    # ⚠️ In real apps: use os.environ or secrets.token_hex(16) instead

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import get_user_by_id
        return get_user_by_id(user_id)

    # Context processor to make current_year available to all templates
    @app.context_processor
    def inject_current_year():
        return dict(current_year=datetime.now().year)

    # Initialize database if it doesn't exist
    from app.models import DB_NAME
    if not os.path.exists(DB_NAME):
        print("Database not found. Please run 'python app/create_db.py' to create it.")

    # Import & register blueprints
    from app.routes.home import home_bp
    from app.routes.about import about_bp
    from app.routes.projects import projects_bp
    from app.routes.contact import contact_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(auth_bp)

    return app
