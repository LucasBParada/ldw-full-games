from flask import Blueprint, jsonify
from sqlalchemy import text

from database import engine

health_bp = Blueprint("health", __name__)


@health_bp.route("", methods=["GET"])
def health_check():
    """
    Verifica a saúde da aplicação
    ---
    tags:
      - Health
    responses:
      200:
        description: Aplicação saudável
      503:
        description: Falha em algum serviço
    """

    database_status = "UP"

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as error:
        database_status = "DOWN"

        return jsonify({
            "status": "DOWN",
            "database": database_status,
            "error": str(error)
        }), 503

    return jsonify({
        "status": "UP",
        "database": database_status,
        "service": "LDW Merge Skills API",
        "version": "1.0.0"
    }), 200