from flask import Flask
from calculator.routes import calculator_bp

app = Flask(__name__)
app.register_blueprint(calculator_bp, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(debug=True)
