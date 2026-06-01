from flask import Flask, jsonify
from flasgger import Swagger

from database import create_database, init_db

from routes.health import health_bp
from routes.hosts import hosts_bp
from routes.games import games_bp
from routes.players import players_bp


def create_app():
    app = Flask(__name__)

    # Banco
    create_database()
    init_db()

    app.config["SWAGGER"] = {
        "title": "LDW Merge Skills API",
        "uiversion": 3,
        "description": "API de Hosts, Games e Players"
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "LDW Merge Skills API",
            "version": "1.0.0",
            "description": "Documentação da API"
        },
        "basePath": "/",
        "schemes": ["http"]
    }

    Swagger(app, template=swagger_template)

    # HOME
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "LDW Merge Skills API",
            "docs": "/apidocs/"
        })

    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(hosts_bp, url_prefix="/hosts")
    app.register_blueprint(games_bp, url_prefix="/games")
    app.register_blueprint(players_bp, url_prefix="/players")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )