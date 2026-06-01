from flask import Blueprint, jsonify, request
from database import SessionLocal
from models.player import Player

players_bp = Blueprint("players", __name__)


@players_bp.route("/", methods=["GET"])
def get_players():
    """
    Lista todos os players
    ---
    tags:
      - Players
    responses:
      200:
        description: Lista de players
    """
    session = SessionLocal()
    players = session.query(Player).all()

    return jsonify([
        {
            "id": p.id,
            "game_id": p.game_id,
            "nickname": p.nickname,
            "level": p.level
        }
        for p in players
    ])


@players_bp.route("/", methods=["POST"])
def create_player():
    """
    Cria um novo player
    ---
    tags:
      - Players
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - game_id
            - nickname
          properties:
            game_id:
              type: integer
            nickname:
              type: string
            level:
              type: integer
    responses:
      201:
        description: Player criado com sucesso
    """
    data = request.get_json()

    session = SessionLocal()

    player = Player(
        game_id=data["game_id"],
        nickname=data["nickname"],
        level=data.get("level", 1)
    )

    session.add(player)
    session.commit()
    session.refresh(player)

    return jsonify({
        "id": player.id,
        "game_id": player.game_id,
        "nickname": player.nickname,
        "level": player.level
    }), 201