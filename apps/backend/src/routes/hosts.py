from flask import Blueprint, jsonify, request
from database import SessionLocal
from models.host import Host

hosts_bp = Blueprint("hosts", __name__)


@hosts_bp.route("/", methods=["GET"])
def get_hosts():
    """
    Lista todos os hosts
    ---
    tags:
      - Hosts
    responses:
      200:
        description: Lista de hosts
    """
    session = SessionLocal()
    hosts = session.query(Host).all()

    return jsonify([
        {
            "id": h.id,
            "name": h.name,
            "country": h.country
        }
        for h in hosts
    ])


@hosts_bp.route("/", methods=["POST"])
def create_host():
    """
    Cria um novo host
    ---
    tags:
      - Hosts
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - country
          properties:
            name:
              type: string
            country:
              type: string
    responses:
      201:
        description: Host criado com sucesso
    """
    data = request.get_json()

    session = SessionLocal()

    host = Host(
        name=data["name"],
        country=data["country"]
    )

    session.add(host)
    session.commit()
    session.refresh(host)

    return jsonify({
        "id": host.id,
        "name": host.name,
        "country": host.country
    }), 201