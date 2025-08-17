from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from app.routes.home import home_bp
    from app.routes.about import about_bp
    from app.routes.projects import projects_bp
    from app.routes.contact import contact_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(contact_bp)

    return app
