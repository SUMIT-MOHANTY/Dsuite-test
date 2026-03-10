from flask import Flask
from calculator.routes import calculator_bp
from calculator.errors import errors_bp

def create_app():
    """Application factory for Flask."""
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(calculator_bp)
    app.register_blueprint(errors_bp)
    
    return app

# Create and run app for deployment
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
