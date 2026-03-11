from flask import Blueprint, request, jsonify
from app.calculator import perform_add, perform_divide

api_bp = Blueprint("api", __name__)

@api_bp.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    try:
        x = float(data["x"])
        y = float(data["y"])
        result = perform_add(x, y)
        return jsonify({"result": result}), 200
    except (TypeError, ValueError, KeyError):
        return jsonify({"error": "invalid_input"}), 400

@api_bp.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    try:
        x = float(data["x"])
        y = float(data["y"])
        result = perform_divide(x, y)
        return jsonify({"result": result}), 200
    except ZeroDivisionError:
        return jsonify({"error": "division_by_zero"}), 400
    except (TypeError, ValueError, KeyError):
        return jsonify({"error": "invalid_input"}), 400
