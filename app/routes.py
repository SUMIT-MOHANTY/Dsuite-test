from flask import Blueprint, request, jsonify
from .calculator import perform_add, perform_divide

bp = Blueprint("api", __name__, url_prefix="/")


@bp.post("/add")
def add():
    data = request.get_json(silent=True) or {}
    x = data.get("x")
    y = data.get("y")
    try:
        result = perform_add(x, y)
    except TypeError:
        return jsonify({"error": "invalid_input"}), 400
    return jsonify({"result": result})


@bp.post("/divide")
def divide():
    data = request.get_json(silent=True) or {}
    x = data.get("x")
    y = data.get("y")
    try:
        result = perform_divide(x, y)
    except ValueError:
        return jsonify({"error": "division_by_zero"}), 400
    except TypeError:
        return jsonify({"error": "invalid_input"}), 400
    return jsonify({"result": result})
