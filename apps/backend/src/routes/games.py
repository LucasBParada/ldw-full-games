from flask import Blueprint, jsonify, request
from database import SessionLocal
from models.game import Game

games_bp = Blueprint("games", __name__)


@games_bp.route("/", methods=["GET"])
def get_games():
    """
    Lista todos os jogos
    ---
    tags:
      - Games
    responses:
      200:
        description: Lista de games
    """
    session = SessionLocal()
    games = session.query(Game).all()

    return jsonify([
        {
            "id": g.id,
            "host_id": g.host_id,
            "name": g.name,
            "genre": g.genre
        }
        for g in games
    ])


@games_bp.route("/", methods=["POST"])
def create_game():
    """
    Cria um novo jogo
    ---
    tags:
      - Games
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - host_id
            - name
          properties:
            host_id:
              type: integer
            name:
              type: string
            genre:
              type: string
    responses:
      201:
        description: Game criado com sucesso
    """
    data = request.get_json()

    session = SessionLocal()

    game = Game(
        host_id=data["host_id"],
        name=data["name"],
        genre=data.get("genre", "FPS")
    )

    session.add(game)
    session.commit()
    session.refresh(game)

    return jsonify({
        "id": game.id,
        "host_id": game.host_id,
        "name": game.name,
        "genre": game.genre
    }), 201