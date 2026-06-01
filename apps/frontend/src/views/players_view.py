import flet as ft

from src.api import ApiClient
from src.components.info_card import info_card


def build(page: ft.Page):

    players_column = ft.Column()

    nickname_field = ft.TextField(label="Nickname")
    level_field = ft.TextField(label="Nível")
    game_id_field = ft.TextField(label="Game ID")

    def load_players():

        players_column.controls.clear()

        for player in ApiClient.get_players():

            players_column.controls.append(
                info_card(
                    player["nickname"],
                    f"Nível: {player['level']} | Game ID: {player['game_id']}"
                )
            )

        page.update()

    def create_player(e):

        ApiClient.create_player({
            "nickname": nickname_field.value,
            "level": int(level_field.value),
            "game_id": int(game_id_field.value)
        })

        nickname_field.value = ""
        level_field.value = ""
        game_id_field.value = ""

        load_players()

    load_players()

    return ft.Column(
        controls=[
            ft.Text("Players", size=30, weight=ft.FontWeight.BOLD),

            ft.Card(
                content=ft.Container(
                    padding=20,
                    content=ft.Column([
                        nickname_field,
                        level_field,
                        game_id_field,
                        ft.ElevatedButton(
                            "Cadastrar Player",
                            on_click=create_player
                        )
                    ])
                )
            ),

            players_column
        ]
    )