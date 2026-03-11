from flask import Flask, jsonify
from flask_bootstrap import Bootstrap

# Configuration
SECRET_KEY = 'development-secret-key-change-in-production'
DEBUG = True

# Create Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize Bootstrap
Bootstrap(app)

@app.route('/health')
def health_check():
    """Basic health check endpoint for testing"""
    return jsonify({'status': 'ok', 'message': 'Flask backend is running'})

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
