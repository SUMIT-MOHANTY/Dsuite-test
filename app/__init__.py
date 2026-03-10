from flask import Flask
from flask_caching import Cache

cache = Cache()

def create_app():
    app = Flask(__name__)
    
    # Cache configuration for optimization
    app.config['CACHE_TYPE'] = 'simple'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300
    
    cache.init_app(app)
    
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app
