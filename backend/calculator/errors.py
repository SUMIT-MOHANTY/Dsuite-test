from flask import jsonify, Blueprint

errors_bp = Blueprint('errors', __name__)

class BadRequestError(ValueError):
    """Custom exception for bad request errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

@errors_bp.app_errorhandler(BadRequestError)
@errors_bp.app_errorhandler(400)
def handle_bad_request(error):
    """Return JSON error response."""
    return jsonify({'error': str(error)}), 400

# Also handle ValueError type for broader compatibility
@errors_bp.app_errorhandler(ValueError)
def handle_value_error(error):
    """Handle ValueError as bad request."""
    return jsonify({'error': str(error)}), 400
