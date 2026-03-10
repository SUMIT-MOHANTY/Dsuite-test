from flask import Flask

def create_app():
    """Create and configure Flask application."""
    app = Flask(__name__)
    
    # Import routes after app is created to avoid circular imports
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app

# This is used by gunicorn/Procfile
app = create_app()
